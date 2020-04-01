class Server():
    COST_PER_TICK = 1.00

    def __init__(self, total_of_users_per_server):
        self.total_of_users_per_server = total_of_users_per_server
        self.users = []
        self.ticks = 0

    def append_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def is_empty(self):
        return len(self.users) == 0

    def is_full(self):
        return len(self.users) == self.total_of_users_per_server

    def tick(self):
        self.ticks += 1

    def tick_users(self):
        users = self.users.copy()
        for user in users:
            if user.task_completed():
                self.remove_user(user)
                continue
            user.tick()
