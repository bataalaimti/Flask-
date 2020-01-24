from random import choice


def game_rps(player):
    item = ['хайч', 'чулуу', 'даавуу']
    com = choice(item)
    print(com)
    player = player.lower()
    if player == com:
        return "Тэнцлээ"
    elif player == item[0] and com == item[1]:
        return "Com хожлоо"
    elif player == item[0] and com == item[2]:
        return "Player хожлоо баяр хүргье"
    elif player == item[1] and com == item[0]:
        return "Player хожлоо баяр хүргье"
    elif player == item[1] and com == item[2]:
        return "Com хожлоо"
    elif player == item[2] and com == item[0]:
        return "Com хожлоо"
    elif player == item[2] and com == item[1]:
        return "Player хожлоо баяр хүргье"
    else:
        return "Буруу утга оруулсан байна"
