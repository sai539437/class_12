# def
def ablines(data): # parameter
    for i in data:
            print(i.strip())


            # main program
            conn = open('1.txt','r')
            data = conn.readlines()

            ablines(data) # argument

            conn.close() 
    print("The file '1.txt' was not found.")
