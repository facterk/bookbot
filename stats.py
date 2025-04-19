def num_of_words():
    book_txt = main()
    book_txt_string = str(book_txt)
    word_count = len(book_txt_string.split())
    result = f"{word_count} words found in the document"
    return result