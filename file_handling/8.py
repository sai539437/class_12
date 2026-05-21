#. Long Word Counter
#Write a method which counts the occurrence of words with more than 5 characters from a text file.
r=open("1.txt",'r')
line=r.read()
words=line.split()
count=0
for word in words:
    if len(word)>5:
        count+=1
        print(word)
r.close()

