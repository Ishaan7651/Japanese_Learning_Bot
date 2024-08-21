import random
import keyboard
from time import sleep

running = True
Correct = 0
Incorrect = 0

class Check():
    def __init__(romaji,i):
        global Correct
        global Incorrect
        ans1 = input("Enter your answer :-")
        
        if ans1 == romaji[i]:
            print("Correct")
            Correct = Correct + 1
            sleep(1)
        else:
            print("Wrong")
            Incorrect = Incorrect + 1
            sleep(1)
            print(f"The correct answer is {romaji[i]}")
            sleep(1)
        

class hiragana(Check):
    
    def __init__(self):
        global Correct
        global Incorrect
        
        
    def run(self,i):    
        chars = [
    'あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん'
]
        
        print(f"What is this charector? {chars[i]}")

        romaji = [
    'a', 'i', 'u', 'e', 'o',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'sa', 'shi', 'su', 'se', 'so',
    'ta', 'chi', 'tsu', 'te', 'to',
    'na', 'ni', 'nu', 'ne', 'no',
    'ha', 'hi', 'fu', 'he', 'ho',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ya', 'yu', 'yo',
    'ra', 'ri', 'ru', 're', 'ro',
    'wa', 'wo','n'
]
        Check.__init__(romaji,i)

# ----------END OF CLASS HIRAGANA-------------------------------------------------------------------------------------------------------------    

class katakana(Check):
    
    def __init__(self):
        global Correct
        global Incorrect

    def run(self,i):
        chars = [
    'ア', 'イ', 'ウ', 'エ', 'オ',
    'カ', 'キ', 'ク', 'ケ', 'コ',
    'サ', 'シ', 'ス', 'セ', 'ソ',
    'タ', 'チ', 'ツ', 'テ', 'ト',
    'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
    'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
    'マ', 'ミ', 'ム', 'メ', 'モ',
    'ヤ', 'ユ', 'ヨ',
    'ラ', 'リ', 'ル', 'レ', 'ロ',
    'ワ', 'ヲ', 'ン'
]
        romaji = [
    'a', 'i', 'u', 'e', 'o',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'sa', 'shi', 'su', 'se', 'so',
    'ta', 'chi', 'tsu', 'te', 'to',
    'na', 'ni', 'nu', 'ne', 'no',
    'ha', 'hi', 'fu', 'he', 'ho',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ya', 'yu', 'yo',
    'ra', 'ri', 'ru', 're', 'ro',
    'wa', 'wo', 'n'
]

        print(f"What is this charector? {chars[i]}")
        Check.__init__(romaji,i)






# ----------END OF CLASS KATAKANA-------------------------------------------------------------------------------------------------------------    

def score():
    
    print(f"Correct: {Correct}\nIncorrect: {Incorrect}")
    sleep(1)

    
def stop_program():
    global running
    running = False
    print("\nThe program has ended")
    score()
    keyboard.unhook_all()
    
keyboard.add_hotkey('esc', stop_program)
 


# ------------------MAIN CODE-------------------------------------------------------------------------------------------------------------------


print("-------------Welcome to the Japanese Quiz---------------\nLearn Japanese Charectors with us")
sleep(1)
x=int(input("Which Charectors do you want to learn?\nPress 1 for Hiragana \nPress 2 for Katakana\n"))
if x == 1:
    while running:
        n = random.randint(0,45)
        a = hiragana()
        a.run(n)
        print("------------Press escape anytime to quit and get score------------")
        sleep(1)

elif x == 2:
    while running:
        n = random.randint(0,45)
        b = katakana()
        b.run(n)
        print("------------Press escape anytime to quit and get score------------")
        sleep(1)