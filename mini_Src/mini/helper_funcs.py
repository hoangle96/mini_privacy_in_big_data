'''
Created on 2 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''

'''helper functions'''
from _functools import reduce
import re
'''updates a single index-i which corresponds to value-value in the node root'''
def map_iterator_int(value,i,root):
    children = root["children"] 
    if  children == []:
        if (root["data"][0]<=int(value)) and (int(value)<=root["data"][1]):
            root['index'].append(i)
    else:
        list(map(lambda child : map_iterator_int(value,i,child), children))
    '''
    for key,mapval in root.items():
        if key == 'children' :       
            if mapval != []:
                for child in root.get('children'):
                    map_iterator_int(value,i,child)        
            else: 
                r = range(root.get('data')[0],root.get('data')[1]+1)
                if int(value) in r:
                    to_add = i
                    root.get('index').append(to_add)
    '''
'''updates a single index-i which corresponds to value-value in the node root'''
def map_iterator_str(value,i,root): 
    children = root["children"] 
    if  children == []:
        if value.lower() == root["data"].lower():
            root['index'].append(i)
    else:
        list(map(lambda child : map_iterator_str(value,i,child), children))
    
    '''
    for key,mapval in root.items():
        if key == 'children' :       
            if mapval != []:
                for child in root.get('children'):
                    map_iterator_str(value,i,child)        
            else: 
                if value.lower() == root.get('data').lower(): 
                    to_add = i
                    root.get('index').append(to_add)
    ''' 
'''returns the size number of the node's-node support'''                    
def sum_of_supports(node):
    if node.get('children') == []:
        length=len(node.get('index'))
        return length
    
    lst=list(map(sum_of_supports,node.get('children')))    
    summ = reduce(lambda x,y: x+y,lst) 
    return summ
'''returns the set of the node's-node support'''
def set_of_supports(node):
    if node.get('children') == []:
        return set(node.get('index'))
        
    lst=list(map(set_of_supports,node.get('children')))    
    output_set = reduce(lambda x,y: x.union(y),lst) 
    return output_set
'''
def intersection_support(child, root):
    support_child = set_of_supports(child)
    support_root = set_of_supports(root)
    return support_child.intersection(support_root)
'''
'''tags nodes which their support is less than k with deleted mark - stops the current depth scan when reaching such a node'''
def remove_nodes_under_k(node,k):
    if sum_of_supports(node) < k :
        node.update({'isDeleted' : True})
    else:
        node.update({'isDeleted' : False})
        list(map(lambda n:remove_nodes_under_k(n,k) , node.get('children')))
'''       
def is_set_in_set(the_out_set,the_in_set):
    for item in the_out_set:
        if(the_in_set == item):
            return True
    return False
'''
'''returns the number of leaves in a node - is used in algorithm 4 in the computation of the cost function'''
def number_of_leaves(node):
    if node.get('children') == []:
        return 1
    
    lst=list(map(number_of_leaves,node.get('children')))    
    summ = reduce(lambda x,y: x+y,lst) 
    return summ
'''computes the generalized sets of the closed frequent sets(F_CF(denoted by S)) saves each R(j) in a set of its own 
   the combined row is R(j) 0<=j<=len(attributes_array_by_order_database) and there is a row for each set in F_CF(denoted by S)'''
def generalize_S(database_path, S, relevant_indexes,attributes_array_by_order_database):
    generalized_records = [[set() for i in range(0,len(attributes_array_by_order_database))] for j in range(0,len(S)) ] 
    with open(database_path) as f: 
        i = 1
        for line in f:
            line_arr = re.split(", |\\n",line)
            if i in relevant_indexes:
                for q in range(0,len(attributes_array_by_order_database)):
                    for j in range(0,len(S)):
                        if i in S[j]:
                            generalized_records[j][q].add(line_arr[q])
            i = i + 1
    return generalized_records




