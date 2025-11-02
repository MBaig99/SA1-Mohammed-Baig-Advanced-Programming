# Exercise B: Locations List

# Example List
locations = ['Dubai', 'Paris', 'Switzerland', 'London', 'Amsterdam', 'New York']

# 1️ Print the list and its length
print("Original list:", locations)
print("Length of list:", len(locations))

# 2️ Print alphabetically using sorted() without modifying the original
print("\nSorted (alphabetical, temporary):", sorted(locations, key=str.lower))

# 3️ Show list is still in original order
print("Still original order:", locations)

# 4️ Print reverse alphabetical using sorted() again
print("\nSorted (reverse alphabetical):", sorted(locations, key=str.lower, reverse=True))

# 5️ Show list is still same
print("Still original order:", locations)

# 6️ Use reverse() to reverse the order
locations.reverse()
print("\nAfter reverse():", locations)

# 7️ Use sort() to sort alphabetically
locations.sort(key=str.lower)
print("After sort() alphabetical:", locations)

# 8️ Use sort() again to sort in reverse alphabetical order
locations.sort(key=str.lower, reverse=True)
print("After sort() reverse alphabetical:", locations)
