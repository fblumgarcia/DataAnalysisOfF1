def resumeNationality(): # Function to create a list with the nationality of the drivers
    nationality = []
    with open("../data/nationality.csv", "r", encoding="utf-8") as f:
        for line in f:
            nationality.append(str(line))
    nationality = list(set(nationality))
    nationality.remove("NATIONALITY\n")
    with open("../data/nationality.csv", "a", encoding="utf-8") as f:
        f.write("\n\n")
        f.write("The Nationalities")
        f.write("\n\n")
        for i in nationality:
            f.write(i)

def assignContinent():
    america = ["USA\n","BRA\n","CAN\n","ARG\n","VEN\n","COL\n","MEX\n"]
    africa = ["RHO\n","RSA\n"]
    europe = ["SUI\n","ITA\n","NED\n","SWE\n","FRA\n","POL\n",
                "FIN\n","IRL\n","HUN\n","BEL\n","AUT\n","POR\n","MON\n",
                "GER\n","DEN\n","ESP\n","GBR\n"]
    asia = ["THA\n","INA\n","CHI\n","RUS\n","JPN\n","MAS\n","IND\n"]
    oceania = ["NZL\n","AUS\n"]
    nationality = []
    with open("../data/Nationality.csv", "r", encoding="utf-8") as f:
        for line in f:
            nationality.append(str(line))
    with open("../data/Nationality.csv", "a", encoding="utf-8") as f:        
        f.write("\n\n")
        f.write("The Continents")
        f.write("\n\n")
        for i in nationality:
            if i in america:
                f.write("AMERICA")
                f.write("\n")
            elif i in africa:
                f.write("AFRICA")
                f.write("\n")
            elif i in asia:
                f.write("ASIA")
                f.write("\n")
            elif i in europe:
                f.write("EUROPE")
                f.write("\n")
            elif i in oceania:
                f.write("OCEANIA")
                f.write("\n")
            else:
                continue   

def main():
    #resumeNationality()
    assignContinent()

if __name__ == "__main__":
    main()