import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

generate_content_config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required = ["scenes"],
        properties = {
            "scenes": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                description = "An array containing individual scenes extracted from the video.",
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["time", "visuals", "audio"],
                    properties = {
                        "time": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "The timestamp indicating when the scene occurs in the video ('HH:MM:SS').",
                        ),
                        "visuals": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "A description or analysis of the visual content of the scene.",
                        ),
                        "audio": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "A description, transcription, or analysis of the audio content of the scene.",
                        ),
                    },
                ),
            ),
        },
    ),
)

model = "gemini-2.5-pro-exp-03-25"
# model = "gemini-2.0-flash"

prefix, uri = "fall", "https://youtu.be/n17NFYBBjXY"
# prefix, uri = "neolatin", "https://youtu.be/BrHClxlgUnw"

prompt = "Please analyze the video according to the JSON schema."
# prompt = "Please analyze the video according to the JSON schema from 05:18 onwards."

text = ""
for chunk in client.models.generate_content_stream(
    model=model,
    contents=[
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
    ],
    config=generate_content_config,
):
    print(chunk.text, end="")
    text += chunk.text

i = 1
while os.path.exists(md := f"json/{prefix}-{i:02d}.json"):
    i += 1
with open(md, "w", encoding="utf-8") as f:
    print(text.rstrip(), file=f)
