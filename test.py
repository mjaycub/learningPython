import json
from pprint import pprint

with open('data.json') as file:
	data = json.load(file)

# pprint(data)

# Access the 'data' object and get the 'transcript' attribute
storyTranscript = data["transcript"]
pprint(storyTranscript)

# Remember arrays work on "zero-based indexing/numbering"
# This means that the initial element is assigned the index 0
# To access the FIRST word in our words array, we access data["words"][0]
firstWord = data["words"][0]["word"]
pprint("The first word is: " + firstWord)