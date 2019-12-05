import sys


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)


class Puzzle:
    wires = [[Coordinate(0, 0)], [Coordinate(0, 0)]]

    def __init__(self, file_path):
        with open(file_path) as f:
            for i in range(2):
                self.store_coord(i, f.readline())

    def store_coord(self, wire_no, line):
        for pt in line.split(','):
            direction = pt[0]
            dist = int(pt[1:])
            last_pos = self.wires[wire_no][-1]
            if direction == 'U' or direction == 'D':
                disp = dist if direction == 'U' else -dist
                self.wires[wire_no].append(Coordinate(last_pos.x, last_pos.y + disp))
            else:
                disp = dist if direction == 'R' else -dist
                self.wires[wire_no].append(Coordinate(last_pos.x + disp, last_pos.y))

    def solve_part_one(self):
        wire1 = self.wires[0]
        wire2 = self.wires[1]
        min_dist = sys.maxsize
        for i in range(1, len(wire1)):
            for j in range(1, len(wire2)):
                if Puzzle.check_cross(wire1[i], wire1[i - 1], wire2[j], wire2[j - 1]):
                    if wire1[i].y == wire1[i - 1].y:
                        dist = abs(wire2[j].x) + abs(wire1[i].y)
                        if dist < min_dist:
                            min_dist = dist
                    else:
                        dist = abs(wire1[i].x) + abs(wire2[j].y)
                        if dist < min_dist:
                            min_dist = dist
        return min_dist

    def solve_part_two(self):
        wire1 = self.wires[0]
        wire2 = self.wires[1]
        steps = []
        step1 = 0
        for i in range(1, len(wire1)):
            step1 += abs(wire1[i].x - wire1[i - 1].x) + abs(wire1[i].y - wire1[i - 1].y)
            step2 = 0
            for j in range(1, len(wire2)):
                step2 += abs(wire2[j].x - wire2[j - 1].x) + abs(wire2[j].y - wire2[j - 1].y)
                if Puzzle.check_cross(wire1[i], wire1[i - 1], wire2[j], wire2[j - 1]):
                    steps.append(step1 + step2 - abs(wire2[j].x - wire1[i].x) - abs(wire2[j].y - wire1[i].y))
        return min(steps)

    @staticmethod
    def check_cross(pos1, pos2, pos3, pos4):
        if pos1.x == pos2.x and pos3.x != pos4.x:
            return is_bounded(pos1.x, pos3.x, pos4.x) and is_bounded(pos3.y, pos1.y, pos2.y)
        elif pos3.y != pos4.y:
            return is_bounded(pos1.y, pos3.y, pos4.y) and is_bounded(pos3.x, pos1.x, pos2.x)
        return False


'''
Checks if a is bounded between b and c
'''


def is_bounded(a, b, c):
    return c < a < b or b < a < c


if __name__ == '__main__':
    p = Puzzle('input')
    print(p.solve_part_two())
