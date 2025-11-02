# Further Bonus Exercise IV: Count items

staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", 
         "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Creating an empty dictionary to store counts
count_dict = {}

# Loop through each name and count the number of times the name appears
for name in staff:
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

# Print results
print("Staff count summary:")
for name, count in count_dict.items():
    print(f"{name}: {count}")
