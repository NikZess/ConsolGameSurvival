import random
import time
import sys

def game(random_answer):
    list_letter = list(random_answer)  

    print(list_letter)

    encrypted_word = ' '.join(['_' for _ in list_letter])
    print(f"Слово: {encrypted_word}")
    time.sleep(1)
    guessed_letters = [] 
    
    heart = '❤️'
    number_of_hearts = 6

    lives = heart * number_of_hearts
    
    print(f"Количество жизней 💓: {lives}")
    time.sleep(1)

    while number_of_hearts > 0:
        user_answer_on_mystery = input("Введите букву: ").lower()

        if len(user_answer_on_mystery) == 1 and user_answer_on_mystery.isalpha():
            if user_answer_on_mystery in guessed_letters:
                print("Вы уже угадали эту букву.")
                continue
            
            guessed_letters.append(user_answer_on_mystery)

            if user_answer_on_mystery in list_letter:
                print("Правильно!")
                
                encrypted_word = ' '.join([letter if letter in guessed_letters else '_' for letter in list_letter])
                print(f"Слово: {encrypted_word}")

                if '_' not in encrypted_word:
                    print("Поздравляем! Вы угадали слово!")
                    break
            else:
                number_of_hearts -= 1
                print(f"Неправильно! Осталось попыток: {heart * number_of_hearts}")
        else:
            print("Введите одну букву.")

    if number_of_hearts == 0:
        print(f"Вы исчерпали все попытки! Загаданное слово было: {random_answer}")

tips_on_answer = ["Программа переводящая код в машинный", "летающий транспорт", "предмет, который выводит изображение на монитор"]
true_answer = ["компилятор", "самолет", "видеокарта"]

print("Добро пожаловать! Это игра виселица!")
time.sleep(1.5)

random_num_for_question = random.randint(0, 2)

random_question = tips_on_answer[random_num_for_question]
random_answer = true_answer[random_num_for_question]

print("Слово загаданно! Начать игру?: Да/Нет (y/n) ")
answer_on_start = input().lower()

if answer_on_start in ('yes', 'да', 'y', 'д'):
    print("Начинаем!")
    time.sleep(1)
    game(random_answer)
else:
    print("Еще увидимся!")
    sys.exit()