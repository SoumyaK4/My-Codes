import re

pattern1 = r'^for.*:$'
pattern2 = r'^while.*:$'

with open('main.py') as f:
    x = 0
    for line in f:
        if pattern1 or pattern2 in line:
            x = x + line.count(pattern1)
            x = x + line.count(pattern2)

    'while :'
        
    print(x)
