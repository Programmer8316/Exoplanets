#simplify program
import csv
import sys
from exceptions import *

def main():
    planet = input("Enter exoplanet name: ").lower()
    search(planet)

    while True:
        response = input("Would you like to proceed: ").lower()
        
        if PassError().catch(response, False):
            if response == "yes":
                print()
                main() #recursion
            elif response == "no":
                sys.exit()
            else:
                print("Response was unclear, try again.\n")
        else:
            print()

def search(planet):
    with open("exoplanets.csv") as file:
        reader = csv.DictReader(file)
        found = False   
        
        print()

        if planet != "access all":
            for row in reader:
                if row["name"].lower() == planet:
                    print(f"Name: {row['name']}\nRadius[Earth Radius]: {row['radius']}\nDiscovery Year: {row['year']}\n")
                    found = True
                    break
            
            if not found:
                print("Exoplanet not found.\n")
        else:
            for row in reader:
                print(f"Name: {row['name']}\nRadius[Earth Radius]: {row['radius']}\nDiscovery Year: {row['year']}\n")

if __name__ == "__main__":
    main()