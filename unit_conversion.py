print("Welcome to my smart unit converter!\n")
print("Select what category of unit that are you trying to convert from - ")

def menu():
    print("Options are listed below;")
    print("1. Distance / Length")
    print("2. Weight / Mass")
    print("3. Temperature")
    print("4. Area")
    print("5. Volume")
    print("6. Time")
    print("7. Speed")
    print("8. Pressure")
    print("9. Energy")

    while True:
        category_1 = int(input("Enter your option number : "))
        try:
            thisdict ={
                1 : "Distance / Length",
                2: "Weight / Mass",
                3: "Temperature",
                4: "Area",
                5: "Volume",
                6: "Time",
                7: "Speed",
                8: "Pressure",
                9: "Energy"

            }
            if 0 <category_1 <= 9:
                    print("You have selected the valid option number", category_1, "corresponding to",thisdict[category_1]+ ".")
                    break
            else:
                 print("You have not selected a numerical value from 1 - 9.")
                 print("Please try again.\n")
                 continue
        except:
             print("You have chosen an invalid option or reponded incorrectly")
             print("Please try again.\n")
             continue
    return (category_1)

menu()

def distance_or_length(category_1):