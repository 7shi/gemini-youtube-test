import os
import gemini_yt.gemini as gemini

models = [
    ("25p", "gemini-2.5-pro-exp-03-25"),
    ("20f", "gemini-2.0-flash"),
]
targets = [
    ("https://youtu.be/n17NFYBBjXY", "fall"),
    ("https://youtu.be/BrHClxlgUnw", "neolatin"),
]
prompt = "Please analyze the video according to the JSON schema."

dir = "json"
os.makedirs(dir, exist_ok=True)

for uri, target in targets:
    for suffix in ["1", "m"]:
        config = gemini.config_from_schema(f"schema-{suffix}.json")
        for m, model in models:
            filename = f"{dir}/{target}-{m}-{suffix}.json"
            gemini.generate(model, uri, prompt, config, filename)
