import random


radicals = {
    "本": "book",
    "弓": "bow",
    "子": "child",
    "牛": "cow",
    "彡": "hair",
    "手": "hand",
    "冂": "head",
    "天": "heaven",
    "王": "king",
    "儿": "legs",
    "中": "middle",
    "月": "moon",
    "ナ": "narwhal",
    "ム": "private",
    "田": "rice paddy",
    "小": "small",
    "立": "stand",
}


kanji_readings = {"大": "tie", "正": "sho"}

kanji_meaning = {"正": "correct"}


if __name__ == "__main__":

    score = 0
    total_kanji_shown = 0
    while True:
        total_kanji_shown += 1

        radical, mnemonic = random.choice(list(radicals.items()))
        print(radical)

        radical_meaning = input("enter radical meaning: ")

        if radical_meaning != mnemonic:
            print(f"\nWRONG, ITS: {mnemonic}!")
        else:
            print("\nCORRECT")
            score += 1

        print(f"Correct {score} out of {total_kanji_shown}\n")
