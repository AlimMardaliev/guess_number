from random import randint

robot_num = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    player_num = int(input('Ведите ваше число: '))
    if robot_num == player_num:
        break
    elif robot_num > player_num:
        print('Ваше число меньше того, что загадано)')
        print('Попробуйте снова')
    elif robot_num < player_num:
        print('Ваше число больше того, что загадано')
        print('Попробуйте снова')

print('Отличная интуиция! Вы угадали число :)')