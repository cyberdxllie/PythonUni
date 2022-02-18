# libraries
import re


# functions
def remove_non_letters(tempdata):
    pattern = "[^a-z\s]"
    repl = ""
    return re.sub(pattern, repl, tempdata, 0, re.IGNORECASE | re.MULTILINE)

def remove_pairs(words):
    print("Pair of words removed, with a total of 20 characters:", end=" ")
    for w1 in words:
        for w2 in words:
            if w1 != w2 and len(w1) + len(w2) == 20:
                print((w1, w2), end=" ")
                words.remove(w1)
                words.remove(w2)
                break
    print("\n")
    return words


# main code
with open("two_cities_ascii.txt", "r") as file1:
    tempdata = file1.read()
    data = remove_non_letters(tempdata) # replaces every character that isn't a letter(uppercase or lowercase) or space with ""

    with open("modified1.txt", "w") as file2:
        file2.write(data)
        words = data.split() # edited text is split into words by whitespace
        print("Words from two_cities_ascii.txt:", words, "\n")

        print("Remaining words:", remove_pairs(words), "\n") # removes pairs of words whose number of letters summed up is 20

        length = [len(x) for x in words]
        print("There are:")
        lst = []
        for i in sorted(length):
            if i in lst:
                continue

            num = sorted(length).count(i) # gets statistics based on the number of the words' letters

            if i == 1:
                if num == 1:
                    print(f"{num} word with {i} letter")
                else:
                    print(f"{num} words with {i} letter")
            else:
                if num == 1:
                    print(f"{num} word with {i} letters")
                else:
                    print(f"{num} words with {i} letters")

            lst.append(i)
