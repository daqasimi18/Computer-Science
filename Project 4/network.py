"""
Project: Project 4
Name: Darab Ali Qasimi
Date: 21 Nov 2020
Collaboration: Sofia, Dipesh, and Pyone
"""
import sys
from collections import defaultdict, deque
from heap import heap

def broadcast(src, graph, ttl):
    vals = {}
    ttl_vals = {}
    stack = deque()
    stack.append(src)
    ttl_vals[src] = ttl
    while len(stack)!=0 and ttl !=0:
        pop_src = stack.pop()
        print(pop_src)
        for i in graph[pop_src].keys():
            if i in vals or ttl_vals[pop_src] <= 0:
                pass
            else:
                stack.append(i)
                vals[i] = pop_src
                ttl_vals[i] = ttl_vals[pop_src]-1
    return vals
    
def direct(src, graph):
    diss = {v: float('infinity') for v in graph.keys()}
    vals_dic = {}
    diss[src] = 0
    prio_que = heap(diss.keys(), diss.values())
    while not prio_que.is_empty() :
        cur_dist, cur_v = prio_que.pop()
        for neigh, weight in graph[cur_v].items():
            dist = cur_dist + weight
            if dist < diss[neigh]:
                diss[neigh] = dist
                prio_que.decrease_key(neigh, dist)
                vals_dic[neigh] = cur_v
    return vals_dic

def mst(src, graph):
    diss = {v: float('infinity') for v in graph.keys()}
    vals_dic = {}
    diss[src] = 0
    prio_que = heap(diss.keys(), diss.values())
    while not prio_que.is_empty():
        cur_dist, cur_v = prio_que.pop()
        for neigh, weight in graph[cur_v].items():
            if weight < prio_que.prio(neigh):
                prio_que.decrease_key(neigh, weight)
                vals_dic[neigh] = cur_v
    return vals_dic

def print_paths(graph, prev, msg, src):
    for v in graph.keys():
        if v == src:
            continue
        if not v in prev:
            print("Could not find path to", v)
            continue
        path = v
        cost = 0
        u = v
        while u != src:
            past = u
            u = prev[u]
            cost += graph[u][past]
            path = u + " " + path
        print(v, "received", msg, "along path", path, "with cost", cost)

if __name__ == "__main__":
    graph = defaultdict(dict)
    
    infile = open(sys.argv[1], "r")

    for line in infile:
        data = line.split(" ")
        start = data[0]
        end = data[1]
        cost = int(data[2])

        graph[start][end] = cost
        graph[end][start] = cost
        
    cmd = input()
    while cmd != "exit":
        print("Command:", cmd)
        method, msg, src = cmd.split(" ")[:3]
        prev = None
        if method == "broadcast":
            ttl = int(cmd.split(" ")[-1])
            prev = broadcast(src, graph, ttl)
        elif method == "direct":
            prev = direct(src, graph)
        elif method == "MST":
            prev = mst(src, graph)
        else:
            print("Invalid command!")
        if prev != None:
            print_paths(graph, prev, msg, src)
        cmd = input()
    print("Goodbye!")
