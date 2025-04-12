import os
import gemini_yt.gemini as gemini

models = [
    ("15p", "gemini-1.5-pro-latest"),
    ("20p", "gemini-2.0-pro-exp-02-05"),
    ("25p", "gemini-2.5-pro-exp-03-25"),
    ("20f", "gemini-2.0-flash"),
]
config = gemini.config_text

targets = [
    ("https://youtu.be/n17NFYBBjXY", "fall"),
    ("https://youtu.be/BrHClxlgUnw", "neolatin"),
]

prompts = [
    ("ja", "動画の内容を日本語で記事として書き直してください。"),
    ("en", "Rewrite the content of the video as an article in English."),
]

dir = "article"
os.makedirs(dir, exist_ok=True)

for lang, prompt in prompts:
    for uri, target in targets:
        for m, model in models:
            filename = f"{dir}/{target}-{m}-{lang}.md"
            gemini.generate(model, uri, prompt, config, filename)
