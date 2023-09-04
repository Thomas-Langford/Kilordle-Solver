letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    words = open("all_words.txt").read().splitlines()
    scores = {}
    init_dict(scores)

    for word in words:
        count_letters_at_pos(scores, word)
    
    ranking = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    out = open("letters_by_rank.txt", "a")
    for i in ranking:
        out.write(f"{i[0]} {i[2]}\n")

def count_letters_at_pos(d, word):
    for i in range(len(word)):
        key = f"{word[i]}_{i}"
        d[key] += 1

def init_dict(d):
    for i in letters:
        for j in range(5):
            key = f"{i}_{j}"
            d[key] = 0


if __name__ == "__main__":
    main()