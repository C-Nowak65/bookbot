def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_charecter_count(text)
    sorted_char_count = sort_charecter_count(char_count)
    print_report(book_path, word_count, sorted_char_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_charecter_count(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count

def sort_charecter_count(char_count):
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)

def print_report(book_path, word_count, sorted_char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_char_count:
        if not char.isalpha():
            continue
        print(f" The {char} charecter was found {count} times")
    print("---End report ---")





main()