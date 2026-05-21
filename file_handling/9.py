#wap a prompt for a phn number of 10 digits and two dashes with two dashes with dashes after the area code and the next three numbers 
##017-555-1212 is a legal input 

numb = input('Enter the number : ')
print('Number : ',numb[0:3],'-',numb[3:6],'-')