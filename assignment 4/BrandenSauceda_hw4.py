import os
import sys
import pwd
import grp
import stat

# Function to perform the "details" operation
def details_operation(ext, directory):
    try:
        # Iterate over files in the given directory
        for filename in os.listdir(directory):
            # Check if the file has the specified extension
            if filename.endswith(ext):
                filepath = os.path.join(directory, filename)
                
                # Get file stats
                file_stat = os.stat(filepath)
                
                # Get file permissions in octal
                permissions = oct(file_stat.st_mode & 0o777)
                
                # Get file owner's username and group
                owner = pwd.getpwuid(file_stat.st_uid).pw_name
                group = grp.getgrgid(file_stat.st_gid).gr_name

                # Print file details
                print(f"File: {filename}")
                print(f"Permissions: {permissions}")
                print(f"Owner: {owner}")
                print(f"Group: {group}")
                print()

    except Exception as e:
        print(f"Error: {e}")

# Function to perform the "search" operation
def search_operation(ext, directory, search_keyword):
    try:
        # Iterate over files in the given directory
        for filename in os.listdir(directory):
            # Check if the file has the specified extension
            if filename.endswith(ext):
                filepath = os.path.join(directory, filename)
                
                # Open and search the file for the keyword
                with open(filepath, 'r') as file:
                    found = False
                    for line in file:
                        if search_keyword in line:
                            found = True
                            break
                    
                if found:
                    print(f"Keyword found in file: {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 yourname_hw4.py <operation> <ext> <directory> [search_keyword]")
        sys.exit(1)

    operation = sys.argv[1]
    ext = sys.argv[2]
    directory = sys.argv[3]

    if operation == "details":
        # Perform details operation
        details_operation(ext, directory)
    elif operation == "search":
        if len(sys.argv) < 5:
            print("Search keyword required for 'search' operation")
            sys.exit(1)
        
        search_keyword = sys.argv[4]
        # Perform search operation
        search_operation(ext, directory, search_keyword)
    else:
        print("Invalid operation. Use 'details' or 'search'")
        sys.exit(1)
