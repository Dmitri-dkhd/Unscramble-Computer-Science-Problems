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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
class Textline:
    def __init__(self, list):
        self.incoming = list[0]
        self.answering = list[1]
        self.time = list[2]
        if len(list) > 3:
            self.seconds = list[3]

first_record = Textline(texts[0])

last_record = Textline(calls[-1])

print("First record of texts, "+first_record.incoming + " texts " +
      first_record.answering + " at time "+first_record.time)

print("Last record of calls, "+last_record.incoming + " calls "+last_record.answering +
      " at time "+last_record.time+", lasting " + last_record.seconds+" seconds")