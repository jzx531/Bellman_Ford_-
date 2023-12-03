import heapq
from collections import defaultdict
from math import inf

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [(3, 'A', 'B'),
         (2, 'A', 'C'),
         (5, 'A', 'D'),
         (1, 'B', 'D'),
         (4, 'B', 'E'),
         (2, 'C', 'D'),
         (1, 'C', 'F'),
         (3, 'D', 'E'),
         (2, 'E', 'F'),
         ]
def AdjacencyList(edges):
    adjacent_dict = defaultdict(list)  # 注意：defaultdict(list)必须以list做为变量
    for weight, v1, v2 in edges:
        adjacent_dict[v1].append((weight, v1, v2))
        adjacent_dict[v2].append((weight, v2, v1))
    return adjacent_dict

def BellmanFord(Adjacent_dict,destination):
    RouterTable={}
    for key in Adjacent_dict:
        RouterTable[key] = [-1,inf]
    oldtable=dict.copy(RouterTable)
    try:
        visited=list()
        visited.append(destination)
        for terminal in Adjacent_dict:
            for labor in Adjacent_dict[terminal]:
                if destination in labor:
                    RouterTable[terminal]=[destination,labor[0]]
                    if terminal not in visited:
                      visited.append(terminal)
        length=len(RouterTable)

        while len(visited)<length:
            for terminal in Adjacent_dict:
                    terminal_dest=list()
                    for labor in Adjacent_dict[terminal]:
                        if labor[2] in visited:
                            terminal_dest.append((RouterTable[terminal][1],RouterTable[terminal][0]))
                            terminal_dest.append(((RouterTable[labor[2]][-1]+labor[0]),labor[2]))
                    if(len(terminal_dest)>1):
                        dest=sorted(terminal_dest)[0]
                        RouterTable[terminal]=[dest[1],dest[0]]
                        visited.append(terminal)

        while (RouterTable != oldtable):
            oldtable=dict.copy(RouterTable)
            for terminal in Adjacent_dict:
                # if terminal not in visited:
                terminal_dest = list()
                for labor in Adjacent_dict[terminal]:
                    #if labor[2] in visited:
                        terminal_dest.append((RouterTable[terminal][1], RouterTable[terminal][0]))
                        terminal_dest.append(((RouterTable[labor[2]][-1] + labor[0]), labor[2]))
                if (len(terminal_dest) > 1):
                    dest = sorted(terminal_dest)[0]
                    RouterTable[terminal] = [dest[1], dest[0]]
                    visited.append(terminal)


        RouterTable[destination] = [destination,0]
        return RouterTable

    except:
       return ("destination is not in this LAN")

if __name__ =='__main__':
    AD=AdjacencyList(edges)
    print(f"生成得到路由表={BellmanFord(AD,'B')}")


