import sys
import copy

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def dist(a , b):
    return abs(a-b)

def make_dist_mat(lst_nums):
    mat = []
    for i in range(0 , len(lst_nums)):
        row = list(map(lambda num : dist(num,lst_nums[i]) , lst_nums))
        row[i] = sys.maxsize
        mat.append(row)
    return mat
def calc_min(mat):
    minVal = sys.maxsize
    min_i = 0
    min_j = 0
    for i in range (0 ,  len(mat)):
        for j in range (0 ,  len(mat[0])):
            if mat[i][j] < minVal :
                minVal = mat[i][j]
                min_i = i
                min_j = j
    return (min_i ,min_j , minVal)

def calc_dist_two_clusters(lst_clutser1 , lst_cluster2):
    mat = []
    for i in range(0 , len(lst_clutser1)):
        row = list(map(lambda num : dist(num,lst_clutser1[i]) , lst_cluster2))
        mat.append(row)
        (_ ,_ , minVal) = calc_min(mat)
        return minVal
       
    
def make_dist_mat_from_clusters(lst_clusters):
    mat = []
    for i in range(0 , len(lst_clusters)):    
        row = list(map(lambda cluster : calc_dist_two_clusters(cluster["data"],lst_clusters[i]["data"]) , lst_clusters))
        row[i] = sys.maxsize
        mat.append(row)
    return mat
def single_linkage_clustering (lst_nums):
    lst_children  = list(map(lambda num : {"data":[num] , "children":[] , "index":[]},lst_nums))
    while(len(lst_children) > 1): 
        dist_mat_clusters = make_dist_mat_from_clusters(lst_children)
        #print(dist_mat_clusters)
        (min_i ,min_j , _) = calc_min(dist_mat_clusters)
        clust_i = lst_children[min_i]
        clust_j = lst_children[min_j]
        cluster_i = copy.deepcopy(lst_children[min_i])
        cluster_j = copy.deepcopy(lst_children[min_j])
        lst_union = {"data":cluster_i["data"]+cluster_j["data"] , "children":[cluster_i , cluster_j] }
        lst_children.remove(clust_i)
        lst_children.remove(clust_j)
        lst_children.append(lst_union)
        #print("lstchildren : ")
        #print(lst_children)
    return lst_children.pop() 
