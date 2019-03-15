f = open("wordlist.txt", "r")

# Read in the wordlist file to an array
words = []
for x in f:
    words.append(x.strip())

# Declare variables needed for the unscramble loop
x = ""
finalWords = []

while x != "j":
    # strip the input of eronious \n characters
    x = input().strip()

    # Only bother searching if there is a word there
    if len(x) > 2:
        for q in words:
            # Sort annd compare, if identical, the word is saved
            if sorted(x) == sorted(q):
                finalWords.append(q)
                break

# Rrint all of the words found
for i in finalWords:    
    print(i.strip(), end=",")