# A program that guesses a computer-guessed natural number from 1 to 100 in the minimum number of attempts

import numpy as np

def game_core_v3(number):
    """The function takes a hidden number and returns the number of attempts"""
    count = 0
    min_number = 1
    max_number = 100
    predict = np.random.randint(1,101) # Generates a one random number
    
    while count<100 and number!=predict:
        count += 1
        if number > predict: 
            min_number = predict
        elif number < predict: 
            max_number = predict
        predict = (min_number + max_number)//2
        
    return (count)

def score_game(game_core):
    """The function runs the game 1000 times to see how quickly the number is guessed"""
    count_ls = []
    np.random.seed(1) # Fixing RANDOM SEED, for reproduction
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

# Launch the game
score_game(game_core_v3)

