import argparse
import re
from . import gemini
from .__init__ import name, __version__

def main():
    parser = argparse.ArgumentParser(description="Process a YouTube URL and analyze the video content.")
    parser.add_argument("-v", "--version", action="version", version=f'{name} {__version__}')
    parser.add_argument("-m", "--model", required=True, help="Model to use")
    parser.add_argument("-s", "--schema", help="Schema file to use")
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument("-p", "--prompt", help="Prompt to use")
    parser.add_argument("url", help="URL to process")
    args = parser.parse_args()

    if not (output := args.output):
        if m := re.search(r'([a-zA-Z0-9]+)$', args.url):
            output = m.group(1) + ".json"
        else:
            raise ValueError("Could not extract output from the URL using the regex.")

    if args.schema:
        config = gemini.config_from_schema(args.schema)
        prompt = args.prompt or "Please analyze the video according to the JSON schema."
    else:
        config = gemini.config_text
        prompt = args.prompt or "Please analyze the video."

    gemini.generate(
        model=args.model,
        uri=args.url,
        prompt=prompt,
        config=config,
        filename=output,
    )

if __name__ == "__main__":
    main()
