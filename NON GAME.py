# THE HANGMAN GAME
from getpass import getpass
while True:
	print('This is an HANGMAN GAME\nNOTE: you have Seven(7) Trials\n')
	print('INSTRUCTION: You will be given free 10 points if you get a letter correctly you get 5 points\n After seven different incorrect trials you loose')
	friend_word = getpass('Friend, Enter your word: ')
	incomplete_complete_word = []
	print('Your current score is 10')


	def open_file(word):
		global friend_word
		"""function to help save the word the friend inputs into a .txt file on the system"""

		with open('C:\\Users\\MY PC\\Downloads\\hangman_game_database.txt', 'a') as f:
			friend_word_database = f.write(f'{friend_word}\n')
			print(friend_word_database)
			return friend_word


	use_friend_word = open_file(friend_word)

	def word_output_and_score():
		global friend_word, incomplete_complete_word
		"""function that uses the use_friend_word as a parameter and returns the result of the program"""

		letters_used = set()
		used_letters = set()
		while True:
			score_board = 0
			my_letters = input('Enter a letter you think is in the word your friend has in mind: ')
			if my_letters not in list(friend_word):
				print('WRONG LETTER ENTERED!!! \n')
				used_letters.add(my_letters)
				print(f'wrong words used are {used_letters}')
				if len(used_letters) == 7:
					print('GAME OVER!!!')
					print(f'The word your friend entered is: {friend_word} ')
					break
				else:
					continue
			else:
				letters_used.add(my_letters)
				for l in letters_used:
					score_board += 5
				incomplete_complete_word = [letters if letters in letters_used else '-' for letters in friend_word]
				print(' '.join(incomplete_complete_word))
			print(f'your current score is {score_board} ')
			if '-' not in incomplete_complete_word:
				print(f'Your final score is {score_board} ')
				break
			else:
				continue

		return ' '.join(incomplete_complete_word)


	print(word_output_and_score())
	play_again = input('Would you like to play this game again (Y/N): ')
	if play_again.lower() == 'y':
		continue
	else:
		break
