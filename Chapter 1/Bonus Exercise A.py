#------------------- BONUS EXERCISE A -------------------------------------

# THIS PROGRAM PRINTS MULTIPLICATION TABLES FROM 1 TO 10
# OUTER LOOP SELECTS WHICH TABLE NUMBER
# INNER LOOP PRINTS MULTIPLICATION TABLE


for i in range(1, 11):
    print(f"\nMultiplication table of : {i}")

    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
        
