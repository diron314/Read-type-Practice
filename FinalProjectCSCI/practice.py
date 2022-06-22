import random
import time


"""

print("Read the text, and then copy it exactly.")
textToCopy = "Example text!"
print(textToCopy)
repliedText = input()
if repliedText == textToCopy:
    print("Correct!")
else:
    print("Incorrect!")

"""






list =[]
selectedText = ""
with open("HarryPotter1.txt", "r", encoding="utf-8") as book:
    line = book.readlines()
    print(type(line))
    print(len(line))
    selectedTextAll = line[random.randrange(0,13019)]
    selectedText = selectedTextAll.strip("\n")
    selectedText = selectedTextAll.strip()


start = time.time()
stop_seconds = .33*len(selectedText)
promptText = "Write exactly the text that appears below. \nYou have " + str(round(stop_seconds,2)) + " seconds."

while time.time() - start < stop_seconds:
    print(promptText)
    print(selectedText)
    userText = input()

    if time.time() - start < stop_seconds and userText == selectedText:
        print("On Time and Correct!")
        break
    elif time.time() - start < stop_seconds and userText != selectedText:
        print("Incorrect")
        break
    else:
        print("Too late!")
        break






"""
repliedtext = input()
if repliedtext == selectedText:
    print("CORRECT")
else:
    print("Incorrect")

rT = []
sT = []






#This prints the characters and the index of both texts 
for char in range(len(selectedText)):
    sT.append([selectedText[char], char])
print(sT)
for char in range(len(repliedtext)):
    rT.append([repliedtext[char], char])
print(rT)




# This lists characters different from the input and the selected text.
incorrectChars = []
for char in range(len(repliedtext)):
    if selectedText[char] != repliedtext[char]:
        incorrectChars.append(selectedText[char])
print(incorrectChars)

"""



