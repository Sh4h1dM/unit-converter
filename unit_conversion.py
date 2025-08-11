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
    print("9. Energy\n")

    while True:
        try:
            category = int(input("Enter your option number : "))
            thisdict ={
                1: "Distance / Length",
                2: "Weight / Mass",
                3: "Temperature",
                4: "Area",
                5: "Volume",
                6: "Time",
                7: "Speed",
                8: "Pressure",
                9: "Energy"

            }
            if 0 <category <= 9:
                print("-{You have selected the valid option number", category, "corresponding to", thisdict[category], ".}-\n")
                selected_category = thisdict[category]
                break
            else:
                print("[[Please select a number within the range 1 - 9.]]")
                print("[[Try again]]\n")
                continue
        except ValueError:
             print("[[You have chosen an invalid option or reponded incorrectly]]")
             print("[[Please try again.]]\n")
             continue
    return(selected_category)



def distance_or_length_conversion_module(user_choice):
    if user_choice != "Distance / Length":
        print("[[category 1 has not been selected, conversion not performed.]]")
        return None
    else:
        def unit_selection_1():
                while True:
                    print("From the following measurement category select the unit you would like to convert from;")
                    print("1. Meters (m) ")
                    print("2. Kilometers (km)")
                    print("3. Miles (M)")
                    print("4. Feet (ft)")
                    print("5. Inches (in)")
                    print("6. Centimeters (cm)")
                    print("7. Milimeters (mm)\n")
                    try: 
                        unit_choice_1 = int(input("Enter option number here:"))
                        if unit_choice_1 > 0 and unit_choice_1 <= 7:
                            print("-{You have successfully selected a valid option!}-")
                            break
                        elif unit_choice_1 < 0 or unit_choice_1 > 9:
                            print("[[Please try again by entering an existing value]]")
                            continue
                    except ValueError:
                        print("[[Please try again and enter a valid numerical value]]")
                        continue
                return unit_selection_1()

user_choice_1 = menu()
distance_or_length_conversion_module(user_choice_1)