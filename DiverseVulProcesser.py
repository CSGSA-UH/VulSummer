import json

# Define the path to the input and output files
input_path = '/Users/devin/OneDrive/Desktop/Database/SWE/REU2024/Data/diversevul.json'  # JSON lines file
output_path = '/Users/devin/OneDrive/Desktop/Database/SWE/REU2024/Data/processedData.json'

def process_data(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        # Process each line in the input JSON lines file
        for line in infile:
            # Parse the JSON data
            data = json.loads(line)
            
            # Extract necessary fields
            func = data.get('func', '') # The actual code
            target = data.get('target', 0) # Indicates if code is vulnerable or not (1 or 0)
            cwe = data.get('cwe', []) # Common Weakness Enumeration
            message = data.get('message', '') # Commit message.
            
            # Create a new JSON object
            new_data = {
                'func': func,
                'target': target,
                'cwe': cwe,
                'message': message
            }
            
            # Write the new JSON object to the output file
            json.dump(new_data, outfile)
            outfile.write('\n')  # Newline for JSON lines format

# Call the function with your file paths
process_data(input_path, output_path)

print('Dataset has been processed!')
