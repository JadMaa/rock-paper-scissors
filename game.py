# Write your code here
import random

all_game_options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
game_options = ['rock', 'paper', 'scissors']
rating_dict = {}
user_choice = ''
user_rating = 0

rating_file = open('rating.txt', 'r', encoding='utf-8')
for line in rating_file:
    rating_dict[line.split()[0]] = line.split()[1]
rating_file.close()

name = input("Enter your name: ")
print("Hello, {}".format(name))
if name in rating_dict:
    user_rating = int(rating_dict[name])

user_options = input().split(',')
for opt in user_options:
    if opt != '' and opt not in game_options:
        game_options.append(opt)

valid_options = ['!exit', '!rating'] + game_options
print("Okay, let's start")

while user_choice != "!exit":
    valid_option = False
    while not valid_option:
        user_choice = input()
        if user_choice in valid_options:
            valid_option = True
            break
        else:
            print("Invalid input")
    npc_choice = random.choice(game_options)
    if user_choice == '!exit':
        break
    elif user_choice == '!rating':
        print("Your rating: {}".format(user_rating))
        continue
    if user_choice == npc_choice:
        print("There is a draw (" + user_choice + ")")
        user_rating += 50
    if user_choice != npc_choice:
        beat_list = []
        idx = all_game_options.index(user_choice)
        for i in range(0, 7):
            if idx == 14:
                idx = -1
            beat_list.append(all_game_options[idx + 1])
            idx += 1
        if npc_choice in beat_list:
            print("Well done. Computer chose " + npc_choice + " and failed")
            user_rating += 100
        else:
            print("Sorry, but computer chose " + npc_choice)

print("Bye!")
