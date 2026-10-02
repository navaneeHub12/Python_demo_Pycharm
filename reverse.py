data = "Python"
reversed_data = ""

for i in range(len(data) - 1, -1, -1):
    reversed_data += data[i]

print("Reversed string:", reversed_data)