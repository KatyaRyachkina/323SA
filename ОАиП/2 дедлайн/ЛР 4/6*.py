from random import randint

def print_field(field):
    print("   0  1  2")
    for i in range(3):
        print(f"{i}  {'  '.join(field[i])}")

def check_win(field, player):
    for i in range(3):
        if all(field[i][j] == player for j in range(3)):
            return True
    for j in range(3):
        if all(field[i][j] == player for i in range(3)):
            return True
    if all(field[i][i] == player for i in range(3)):
        return True
    if all(field[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(field):
    for row in field:
        if ' ' in row:
            return False
    return True

def ai_move(field):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                empty_cells.append((i, j))
    if empty_cells:
        return empty_cells [randint(0, len(empty_cells)-1)]
    return None

def play_game():
    field = [[' ', ' ', ' '],
             [' ', ' ', ' '], 
             [' ', ' ', ' ']]
    
    players = ['X', 'O']
    current_player = 0
    
    print("Добро пожаловать в Крестики-нолики!")
    print("Вводите координаты в формате: строка столбец (0-2)")
    
    while True:
        print_field(field)
        player_symbol = players[current_player]
        
        if player_symbol == 'X':
            try:
                coords = input(f"Ход игрока {player_symbol}: ").split()
                if len(coords) != 2:
                    print("Введите две координаты!")
                    continue             
                row, col = int(coords[0]), int(coords[1])            
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Координаты должны быть от 0 до 2!")
                    continue
                if field[row][col] != ' ':
                    print("Клетка уже занята!")
                    continue
                field[row][col] = player_symbol  
            except (ValueError, IndexError):
                print("Некорректный ввод!")
                continue
        else:
            print("Ход компьютера (O)...")
            row, col = ai_move(field)
            field[row][col] = player_symbol
        
        if check_win(field, player_symbol):
            print_field(field)
            if player_symbol == 'X':
                print("Поздравляем! Вы победили!")
            else:
                print("Компьютер победил!")
            break
        
        if check_draw(field):
            print_field(field)
            print("Ничья!")
            break
        
        current_player = (current_player + 1) % 2

play_game()
