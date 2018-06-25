l = ['ADJECTIVE','NOUN','ADVERB','VERB']
s = r'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
print(s)
for word in l:
    if word in s:
        print('enter a ' + word.lower())
        i = input()
        s = s.replace(word,i)

print(s)