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
- `fall-json.py`: JSON generator for Fall video analysis
- `fall-text.py`: Text generator for Fall video analysis
- `neolatin-json.py`: JSON generator for Neolatin video analysis
- `schema-1.json`: Basic JSON schema
- `schema-m.json`: Detailed JSON schema (with speaker information)

## Models Used

- Gemini 2.5 Pro (Experimental)
- Gemini 2.0 Flash

## Output Formats

### JSON Format

- Structured scenes array for each video segment
- Records timestamps, visual elements, and audio content
- Additional metadata like speaker information based on schema version

### Markdown Format

- Chronological scene descriptions
- Text transcription of visual elements and audio
- Bilingual output (Japanese/English)

## Output Files

Generated files are stored in the following directories:

- `fall-json/`: JSON analysis results for Fall videos
- `fall-text/`: Markdown analysis results for Fall videos
- `neolatin-json/`: JSON analysis results for Neolatin videos

File naming convention:

- `25p-`: Generated using Gemini 2.5 Pro
- `20f-`: Generated using Gemini 2.0 Flash
- `-1.json`: Single schema (single transcript for the entire scene)
- `-m.json`: Multiple schema (multiple transcripts split by speaker)
- `-en.md`: English Markdown
- `-ja.md`: Japanese Markdown

### Testing

The `test/` directory contains sample files and test scripts:

- `test-json.py`: Tests JSON generation functionality
- `test-text.py`: Tests Markdown generation functionality
- Sample generated files in `test/json/` and `test/text/`
