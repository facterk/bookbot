
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
    result = f"{word_count} words found in the document"
    return result
print (num_of_words())

