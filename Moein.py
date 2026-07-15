def AgeChack(Age):
    if  Age > 140 or Age < -1 :
        while 1:
            print("The age is wrong")
            Age = int(input("Re-enter the Age's life:"))
            if  Age < 140 and Age >= -1 : break
    return Age


def  is_int(Num):
    try:
        Num = int(Num)
        return Num
            
    except ValueError:
        while True:
            print("The input entered is not a number.")
            Num =(input("Re-enter the input:"))
            try:
                Num = int(Num)
                return Num
            except ValueError:
                continue
            
            
def NumChack(number ,num1 ,num2):
    if  number > num2 or number < num1 :
        while True:
            print(f"The number entered is not limited to {num1} to {num2}")
            number = int(input(f"Enter the number in the range from {num1} to {num2}:"))
            if num1 <= number <= num2: break
    return number


def is_float(number):
    
    while True:
        number = str((number))
        position = number.find(".")
        if position == -1 :
            print("The input is not a decimal number.")
            number = float(input("Re-enter the decimal number:"))
            number = str((number))
            position = number.find(".")
            if position == -1 : continue
        elif position != -1:
            return number
                        
        
        
a = (input(":"))    
print(type(is_float(a)))


    
    