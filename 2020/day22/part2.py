def score(deck):
    return sum([(i+1)*card for i,card in enumerate(reversed(deck))])

def combat(player1, player2, combat_level, max_cl, combat_level_tracker):
    rounds = set()
    game_winner = None
    combat_level += 1
    max_cl = combat_level if combat_level > max_cl else max_cl
    combat_level_tracker.append(combat_level)

    while player1 and player2:
        this_round = (tuple(player1), tuple(player2))
        if this_round in rounds:
            game_winner = "player1"
            break
        else:
            rounds.add(this_round)

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 <= len(player1) and p2 <= len(player2):
            p1_deck = player1.copy()[:p1]
            p2_deck = player2.copy()[:p2]
            round_winner, _, combat_level, max_cl, combat_level_tracker = combat(p1_deck, p2_deck, combat_level, max_cl, combat_level_tracker)
            combat_level_tracker.append(combat_level)
        else:
            round_winner = "player1" if p1 > p2 else "player2"

        if round_winner == "player1":
            player1 += [p1, p2]
        else:
            player2 += [p2, p1]

    if game_winner is None:
        game_winner = "player1" if player1 else "player2"
    game_score = score(player1) if game_winner == "player1" else score(player2)

    combat_level -= 1
    return (game_winner, game_score, combat_level, max_cl, combat_level_tracker)

with open("day22/thomas_input.txt", "r") as f:
    player1, player2 = f.read().split("\n\n")

    player1 = [int(card) for card in player1.splitlines()[1:]]
    player2 = [int(card) for card in player2.splitlines()[1:]]

    combat_level = 0
    max_cl = 0
    combat_level_tracker = []
    end_winner, end_score, combat_level, max_cl, combat_level_tracker = combat(player1, player2, combat_level, max_cl, combat_level_tracker)
    print(end_winner, end_score)
    