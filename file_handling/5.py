#Filter Lines by 'I' or 'T'
#WAP to read lines from text and display those starting with the characters 'I' or 'T'.

r=open("1.txt",'r')
line=r.readlines()

for i in line:
    if i[0]=='I':
        print(i)
    elif i[0]=='T':
        print(i)

r.close()
