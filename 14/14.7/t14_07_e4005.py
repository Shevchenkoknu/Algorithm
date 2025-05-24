from collections import deque
import sys

def game(n, first_deck, second_deck):
    first = deque(first_deck)
    second = deque(second_deck)

    for count in range(1, 2 * 10 ** 5 + 1):
        if not first:
            return f"second {count - 1}"
        if not second:
            return f"first {count - 1}"
        card1, card2 = first.popleft(), second.popleft()

        if (card1 > card2 and not (card1 == n - 1 and card2 == 0)) or (card1 == 0 and card2 == n - 1):
            first.extend([card1, card2])
        else:
            second.extend([card1, card2])

    return "draw"

if __name__ == "__main__":
    data = sys.stdin.read().strip().split("\n")
    n = int(data[0].strip())
    first_deck = list(map(int, data[1].strip().split()))
    second_deck = list(map(int, data[2].strip().split()))
    print(game(n, first_deck, second_deck))
