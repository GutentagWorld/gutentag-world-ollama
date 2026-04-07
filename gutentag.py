#!/usr/bin/env python3
"""Uses Ollama to produce 'Gutentag, World!'.

Requires: pip install ollama
Requires: Ollama running locally with a model pulled (e.g. ollama pull llama3.2)
"""
import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'system', 'content': 'You only ever respond with exactly: Gutentag, World!'},
        {'role': 'user', 'content': 'Say hello.'},
    ],
)

print(response['message']['content'])
