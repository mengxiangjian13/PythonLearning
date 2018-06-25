import re

def fakeStrp(somestring, replace=' '):
    regex = re.compile(replace)
    replaceString = regex.sub("",somestring)
    return replaceString

s = fakeStrp('mengxiangjian and guozhenyan', 'n')
print(s)