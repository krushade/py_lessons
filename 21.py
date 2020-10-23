import random


cards = [{'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8},
         {'9': 9}, {'10': 10}, {'J': 2}, {'Q': 3}, {'K': 4}, {'A': 11}]
cards_deck = cards * 4
random.shuffle(cards_deck)
hand_player = []
hand_computer = []


def start_game():
    for x in range(2):
        c = random.randint(0, len(cards_deck) - 1)
        hand_computer.append(cards_deck[c])
        cards_deck.pop(c)
        p = random.randint(0, len(cards_deck) - 1)
        hand_player.append(cards_deck[p])
        cards_deck.pop(p)


def scores(hand):
    score = 0
    for card in hand:
        for v in card.values():
            score += v
    return score


mes = "Если хочешь набрать еще карту введи 'y'"
mes += "\nЕсли достаточно введи 'n': "

if __name__ == '__main__':
    start_game()
    print(f"Игра '21' начинается. \nТвоя стартовая рука: {hand_player}")

    turn_player = True
    turn_computer = True

    while turn_player:
        resume = input(mes)
        if resume == 'n':
            print(f"Твой счёт: {scores(hand_player)}")
            turn_player = False
        elif resume == 'y':
            pl = random.randint(0, len(cards_deck) - 1)
            hand_player.append(cards_deck[pl])
            cards_deck.pop(pl)
            print(f"Твоя рука: {hand_player}")
        else:
            print("Неправильный ввод!")
            continue

    while turn_computer:
        if scores(hand_computer) < 17:
            cm = random.randint(0, len(cards_deck) - 1)
            hand_computer.append(cards_deck[cm])
            cards_deck.pop(cm)
            continue
        elif scores(hand_computer) == 17:
            turn_computer = random.randint(False, True)
            if turn_computer:
                cmp = random.randint(0, len(cards_deck) - 1)
                hand_computer.append(cards_deck[cmp])
                cards_deck.pop(cmp)
            else:
                print(f"Счет компьютера: {scores(hand_computer)}")
        else:
            print(f"Счет компьютера: {scores(hand_computer)}")
            turn_computer = False

    total_player = scores(hand_player)
    total_computer = scores(hand_computer)

    if total_player > 21:
        total_player = 0
    if total_computer > 21:
        total_computer = 0
    if total_player > total_computer:
        print("Ты уделал комп, мои поздравления!!!")
    elif total_computer > total_player:
        print("Ввостание машин не за горами. Ты проиграл...")
    elif total_computer == total_player:
        print("Это была ЛЕГЕНДАРНАЯ битва! Ничья")
