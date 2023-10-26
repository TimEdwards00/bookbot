def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    letters = {}
    file_contents = file_contents.lower()

    for char in file_contents:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    
    return letters

def dict_to_clean_list(dictionary):
    my_list = [(k,v) for k, v in dictionary.items()]
    new_list = []
    for entry in my_list:
        if entry[0].isalpha():
            new_list.append(entry)
    new_list.sort(key=lambda a: a[1], reverse=True)
    return new_list


file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letters_count = dict_to_clean_list(count_letters(file_contents))

    print(f'--- Begin report of {file_path} ---')
    print(f'{word_count} words found in the document')
    for entry in letters_count:
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    print("--- End report ---")