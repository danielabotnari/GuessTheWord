from email.mime import image
import random
from PIL import Image, ImageFilter

# start page
print('Welcome in "Guess the word"\n')
name = input('What is your name? ')
print('\nHello ' + name)

# lists with words and pictures
word_list = ['octopus', 'forest', 'balloon', 'horse', 'cactus', 'fontys', 'dracula']
pictures = ['octopus.png', 'forest.png', 'balloon.png', 'horse.png', 'cactus.png', 'fontys.png', 'dracula.npg']
your_word = random.choice(word_list)

# synchronization of words and pictures

if your_word == "horse":
    test = "horse.png"
elif your_word == "octopus":
    test = "octopus.png"
elif your_word == "forest":
    test = "forest.png"
elif your_word == "balloon":
    test = "balloon.png"
elif your_word == "cactus":
    test = "cactus.png"
elif your_word == "fontys":
    test = "fontys.png"
elif your_word == "dracula":
    test = "dracula.png"

open_image = Image.open(test)

# just length of word
for letter in your_word:
    print('_', end=' ')


def mistakes(try_again):
    if try_again == 5:
        print("Oh no, you are out of guesses, do your best next time\nರ╭╮ರ")
    elif try_again == 4:
        print('\nTime to do your best, your last chance (￣ヘ￣;)')
    elif try_again == 3:
        print('\nHmmm, think better! (ー_ー゛)')
    elif try_again == 2:
        print("\nDon't worry, you can try again ʕ ꈍᴥꈍʔ")
    else:
        print('\n 〜(꒪꒳꒪)〜(ノ^_^)ノ(~‾▿‾)~')


# function for the position of the letter in the word
def next_letter(correctly_guessed):
    position_word = 0  # position of the letter in word
    count_letters = 0  # amount of letters we already guessed in the turn
    for x in your_word:
        if x in correctly_guessed:
            print(your_word[position_word], end=' ')
            count_letters += 1
        else:
            print('_', end=' ')
        position_word += 1
    return count_letters


word_length = len(your_word)
trials = 0
correct_letter = 0  # amount of correct guessed letters
guessed_letters = []
guessed_amount = 0  # total amount of letters
blurry = 100


# function for blurring pictures
def blur():
    blurred_image = open_image.filter(ImageFilter.BoxBlur(blurry))
    blurred_image.show(open_image)
    return blurred_image


# the loop for guessing letters
while trials != 5 and guessed_amount != word_length:
    print("\n\nDo you know what is it?\n")
    blur()

    for letter in guessed_letters:
        print(letter, end=" ")

    correctly_guessed_letter = input('\n Guess the letter: ')
    if correctly_guessed_letter in your_word:
        mistakes(trials)
        correct_letter += 1
        blurry -= 25
        guessed_letters.append(correctly_guessed_letter)
        guessed_amount = next_letter(guessed_letters)

    else:
        trials += 1
        print("Oops!...wrong letter")
        mistakes(trials)
        guessed_letters.append(correctly_guessed_letter)
        guessed_amount = next_letter(guessed_letters)

if guessed_amount == word_length:
    print('\nGOOD JOB! YOU WON 〜(꒪꒳꒪)〜(ノ^_^)ノ(~‾▿‾)~')
print('\n end')
