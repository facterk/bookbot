
def get_book_text(book_location):
    with open(book_location , encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents
def main():
    book_location = ("/home/karamalatia/workspace/github.com/bookbot/books/frankenstein.txt")
    book_text = get_book_text(book_location)
    return book_text
from stats import num_of_words
print (num_of_words())

