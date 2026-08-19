import re


def clean_text(text):
    """Remove repeated whitespace without changing the actual words."""
    return re.sub(r"\s+", " ", text).strip()


def split_for_model(text, chunk_size=1200):
    """Split long notes near sentence endings for smaller model prompts."""
    if len(text) <= chunk_size:
        return [text]

    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    current = ""
    for sentence in sentences:
        if current and len(current) + len(sentence) + 1 > chunk_size:
            chunks.append(current)
            current = sentence
        else:
            current = (current + " " + sentence).strip()
    if current:
        chunks.append(current)
    return chunks

