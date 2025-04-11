import os, common

models = [
    ("25p", "gemini-2.5-pro-exp-03-25"),
    ("20f", "gemini-2.0-flash"),
]
config = common.config_text

uri = "https://youtu.be/n17NFYBBjXY"  # Fall
prompts = [
    ("ja", "動画の内容を、内容のまとまりごとに区切って（時間を明示）、映像を文章化して、音声の文字起こしを添えて出力してください。"),
    ("en", "Divide the content of the video into sections (indicating the time), describe the visuals in text, and include a transcription of the audio."),
]

dir = os.path.splitext(__file__)[0]
os.makedirs(dir, exist_ok=True)

for lang, prompt in prompts:
    for m, model in models:
        filename = f"{dir}/{m}-{lang}.md"
        common.generate(model, uri, prompt, config, filename)
