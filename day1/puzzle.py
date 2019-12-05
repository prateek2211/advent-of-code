class Puzzle:
    def __init__(self, file_path):
        self.data = [int(x) for x in open(file=file_path).read().split()]

    def solve_part1(self):
        return sum(map(lambda x: x // 3 - 2, self.data))

    def solve_part2(self):
        return sum([self.calc_fuel(x // 3 - 2) for x in self.data])

    def calc_fuel(self, fuel_weight):
        if fuel_weight < 0:
            return 0
        total_fuel = fuel_weight
        total_fuel += self.calc_fuel(fuel_weight // 3 - 2)
        return total_fuel


if __name__ == "__main__":
    p = Puzzle('input.txt')
    print(p.solve_part1())
    print(p.solve_part2())
