# Using with to Automatically Close the File:
# The with statement ensures that the file is properly closed, even if an error occurs.

with open("example.txt", "w") as file:
    file.write("Writing inside the file.")
