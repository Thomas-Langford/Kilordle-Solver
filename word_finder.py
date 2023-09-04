letters_by_freq = [
    "e",
    "t",
    "a",
    "o",
    "i",
    "n",
    "s",
    "h",
    "r",
    "d",
    "l",
    "c",
    "u",
    "m",
    "w",
    "f",
    "g",
    "y",
    "p",
    "b",
    "v",
    "k",
    "j",
    "x",
    "q",
    "z"
]

solved = {k:[False for x in range(5)] for k in reversed(letters_by_freq)}

letter_order = [x for x in reversed(open("letters_by_rank.txt").read().splitlines())]

def main():
    words = open("all_words.txt").read().splitlines()

    chosen_words = list()

    print("Starting search...")
    count = 1
    while not all_solved():
        letter, pos = smart_next_letter_and_pos()
        word, score = choose_best_next_word(words, letter, pos)
        print(f"Word {count}: {word} with score {score}")
        if word == "":
            print(f"Could not find {letter} at position {pos}")
            print("Skipping...")
            solved[letter][pos] = True
            continue
        mark_used_letters(word)
        chosen_words.append(word)
        count += 1

    result = sorted(chosen_words, key=sort_words)
    output = open("out.txt", "a")
    for i in result:
        output.write(f"{i}\n")
    
def sort_words(word):
    score = 0
    for i in word:
        score += letters_by_freq.index(i)
    return score

def all_solved():
    for i in solved.keys():
        for j in range(len(solved[i])):
            if not solved[i][j]:
                return False
    return True

def choose_best_next_word(words, letter, pos):
    
    possible_words = get_words_with_letter_at_pos(words, letter, pos)
    best_word, score = score_potential_words(possible_words)
    return best_word, score
    
def mark_used_letters(word):
    for i in range(len(word)):
        solved[word[i]][i] = True

# Scores words based on how many unpositioned letters they get
def score_potential_words(words):
    best = ""
    best_score = 0

    for word in words:
        score = score_word(word)
        if score > best_score:
            best_score = score
            best = word

    return best, best_score

def score_word(word):
    score = 0
    for j in range(len(word)):
        if not letter_used(word[j], j):
            pair = f"{word[j]} {j}"
            pos = len(letter_order) - letter_order.index(pair)
            score += pos
    return score

def letter_used(letter, pos):
    return solved[letter][pos]

def get_words_with_letter_at_pos(words, letter, pos):
    result = list()
    for i in words:
        if i[pos] == letter:
            result.append(i)
    return result

def smart_next_letter_and_pos():
    for i in letter_order:
        letter = i[0]
        pos = int(i[2])
        if not solved[letter][pos]:
            print(f"Next letter is {letter} at position {pos}")
            return letter, pos
    return "", -1

def next_letter_and_pos():
    for i in solved.keys():
        for j in range(len(solved[i])):
            if solved[i][j] == False:
                print(f"Next letter is {i} at position {j}")
                return i, j
    return "", -1

if __name__ == "__main__":
    main()