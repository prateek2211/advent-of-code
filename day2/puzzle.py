class Puzzle:

    def __init__(self, file_path, output):
        self.output = output
        self.input = [int(x) for x in open(file=file_path).read().split(',')]
        # self.restore()

    def restore(self):
        self.input[1] = 12
        self.input[2] = 2

    def program(self):
        working_input = self.input.copy()
        for i in range(0, len(working_input), 4):
            if working_input[i] == 1:
                working_input[working_input[i + 3]] = working_input[working_input[i + 1]] + working_input[
                    working_input[i + 2]]
            elif self.input[i] == 2:
                working_input[working_input[i + 3]] = working_input[working_input[i + 1]] * working_input[
                    working_input[i + 2]]

            else:
                return working_input[0]

        return working_input[0]

    def program_input(self, noun, verb):
        self.input[1] = noun
        self.input[2] = verb

    def solve_part_two(self):
        size = len(self.input)
        for noun in range(size):
            for verb in range(size):
                self.program_input(noun, verb)
                if self.program() == self.output:
                    return noun, verb


if __name__ == "__main__":
    p = Puzzle('input', 19690720)
    print(p.solve_part_two())
