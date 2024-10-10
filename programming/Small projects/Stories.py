with open('story.txt', 'r') as i:
    story = i.read()
    print(story, '\n')

start_word = None
words = set()
start_target = '<'
end_target = '>'

for x, y in enumerate(story):
    if y == start_target:
        start_word = x
    if y == end_target and start_word != None:
        word = story[start_word: x + 1]
        words.add(word)

answers = {}
for x in words:
    answer = input('Enter a word for ' + x +': ')
    answers[x] = answer

for z in words:
    story = story.replace(z, answers[z])

print(story)



