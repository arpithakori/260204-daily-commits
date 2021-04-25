def search(text, word):
    if word in text:
        print("Word found")
    else:
        print("Word not found")


text = input("Enter the text: \n")
word = input("Enter the word you want to search: \n")
search(text, word)

