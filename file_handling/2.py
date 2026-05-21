# read the text file - 1.txt, count number of words starting from letter : I/i

f = open("1.txt", 'r')
content=f.read()
words = content.split()

print(len(words))

print(words)

f.close()
