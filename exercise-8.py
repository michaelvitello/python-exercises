# Function to count capital letters in a file
# First, need to open and read (r mode only) text file
# Second, create counter then count and print number of capital letters


path = '/Users/michaelvitello/Desktop/text.txt' #change your file path accordingly
text_file  = open(path, 'r')
text = text_file.read()

uppercase_count = 0

for x in text :
    if x.isupper():
        uppercase_count += 1

print uppercase_count
