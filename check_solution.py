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

def main():
    words = open("out.txt").read().splitlines()

    for word in words:
        for i in range(len(word)):
            solved[word[i]][i] = True
    
    if all_solved():
        print("All letter positions accounted for!")
    else:
        for letter in solved.keys():
            for i in range(len(solved[letter])):
                if not solved[letter][i]:
                    print(f"{letter} at position {i} is missing")


def all_solved():
    for i in solved.keys():
        for j in range(len(solved[i])):
            if not solved[i][j]:
                return False
    return True


if __name__ == "__main__":
    main()