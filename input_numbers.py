# Array to store all entries
entries = []

# Loop for continuous input prompt and validation
while True:
    try:
        # Prompt user to input a number from 1-50
        entry = int(input("Please input a number within 1-50: "))

    except:
        print("")
       
# If statement for checking input
# If valid, proceed to storing in the array
# If input is invalid, display count of all valid inputs within its number group/range