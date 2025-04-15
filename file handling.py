import os

def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    # Check if file exists and can be read
    if not os.path.isfile(filename):
        print(f"❌ Error: The file '{filename}' does not exist.")
        return

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            print("✅ File read successfully.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    # Modify the content (e.g., reverse each line)
    modified_content = '\n'.join(line[::-1] for line in content.splitlines())

    # Create a new filename for output
    output_filename = 'modified_' + filename

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}'.")
    except Exception as e:
        print(f"❌ Error writing file: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
