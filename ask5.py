# libraries
import re
from collections import Counter


# functions
def remove_non_letters(tempdata):
    pattern = "[^a-z\s]"
    repl = ""
    return re.sub(pattern, repl, tempdata, 0, re.IGNORECASE | re.MULTILINE)

def unique(words):
    seen = set()
    return [x for x in words if not (x in seen or seen.add(x))]


# main code
with open("two_cities_ascii.txt", "r") as file1:
    tempdata = file1.read()
    data = remove_non_letters(tempdata) # replaces every character that isn't a letter or space with ""
    data = data.lower() # converts all uppercase characters to lowercase

    with open("modified2.txt", "w") as file2:
        file2.write(data)
        words = data.split() # edited text is split into words by whitespace
        print("Words from two_cities_ascii.txt:", words, "\n")

        mostCommonWords = Counter(words).most_common(10) # returns the 10 most common words
        print("10 most common words:", end=" ")
        print(", ".join(str(mostCommonWords[i][0]) for i in range(len(mostCommonWords))), "\n")


        firstTwo = []
        setWords = unique(words)
        for j in range(len(setWords)):
            firstTwo.append(setWords[j][:2]) # creates a list of the first two letters every word starts with
        mostCommon2Letters = Counter(firstTwo).most_common(3) # returns the 3 most common first two letters

        print("3 most common first two letters:", mostCommon2Letters)
        print("First 3 combos of the first 2 letters that most words begin with:", end=" ")
        # prints the first 3 combos of the first 2 letters that most words start with
        print("-".join(str(mostCommon2Letters[i][0]) for i in range(len(mostCommon2Letters))), "\n")


        firstThree = []
        for z in range(len(setWords)):
            firstThree.append(setWords[z][:3]) # creates a list of the first three letters every word starts with
        mostCommon3Letters = Counter(firstThree).most_common(3) # returns the 3 most common first three letters

        print("3 most common first three letters:", mostCommon3Letters)
        print("First 3 combos of the first 3 letters that most words begin with:", end=" ")
        # prints the first 3 combos of the first 3 letters that most words start with
        print("-".join(str(mostCommon3Letters[i][0]) for i in range(len(mostCommon3Letters))), "\n")
