def get_book_text(book_location):
    with open(book_location , encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    book_location = ("/home/karamalatia/workspace/github.com/bookbot/books/frankenstein.txt")
    book_text = get_book_text(book_location)
    return book_text

def num_of_words():
    book_txt = main()
    book_txt_string = str(book_txt)
    word_count = len(book_txt_string.split())
    result = f"found {word_count} total words"
    return result

def get_num_charechters():
    book_txt = main()
    book_txt_string = str(book_txt)
    book_txt_string_lower =book_txt_string.lower()
    book_txt_charechters = list(book_txt_string_lower)
    letters_dictionary = {
        "a" : 0 ,
        "b" : 0 ,
        "c" : 0 ,
        "d" : 0 ,
        "e" : 0 ,
        "f" : 0 ,
        "g" : 0 ,
        "h" : 0 ,
        "i" : 0 ,
        "j" : 0 ,
        "k" : 0 ,
        "l" : 0 ,
        "m" : 0 ,
        "n" : 0 ,
        "o" : 0 ,
        "p" : 0 ,
        "q" : 0 ,
        "r" : 0 ,
        "s" : 0 ,
        "t" : 0 ,
        "u" : 0 ,
        "v" : 0 ,
        "w" : 0 ,
        "x" : 0 ,
        "y" : 0 ,
        "z" : 0 ,
    }
    for i in book_txt_charechters:
        if i in letters_dictionary:
            letters_dictionary[i] += 1
    return letters_dictionary
def sort_diction():
    list = get_num_charechters()
    sorted_lst = dict(sorted(list.items(), key=lambda item: item[1] , reverse=True))
    return sorted_lst