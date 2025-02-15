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

hiragana_dict = [
    {"あ": "a",  "い": "i",  "う": "u",  "え": "e",  "お": "o"},
    {"か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko"},
    {"さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so"},
    {"た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to"},
    {"な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no"},
    {"は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho"},
    {"ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo"},
    {"や": "ya", "ゆ": "yu", "よ": "yo"},
    {"ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro"},
    {"わ": "wa", "を": "wo"},
    {"ん": "n"},
    {"が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go"},
    {"ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo"},
    {"だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do"},
    {"ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo"},
    {"ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"},
    {"きゃ": "kya", "きゅ": "kyu", "きょ": "kyo"},
    {"しゃ": "sha", "しゅ": "shu", "しょ": "sho"},
    {"ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho"},
    {"にゃ": "nya", "にゅ": "nyu", "にょ": "nyo"},
    {"ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo"},
    {"みゃ": "mya", "みゅ": "myu", "みょ": "myo"},
    {"りゃ": "rya", "りゅ": "ryu", "りょ": "ryo"},
    {"ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo"},
    {"じゃ": "ja",  "じゅ": "ju",  "じょ": "jo"},
    {"びゃ": "bya", "びゅ": "byu", "びょ": "byo"},
    {"ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"}
]

columns = ["A", "I", "U", "E", "O"]

def character_practice(type):
    # return "Modo practica"
    print("🇯🇵  Mode Practice On 🍥\n")
    flag = True
    n_correct = 0
    
    while(flag):
        if type == "katakana":
            random_dict = random.choice(katakana_dict)
        elif type == "hiragana":
            random_dict = random.choice(hiragana_dict)
            
        random_item = random.choice(list(random_dict.items()))
        answer = input(f"\t\t\t  {n_correct+1} -> {random_item[0]}: ")
        if answer.lower() == random_item[1]:
            n_correct += 1
            continue
        else:
            print(f"❌ Incorrect: {random_item[0]} -> {random_item[1]}\n")
            flag = False
    return n_correct

# def view_word():
#     word = input("🔍 Insert the word in romaji: ")

def view_random_word():
    try:
        with open("katakana-words.txt", "r", encoding="utf-8") as file:

            lineas = file.readlines()
            
            # limpiar saltos de linea y guardar en una lista
            palabras = [linea.strip() for linea in lineas]
            
            palabra_aleatoria = random.choice(palabras)
            
            # Imprimir la palabra al azar
            print(f'\n\t\tPalabra al azar: {palabra_aleatoria}\n')
        
    except FileNotFoundError:
        print("File Not Found -> Closing app :( ")
        exit()


def view_dict(type):
    # for key,value in katakana_dict.items():
    #     print(f"{key} -> {value}")

    if type == "katana":
        print("\n\t📜 Katakana Chart 📜")
    elif type == "hiragana":
        print("\n\t📜 Hiragana Chart 📜")

    print("──────────────────────────────────────")
    print("       " + "      ".join(columns))  # Encabezado

    dict = katakana_dict if type == "katakana" else hiragana_dict if type == "hiragana" else None
    for elem in dict:
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
    print(" 0️⃣  Exit")
    print(" 1️⃣  Start Katakana Practice")
    print(" 2️⃣  Start Hiragana Practice")
    print(" 3️⃣  View Katakana Dict")
    print(" 4️⃣  View Hiragana Dict")
    print(" 5️⃣  View Katakana Random Word")
    
    # ---- Timer: Cuanto tiempo dedicaste a practicar! ----
    timer = 0
    
    # ---- Main program: ----
    mode = int(input("\nSelect an option (0-5): "))

    if mode == 0:
        exit_app()
    
    elif mode == 1:
        try:
            with open("record.txt", "r") as file:
                current_record = int(file.read().strip())
        
        except FileNotFoundError:
            current_record = 0
        print("──────────────────────────────────────")
        print(f"\nThe actual record is: {current_record}! 📚")

        n_corrects = character_practice("katakana")
        print (f"🇯🇵 Numbers char correct: {n_corrects} 😈")
        
        if n_corrects > current_record:
            with open("record.txt", "w") as file:
                file.write(str(n_corrects))  
            print(f"¡New Record! Actual score: {n_corrects}.")
        else:
            print(f"Keep working: Record is still: {current_record}.\n")

    elif mode == 2:
        try:
            with open("record-hiragana.txt", "r") as file:
                current_record = int(file.read().strip())
        
        except FileNotFoundError:
            current_record = 0
        print("──────────────────────────────────────")
        print(f"\nThe actual record is: {current_record}! 📚")

        n_corrects = character_practice("hiragana")
        print (f"🇯🇵 Numbers char correct: {n_corrects} 😈")
        
        if n_corrects > current_record:
            with open("record-hiragana.txt", "w") as file:
                file.write(str(n_corrects))  
            print(f"¡New Record! Actual score: {n_corrects}.")
        else:
            print(f"Keep working: Record is still: {current_record}.\n")


    elif mode == 3: # Katakana Dict
        view_dict("katakana")

    elif mode == 4: # Katakana Dict
        view_dict("hiragana")
    
    elif mode == 5:
        view_random_word()
    
    else:
        print("\n❌ Invalid choice! Please select a valid option.\n")


if __name__ == "__main__":
    print("\n\t\t 🇯🇵  Welcome to the Katakana Practice App! 🎌")
    print()
    while(True):
        main()  