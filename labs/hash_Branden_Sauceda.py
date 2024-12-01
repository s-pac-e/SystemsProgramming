import hashlib
import sys

def main():
    # Ensure at least one argument (input file) is provided
    if len(sys.argv) < 2:
        print("Error: No input file specified.")
        sys.exit(1)

    # Extract input file and optional hash algorithm
    input_file = sys.argv[1]
    hash_algorithm = sys.argv[2] if len(sys.argv) > 2 else "sha256"
    output_file = "output.txt"

    # Check if the specified hash algorithm is valid
    if hash_algorithm not in hashlib.algorithms_available:
        print(f"Provided unknown hash, using the default sha256 hash.")
        hash_algorithm = "sha256"

    try:
        # Read the input file
        with open(input_file, 'rb') as file:
            file_content = file.read()

        # Compute the hash
        hash_func = hashlib.new(hash_algorithm)
        hash_func.update(file_content)
        hash_value = hash_func.hexdigest()

        # Write the hash to the output file
        with open(output_file, 'w') as output:
            output.write(hash_value)
        print(f"Hash successfully written to {output_file} using {hash_algorithm}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
