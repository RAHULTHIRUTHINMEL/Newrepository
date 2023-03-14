#setcomprehnsion

def main():
    ctemps = [5,10,12,14,0,23,41,30,12,24,12,18,29]

    ftemps1 = [(t*9/5)+32 for t in ctemps]  #list
    ftemps2 = {(t*9/5)+32 for t in ctemps}  #set we use curly brackets
    print(ftemps1)
    print(ftemps2)

    #build a set of unique Fahrenheit temperatures





    #build a set from an input source
    sTemp = "The qick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}   #isspace to avoid space 
    print(chars)



if __name__ == "__main__":
    main()