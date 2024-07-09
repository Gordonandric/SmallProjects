# Gordon Andric
# Programming
# 24 March 18
# RandomData
# Write a program called RandomData.py that creates a data file of at least 10 lines (records) with 8 random numbers per line (fields). 
# Your data file should be called numbers.data. Then open your data file and read each record.

# Import random module
import random

# Open a text file with write method
text_file = open("numbers.data", "w")

# Loop to generate 10 lines that each contain 8 random number
for i in range(10):
    # Loop to generate 8 random numbers for each line
    for i in range(8):
        # Generate a randon number between 1 and 100 and conver to string
        random_num = str(random.randint(1, 100))
        # Write the random number to the file followed by a space
        text_file.write(random_num)
        text_file.write(" ")
    # Add a new line after each line of 8 random numbers
    text_file.write("\n")
    
# Close the text file
text_file.close()

# Open the text file and read it
text_file = open("numbers.data", "r")
# Print the data of the file
print(text_file.read())
# Close the file
text_file.close()

# Prompt user to press the enter key to exit
input("\n\nPress the enter key to exit")