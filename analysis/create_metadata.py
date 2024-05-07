import json
import os

# Predefined list of metadata keys
metadata_keys = ['title', 'author', 'date', 'description']

# Initialize an empty dictionary to store metadata
metadata = {}

folder_path = folder = r"C:\Users\Goerner\Desktop\Hamburg_zaehlstellen"

# Ask user to input metadata keys and values
while True:
    key = input("Enter metadata key (press Enter to stop): ").strip()
    if not key:
        break  # Stop loop if user presses Enter without inputting a key
    value = input("Enter metadata value: ").strip()
    metadata[key] = value

metadata["folderpath"] = folder_path

# Write metadata to a JSON file in the specified folder
metadata_file = os.path.join(folder_path, "metadata.json")
with open(metadata_file, "w") as file:
    json.dump(metadata, file, indent=4)

print("Metadata has been saved to metadata.json")