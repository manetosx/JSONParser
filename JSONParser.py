import json
import jmespath
import os

# Get the absolute file path
fileName = input("Enter your file's name: ")
file_path = os.path.join(os.getcwd(), fileName)

# Read data from the JSON file
with open(file_path, "r") as file:
    data = json.load(file)


#query = ""     # Figure out your query and change this, without this the script won't work
result = jmespath.search(query, data)

# Filter out None values # May need to change the variable value to fit your query(What you need to extract. E.g I wanted to extract the field "value" from my JSON file)
result = [value for value in result if value is not None]

# Remove the .json extension and replace it with .txt
output_file_name = os.path.splitext(fileName)[0] + ".txt"
output_file = os.path.join(os.getcwd(), output_file_name)

with open(output_file, "a") as file:
    if result:
        file.write("\n".join(result) + "\n")

print(f"Result appended to {output_file}")
