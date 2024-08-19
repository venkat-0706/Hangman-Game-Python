import random

def hangman():
  word_list = ["python", "hangman", "programming", "game"]
  word = random.choice(word_list)
  word_length = len(word)
  lives = 6
  guessed_letters = []
  word_display = "_" * word_length

  while lives > 0:
    print(word_display)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(guess)

    if guess in word:
      word_as_list = list(word_display)
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices:
        word_as_list[index] = guess
      word_display = "".join(word_as_list)
      if "_" not in word_display:
        print("You win!")
        break
    else:
      lives -= 1
      print(f"Incorrect. You have {lives} lives left.")

  if lives == 0:
    print("You lose! The word was", word)

hangman()