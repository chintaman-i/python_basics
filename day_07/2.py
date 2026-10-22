#Read all the lines from a file into a list .print the total number of lines and display  the 2nd and 4th line

with open("sample.txt", "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))
print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())