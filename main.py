#importing other functions 
from stats import word_count
from stats import character_count
from stats import sorter

#defining function to take input and retrieve book text 
def get_book_text(path):
    with open(path) as f: 
        file_contents = f.read()
        return(file_contents)

#defining the main bookbot function 
def main(): 

    #establishing path for bookbot to find books in 
    path = "books/frankenstein.txt"
    
    # retrieving text 
    text = get_book_text(path)

    # retrieving found count from text 
    w_count = word_count(text)
  
    # Returns list of dictionaries {["char": char, "count": count]}
    characters = (character_count(text))

    # sorting function
    sorted_list = sorter(characters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}. . . ")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

    #print(text)
    
main()