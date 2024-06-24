import random


radicals = {"本": "book", "弓": "bow", "子": "child"}



if __name__ == "__main__":
    
    score = 0
    total_kanji_shown = 0
    while True:
        total_kanji_shown += 1

        radical, mnemonic = random.choice(list(radicals.items()))
        print(radical)
        
        radical_meaning = input("enter radical meaning: ")

        if radical_meaning != mnemonic:
            print("\nWRONG, TRY AGAIN!")
        else:
            print("\nCORRECT")
            score += 1

        print(f"Correct {score} out of {total_kanji_shown}\n")








