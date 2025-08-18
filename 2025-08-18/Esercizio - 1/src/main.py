import spacy
from collections import Counter
import os

# Load spaCy model (you may need to download it first with: python -m spacy download <model_name>)
MODEL_NAME = "it_core_news_sm"
try:
    nlp = spacy.load(MODEL_NAME)
except OSError:
    print(f"Please install the required model: python -m spacy download {MODEL_NAME}")
    exit(1)

def count_lines(content: str) -> int:
    """Count the number of non-empty lines in the content."""
    return len([line for line in content.split('\n') if line.strip()])

def count_words(content: str) -> int:
    """Count the total number of words in the content using spaCy tokenization."""
    doc = nlp(content)
    # Count tokens that are not whitespace, punctuation, or symbols
    return len([token for token in doc if not token.is_space and not token.is_punct])

def get_top_words(content: str, n: int = 5) -> list:
    """Get the top n most frequent words in the content using spaCy."""
    doc = nlp(content.lower())
    # Filter tokens: exclude whitespace, punctuation, stop words, and non-alphabetic tokens
    words = [
        token.text
        for token in doc
        if not token.is_space 
            and not token.is_punct
            and token.is_alpha
    ]
    word_freq = Counter(words)
    return word_freq.most_common(n)

if __name__ == "__main__":
    FILE_PATH = os.path.join(".", "2025-08-18", "Esercizio - 1", "rsc", "input.txt")
    try:
        # Ensure the input file exists
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            content = file.read()

            # Count lines
            total_lines = count_lines(content)
            print(f"Total lines: {total_lines}")

            # Count words
            total_words = count_words(content)
            print(f"Total words: {total_words}")

            # Get top 5 most frequent words
            top_5_words = get_top_words(content)
            print("Top 5 most frequent words:")
            for word, count in top_5_words:
                print(f"  {word}: {count}")
    except FileNotFoundError:
        print("Input file not found. Please ensure 'input.txt' exists in the 'rsc' directory.")
        exit(1)