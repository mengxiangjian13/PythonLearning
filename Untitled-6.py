import re

regrex = re.compile(r'^(alice|bob|carol)+\s(alice|bob|carol)+\s(alice|bob|carol)$',re.IGNORECASE)
s = input()
mo = regrex.search(s)

print(mo.group())