#Write dispBook(BOOKS) to display names in uppercase if they start with a consonant.
#BOOKS = {1:"Python", 2:"Internet Fundamentals", 3:"Networking", 4:"Oracle sets", 5:"Understanding HTML"}
#Expected Output:PYTHON,netoworking
def disbook(books):
    for i in books:
        if books[i][0].lower() not in 'aeiou':
            print(books[i].upper())
        else:
            print(books[i])
books = { 1: "python", 2: "internet fundamentals",3: "networking",4:"orcale sets",5:"understanding html"}
disbook(books)