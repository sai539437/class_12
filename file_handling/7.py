#. Word Occurrence Search
#Write a function to read a file and display the occurrence of the word 'World'.
r=open("1.txt",'r')
line=r.read()
count=line.count('world')
print(count)
r.close()
