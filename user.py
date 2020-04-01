class User():

    def __init__(self, total_amount_of_ticks):
        self.total_amount_of_ticks = total_amount_of_ticks
        self.current_tick = 0

    def tick(self):
        self.current_tick += 1

    def task_completed(self):
        return self.current_tick == self.total_amount_of_ticks
