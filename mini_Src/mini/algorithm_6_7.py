'''
Created on 2 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''

import re
from mini.helper_funcs import map_iterator_int
from mini.helper_funcs import map_iterator_str
from mini.helper_funcs import remove_nodes_under_k
from mini.helper_funcs import sum_of_supports
from _functools import reduce
from mini.helper_funcs import set_of_supports


def algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string):
    '''step 1'''
    with open(database_path) as f: 
        i = 1
        for line in f:
            line_arr = re.split(", |\\n",line)
            #line_arr = line.split(", ")
            if "?" in line_arr:
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                if attributes_array_int_then_string.index(current_row) in range(0,6):
                    map_iterator_int(line_arr[j],i,current_row)
                else:
                    map_iterator_str(line_arr[j],i,current_row)        
            i = i + 1
            
    '''step 2'''
    list(map(lambda n:remove_nodes_under_k(n,k),attributes_array_by_order_database))
    ''' steps 5-9'''
    attributes_map = {"data": "root", "children": attributes_array_by_order_database}
    processed = []
    F_cf = []
    F_cf = algorithm_7(attributes_map, k, processed,F_cf)
    return F_cf

def algorithm_6_test(k,taxonomies_tree):
    '''step 1'''
            
    '''step 2'''
    list(map(lambda n:remove_nodes_under_k(n,k),taxonomies_tree))
    ''' steps 5-9'''
    attributes_map = {"data": "root", "children": taxonomies_tree}
    processed = []
    F_cf = []
    F_cf = algorithm_7(attributes_map, k, processed,F_cf)
    return F_cf  

def algorithm_7(root,k,processed,closed):
    
                     
    if(root in processed) or sum_of_supports(root) < k:
        return []

    processed.append(root)
    isRootClosed = True
    break_loop = False
    
    support_of_root = reduce(lambda a , b : a.intersection(b) ,  list(map(set_of_supports , root["children"]) ) ) 
    
    filtered_children = list (filter(lambda x : x.get("isDeleted") != True ,root.get('children')))
    
    for j in range(0,len(filtered_children)):
        filtered_grand_children = list(filter(lambda x : x.get("isDeleted") != True ,filtered_children[j].get('children')))
        for i in range(0,len(filtered_grand_children)):
            child = filtered_grand_children[i]
            new_support = set_of_supports(child).intersection(support_of_root) 
            if(len(new_support) >= k):
                if(len(new_support) == sum_of_supports(root)):
                    isRootClosed = False
                new_child_list = filtered_children
                #head = new_child_list[:j]
                #tail = new_child_list[j+1:]
                new_root = {"data":root["data"] , "children":new_child_list[:j]+[child]+new_child_list[j+1:]}
                algorithm_7(new_root, k, processed, closed)
                if(isRootClosed == False):
                    break_loop = True
                    break
                
        if(break_loop):
            break
    
    if(isRootClosed):
        if(not support_of_root in closed):
            closed.append(support_of_root)
        return closed
    else:
        return closed
