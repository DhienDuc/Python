# madlibs generator
with open("Madlibs.txt","r") as f:
    story = f.read()

# initial data
words = []
start_idx = -1
search_start = '['
search_end = ']'

# search through story to find key inside []
for i, char in enumerate(story):
    # find start search charater
    if char == search_start:
        start_idx = i
    # find end search charater
    if char == search_end and start_idx != -1:
        # add to words list
        word = story[start_idx : i+1]
        words.append(word)
        # reset index
        start_idx = -1

# initial dictionary to store key data input by user
answers = {}
for word in words:
    answer = input("Enter " + word + ": ")
    answers[word] = answer

# replace word
for word in words:
    story = story.replace(word, answers[word])

print(story)
