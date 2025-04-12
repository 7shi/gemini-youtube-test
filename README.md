# Gemini YouTube Test

A research project to analyze YouTube video content using Google's Gemini AI models, structuring the content in both JSON and Markdown formats.

## Overview

This project serves as a test environment for:

- Scene-by-scene analysis of YouTube video content
- Structured recording of visual elements and audio content
- Content generation using multiple Gemini models (2.5 Pro and 2.0 Flash)
- Output support in both JSON and Markdown formats
- `gemini-yt` tool includes sample analysis scripts to help you get started.

## Prerequisites

To set up the environment for running the scripts, follow these steps:

1. Obtain an API Key from [Google AI Studio](https://aistudio.google.com/) and set it as the environment variable `GEMINI_API_KEY`.
2. Ensure you have `uv` installed on your system.
3. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/7shi/gemini-youtube-test.git
    cd gemini-youtube-test
    ```
4. Install the required dependencies using `uv`:
    ```bash
    uv sync
    ```

Once the setup is complete, you can proceed to run the scripts as described in the usage section.

## Running the Sample Command

Use the `gemini-yt` command to analyze YouTube videos:

```bash
uv run gemini-yt -m <model> -s <schema_file> <youtube_url>
```

Parameters:
- `-v`, `--version`: Show the version of the script
- `-m`, `--model`: (Required) The Gemini model to use (e.g., "gemini-2.5-pro-exp-03-25", "gemini-2.0-flash")
- `-s`, `--schema`: Schema file to use (optional)
- `-o`, `--output`: Output filename (optional, defaults to YouTube ID with .json extension)
- `-p`, `--prompt`: Custom prompt to use for analysis (optional)
- `url`: YouTube URL to analyze

Examples:

```bash
# Analyze with default settings, using Gemini 2.5 Pro Experimental 03-25
uv run gemini-yt -m gemini-2.5-pro-exp-03-25 https://www.youtube.com/watch?v=n17NFYBBjXY

# Analyze with custom schema and output filename
uv run gemini-yt -m gemini-2.5-pro-exp-03-25 -s schema-m.json -o my-analysis.json https://www.youtube.com/watch?v=n17NFYBBjXY
```

## Project Structure

- `gemini_yt/`: Main package directory containing the core functionality
- `test-json.py`: Test JSON generator
- `test-text.py`: Test Text generator
- `test-article.py`: Article generator for processed video content
- `schema-1.json`: Basic JSON schema
- `schema-m.json`: Detailed JSON schema (with speaker information)
- `schema-a.json`: Transcription of audio only

### Output Files

Generated files are stored in the following directories:

- `json/`: JSON analysis results
- `text/`: Markdown analysis results
- `article/`: Generated article content from processed video analysis
- `test/`: Test files and scripts, which are remnants of initial experimental setups

File naming convention:

- `-25p-`: Generated using Gemini 2.5 Pro Experimental 03-25
- `-20f-`: Generated using Gemini 2.0 Flash
- `-1.json`: Single schema (single transcript for the entire scene)
- `-m.json`: Multiple schema (multiple transcripts split by speaker)
- `-en.md`: English Prompt
- `-ja.md`: Japanese Prompt

### JSON Format

- Structured scenes array for each video segment
- Records timestamps, visual elements, and audio content
- Additional metadata like speaker information based on schema version

### Markdown Format

- Chronological scene descriptions
- Text transcription of visual elements and audio
- Bilingual output (Japanese/English)
