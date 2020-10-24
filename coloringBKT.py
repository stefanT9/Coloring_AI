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
            find_solution_using_bkt(nodes,nodes_sets,edges)
            if stop_flag:
                break
            sol = sol[:idx]

nodes = [1,2,3,4]
node_sets = [[1,2,3,4] for i in range(4)]
edges = [(1,2),(2,3),(0,3),(1,3)]
find_solution_using_bkt(nodes,node_sets,edges)

print(sol)