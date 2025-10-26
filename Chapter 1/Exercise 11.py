#----------------------------Exercise 11-----------------------------

# This program does different operations using tuple

# The given tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)


# Access value at index -3
print(f"Value at index -3: {year[-3]}")


# Reverse the tuple (I used slice)
reversed_year = year[::-1]


# Printing original and reversed tuple
print("\nOriginal Tuple:")
print(year)

print("\nReversed Tuple:")
print(reversed_year)


# Count the amount of times 2009 appears
count_2009 = year.count(2009)
print(f"/nNumber of times 2009 appears: {count_2009}")


# Get the index value of 2018
index_2018 = year.index(2018)
print(f"Index of 2018: {index_2018}")

# Length of Tuple
length = len(year)
print(f"Length of Tuple: {length}")
