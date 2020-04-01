from user import User
from server import Server


class Main():

    def __init__(self, total_ticks, total_of_users_per_server, users_per_tick, servers=None):
        self.total_ticks = total_ticks
        self.total_of_users_per_server = total_of_users_per_server
        self.users_per_tick = users_per_tick
        self.servers = servers if servers is not None else [
            Server(self.total_of_users_per_server)]
        self.total_cost = 0

    def create_new_server_for_user(self):
        new_server = Server(self.total_of_users_per_server)
        self.servers.append(new_server)
        return new_server

    def is_the_last_server(self, server):
        return self.servers[len(self.servers) - 1] == server

    def get_the_last_server(self):
        if len(self.servers) == 0:
            return None
        return self.servers[len(self.servers) - 1]

    def handle_new_user(self):
        last_server = self.get_the_last_server()
        if last_server is None or last_server.is_full():
            last_server = self.create_new_server_for_user()
        last_server.append_user(User(self.total_ticks))

    def handle_server(self, server):
        # tick, and remove if necessary, all the server's users
        server.tick_users()
        if server.is_empty():
            # before we remove this server, calculate it's cost
            self.total_cost += server.ticks * Server.COST_PER_TICK
            self.servers.remove(server)
        else:
            server.tick()


if __name__ == "__main__":
    main = Main(4, 2, [1, 3, 0, 1, 0, 1], [Server(2)])
    tick = 0

    while len(main.servers) > 0 or tick < len(main.users_per_tick):
        if tick < len(main.users_per_tick):
            for _ in range(main.users_per_tick[tick]):
                main.handle_new_user()
        total_users = []
        # To avoid changing the list in place
        _servers = main.servers.copy()
        for server in _servers:
            main.handle_server(server)
            # Edge case for no more servers are available
            if len(server.users) > 0 or len(main.servers) == 0:
                total_users.append(str(len(server.users)))

        print('tick:' + str(tick) + ' ' + ','.join(total_users))
        tick += 1

    print(main.total_cost)
