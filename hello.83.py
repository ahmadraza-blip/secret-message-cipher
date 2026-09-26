# Create a program that can code and decode a message using a secret coding language.
# Rules
# For coding:
# If the word has 3 or more characters, remove the first character.
# Put that first character at the end.
# Add 3 random characters at the beginning and 3 random characters at the end.
# If the word has less than 3 characters, simply reverse it.
# For decoding:
# Remove the first and last 3 characters.
# Move the last character back to the beginning.
# For words shorter than 3 characters, reverse them again)


message = input("Enter a message: ")
words = message.split(" ")
new_word = [ ]
coding = int(input("Enter 1 for coding and 0 for decoding:"))
for word in words:
    if coding == 1:
        if len(word) >=3:
            a = "run"
            b = "nun"
            new = a + word[1:] + word[0] + b
            print(new, end = " ")
        else:
            if len(word) < 3:
                print(word[::-1], end = " ")
    elif coding == 0:
        if len(word) >= 9:
            stripped = word[3:-3]
            original = stripped[-1] + stripped[:-1]
            print(original, end = " ")
        else:
            if len(word) < 3:
                print(word[::-1], end = " ")
                
            



  


    





 


