# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

#add 4 to array
x.append(4)

print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
#adds y array to x array
x.extend(y)

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

#deletes array position 4 -> number 8
del x[4]

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

# insert at index 5, number 99 
x.insert(5,99)

print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

x1000 = [i * 1000 for i in x]
print(x1000)
