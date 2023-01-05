def search(text,word):
    if word in text:
        print("Word found")
    else:
        print("Word not found")
text = input("Enter the txet.")
word = input("enter the word which you want to find")
print(search(text, word))