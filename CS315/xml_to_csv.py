import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file, csv_file):
    # Step 1: collect all fieldnames (first pass)
    fieldnames = set()

    print(f"Scanning fields in {xml_file}...")

    for event, elem in ET.iterparse(xml_file, events=("end",)):
        if elem.tag == "row":
            fieldnames.update(elem.attrib.keys())
            elem.clear()

    fieldnames = list(fieldnames)
    print(f"Total fields: {len(fieldnames)}")

    # Step 2: write CSV (second pass)
    print(f"Writing CSV {csv_file}...")

    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for event, elem in ET.iterparse(xml_file, events=("end",)):
            if elem.tag == "row":
                writer.writerow(elem.attrib)
                elem.clear()

    print(f"Done: {xml_file} → {csv_file}")
files = ["PostHistory"]

for file in files:
    xml_to_csv(f"{file}.xml", f"{file}.csv")