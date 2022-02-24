# THE HANGMAN GAME
from getpass import getpass

print(
    'This is a naming game for name of programming language(tech jargons too) and name of popular individuals in tech\n')
print('WARNING!!!: this game must be played by 2 people')
while True:
    programming_language = getpass("Friend, Enter a programming language you know: ").lower()
    while True:
        print('NOTE: you have Seven(7) Trials\n')
        print(
            'INSTRUCTION: You will be given free 10 NFTs, if you get a letter correctly you get 5 NFTs if you do not, you get a deduction of 2marks')
        friend_word = programming_language
        incomplete_complete_word = []
        score_board = 14
        print('Your current amount of NFTs is 14')


        def open_file(word):
            global friend_word
            """function to help save the word the friend inputs into a .txt file on the system"""

            with open('C:\\Users\\MY PC\\Downloads\\hangman_game_database.txt', 'a') as f:
                friend_word_database = f.write(f'{friend_word}\n')#ADDING the user input to a file to avoid confusion from getpass
                print(friend_word_database)
                return friend_word


        use_friend_word = open_file(friend_word)


        def word_output_and_score(friend_word):
            global incomplete_complete_word, score_board
            """function that uses the use_friend_word as a parameter and returns the result of the program"""

            letters_used = set()
            used_letters = ''
            while True:
                my_letters = input('Enter a letter you think is in the word your friend has in mind: ').lower()
                if my_letters in list(friend_word):
                    score_board += 5
                    letters_used.add(my_letters)
                    incomplete_complete_word = [letters if letters in letters_used else '-' for letters in friend_word]
                    print(' '.join(incomplete_complete_word))
                elif my_letters not in list(friend_word):
                    score_board -= 2
                    used_letters += my_letters
                    print(f' Used words are {used_letters} ')
                    if len(set(used_letters)) == 7:
                        print(f'wrong words used are {used_letters.upper()}')
                    print(f'Your current amount of NFTs is {score_board} ')
                    if score_board == 0:
                        print('GAME OVER!!!')
                        print(f'The word your friend entered is: {friend_word} ')
                        break
                    else:
                        continue
                print(f'your amount of NFTs is {score_board} ')
                if '-' not in incomplete_complete_word:
                    print(f'Your Total amount of NFTs is {score_board} ')
                    break
                else:
                    continue

            return ' '.join(incomplete_complete_word)


        print(word_output_and_score(friend_word))
        next_game = input('Would you like to play the next game? [Y/N]: ')
        if next_game.lower() == 'y':
            def popular_individuals():
                global friend_word, incomplete_complete_word, score_board
                popular_individual = getpass('Enter the popular individual name: ').lower()
                return word_output_and_score(popular_individual)
            print(popular_individuals())
            break
        else:
            break
    play_again = input('Would you like to play this game again (Y/N): ')
    if play_again.lower() == 'y':
        continue
    else:
        break
