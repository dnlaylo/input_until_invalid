# Array to store all entries
entries = []

# Loop for continuous input prompt and validation
while True:
    try:
        # Prompt user to input a number from 1-50
        entry = int(input("Please input a number within 1-50: "))

        # If statement for checking input
        if entry < 1 or entry > 50:
            print("Input is not valid.\n")
            break

        # If valid, proceed to storing in the array
        entries.append(entry)

    except:
        print("Input is not valid. Integers only.\n")

# If input is invalid, display count of all valid inputs within its number group/range
