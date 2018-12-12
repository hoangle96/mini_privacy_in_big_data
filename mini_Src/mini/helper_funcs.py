'''
Created on 2 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''

'''helper functions'''
from _functools import reduce

def map_iterator_int(value,i,root): 
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
    
def map_iterator_str(value,i,root): 
    for key,mapval in root.items():
        if key == 'children' :       
            if mapval != []:
                for child in root.get('children'):
                    map_iterator_str(value,i,child)        
            else: 
                if value.lower() == root.get('data').lower(): 
                    to_add = i
                    root.get('index').append(to_add)
                         
def sum_of_supports(node):
    if node.get('children') == []:
        length=len(node.get('index'))
        return length
    
    lst=list(map(sum_of_supports,node.get('children')))    
    summ = reduce(lambda x,y: x+y,lst) 
    return summ

def set_of_supports(node):
    if node.get('children') == []:
        return set(node.get('index'))
        
    lst=list(map(set_of_supports,node.get('children')))    
    output_set = reduce(lambda x,y: x.union(y),lst) 
    return output_set

def intersection_support(child, root):
    support_child = set_of_supports(child)
    support_root = set_of_supports(root)
    return support_child.intersection(support_root)

def remove_nodes_under_k(node,k):
    if sum_of_supports(node) < k :
        node.update({'isDeleted' : True})
    else:
        node.update({'isDeleted' : False})
        list(map(lambda n:remove_nodes_under_k(n,k) , node.get('children')))
        
def is_set_in_set(the_out_set,the_in_set):
    for item in the_out_set:
        if(the_in_set == item):
            return True
    return False

def number_of_leaves(node):
    if node.get('children') == []:
        return 1
    
    lst=list(map(number_of_leaves,node.get('children')))    
    summ = reduce(lambda x,y: x+y,lst) 
    return summ





