import subprocess

# Part a: Write "Hello World" to a file
print("Using popen to echo 'Hello World' to a file")
with open("test.txt", "w") as file:
    process = subprocess.Popen(["echo", "Hello World"], stdout=file)
    process.communicate()

# Part b: Read the contents of the file using `cat`
print("Using popen to cat test.txt")
process = subprocess.Popen(["cat", "test.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Print the contents to the screen
if process.returncode == 0:
    print(stdout.decode().strip())
else:
    print(f"Error: {stderr.decode().strip()}")
