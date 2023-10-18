# Initialize an empty list called 'T'.
T = []

# Input: Ask the user to determine the size of the list
n = int(input("Enter the size of the list you want: "))

# Use a loop to take user input for the elements of the list and append each one to the list.
for i in range(0, n):
    T.append(int(input("Enter the element: ")))

# Display the original list entered by the user.
print("The entered list is:", T)

# Use selection sort algorithm to sort the list in ascending order.
for i in range(0, n):
    Min = T[i]  # Assume the current element is the minimum.
    for j in range(i, n):
        if Min > T[j]:
            Min = T[j]     # If a smaller element is found, update the minimum.
            T[j] = T[i]    # Swap the elements to sort them.
            T[i] = Min

# Output: Display the sorted list.
print("The list sorted in ascending order is:", T)
