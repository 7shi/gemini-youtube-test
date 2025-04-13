import os
import gemini_yt.gemini as gemini
from test_common import *

prompts = [
    ("ja", "動画の内容を日本語で記事として書き直してください。"),
    ("en", "Rewrite the content of the video as an article in English."),
]

dir = "article"
os.makedirs(dir, exist_ok=True)

config = gemini.config_text
for lang, prompt in prompts:
    for uri, target in targets:
        for m, model in models:
            filename = f"{dir}/{target}-{m}-{lang}.md"
            gemini.generate(model, uri, prompt, config, filename)
