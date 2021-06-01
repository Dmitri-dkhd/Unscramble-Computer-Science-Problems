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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


class Textline:
    def __init__(self, list):
        self.incoming = list[0]
        self.answering = list[1]
        self.time = list[2]
        if len(list) > 3:
            self.seconds = list[3]


# changed list to set as suggested in review
bangolore_set = set()
counter_in = 0
counter_ans = 0

for line in calls:
    record = Textline(line)

    if record.incoming[:5] == "(080)":

        if ' ' in record.answering:
            bangolore_set.add(record.answering[:4])

        if "(" in record.answering:
            code = ""
            for i in record.answering:
                code += i
                if i == ")":
                    bangolore_set.add(code)
                    break

        if "140" in record.answering[:3]:
            bangolore_set.add(record.answering[:3])

        # fixed the whitespaces for counter_in and counter_ans

        counter_in += 1
        if record.answering[:5] == "(080)":
            counter_ans += 1

print("The numbers called by people in Bangalore have codes:")
for line in sorted(bangolore_set):
    print(line)

# fixed the procentage with "round"
print(round(counter_ans*100/counter_in, 2),
      'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
