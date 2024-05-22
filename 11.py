from random import choice
import json
import random
def playAgain():
    while True:
        play_again = input("Want to play again? (Yes/No): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            return False
        else:
            print("Please enter 'Yes' or 'No'")

while True:
    print("\n Давай сыграем в игру висилица! \n Но чтоб это было не только весело, но и полезно - играть мы будем на английском! Так ты сможешь  узнать новые для себя слова!\n")
    print("\n Let's start!!\n")
    with open('hangmans/6lives.txt', 'r', encoding='utf-8') as file:
        sixlives = file.read()
    with open('hangmans/5lives.txt', 'r', encoding='utf-8') as file:
        fivelives = file.read()
    with open('hangmans/4lives.txt', 'r', encoding='utf-8') as file:
        fourlives = file.read()
    with open('hangmans/3lives.txt', 'r', encoding='utf-8') as file:
        treelives = file.read()
    with open('hangmans/2lives.txt', 'r', encoding='utf-8') as file:
        twolives = file.read()
    with open('hangmans/1lives.txt', 'r', encoding='utf-8') as file:
        onelives = file.read()
    with open('hangmans/0lives.txt', 'r', encoding='utf-8') as file:
        zerolives = file.read()
    HANGMAN = (sixlives,fivelives,fourlives,treelives,twolives,onelives,zerolives)


    def loading_jsonword():
        with open('word.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            random.shuffle(words)
            return words
    
    def get_finalword(words):
        word = choice(words)
        return word['word'],word['description']
        
    
    max_wrong = len(HANGMAN) - 1

    word_final, descriptionword = get_finalword(loading_jsonword())  # Слово, которое нужно угадать
    so_far = "_" * len(word_final)  # Одна черточка для каждой буквы в слове, которое нужно угадать
    wrong = 0  # Количество неверных предположений, сделанных игроком
    used = []  # Буквы уже угаданы







    while wrong < max_wrong and so_far != word_final:
        print(HANGMAN[wrong])  # Вывод висельника по индексу

        print("\nYou used the following letters:\n", used)
        print("\nAt the moment the word looks like this:\n", so_far)
        print("\nПодсказка:\n", descriptionword)

        guess = input("\n\nEnter your guess:")  # Пользователь вводит предполагаемую букву

        while guess in used:
            print("You have already entered a letter", guess)  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
            guess = input("Enter your guess: ")  # Пользователь вводит предполагаемую букву

        used.append(guess)  # В список использованных букв добавляется введённая буква

        if guess in word_final:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
            print("\nYes!", guess, "is in the word!")
            new = ""
            for i in range(len(word_final)):  # В цикле добавляем найденную букву в нужное место
                if guess == word_final[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nSorry, the letter\"" + guess + "\"is not in the word.")  # Если буквы нет, то выводим соответствующее сообщение
            wrong += 1

    if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
        print(HANGMAN[wrong])
        print("""

$$\     $$\  $$$$$$\  $$\   $$\       $$\        $$$$$$\   $$$$$$\  $$$$$$$$\       $$\       $$\       $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |      $$  __$$\ $$  __$$\ $$  _____|      $$ |      $$ |      $$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |      $$ /  $$ |$$ /  \__|$$ |            $$ |      $$ |      $$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |\$$$$$$\  $$$$$\          $$ |      $$ |      $$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ | \____$$\ $$  __|         \__|      \__|      \__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$\   $$ |$$ |                                    
    $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\  $$$$$$  |\$$$$$$  |$$$$$$$$\       $$\       $$\       $$\ 
    \__|     \______/  \______/       \________| \______/  \______/ \________|      \__|      \__|      \__|
                                                                                                                                                                                    
""")
        print("\nYou've been hanged!")
        
        print("\nThe hidden word was\"" + str(word_final) + '\" \n')
        if playAgain():
            continue
        else:
            print("Thanks for playing! See you again!")
            break
    else:  # Если кол-во ошибок не превышено, то игрок выиграл
   
        print("""

$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\       $$\       $$\       $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |      $$ |      $$ |      $$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |      $$ |      $$ |      $$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |      $$ |      $$ |      $$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |      \__|      \__|      \__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |                              
    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |      $$\       $$\       $$\ 
    \__|     \______/  \______/       \__/     \__|\______|\__|  \__|      \__|      \__|      \__|
                                                                                                
""")
        print("\nYou guessed the word!")
        print("\nThe hidden word was\"" + str(word_final) + '\" \n')
        if playAgain():
            continue
        else:
            print("Thanks for playing! See you again!")
            break


