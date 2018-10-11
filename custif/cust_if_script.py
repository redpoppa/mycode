#!/usr/bin/env python3
message = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 30:
    message = message + 'setting video to 4k.'
elif connection >= 10:
    message = message + 'setting video to 1080p.'
elif connection >= 1:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)
