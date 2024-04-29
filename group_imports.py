import re
from collections import defaultdict

# Path to the temporary file generated by the bash script
temp_file = 'imports_found.txt'
report_file = 'mui_usage.txt'

# Dictionary to hold the mapping of component to file paths
imports_dict = defaultdict(set)

# Regular expression to extract components from new import style
component_regex = re.compile(r"import\s+([^\s]+)\s+from\s+'~/components/")

# Read the temporary file and populate the dictionary
with open(temp_file, 'r') as file:
  for line in file:
    filepath, import_statement = line.split(':')
    component_match = component_regex.search(import_statement)
    if component_match:
      component = component_match.group(1)
      imports_dict[component].add(filepath.strip())

# Writing to the report file, sorted alphabetically
with open(report_file, 'w') as file:
  for component in sorted(imports_dict):
    file.write(f"{component}\n")
    for filepath in sorted(imports_dict[component]):
      file.write(f"  - {filepath}\n")
    file.write("\n")
