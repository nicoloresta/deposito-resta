import os

if __name__ == "__main__":
    FILE_PATH = os.path.join(".", "2025-08-18", "Esercizio - 1", "rsc", "input.txt")
    try:
        # Ensure the input file exists
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        print("Input file not found. Please ensure 'input.txt' exists in the 'rsc' directory.")
        exit(1)