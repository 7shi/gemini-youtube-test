import os
import gemini_yt.gemini as gemini
from test_common import *

prompt = "Please analyze the video according to the JSON schema."

dir = "json"
os.makedirs(dir, exist_ok=True)

for uri, target in targets:
    for suffix in ["1", "m"]:
        config = gemini.config_from_schema(f"schema-{suffix}.json")
        for m, model in models:
            filename = f"{dir}/{target}-{m}-{suffix}.json"
            gemini.generate(model, uri, prompt, config, filename)
