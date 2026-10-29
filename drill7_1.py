# 1. Prepare file handle and counters
handle = open("mbox-short.txt")
confidence_total = 0
confidence_count = 0

# 2. Loop through lines, find X-DSPAM-Confidence and extract float numbers
for line in handle:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        colon = line.find(":")
        number = float(line[colon + 1:])
        confidence_total = confidence_total + number
        confidence_count = confidence_count + 1

# 3. Calculate average and print the result
if confidence_count > 0:
    average = confidence_total / confidence_count
    print("Average spam confidence:", average)

else:
    print('No confidence lines found.')