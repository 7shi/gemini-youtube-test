import os
import gemini_yt.gemini as gemini
from test_common import *

prompts = [
    ("ja", "動画の内容を、内容のまとまりごとに区切って（時間を明示）、映像を文章化して、音声の文字起こしを添えて出力してください。"),
    ("en", "Divide the content of the video into sections (indicating the time), describe the visuals in text, and include a transcription of the audio."),
]

dir = "text"
os.makedirs(dir, exist_ok=True)

config = gemini.config_text
for uri, target in targets:
    for lang, prompt in prompts:
        for m, model in models:
            filename = f"{dir}/{target}-{m}-{lang}.md"
            gemini.generate(model, uri, prompt, config, filename)
