'''
search all the possible solution space
binary tree depth first search
recursive

bad performance as time consume is O(2^depth)
'''

a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[7, 4, 5, 0],
     [9, 2, 8, 0]]
e = [10, 12]
x = [18, 7]

rt = None
st = 1000000000


def dfs(station, line, c_path, c_time):
    # get the size of assemly line
    size = len(a[0])
    # when station is the last one, finish search
    if station == size - 1:
        c_path[station] = (line, station)
        c_time += a[line][station]
        # add exit cost
        c_time += x[line]
        global st
        global rt
        if c_time < st:
            st = c_time
            rt = c_path.copy()
        return
    # add entry cost
    if station == 0:
        c_time += e[line]
    # otherwise save the current path, cost and continue
    # with next station in the same line
    c_path[station] = (line, station)
    c_time += a[line][station]
    dfs(station + 1, line, c_path, c_time)
    # calculate the path and cost if change to other line
    c_time += t[line][station]
    line = (line + 1) % 2
    dfs(station + 1, line, c_path, c_time)


# cannot use list.append() method,
# because list will not recorver in stytem stack
c_path = [None] * len(a[0])
c_time = 0
dfs(0, 0, c_path, c_time)

print(rt, st)
