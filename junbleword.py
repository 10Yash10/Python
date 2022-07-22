import random
d1 = ["fruits",
      "Vegetables",
      "animals",
      "bikes",
      "encyclopedia",
      "kingdom",
      "amazing",
      "submit",
      "trimmer",
      "transmission"]
def selectWord(word):
    selected_word = random.choice(word)
    return selected_word

def jumble(word):
    rand_word = random.sample(word,len(word))
    jumbledWord = "".join(rand_word)
    return jumbledWord

word = selectWord(d1)
print(jumble(word))

str = input("Guess the word: ")
if str in d1:
    print("you have won")
else:
    print("Try again")
    