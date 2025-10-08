# RAG AI Email Assistant

A RAG-compatible AI email assistant with structured prompts and professional tone.

## Features
- Prompt engineering for controlled email replies
- Retrieval-Augmented Generation using ChromaDB
- Structured JSON-like output for downstream processing
- Test scenarios included

## Tech Stack
- Python + LangChain + OpenAI GPT-4o-mini
- ChromaDB for vector retrieval
- dotenv for environment variables

## Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Set `OPENAI_API_KEY` in `.env`
3. Run: `python main.py`

## Testing
Use Jupyter notebook in `tests/prompt_evaluation.ipynb` to test multiple email scenarios.
