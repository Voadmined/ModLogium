# ModLogium

A CLI-based moderation logging application written in Python.

## Features

> * Interactive terminal prompts with validation
> * Automatic sequential ID generation
> * JSON-based persistent storage
> * Styled log output tables with word wrapping
> * Built-in search functionality across all log fields (Username, User ID, Action, Reason, Moderator)
> * *Planned:* Standalone executable file (.exe) for non-Python users

## Requirements

> * Python 3.x
> * Questionary
> * Rich

## Directory Structure

```text
main/
├── data/
│   └── logs.json
├── database.py
├── logs.py
└── main.py
```

## Setup & Usage

Install dependencies:

```Bash
pip install -r requirements.txt
```

Run the application:

```Bash
python main.py
```

## Credits

**Enpaged**
> Tester, Contributor
