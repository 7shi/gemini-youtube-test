import os, sys, json, time
from google import genai
from google.genai import types

models = [
    "gemini-2.5-pro-preview-03-25",
    "gemini-2.5-pro-exp-03-25",
    "gemini-2.0-flash",
]

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

config_text = types.GenerateContentConfig(
    response_mime_type="text/plain",
)

def build_schema_from_json(json_data):
    t = json_data.get("type")
    match t:
        case "object":
            properties = {}
            for prop_name, prop_data in json_data["properties"].items():
                properties[prop_name] = build_schema_from_json(prop_data)
            return genai.types.Schema(
                type=genai.types.Type.OBJECT,
                required=json_data.get("required", json_data["required"]),
                properties=properties
            )
        case "string":
            return genai.types.Schema(
                type=genai.types.Type.STRING,
                description=json_data.get("description", "")
            )
        case "array":
            return genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description=json_data.get("description", ""),
                items=build_schema_from_json(json_data["items"])
            )
        case _:
            raise ValueError(f"Unsupported type: {t}")

def config_from_schema(schema_filename):
    with open(schema_filename, 'r', encoding='utf-8') as f:
        schema = build_schema_from_json(json.load(f))
    return types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=schema,
    )

def generate_content_retry(model, config, contents):
    for _ in range(5):
        try:
            response = client.models.generate_content_stream(
                model=model,
                config=config,
                contents=contents,
            )
            text = ""
            for chunk in response:
                print(chunk.text, end="")
                text += chunk.text
            return text
        except genai.errors.APIError as e:
            if e.code in [429, 500, 503]:
                print(e, file=sys.stderr)
                for i in range(15, -1, -1):
                    print(f"\rRetrying... {i:2d}", end="", file=sys.stderr, flush=True)
                    if i:
                        time.sleep(1)
                print(file=sys.stderr)
                continue
            else:
                raise
    raise RuntimeError("Max retries exceeded.")

def show_params(f, model, uri, prompt):
    print("- model:", model, file=f)
    print("- uri  :", uri, file=f)
    print(file=f)
    for line in prompt.splitlines():
        print(">", line, file=f)
    print(file=f)

def generate(model, uri, prompt, config, filename):
    if os.path.exists(filename):
        print(f"File '{filename}' already exists. Skipping generation.")
        return
    print("=" * 40)
    show_params(sys.stdout, model, uri, prompt)
    text = generate_content_retry(model, config, [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=uri,
                    mime_type="video/*",
                ),
                types.Part.from_text(text=prompt),
            ],
        ),
    ])
    if not text.endswith("\n"):
        print()
    with open(filename, "w", encoding="utf-8") as f:
        if not filename.endswith(".json"):
            show_params(f, model, uri, prompt)
        print(text.rstrip(), file=f)
