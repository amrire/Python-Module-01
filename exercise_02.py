#!/usr/bin/python3


def main():
    # Step 1: Initialize a string variable
    string_var = "HI THIS IS BRAIN"
    # Step 2: Create references to the string
    string_ptr = string_var  # Pointer equivalent in Python (reference)
    string_ref = string_var  # Another reference to the same object
    # Step 3: Print memory addresses
    print("Memory Addresses:")
    print(f"Address of string_var: {id(string_var)}")
    print(f"Address held by string_ptr: {id(string_ptr)}")
    print(f"Address held by string_ref: {id(string_ref)}")
    # Step 4: Print values
    print("\nValues:")
    print(f"Value of string_var: {string_var}")
    print(f"Value pointed to by string_ptr: {string_ptr}")
    print(f"Value pointed to by string_ref: {string_ref}")
    

if __name__ == "__main__":
    main()
