class ReadFile:
    STATE_TITLE = 1
    STATE_COUNT = 2
    STATE_INGREDIENTS = 3
    cook_book = {}
    state = STATE_TITLE

    def __init__(self, file: str):
        self.file = file

    def read_file(self):
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                if self.state == self.STATE_TITLE:
                    title = line
                    self.cook_book[title] = []
                    self.state = self.STATE_COUNT

                elif self.state == self.STATE_COUNT:
                    count = int(line)
                    self.state = self.STATE_INGREDIENTS

                else:
                    data = [x.strip() for x in line.split('|')]
                    data[1] = int(data[1])
                    self.cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
                    count -= 1
                    if count == 0:
                        self.state = self.STATE_TITLE

        return self.cook_book
