# unde:
# nodes -> lista cu noduri
# nodes_sets -> lista seturilor pentru fiecare nod din nodes (nodes_sets[i] e pt nodes[i])
# edges -> lista cu muchii (constrangerile practic)
sol=[]
stop_flag = False

def valid_solution(nodes,nodes_sets,edges,sol):
    
    for idx, color in enumerate(sol):
        if not color in nodes_sets[idx]:
            return False
    for edge in edges:
        if sol[edge[0]] == sol[edge[1]]:
            return False

    return True

def find_solution_using_bkt(nodes, nodes_sets, edges):
    global sol
    global stop_flag
    print(sol)
    input()
    if len(sol) == len(nodes):
        if valid_solution(nodes,nodes_sets,edges,sol):
            stop_flag = True
            return
    else:
        idx = len(sol)
        for color in nodes_sets[idx]:
            sol = sol+[color]
            addBack=[]
            for edge in edges:
                if edge[0] == idx:
                    if color in node_sets[edge[1]]:
                        node_sets[edge[1]].remove(color)
                        addBack+=[edge[1],color]
                elif edge[1] == idx:
                    if color in node_sets[edge[0]]:
                        node_sets[edge[0]].remove(color)
                        addBack+=[edge[0],color]

            find_solution_using_bkt(nodes,nodes_sets,edges)
            if stop_flag:
                break

            for toAdd in addBack:
                node_sets[toAdd[0]]+=[toAdd[1]]
            sol = sol[:idx]

nodes = [1, 2, 3, 4]
node_sets = [[1, 2], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
edges = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 3)]
find_solution_using_bkt(nodes,node_sets,edges)

print(sol)