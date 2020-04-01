from user import User
from server import Server


def create_new_server_for_user(servers):
    new_server = Server(total_of_users_per_server)
    servers.append(new_server)
    new_server.append_user(User(total_ticks))


def searched_the_last(servers, server):
    return servers[len(servers) - 1] == server


def get_the_last_server(servers):
    if len(servers) == 0:
        return None
    return servers[len(servers) - 1]


if __name__ == "__main__":
    total_ticks = 4
    total_of_users_per_server = 2
    users_per_tick = [1, 3, 0, 1, 0, 1]
    servers = [Server(total_of_users_per_server)]
    total_cost = 0
    tick = 0

    while len(servers) > 0 or tick < len(users_per_tick):
        if tick < len(users_per_tick):
            for _ in range(users_per_tick[tick]):
                last_server = get_the_last_server(servers)
                if last_server is None:
                    last_server = Server(total_of_users_per_server)
                    servers.append(last_server)
                if last_server.is_full():
                    if searched_the_last(servers, last_server):
                        # If we've searched all servers
                        create_new_server_for_user(servers)
                else:
                    # Avaliable server found, append user and stop searching
                    last_server.append_user(User(total_ticks))
        total_users = []
        # To avoid changing the list in place
        _servers = servers.copy()
        for server in _servers:
            # tick, and remove if necessary, all the server's users
            server.tick_users()
            if server.is_empty():
                # before we remove this server, calculate it's cost
                total_cost += server.ticks * Server.COST_PER_TICK
                servers.remove(server)
            else:
                server.tick()
            # Edge case for no more servers are available
            if len(server.users) > 0 or len(servers) == 0:
                total_users.append(str(len(server.users)))

        print('tick:' + str(tick) + ' ' + ','.join(total_users))
        tick += 1

    print(total_cost)
