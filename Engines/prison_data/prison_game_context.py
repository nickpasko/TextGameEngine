class PrisonGameContext:
    def __init__(self, term):
        self.day = 1
        self.days_left = term

    def get_weekday(self):
        return ((self.day - 1) % 7) + 1

    def tick_day(self):
        self.day += 1
        self.days_left -= 1

    def get_description(self):
        return 'Day ' + str(self.day) + '. You have to be imprisoned for ' + str(self.days_left) + ' days more.'

