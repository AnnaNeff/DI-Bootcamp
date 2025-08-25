import random

month = int(input("What month is it now?: "))
def get_random_temp():
    if 1 <= month <= 2 or month == 12:
        return random.uniform(-10.0, 5.0)
    if 2 < month <= 5:
        return random.uniform(5.0, 23.0)
    if 5 < month <= 8:
        return random.uniform(18.0, 40.0)
    if 8 < month <= 11:
        return random.uniform(0.0, 16.0)

def main():
    temp = get_random_temp()
    main_message = f"The temperature right now is {round(temp, 1)} degrees Celsius."
    advice = False
    if temp < 0:
        advice = f'{main_message} \nBrrr, that’s freezing! Wear some extra layers today.'

    elif 0 < temp < 16:
        advice = f'{main_message} \nQuite chilly! Don’t forget your coat.'

    elif 16 < temp <= 23:
        advice = f'{main_message} \nNice weather.'

    elif 24 <= temp <= 32:
        advice = f'{main_message} \nA bit warm, stay hydrated.'

    elif 32 <= temp <= 40:
        advice = f'{main_message} \nIt’s really hot! Stay cool.'
    
    print(advice)

main()