def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    letter_count = sort_letters(text)
    report = char_report(text)
    print(report)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1
    return chars
    
def sort_letters(text):
    letters = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in letters:
                letters[lowered] += 1
            else:
                letters[lowered] = 1
    return dict(sorted(letters.items(), key=lambda item:item[1], reverse=True))

def char_report(text):
    report_beginning = f"""
    --- Begin report of books/frankenstein.txt ---
    
    {get_num_words(text)} words found in the document\n
    """
    
    chars = []

    for key, value in sort_letters(text).items():
        chars.append(f"The '{key}' character was found {value} times")

    
    report_middle = "\n    ".join(chars)

    report_end = """
    --- End report ---
    """

    report = report_beginning + report_middle + report_end

    return report

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()