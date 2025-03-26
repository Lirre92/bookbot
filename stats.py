#defining a word count function 
def word_count(text_of_book):
    word_count = 0
    words = text_of_book.split()
    for word in words: 
        word_count += 1
    return word_count
    #print(f"Found {word_count} total words")

#defining a character count function 
def character_count(text_of_book):
    characters = {} 
    words = text_of_book.split()
    for word in words:
        word = word.lower()
        for letter in word: 
            if letter in characters:
                characters[letter] += 1 
            else:
                characters[letter] = 1
    return(characters)
                
#defining a functino to sort the character count 
def sorter(characters):
    sorted_list = []
#iterating through each characer and its count in the dictionary 
    for char, count in characters.items():
        if char.isalpha():
            #create a dictionary for this character and add to our list
            char_dict = {"char": char, "count": count}
            sorted_list.append(char_dict)
    # Sort from greatest to least by count 
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list
    
     