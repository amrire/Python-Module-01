#!/usr/bin/python3

def replace_in_file(filename: str, search: str, replace: str):
    """
    Replace all occurrences of a string in a file with another string.

    :param filename: Name of the file to process.
    :param search: The string to search for.
    :param replace: The string to replace with.
    """
    try:
        # Step 1: Open the file and read its content
        with open(filename, "r") as file:
            content = file.read()
        # Step 2: Replace occurrences of the search string
        updated_content = content.replace(search, replace)
        # Step 3: Write the updated content to a new file
        output_filename = f"{filename}.new"
        with open(output_filename, "w") as output_file:
            output_file.write(updated_content)
        print(f"File updated successfully. Output written to: {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Input parameters
	input_file = "example.txt"
	search_string = "old_text"
	replace_string = "new_text"
	print(f"Processing file '{input_file}'...")
	replace_in_file(input_file, search_string, replace_string)
