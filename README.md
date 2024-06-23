<div align="center">
<h1>
Meeting Review Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

Extract key decisions and action items from meeting notes.

1. Prompt `claude-3.5-sonnet` for a summary of the `meeting_notes`
2. Prompt `gpt-4o` to generate a JSON with key decisions and action items
<div align="center">

</div>

## Running the Example

1. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/meeting-review-example
```

2. Change into the directory

```bash
cd meeting-review-example
```

3. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Get an OpenAI and Anthropic key, or see how to configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)

6. Run the example

```bash
OPENAI_API_KEY=... ANTHROPIC_API_KEY=... python meeting_review.py
```

## Using your own Data

Replace the contents of `meeting_notes.txt` with your own, and run the example.