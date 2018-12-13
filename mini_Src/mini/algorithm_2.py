'''
Created on 13 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''
import copy


def algorithm_2(k, cover):
    cluster = copy.deepcopy(cover);
    while intersecting_subsets(cluster)!=[]:
        [S_j,S_i] = intersecting_subsets(cluster)
        R = list(S_j & S_i)[0]
        if len(S_j) > k:
            S_j = S_j - set(R)
        elif len(S_i) > k:
            S_i = S_i - set(R)
        else:
            cluster.remove(S_j)
            cluster.remove(S_i)
            cluster.append(S_j | S_i)
    return cluster
        
 
    
def intersecting_subsets(S):
    for s in S:
        for item in S:
            if(s == item):
                continue
            if len(item & s)!=0:
                return [item,s]
    return []
    

  