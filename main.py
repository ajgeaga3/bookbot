def main():
    book_path = "/Users/a222/workspace/github.com/ajgeaga3/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print_report(book_path, num_words, char_count)
    
    


def get_num_words(text):
    words = text.split()
    return len(words)

def print_report(the_book_path, num_of_words, char_dict):
        print(f"--- Begin report of {the_book_path} ---")
        print(f"{num_of_words} words found in the document")
        list_of_dict = [{'char': key, 'num': value} for key, value in char_dict.items()]
        list_of_dict.sort(reverse=True, key=sort_on)
        for char in list_of_dict:
            chars = char['char']
            count = char['num']
            print(f"The '{chars}' character was found {count} times")
        print("--- End of Report ---")
            
        
        
            
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_dict = {}
    lower_text = text.lower()
    for text_char in lower_text:
        if text_char.isalpha():
            if text_char in char_dict:
                char_dict[text_char] += 1
            else:
                char_dict[text_char] = 1
        
    return char_dict


def sort_on(dict):
    return dict["num"]
    

main()
