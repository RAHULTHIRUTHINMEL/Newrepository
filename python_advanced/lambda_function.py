def CelToFah(temp):
    return (temp * 9/5) + 32

def FahToCel(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [1, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

#use regular functions to convert

    print(list(map(FahToCel, ftemps)))
    print(list(map(CelToFah, ctemps)))

#lambda function to accomplish same
    print(list(map(lambda t : (t-32) * 5/9, ftemps)))
    print(list(map(lambda t : (t * 9/5) + 32, ctemps)))


if __name__  ==  "__main__":
    main()