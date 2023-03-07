import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("E:/Projects/DataSet/FullmetalAlchemist03.xml")
root = tree.getroot()

# Create a list to hold the data
data = []

# Loop through the 'd' elements and extract the data
for d in root.findall("d"):
    timestamp = int(
        float(d.attrib["p"].split(",")[0]) * 1000000
    )  # Convert seconds to microseconds
    content = d.text
    if content is not None:
        content = content.strip()
    data.append({"timestamp": timestamp, "content": content, "key": 3})

# Write the data to a CSV file
with open(
    "E:/Projects/DataSet/CSV/FullmetalAlchemist03.csv",
    "w",
    newline="",
    encoding="utf-8-sig",
) as csvfile:
    fieldnames = ["timestamp", "content", "key"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
