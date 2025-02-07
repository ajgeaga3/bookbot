def count_characters(text):
    char_dict = {}
    lower_text = text.lower()
    for text in lower_text:
        num_count = get_num_words(text)
        char_dict[text] = num_count
    print(char_dict)