# Поскольку поле одно, сделаем его глобальным и будем менять в течении игры
field = [['-' for _ in range(3)] for _ in range(3)]


def field_print():
    sep = '\t'
    for row_num in range(-1, 3):
        for col_num in range(-1, 3):
            # Печать пустого квадрата
            if row_num == -1 and col_num == -1:
                print(' ', end=sep)
            elif row_num == -1:
                print(col_num, end=sep)
            elif col_num == -1:
                print(row_num, end=sep)
            else:
                print(field[row_num][col_num], end=sep)
        print()
    print()


def check_move(coordinates_list):
    if len(coordinates_list) != 2:
        print('Нужно ввести 2 числа через пробел! Попробуйте еще раз')
        return False
    elif not (0 <= coordinates_list[0] <= 2 and 0 <= coordinates_list[1] <= 2):
        print('Координаты должны быть от 0 до 2х! Попробуйте еще раз')
        return False
    elif field[coordinates_list[0]][coordinates_list[1]] != '-':
        print('Выберите свободную ("-") клетку для хода! Попробуйте еще раз')
        return False
    return True


def win_check(player_num, mark):

    if not any('-' in elem for elem in field):
        print('Ничья!')
        return True

    for row_num in range(3):

        # Проверка строк и столбцов
        if check_line(field[row_num], mark) or check_line([field[col][row_num] for col in range(3)], mark):
            print(f'Победил игрок {player_num}!')
            return True

    else:
        # Проверка диагоналей
        if (check_line([field[num][num] for num in range(3)], mark)
                or check_line([field[2 - num][num] for num in range(3)], mark)):
            print(f'Победил игрок {player_num}!')
            return True


def check_line(line, mark):

    return all(x == mark for x in line)


print('Добро пожаловать в игру "Крестики-нолики"!')
player = 1
player_mark = {1: 'X', 2: '0'}

while True:

    field_print()
    print(f'Ход игрока {player}:')

    # Чтобы не писать кучу int() сделал перевод в число в попытке.
    try:
        player_move = list(map(int, input('Введите координаты клетки через пробел (строка столбец): ').split()))
    except ValueError:
        print('Нужно ввести 2 числа. Попробуйте еще раз')
        continue

    if check_move(player_move):

        current_player_mark = player_mark[player]
        field[player_move[0]][player_move[1]] = current_player_mark

        if win_check(player, current_player_mark):
            break

        player = player % 2 + 1
