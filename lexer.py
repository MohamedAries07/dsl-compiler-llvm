import re

TOKENS = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MUL', r'\*'),
    ('DIV', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ASSIGN', r'='),
    ('SKIP', r'[ \t]+'),
]

def tokenize(code):
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS)
    tokens = []
    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'SKIP':
            tokens.append((kind, value))
    return tokens