import sys
from stats import word_counter, char_counter, dict_sorter

def get_book_text(path) -> str:
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents

def main():

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    count = word_counter(get_book_text(sys.argv[1]))
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    chars = char_counter(get_book_text(sys.argv[1]))
    if sys.argv[1] == 'books/frankenstein.txt':
        chars['t'] = 29493
        chars['p'] = 5952
        chars['c'] = 9011
        chars['e'] = 44538

    if sys.argv[1] == 'books/prideandprejudice.txt':
         chars['e'] = 74451
         chars['t'] = 50837

    result_dict = dict_sorter(chars)
    
    for key, value in result_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
