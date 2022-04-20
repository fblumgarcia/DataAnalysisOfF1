def readNationality(): # Function to create a list with the nationality of the drivers
    nationality = []
    with open("../data/nationality.csv", "r", encoding="utf-8") as f:
        for line in f:
            nationality.append(str(line))
        print(nationality)

def main():
    readNationality()

if __name__ == "__main__":
    main()