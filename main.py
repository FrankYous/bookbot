def word_counter(text):
    words = text.split() #Text is split into a list of separate words 
    return len(words)

def char_counter(text):
    counter = {}
    text = text.lower() #Text is changed to lower case to avoid duplicates in counting of the letters

    for i in range(0,len(text)): #Creates a dictionary with all possible characters
        counter[text[i]] = 0
    for i in range(0,len(text)): #Now the same dictionary is filled with the counted numbers
        counter[text[i]] += 1
    return counter

def just_alphabet (dict): #The function removes all non alphabetical characters
    alph_dict ={}
    for char in dict:
        if char.isalpha(): #If the character is in the alphabet,it will be added to the new dictionary
            alph_dict[char] = dict[char]
    return alph_dict

def dict_to_list(dict_letters): #The dictionary is now transformed into a list of tuples
    list_letters =[]
    for letter in dict_letters:
        list_letters.append([letter,dict_letters[letter]])
    return list_letters   

def sorter (letters):
    pass

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read() 

        print(f"number of words in the book Frankenstein: {word_counter(text)}") #Words are counted 
        characters = char_counter(text) #The characters are separated into a dictionary
        alphabet = just_alphabet(characters) #Non letter characters are removed
        letters = dict_to_list(alphabet) #Dictionary is transformed into a list of tuples
        print("numbers of letters are:")
        print (letters)

main()