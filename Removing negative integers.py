def negative(word,count):
    '''Removes negative integers from an array/list '''
    choice =[-1,-2,-3,-4,-5,-6,-7,-8,-9]        #list to for comparison
    if count < 0:
        print(word)
        return
    else:
        if word[count] in choice:
            del word[count]                   #removing negative integers
            negative(word,count-1)            #recursive call
        else:
            negative(word,count-1)            #recursive call
array = [1,-2,2,-3,1,3,-4,2,-2,9,7,5,4,2,1,2,6,3,4,4,5,6,6]    #Sample array 
number = len(array)-1
negative(array,number) #function call