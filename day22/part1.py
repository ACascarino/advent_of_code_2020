with open("day22/input.txt", "r") as f:
    player1, player2 = f.read().split("\n\n")

    player1 = [int(card) for card in player1.splitlines()[1:]]
    player2 = [int(card) for card in player2.splitlines()[1:]]

while player1 and player2:
    if (p1 := player1.pop(0)) > (p2 := player2.pop(0)):
        player1 += [p1, p2]
    else:
        player2 += [p2, p1]

if player1:
    print(sum([(i+1)*card for i,card in enumerate(reversed(player1))]))
else:
    print(sum([(i+1)*card for i,card in enumerate(reversed(player2))]))