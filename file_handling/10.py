#wap that should prompt the utype some sentences followed by enter it should then print the original sentence and the following statics relating 
#to the sentence #no of words #no of characters #% of character of alpha numberic

words = 'Enter a word 1233 !'
count = 0

for i in words:
    if i.isalpha():
        count = count + 1

print('% of alpha number : ',((count / len(words))*100))