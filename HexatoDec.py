

value=str(input("Enter your hexavalue"))
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}




def hexToDec(hexNum):
    verification = True 

    for char in hexNum.upper(): 
        if char not in hexNumbers:
            verification = False 
            break 
    
    if verification == True:
        sum = 0
        counter = 0
        position = len(hexNum)-1

        while counter <= len(hexNum)-1:
        
                sum = sum + (hexNumbers[hexNum[position]]*(16**counter) )
                counter = counter + 1
                position = position -1 
        return sum 

    else :
        return None


print(hexToDec(value))
