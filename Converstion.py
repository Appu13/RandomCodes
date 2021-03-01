
'''
Module to convert and store the recieved input
'''
convo = []
'''
 Used to:
  Recieve the contents of the read file 
  Call the conversion function
  Finally call the store method to store all the contents to the text 

'''
def RecieveList(contents):

    print("Recieved contents: ", contents)
    
    
    for string in contents:
        convo.append(conversion(string))
    
    print ("Converted text: ",convo)
    Store()



# Method to convert the string based on a transtion table
def conversion(string):
   
   # key defintion for converstion
    Key = {
        'a': ';0',
        'e': ':(',
        'i': '*',
        'o': '@#',
        'u': '$%',
        'y': '|`',
        'A': '[]',
        'E': '!@',
        'I': '^%',
        'O': '~|',
        'U': '&#@',
        'Y': '!$)*'
    }
    
    # Making the transtion table
    TransTable = string.maketrans(Key)
    
    # Translating the string using the transition table
    return string.translate(TransTable)


# Used to store the contents into file name 
def Store():
    with open('listfile.txt', 'w') as filehandle:
        filehandle.writelines(convo)

ral = ["Hi my name is vishal\n", "I am twenty\n", "I love bunnies\t", "Cows are fat"]
RecieveList(ral)