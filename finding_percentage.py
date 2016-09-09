students = int(raw_input())
dictionary = dict()

# define som
som = 0
for i in xrange(students):
    string = raw_input()
    string = string.split()
    dictionary[string[0]] = string[1], string[2], string[3]

who = raw_input()

for i in dictionary[who]:
    # turn i into integer, since it's not (yet)
    i = float(i)
    som = som + i
answer = som / 3
answer = format(answer, '.2f')
print answer
