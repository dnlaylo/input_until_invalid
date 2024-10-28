# Method for segregating number entries
def sort_num(entries):
    range_one, range_two, range_three, range_four, range_five = None

    for num in entries:
        if num >= 1 and num <= 10:
            range_one.append(num)
        elif num >= 11 and num <= 20:
            range_two.append(num)
        elif num >= 21 and num <= 30:
            range_three.append(num)
        elif num >= 31 and num <= 40:
            range_four.append(num)
        elif num >= 41 and num <= 50:
            range_five.append(num)

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
