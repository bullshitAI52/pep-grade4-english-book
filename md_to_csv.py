import csv
import re

input_file = 'vocabulary_table.md'
output_file = 'vocabulary.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = []
for line in lines:
    line = line.strip()
    if not line or line.startswith('|---'):
        continue
    
    # Extract cells
    if line.startswith('|'):
        # Split by pipe and remove empty strings from start/end split
        cells = [c.strip() for c in line.split('|')]
        # Filter out empty strings that result from leading/trailing pipes
        cells = [c for c in cells if c]
        
        if len(cells) == 3:
            data.append(cells[1:])

with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Successfully converted {input_file} to {output_file}")
