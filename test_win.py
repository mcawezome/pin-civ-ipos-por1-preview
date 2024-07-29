win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
empty = " "
grid_size = 3
board = [[empty]*grid_size]*grid_size

for wc in win_conditions:
    is_won = False
    win_con_list = []
    for wc2 in wc:
        row = int(wc2 / grid_size)
        column = wc2 % (grid_size)
        digit = board[row][column]
        win_con_list.append(digit)

    set_win_con_list = set(win_con_list)
    win_token = win_con_list[0]
    if len(set_win_con_list) <= 1:
        is_won = True
        print("Player", win_token, "wins!")
        exit(0)
