def dfs(port, tickets, route, list_result):
    route = '{0} {1}'.format(route, port)

    if len(tickets) == 0:
        list_result.append(route)
        return

    for t in tickets:
        if t[0] == port:
            c_tickets = tickets.copy()
            c_tickets.remove(t)
            dfs(t[1], c_tickets, route, list_result)


def solution(tickets):
    list_result = []

    for t in tickets:
        c_tickets = tickets.copy()
        c_tickets.remove(t)
        dfs(t[1], c_tickets, t[0], list_result)

    while True:
        list_result.sort()
        if list_result[0][0:3] == "ICN":
            break
        else :
            list_result.pop(0)

    return list_result[0].split(" ")

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
result = solution(tickets)
print(result)