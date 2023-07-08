import json
import os

def beautify_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)

    print(f"Formatted JSON data has been written to '{output_file}'.")

# Directories
input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unformatted')
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'formatted')

# Create the 'formatted' directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

input_file = "furnidata.json"
input_path = os.path.join(input_dir, input_file)
output_file = os.path.join(output_dir, input_file)

# Convert and format the file to JSON
beautify_json(input_path, output_file)

print(f"Formatted JSON file generated: '{output_file}'")
