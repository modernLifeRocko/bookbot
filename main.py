from stats import *
import sys

def main(book_path: str):
    book_content = get_book_text(book_path)
    # print(f"{count_words(book_content)} words found in the document")
    # print(char_count(book_content))
    report = f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {count_words(book_content)} total words
    --------- Character Count -------
    {'\n'.join(f'\t{k['char']}: {k['count']}' for k in char_dict_sorter(char_count(book_content)) if k['char'].isalpha())}
    ============= END ===============
    """
    print(report)

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
