# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python chat application that provides a web interface for interacting with AI models through PydanticAI. The application uses Gradio for the frontend and connects to a local Ollama instance running the Qwen3:4b model.

## Architecture

The codebase follows a simple two-module architecture:

- **`app.py`**: Main Gradio web application that handles the chat interface, message routing, and UI state management
- **`load_agent.py`**: Agent configuration module that initializes the PydanticAI agent with model settings and system prompts

The application is designed to work with local Ollama models via OpenAI-compatible API endpoints.

## Development Commands

### Environment Setup
```bash
# Install dependencies using uv
uv sync

# Activate virtual environment (if using uv venv)
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### Running the Application
```bash
# Start the Gradio web interface
python app.py

# The app will be available at http://localhost:7860 by default
```

### Prerequisites
- Ensure Ollama is running locally on port 11434
- The Qwen3:4b model should be available in Ollama (`ollama pull qwen3:4b`)

## Key Configuration

### Model Configuration
The agent is configured in `load_agent.py` with:
- **Model**: Qwen3:4b via Ollama
- **Base URL**: `http://localhost:11434/v1`
- **System Prompts**: Configured for concise one-sentence responses with timestamp context

### Agent Initialization
The agent is initialized once at startup and reused for all chat interactions. The `init_agent()` function applies multiple system prompts to ensure consistent behavior.

## Common Development Patterns

### Adding New Models
To add support for additional models, extend the `MODEL_LIST` dictionary in `load_agent.py` with new OpenAIModel configurations.

### Modifying System Prompts
System prompts are applied via decorators in `load_agent.py`. Add new `@agent.system_prompt` decorated functions to modify agent behavior.

### UI Customization
The Gradio interface in `app.py` uses the Blocks API. Modify the interface components and event handlers as needed for UI changes.
- make sure to use uv to manage all dependencies
- use uv to run python files