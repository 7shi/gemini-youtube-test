import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

#model = "gemini-2.5-pro-preview-03-25"
model = "gemini-2.0-flash"

prefix, uri = "fall", "https://youtu.be/n17NFYBBjXY"
# prefix, uri = "neolatin", "https://youtu.be/BrHClxlgUnw"

# prompt = "動画の内容を、内容のまとまりごとに区切って（時間を明示）、映像を文章化して、音声の文字起こしを添えて出力してください。"
prompt = """
動画からスライドを作成するために必要な情報を抽出してください。
日本語で詳細に分析し、主要なセクション、キーポイント、比較要素を特定してください。
内容に応じた最適なスライド構造を設計してください。
""".strip()

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_uri(
                file_uri=uri,
                mime_type="video/*",
            ),
        ],
    ),
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text=prompt),
        ],
    ),
]
generate_content_config = types.GenerateContentConfig(
    response_mime_type="text/plain",
)

text = ""
for chunk in client.models.generate_content_stream(
    model=model,
    contents=contents,
    config=generate_content_config,
):
    print(chunk.text, end="")
    text += chunk.text

i = 1
while os.path.exists(md := f"text/{prefix}-{i:02d}.md"):
    i += 1
with open(md, "w", encoding="utf-8") as f:
    for line in prompt.splitlines():
        print(">", line, file=f)
    print(file=f)
    print(text.strip(), file=f)
