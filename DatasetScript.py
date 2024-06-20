import json
import pandas as pd
import re

# File paths
# json_path = r"C:/Users/devin/OneDrive/Desktop/Desktop/REUCode/CVE2/circl-cve-search-expanded.json"
cve_path = r"C:/Users/devin/OneDrive/Desktop/Database/SWE/REU2024/Data/CVEDataset/cve.csv"

# Load CSV data
cvedf = pd.read_csv(cve_path)

# Normalize and clean summaries
cvedf['summary'] = cvedf['summary'].str.lower().str.strip()
cvedf['summary'] = cvedf['summary'].str.replace(r'[^a-z0-9\s]', '', regex=True)

# Include the CWE code and summary, and drop rows with missing data
cve_data = cvedf[['cwe_code', 'summary']].dropna()

# Concatenate CWE code with summary
cve_data['summary'] = cve_data['cwe_code'].astype(str) + ' - ' + cve_data['summary']

# Prepare to collect JSON data
# json_summaries = []

# Process JSON file
# with open(json_path, 'r', encoding='utf-8') as file:
#    for line in file:
#        try:
#            json_obj = json.loads(line)
#            summary = json_obj.get('summary')
#            if summary:
#                summary = summary.lower().strip()
#                summary = re.sub(r'[^a-z0-9\s.-]', '', summary)
#                summary = re.sub(r'\s+', ' ', summary)
#                summary = re.sub(r'cross-site scripting', 'xss', summary)
#                summary = re.split(r'note: this is a different vulnerability than', summary)[0].strip()
#                json_summaries.append({'summary': summary})
#        except json.JSONDecodeError:
#            continue

# Convert JSON summaries to DataFrame
# json_summaries_df = pd.DataFrame(json_summaries)

# Combine both DataFrames
# combined_data = pd.concat([cve_data, json_summaries_df], ignore_index=True).drop_duplicates()

# Save to new CSV file
output_path = r"C:/Users/devin/OneDrive/Desktop/Database/SWE/REU2024/Data/training_data.csv"
cve_data.to_csv(output_path, index=False)

print(f"Saved cleaned and deduplicated summaries to {output_path}")
print("Sample data before preprocessing:", cvedf['summary'].sample(5))
print("Sample data after preprocessing:", cve_data['summary'].sample(5))