import os, common

models = [
    ("25p", "gemini-2.5-pro-exp-03-25"),
    ("20f", "gemini-2.0-flash"),
]

uri = "https://youtu.be/n17NFYBBjXY"  # Fall
prompt = "Please analyze the video according to the JSON schema."

dir = os.path.splitext(__file__)[0]
os.makedirs(dir, exist_ok=True)

for suffix in ["1", "m"]:
    config = common.config_from_schema(f"schema-{suffix}.json")
    for m, model in models:
        filename = f"{dir}/{m}-{suffix}.json"
        common.generate(model, uri, prompt, config, filename)
