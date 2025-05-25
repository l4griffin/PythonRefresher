values = []

for i in range(5):
    val = float(input(f"Enter value {i+1}: "))
    values.append(val)

average = sum(values) / len(values)
print(f"The average is: {average}")