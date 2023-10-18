import random

def print_6_mistakes():
    print("  [-----]-");
    print("  |     |");
    print("  |     0");
    print("  |    /|\\");
    print("  |     |\\");
    print("  |    / \\");
    print(" /|\\ ");

def print_5():
    print("  [-----]-");
    print("  |     |");
    print("  |     0");
    print("  |    /|\\");
    print("  |     |\\");
def print_4():
    print("  [-----]-");
    print("  |     |");
    print("  |     0");
    print("  |    /|\\");

def print_3():
    print("  [-----]-");
    print("  |     |");
    print("  |     0");

def print_2():
    print("  [-----]-");
    print("  |     |");
def print_1():
    print("  [-----]-");

def print_0():
    print(" ")

def print_status():
    if mistakes == 0 :
        print_0();
    elif mistakes == 1:
        print_1();
    elif mistakes == 2:
        print_2();
    elif mistakes == 3:
        print_3();
    elif mistakes == 4:
        print_4();
    elif mistakes == 5:
        print_5;
    elif mistakes == 6:
        print_6_mistakes
    print("word ", end='')
    for el in guesses:
        print(f"{el} ", end='');
    print(f"\n you have {remaining_guesses} guesses left")
        


words = ["movement""mix","factory","despise","end","crossing","country","formula","pawn","banquet","absence","consult","bush","complex","pest","hard","variable","shoot","carrot","forbid"]

guesses = [];
remaining_guesses = 6;
mistakes = 0;
words_man = random.randint(0,len(words)-1)
word = words[words_man].upper()
print(word);

print_status();

for i in range(len(word)):
    guesses.append('_')

game_over = False

while not game_over:
    print_status();

    user_input = input(" please enter a letter :\n")
    if not user_input:
        print("Not a valid input please try again")
    else:
        letter = user_input[0].upper();
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter;
            if '_' not in guesses:
                game_pver = True;
        else:
            print(" not in the word");
            remaining_guesses -=1
            mistakes+=1
            if mistakes == 6:
                game_over = True;

if mistakes == 6:
    print("Game over ")
else:
    print("You have won the game")