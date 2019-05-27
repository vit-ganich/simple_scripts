lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (13, 55, 32, 53)
}


class LotteryPlayer:
    def __init__(self, name: str, numbers: tuple):
        self.name = name
        self.numbers = numbers

    def total(self) -> int:
        return sum(self.numbers)


player_one = LotteryPlayer("Vitali", (10, 12, 54, 15))
player_two = LotteryPlayer("Adam", (23, 21, 44, 22))

print(player_one.name == player_two.name)

print(player_one.name)
print(player_one.numbers)
print(player_one.total())

print(player_two.name)
print(player_two.numbers)
print(player_two.total())



