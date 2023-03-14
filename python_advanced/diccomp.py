#diccomprehension

def main():

    ctemps = [0,12,34,100]

    #comprehension to build a dictionary
    tempDic = {t : (t*9/5)+32 for t in ctemps if t<100}
    print(tempDic)
    print(tempDic[12])


    #Merge two dictionaries with a comprehesion
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"white": 12, "Macke": 88, "Perce": 4}

    newTeam = {k:v for team in (team1,team2) for k,v in team.items()}

    print(newTeam)


if __name__ == "__main__":
    main()