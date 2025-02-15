# 🌟 Welcome to the Personal-Trainer to improve your katakana lecture
# Hope you like this project, its very simple, but funny for me, i really 👋"

# print("".join(katakana_chars))
# katakana_chars = [chr(i) for i in range(0x30A0, 0x30FF)]

import time
import random

katakana_dict = [
    {"ア": "a",  "イ": "i",  "ウ": "u",  "エ": "e",  "オ": "o"},
    {"カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko"},
    {"サ": "sa", "シ": "shi","ス": "su", "セ": "se", "ソ": "so"},
    {"タ": "ta", "チ": "chi","ツ": "tsu","テ": "te", "ト": "to"},
    {"ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no"},
    {"ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho"},
    {"マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo"},
    {"ヤ": "ya", "ユ": "yu", "ヨ": "yo"},
    {"ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro"},
    {"ワ": "wa", "ヲ": "wo"},
    {"ン": "n"},
    {"ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go"},
    {"ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo"},
    {"ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do"},
    {"バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo"},
    {"パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"},
    {"キャ": "kya", "キュ": "kyu", "キョ": "kyo"},
    {"シャ": "sha", "シュ": "shu", "ショ": "sho"},
    {"チャ": "cha", "チュ": "chu", "チョ": "cho"},
    {"ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo"},
    {"ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo"},
    {"ミャ": "mya", "ミュ": "myu", "ミョ": "myo"},
    {"リャ": "rya", "リュ": "ryu", "リョ": "ryo"},
    {"ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo"},
    {"ジャ": "ja",  "ジュ": "ju",  "ジョ": "jo"},
    {"ビャ": "bya", "ビュ": "byu", "ビョ": "byo"},
    {"ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo"}
]

columns = ["A", "I", "U", "E", "O"]

def character_practice():
    # return "Modo practica"
    print("🇯🇵 Mode Practice On 🍱")
    flag = True
    n_correct = 0
    
    while(flag):
        random_dict = random.choice(katakana_dict)
        random_item = random.choice(list(random_dict.items()))
        answer = input(f"{random_item[0]}: ")
        if answer.lower() == random_item[1]:
            n_correct += 1
            continue
        else:
            flag = False
    return n_correct



def view_dict():
    # for key,value in katakana_dict.items():
    #     print(f"{key} -> {value}")

    print("\n\t📜 Katakana Chart 📜")
    print("──────────────────────────────────────")
    print("       " + "      ".join(columns))  # Encabezado

    for elem in katakana_dict:
        # print(elem)
        # --- Algoritmo a continuacion -> Mejorar: No se me ocurrio otra forma parcialmente
        random_item = random.choice(list(elem.items())) # (llave, valor)
        character = random_item[1][0]
        
        if character.upper() not in columns:
            dict_tolist = list(elem.items())
            print(f"{character.upper()}:", end=" ")
            for item in dict_tolist:
                print(f"{item[0]} ({item[1]})", end=" ")
            print("\n")
       
        else:
            dict_tolist = list(elem.items())
            # print(dict_tolist)
            # print(f"\t {}")
            print("\n  ", end=" ")
            for item in dict_tolist:
                print(f"{item[0]} ({item[1]})", end=" ")
            print("\n")

    print()

def exit_app():
    print("\n👋 Exiting the app. See you soon!")
    exit()

def main():
    print(" 1️⃣  Start Practice")
    print(" 2️⃣  View Katakana Dict")
    print(" 3️⃣  Exit")
    
    # ---- Timer: Cuanto tiempo dedicaste a practicar! ----
    timer = 0
    
    # ---- Main program: ----
    mode = int(input("Select an option (1-3): "))
    
    if mode == 1:
        try:
            with open("record.txt", "r") as file:
                current_record = int(file.read().strip())
        
        except FileNotFoundError:
            current_record = 0
        print("──────────────────────────────────────")
        print(f"\nThe actual record is: {current_record}! 📚")

        n_corrects = character_practice()
        print (f"🇯🇵 Numbers char correct: {n_corrects} 😈")
        
        if n_corrects > current_record:
            with open("record.txt", "w") as file:
                file.write(str(n_corrects))  
            print(f"¡New Record! Actual score: {n_corrects}.")
        else:
            print(f"Keep working: Record is still: {current_record}.")

    elif mode == 2:
        view_dict()
    
    elif mode == 3:
        exit_app()
    
    else:
        print("\n❌ Invalid choice! Please select a valid option.\n")


if __name__ == "__main__":
    print(">> Welcome to the Katakana Practice App! 🎌")
    print("──────────────────────────────────────")
    while(True):
        main()  