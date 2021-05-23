import os

def main():
#Enter information to save to a file.
    directory = input("What directory do you want to save the file : ")
    filename = input("Enter a filename : ")
    fullName = input("What is your full name : ")
    address = input("What is your address : ")
    city = input("What city : ")
    state = input("What state : ")
    zipCode = input("What is your zip code : ")
    phoneNumber = input("What is your phone number : ")

#If else statement to determine directory validation.
    if os.path.isdir(directory):

#Create a file to write to.
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(fullName+', '+address+', '+city+
        ', '+state+', '+zipCode+', '+phoneNumber+'\n')
        writeFile.close()
        print("File information:")

#Read file contents to validate storing information.
        with open(os.path.join(directory,filename),'r') as readFile:
            for line in readFile:
                print(line)
    else:
        print("That directory does not exist")
        question = input("Want to try again? Type Y or N: ")
        if question == 'Y':
            main()
        if question == 'N':
            print("Okay! See you next time!")
            exit()
main()
