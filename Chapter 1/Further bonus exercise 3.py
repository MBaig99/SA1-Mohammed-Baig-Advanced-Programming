#  Further Bonus Exercise III: Arrows (Pyramid Pattern)

rows = 5  # number of levels

for i in range(rows):
    spaces = rows - i - 1        
    stars = (2 * i) + 1          # number of stars per row
    print(" " * spaces + "*" * stars)
