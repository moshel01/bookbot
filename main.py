import sys
from stats import get_book_text, total_words, total_characters, a_z_sorted, bookbot

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookbot(sys.argv[1])
main()