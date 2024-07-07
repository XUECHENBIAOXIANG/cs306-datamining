import xml.dom.minidom
import xml.etree.ElementTree as ET
import csv

# Function to parse XML using DOM and save as CSV
def parse_xml_dom(xml_file, csv_file):
    # Parse XML file using DOM
    dom_tree = xml.dom.minidom.parse(xml_file)
    plants = dom_tree.getElementsByTagName("PLANT")

    # Open CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write CSV header
        writer.writerow(["COMMON", "BOTANICAL", "ZONE", "LIGHT", "PRICE", "AVAILABILITY"])

        # Write data to CSV
        for plant in plants:
            common = plant.getElementsByTagName("COMMON")[0].firstChild.data
            botanical = plant.getElementsByTagName("BOTANICAL")[0].firstChild.data
            zone = plant.getElementsByTagName("ZONE")[0].firstChild.data
            light = plant.getElementsByTagName("LIGHT")[0].firstChild.data
            price = plant.getElementsByTagName("PRICE")[0].firstChild.data
            availability = plant.getElementsByTagName("AVAILABILITY")[0].firstChild.data
            writer.writerow([common, botanical, zone, light, price, availability])

# Function to parse XML using ElementTree and save as CSV
def parse_xml_elementtree(xml_file, csv_file):
    # Parse XML file using ElementTree
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write CSV header
        writer.writerow(["COMMON", "BOTANICAL", "ZONE", "LIGHT", "PRICE", "AVAILABILITY"])

        # Write data to CSV
        for plant in root.findall('PLANT'):
            common = plant.find('COMMON').text
            botanical = plant.find('BOTANICAL').text
            zone = plant.find('ZONE').text
            light = plant.find('LIGHT').text
            price = plant.find('PRICE').text
            availability = plant.find('AVAILABILITY').text
            writer.writerow([common, botanical, zone, light, price, availability])

# Paths
xml_file = "plant_catalog.xml"
csv_file_dom = "plants_dom.csv"
csv_file_elementtree = "plants_elementtree.csv"

# Parse XML using DOM and save as CSV
parse_xml_dom(xml_file, csv_file_dom)
print("CSV file saved using DOM method.")

# Parse XML using ElementTree and save as CSV
parse_xml_elementtree(xml_file, csv_file_elementtree)
print("CSV file saved using ElementTree method.")
