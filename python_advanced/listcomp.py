#comprehensions

def main():

    evens = [2,4,6,8,10,12,14,16,18,20]
    odds = [1,3,5,7,9,11,13,15,17,19]
    
    #perform a amapping and filter function on a list
    evenSquared = list(
        map(lambda t : t **2, filter(lambda t : t >4 and t< 16, evens)))  #appied mapping,lambda and filter together
    print(evenSquared)



    #derive a anew list of numbers from a  given list 
    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)


    #limit the items operated on with a predicate condition
    oddSquared = [e ** 2 for e in odds if e>3 and e<17]
    print(oddSquared)


if __name__ == "__main__":
    main()