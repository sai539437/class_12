#wap short code segment that prints the longest word in a list of words 
words = ["apple", "air","spray","sprinkles","teddybear"]
longest=max(words,key=len)
print(longest)
print("this is your longest word")