import os
import re

word_list = open('D:\\python\\wordle\\valid-wordle-words.txt', 'r')

words = []
for line in word_list:
    if line != "\n":
        words.append(line.strip())
word_list.close()

counts = []

position_leaderboard = [[],[],[],[],[]]
letter_leaderboard = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    counts.append([0,0,0,0,0])
    letter_leaderboard.append([letter, 0])
    for i in range(5):
        position_leaderboard[i].append(["",0])

for letter in alphabet:
    for word in words:
        for ltr in range(5):
            if word[ltr] == letter:
                counts[alphabet.index(letter)][ltr] += 1

for letter in alphabet:
    for i in range(5):
        position_leaderboard[i][alphabet.index(letter)][0] = letter.capitalize()
        position_leaderboard[i][alphabet.index(letter)][1] = counts[alphabet.index(letter)][i]

for letter in range(26):
    for word in words:
        if alphabet[letter] in word:
            letter_leaderboard[letter][1] += 1


def count(elem):
    return elem[1]

for i in range(5):
    position_leaderboard[i].sort(key=count, reverse=True)

word_points = []

index = 0
for word in words:
    word_points.append([word.upper(), 0])
    for i in range(5):
        for j in range(26):
            if (word[i].upper() == position_leaderboard[i][j][0]):
                word_points[index][1] += position_leaderboard[i][j][1]
    index += 1

word_points.sort(key=count, reverse=True)

word_points_2 = []

index = 0
for word in words:
    word_points_2.append([word.upper(), 0])
    for i in range(26):
        if alphabet[i] in word:
            word_points_2[index][1] += letter_leaderboard[i][1]
    index += 1

word_points_2.sort(key=count, reverse=True)

filename = "./wordle/green-letter-words.txt"

if os.path.exists(filename):
    f = open(filename, "w")
else:
    f = open(filename, "x")

for word in word_points:
    f.write(word[0].lower()+"\n")

f.close()

filename = "./wordle/yellow-letter-words.txt"

if os.path.exists(filename):
    f = open(filename, "w")
else:
    f = open(filename, "x")

word_points_2_just_words = []
for word in word_points_2:
    f.write(word[0].lower()+"\n")
    word_points_2_just_words.append(word[0].lower())

f.close()

r = re.compile(".*[aeros].*")
delete_words = list(filter(r.match, word_points_2_just_words))

for word in delete_words:
    word_points_2_just_words.remove(word)

for word in word_points_2_just_words:
    print(word)

letter_leaderboard.sort(key=count, reverse=True)

output =  "+-----------------------------------------------------------+\n"
output += "|     1     |     2     |     3     |     4     |     5     |\n"
output += "+-----------------------------------------------------------+\n"

for letter in alphabet:
    output += "| {:1s} - {:-5d} | {:1s} - {:-5d} | {:1s} - {:-5d} | {:1s} - {:-5d} | {:1s} - {:-5d} |\n".format(position_leaderboard[0][alphabet.index(letter)][0],position_leaderboard[0][alphabet.index(letter)][1],position_leaderboard[1][alphabet.index(letter)][0],position_leaderboard[1][alphabet.index(letter)][1],position_leaderboard[2][alphabet.index(letter)][0],position_leaderboard[2][alphabet.index(letter)][1],position_leaderboard[3][alphabet.index(letter)][0],position_leaderboard[3][alphabet.index(letter)][1],position_leaderboard[4][alphabet.index(letter)][0],position_leaderboard[4][alphabet.index(letter)][1])
    output += "+-----------------------------------------------------------+\n"

filename = "./wordle/letters-leaderboard.txt"

if os.path.exists(filename):
    f1 = open(filename, "w")
else:
    f1 = open(filename, "x")

f1.write(output)
f1.close()

#print(output)
#print("")

letter_output =  "        +-----------+\n"
letter_output += "        |  LETTERS  |\n"
letter_output += "+-------+-----------+\n"

for i in range(26):
    letter_output += "| {:5d} | {:1s} - {:5d} |\n".format(i+1, letter_leaderboard[i][0], letter_leaderboard[i][1])
    letter_output += "+-------+-----------+\n"

#print(letter_output)

best_word_2_output =  "        +----------------+\n"
best_word_2_output += "        |  BEST WORDS 2  |\n"
best_word_2_output += "+-------+----------------+\n"

for i in range(len(word_points_2)):
    best_word_2_output += "| {:5d} | {:5s} -- {:5d} |\n".format(i+1,word_points_2[i][0],word_points_2[i][1])
    best_word_2_output += "+-------+----------------+\n"

#print(best_word_2_output)

# best_word_output =  "        +----------------+\n"
# best_word_output += "        |   BEST WORDS   |\n"
# best_word_output += "+-------+----------------+\n"

# for i in range(len(word_points)):
#     best_word_output += "| {:5d} | {:5s} -- {:5d} |\n".format(i+1,word_points[i][0],word_points[i][1])
#     best_word_output += "+-------+----------------+\n"

# filename = "./wordle/words-leaderboard.txt"

# if os.path.exists(filename):
#     f2 = open(filename, "w")
# else:
#     f2 = open(filename, "x")

# f2.write(best_word_output)
# f2.close()

# print(best_word_output)