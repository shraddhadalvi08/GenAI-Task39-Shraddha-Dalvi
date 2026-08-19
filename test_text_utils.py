from text_utils import clean_text, split_for_model


def main():
    messy = "  GenAI   can create text.\nIt still needs checking.  "
    assert clean_text(messy) == "GenAI can create text. It still needs checking."

    long_text = "Sentence one is useful. " * 100
    chunks = split_for_model(long_text, chunk_size=160)
    assert len(chunks) > 1
    assert all(chunk.strip() for chunk in chunks)
    assert all(len(chunk) <= 160 for chunk in chunks)

    print("PASS: text cleaning and long-input splitting work correctly.")
    print("Chunks created in long-input test:", len(chunks))


if __name__ == "__main__":
    main()

