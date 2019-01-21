'''
Created on Jan 19, 2019

@author: user
'''
import re
from hierarchical_clustering import single_linkage_clustering
from hierarchical_clustering import num

'''make the number taxonomie have intervals instead of sets of numbers in each node'''
def convert_from_newmap_to_oldmap(map_num):
    if map_num["children"] == []:
        num = map_num["data"][0]
        return {"data":[num,num] , "children":[],"index":[]}
    else:
        minVal = min(map_num["data"])
        maxVal = max(map_num["data"])
        return {"data":[minVal , maxVal] , 
                "children":list(map(convert_from_newmap_to_oldmap , map_num["children"])) }

'''populate the each list of numbers with its corresponding attribute numbers'''
def make_int_lists(list_num , database_path,attributes_array_by_order_database,attributes_array_int_then_string,num_lines):
    with open(database_path, 'r') as f: 
        l = 1
        i = 1
        for line in f:
            line_arr = re.split(", |\\n",line)
            #line_arr = line.split(", ")
            #print(line_arr)
            #print(len(line_arr) , " , ", len(attributes_array_by_order_database))
            if ("?" in line_arr) or (len(line_arr)!=1+len(attributes_array_by_order_database) ):
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                index_of_int = attributes_array_int_then_string.index(current_row)
                if index_of_int in range(0,len(list_num)):
                    #print(line_arr[j])
                    print("i : ",i ,"j : ", j)
                    n = num(line_arr[j])
                    if not(n in list_num[index_of_int]):
                        list_num[index_of_int].append(n) 
            if l>=num_lines:
                i = i + 1
                break        
            i = i + 1
            l = l + 1  
        
    f.close()
    return list_num
'''create taxonomies trees for the numbers attributes from the lists of numbers '''
def make_new_int_maps(list_num , attributes_array_by_order_database, attributes_array_int_then_string ):
    print("make_new_int_maps start")
    for i  in range(0 , len(list_num)):
        print("make_new_int_maps start for - i : ",i)
        hierarchical_clustering_i = single_linkage_clustering(list_num[i])
        new_map_i = convert_from_newmap_to_oldmap(hierarchical_clustering_i)
        curr_map = attributes_array_int_then_string[i]
        index_in_order = attributes_array_by_order_database.index(curr_map)
        attributes_array_by_order_database[index_in_order] = new_map_i
        attributes_array_int_then_string[i] = new_map_i
        