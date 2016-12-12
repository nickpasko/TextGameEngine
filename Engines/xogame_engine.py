import os


class XoGameEngine:
    """XO game with pre-defined CPU logic"""
    def __init__(self):
        self.field = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.lines = [
            [0, [[1, 1], [0, 0], [2, 2]]],
            [0, [[1, 1], [0, 2], [2, 0]]],
            [0, [[0, 0], [0, 2], [0, 1]]],
            [0, [[0, 0], [2, 0], [1, 0]]],
            [0, [[2, 2], [0, 2], [1, 2]]],
            [0, [[2, 2], [2, 0], [2, 1]]],
            [0, [[1, 1], [0, 1], [2, 1]]],
            [0, [[1, 1], [1, 0], [1, 2]]]
        ]

# engine members
    def get_description(self):
        description = '  0  1  2' + os.linesep
        description += '  -------' + os.linesep
        for i, row in enumerate(self.field):
            description += str(i) + ' |'
            for item in row:
                description += {
                    0: ' ',
                    1: 'X',
                    -1: 'O'
                }.get(item, '?')
                description += '|'
            description += os.linesep
            description += '  -------' + os.linesep
        return description

    def get_options(self):
        options = []
        for i, row in enumerate(self.field):
            for j, item in enumerate(row):
                if item == 0:
                    options.append([str(i) + ',' + str(j), str(i) + ',' + str(j)])
        if len(options) < 1:
            options.append(['Draw', 'Draw'])
        return options

    def register_option(self, option):
        if option[1] == 'Draw':
            return ['quit', "It's a draw!"]
        splitted = option[1].split(',')
        i = int(splitted[0])
        j = int(splitted[1])
        if self.field[i][j] == 0:
            self.field[i][j] = 1
            win_condition = self.recalculate()
            if win_condition == 1:
                return ['quit', 'You have won!']
            self.make_move()
            win_condition = self.recalculate()
            if win_condition == -1:
                return ['quit', 'CPU have won!']
            return ['move_ok', 'You made your move. I have responded.']
        else:
            return ['move_unable', 'Impossible!']

# internal members
    def recalculate(self):
        for line in self.lines:
            line[0] = 0
            for cell in line[1]:
                line[0] += self.field[cell[0]][cell[1]]
                if line[0] == 3:
                    return 1
                if line[0] == -3:
                    return -1
        return 0

    def not_allowed(self, line):
        for cell in line[1]:
            if self.field[cell[0]][cell[1]] == 0:
                return False
        return True

    def select_line(self):
        min_line = self.lines[0]
        max_line = self.lines[0]
        selected_line = self.lines[0]
        for line in self.lines:
            if self.not_allowed(line):
                continue
            if line[0] < min_line[0]:
                min_line = line
            if line[0] > max_line[0]:
                max_line = line
        if max_line[0] + min_line[0] > 0:
            selected_line = max_line
        else:
            selected_line = min_line
        return selected_line


    def make_move(self):
        selected_line = self.select_line()
        if self.not_allowed(selected_line):
            return
        for cell in selected_line[1]:
            if self.field[cell[0]][cell[1]] == 0:
                self.field[cell[0]][cell[1]] = -1
                return



