def deEmojify(inputString):
     returnString = ""
     for character in inputString:
         try:
             character.encode("ascii")
             returnString += character
         except UnicodeEncodeError:
             returnString += ''
     return returnString
with open('comments.txt', 'r', 1, 'utf-8') as file:
    response = deEmojify(file)
with open('comments.txt', 'w') as file:
    file.write(response)

