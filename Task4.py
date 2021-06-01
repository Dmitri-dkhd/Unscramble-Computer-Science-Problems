"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


class Textline:
    def __init__(self, list):
        self.incoming = list[0]
        self.answering = list[1]
        self.time = list[2]
        if len(list) > 3:
            self.seconds = list[3]


# changed list to set as suggested in review
excluded_set = set()

for line in texts:

    record = Textline(line)
    excluded_set.add(record.incoming)
    excluded_set.add(record.answering)

for line in calls:

    record = Textline(line)
    excluded_set.add(record.answering)

marketing_set = set()

for line in calls:

    record = Textline(line)
    if record.incoming not in excluded_set:

        # fixed the output
        marketing_set.add(record.incoming)

print("These numbers could be telemarketers: ")
for line in sorted(marketing_set):
    print(line)
