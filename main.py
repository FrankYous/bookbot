def word_counter(text):
    words = text.split() #text is split into a list of separate words 
    return len(words)

def char_counter(text):
    counter = {}
    text = text.lower() #text is changed to lower case to avoid duplicates in counting of the letters

    for i in range(0,len(text)): #creates a dictionary with all possible characters
        counter[text[i]] = 0
    for i in range(0,len(text)): #now the same dictionary is filled with the counted numbers
        counter[text[i]] += 1
    return counter

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read() 
        print(f"number of words in the book Frankenstein: {word_counter(text)}") #words are counted 
        print("numbers of letters are:")
        print (char_counter(text))

main()