#!/usr/bin/python3
for i in range(97, 123):
    if i == 'q' or i == 'e':
        continue
    print("{:c}".format(i), end='')
