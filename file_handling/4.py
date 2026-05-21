# Lowercase Counter
# WAP to read data from a text file and count the total number of lowercase characters.
w=open("1.txt",'r')
content=w.read()
count=0
for i in content:
    if i.islower():
        count+=1
print(count)
w.close()
