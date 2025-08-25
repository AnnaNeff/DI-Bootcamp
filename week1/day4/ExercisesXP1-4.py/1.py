import random
def get_random_temp():
    return random.randint(-10, 40)
    
def main():
    temp = get_random_temp()
    message = f"The temperature right now is {temp} degrees Celsius."
    if temp < 0:
        return f'{message} Brrr, that’s freezing! Wear some extra layers today.'

    elif 0 < temp < 16:
        return f'{message} Quite chilly! Don’t forget your coat.'

    elif 16 < temp <= 23:
        return f'{message} Nice weather.'

    elif 24 <= temp <= 32:
        return f'{message} A bit warm, stay hydrated.'

    elif 32 <= temp <= 40:
        return f'{message} It’s really hot! Stay cool.'
    
    print(message)

main()
    