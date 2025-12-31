def NULL_not_found(object: any)-> int:
    #your code here
    if (type(object) == float and object != object): #to detect nan "object != object"
        print("Cheese: nan <class 'float'>")
        return (0)
    elif(type(object) == int and object == 0):
        print ("Zero: 0 <class 'int'>")
        return (0)
    elif(type(object) == str and not object):
        print ("Empty: <class 'str'>")
        return (0)
    elif(type(object) == bool and object == False):
        print("Fake: False <class 'bool'>")
        return (0)
    elif (object == None):
        print("Nothing: None <class 'NoneType'>")
        return (0)
    else:
        print("Type not Found")
    return 1