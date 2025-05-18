#!/bin/bash

# Usage: ./pep-qa.sh "Your question here"

question="$1"

if [ -z "$question" ]; then
  echo "Usage: $0 \"Your question here\""
  exit 1
fi

# Run the first command and capture its output, then pipe to the second command

uv run llm similar -c "$question" -d peps.db peps | uv run llm -s "Answer the question: $question" -m gpt-4.1-mini

