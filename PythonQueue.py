# Initialize an empty list to represent the queue
names = []

print("-- Enter 10 names --\n")

# Input 10 names into the queue using a for loop
for i in range(1, 11):
    name = input(f"Enter name ({i}): ")
    names.append(name)

# Print the initial queue
print("\n", names)

# Dequeuing (popping) each name and printing it
print("\nDequeuing names:\n")
while len(names) > 0:
    print(names.pop(0))

# Print the queue again after dequeuing
print("\n", names)
