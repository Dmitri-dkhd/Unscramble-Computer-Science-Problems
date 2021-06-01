"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


class Textline:
    def __init__(self, list):
        self.incoming = list[0]
        self.answering = list[1]
        self.time = list[2]
        if len(list) > 3:
            self.seconds = list[3]


# modified loop with get and max method as suggested in review
number_dict = {}
for line in calls:
    record = Textline(line)

    number_dict[record.incoming] = number_dict.get(record.incoming, 0) + int(record.seconds)
    number_dict[record.answering] = number_dict.get(record.answering, 0) + int(record.seconds)


max_time_number = max(number_dict, key=number_dict.get)
max_time = number_dict.get(max_time_number)

print(max_time_number+' spent the longest time, ' + str(max_time) +
      ' seconds, on the phone during September 2016.')
