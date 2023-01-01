with open('data.txt', 'r') as f:
    document = f.read()

# Split the document into a list of lines
lines = document.split('\n')

# Initialize an empty list to store the rows of the CSV
csv_rows = []

# Loop through the lines of the document
for i, line in enumerate(lines):
    # If a line starts with "flights:", append the next line to the list of CSV rows
    if line.startswith('flights:'):
        csv_rows.append(lines[i + 1])

# Join the rows of the CSV with a newline character
csv_str = '\n'.join(csv_rows)

# Write the result to a file
with open('output2.csv', 'w') as f:
    f.write(csv_str)
