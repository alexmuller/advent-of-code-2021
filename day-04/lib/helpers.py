class Board:
    def __init__(self, rows):
        self.rows = []

        for row in rows:
            self.rows.append([int(x) for x in row.split(' ') if x])

        self.marked = [[0,0,0,0,0] for i in range(5)]
        self.nums = [num for row in self.rows for num in row]
        self.is_complete = False

    def __str__(self):
        return str(self.rows)

    def is_complete(self):
        return self.is_complete

    def unmarked_sum(self):
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i][j] == 0:
                    unmarked_sum += self.rows[i][j]

        return unmarked_sum

    def new_call(self, number_called):
        if number_called not in self.nums:
            return None

        for i, row in enumerate(self.rows):
            for j, num in enumerate(row):
                if num == number_called:
                    self.marked[i][j] = 1

        for row in self.marked:
            if row == [1,1,1,1,1]:
                self.is_complete = True
                return self.unmarked_sum() * number_called

        for i in range(5):
            column = [x[i] for x in self.marked]
            if column == [1,1,1,1,1]:
                self.is_complete = True
                return self.unmarked_sum() * number_called

        return None
