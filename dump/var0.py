
# Create a list with 3 elements by combining values inside square brackets. 
# Variable "a" is a reference to that list.
a = [1, 2, 3]
print(a)

# Variable "b" become a reference to the same object to which "a" refers.
b = a

# The following statement checks whether "a" and "b" both refer to
# the same object. Observe that it returns "True".
b is a

# Now, try to modify "a". Append number 4 at the end of the list.
a.append(4)
print(a)

# Show the value of "b". Verify that it looks the same as "a".
print(b)

# Explicitly check whether "a" and "b" still refer to the same object.
b is a
