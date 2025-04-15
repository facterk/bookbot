
def get_book_text(book_location):
    with open(book_location) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_location = input("file location here")
    book_text = get_book_text(book_location)
    print(book_text)
main()

