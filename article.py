import os, common

models = [
    ("25p", "gemini-2.5-pro-exp-03-25"),
    ("20f", "gemini-2.0-flash"),
]
config = common.config_text

targets = [
    ("https://youtu.be/n17NFYBBjXY", "fall"),
    ("https://youtu.be/BrHClxlgUnw", "neolatin"),
]

prompt = "動画の内容を記事として書き直してください。"

dir = os.path.splitext(__file__)[0]
os.makedirs(dir, exist_ok=True)

for uri, target in targets:
    for m, model in models:
        filename = f"{dir}/{target}-{m}.md"
        common.generate(model, uri, prompt, config, filename)
