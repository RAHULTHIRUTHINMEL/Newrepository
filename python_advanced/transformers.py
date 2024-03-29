#filter function

def filterFunc(x):
    if x % 2 == 0 :
        return False
    return True

def filFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x ** 2


def toGrade(x):
    if x >= 90:
        return "A"
    elif ( x >= 80 and x < 90):
        return "B"
    elif (x >=70 and x < 80):
        return "C"
    elif (x >=60 and x < 70):
        return "D"
    else:
        return "F"
    
    

def main():
    nums  = (1,8,4,5,13,26,381,410,58,47)

    chars = "abcDeFGHiJklmnoP"
    grades =  (81,89,94,78,61,66,99,74)

    # #use filter to remove itmes from a list
    odds = list(filter(filterFunc, nums))
    print(odds)
    # #use filter on non-numeric sequence
    lowers = list(filter(filFunc2, chars))
    print(lowers)


    #use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)


    #use sorted and map to change numbers to grades
    grades = sorted(grades)
    print(grades)
    letters = list(map(toGrade, grades))
    print(letters)



if __name__ == "__main__":
    main()
