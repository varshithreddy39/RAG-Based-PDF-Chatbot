import re

def clean_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove space before and after newline
    text = re.sub(r'\s*\n\s*', '\n', text)

    # Strip leading and trailing spaces
    text = text.strip()

    return text
