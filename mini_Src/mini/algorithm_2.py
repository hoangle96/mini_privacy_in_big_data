'''
Created on 13 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''
import copy


def algorithm_2(k, cover):
    print("algorithm 2 started")
    cluster = copy.deepcopy(cover);
    while intersecting_subsets(cluster)!=[]:
        [S_j, j, S_i, i] = intersecting_subsets(cluster)
        S_j = copy.deepcopy(cluster[j])
        S_i = copy.deepcopy(cluster[i])
        R = list(S_j & S_i)[0]
        if len(S_j) > k:         
            cluster[j] = S_j.difference(set([R]))        
        elif len(S_i) > k:    
            cluster[i] = S_i.difference(set([R]))
        else:
            cluster.remove(cluster[j])
            cluster.remove(cluster[i])
            cluster.append(S_j | S_i)
    print("algorithm 2 ended")
    return cluster
        
 
    
def intersecting_subsets(S):
    i = 0
    for s in S:
        j = 0
        for item in S:
            if(s == item):
                j = j + 1
                continue
            if len(item & s)!=0:
                return [item, j, s, i]
            j = j + 1
        i = i + 1
    return []
    

  