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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


class Textline:
    def __init__(self, list):
        self.incoming = list[0]
        self.answering = list[1]
        self.time = list[2]
        if len(list) > 3:
            self.seconds = list[3]


# changed list to set as suggested in review
number_set = set()

for line in texts:
    record = Textline(line)
    number_set.add(record.incoming)
    number_set.add(record.answering)

for line in calls:
    record = Textline(line)
    number_set.add(record.incoming)
    number_set.add(record.answering)

count = len(number_set)

print("There are "+str(count)+" different telephone numbers in the records.")
