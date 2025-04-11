# Gemini YouTube Test

A research project to analyze YouTube video content using Google's Gemini AI models, structuring the content in both JSON and Markdown formats.

## Overview

This project serves as a test environment for:

- Scene-by-scene analysis of YouTube video content
- Structured recording of visual elements and audio content
- Content generation using multiple Gemini models (2.5 Pro and 2.0 Flash)
- Output support in both JSON and Markdown formats

## Project Structure

- `common.py`: Common utility functions
- `test-json.py`: Test JSON generator
- `test-text.py`: Test Text generator
- `article.py`: Article generator for processed video content
- `schema-1.json`: Basic JSON schema
- `schema-m.json`: Detailed JSON schema (with speaker information)

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
