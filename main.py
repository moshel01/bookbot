from stats import get_book_text, total_words, total_characters

def main():
    print(f"Found {total_words("./books/frankenstein.txt")} total words.")
    print(total_characters(get_book_text("./books/frankenstein.txt")))
main()