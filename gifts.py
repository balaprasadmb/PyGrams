'''
Input Format

First line of input contains 2 integers N - the number of houses in the city and M - the number of days for which Santa comes to the city.

Next N - 1 lines contains two integers u and v meaning there is a road between house u and house v, u != v.

Next M lines contains two integers ai and bi representing the starting and ending house on ith visit of Santa.

Input
4 2

1 2
2 3
2 4

1 4
3 4

OP: 2


Input:
5 10

3 4
1 5
4 2
5 4

5 4
5 4
3 5
4 3
4 3
1 3
3 5
5 4
1 5
3 4

OP: 9
'''
def main():
    line = raw_input().split(' ')
    n = int(line[0])
    m = int(line[1])
    gifts = []
    for _ in range(n):
        gifts.append(0)
    print gifts
    roads = []
    for row in range(n):
        roads.append([0])
        for col in range(n-1):
            roads[row].append(0)
    print roads
    for _ in range(n-1):
        line = raw_input().split(' ')
        u = int(line[0])-1
        v = int(line[1])-1
        roads[u][v] = 1
        roads[v][u] = 1
    print roads
    for _ in range(m):
        line = raw_input().split(' ')
        a = int(line[0])-1
        b = int(line[1])-1
        if roads[a][b] == 1 or roads[b][a] == 1:
            gifts[a] += 1
            gifts[b] += 1
        else:
            for row in range(n):
                for col in range(row, n):
                    if roads[row][col] == 1:
                        if roads[col][b] == 1:
                            gifts[a] += 1
                            gifts[b] += 1
    print max(gifts)

# def main():
#     line = raw_input().split(' ')
#     n = int(line[0])
#     m = int(line[1])
#     gifts = []
#     for _ in range(n+1):
#         gifts.append(0)
#     print gifts
#     roads = {}
#     for _ in range(n-1):
#         line = raw_input().split(' ')
#         u = int(line[0])
#         v = int(line[1])
#         if v in roads:
#             roads[v].append(u)
#         else:
#             roads[v] = [u]
#     print roads
#     for _ in range(m):
#         line = raw_input().split(' ')
#         a = int(line[0])
#         b = int(line[1])
#         print '{0} in roads {1}'.format(a, a in roads)
#         print '{0} in roads {1}'.format(b, b in roads)
#         if b in roads.keys():
#             gifts[b] += 1
#             if a == roads[b]:
#                 gifts[a] += 1
#             else:
#                 for k in roads[b]:
#                     gifts[k] += 1
#     print max(gifts)

# def main():
#     line = raw_input().split(' ')
#     n = int(line[0])
#     m = int(line[1])
#     gifts = []
#     for _ in range(n+1):
#         gifts.append(0)
#     print gifts
#     roads = {}
#     for _ in range(n-1):
#         line = raw_input().split(' ')
#         u = int(line[0])
#         v = int(line[1])
#         roads[v] = u
#     print roads
#     for _ in range(m):
#         line = raw_input().split(' ')
#         a = int(line[0])
#         b = int(line[1])
#         print '{0} in roads {1}'.format(a, a in roads)
#         print '{0} in roads {1}'.format(b, b in roads)
#         if b in roads.keys():
#             gifts[b] += 1
#             if a == roads[b]:
#                 gifts[a] += 1
#             else:
#                 gifts[roads[b]] += 1
#     print max(gifts)

main()
