
import re
from taxonomies import attributes_array_by_order_database
from taxonomies import attributes_array_int_then_string
from taxonomies import list_num

from algorithm_6_7 import algorithm_6
from algorithm_6_7 import algorithm_6_test
from test_taxonomies import *

from hierarchical_clustering import single_linkage_clustering
from hierarchical_clustering import num


def convert_from_newmap_to_oldmap(map_num):
    if map_num["children"] == []:
        num = map_num["data"][0]
        return {"data":[num,num] , "children":[],"index":[]}
    else:
        minVal = min(map_num["data"])
        maxVal = max(map_num["data"])
        return {"data":[minVal , maxVal] , 
                "children":list(map(convert_from_newmap_to_oldmap , map_num["children"])) }


def make_int_lists(list_num):
    with open("./database") as f: 
        i = 1
        for line in f:
            line_arr = re.split(", |\\n",line)
            #line_arr = line.split(", ")
            if "?" in line_arr:
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                index_of_int = attributes_array_int_then_string.index(current_row)
                if index_of_int in range(0,6):
                    #print(line_arr[j])
                    list_num[index_of_int].append(num(line_arr[j]))   
            i = i + 1
    return list_num

def make_new_int_maps(list_num , attributes_array_int_then_string , attributes_array_by_order_database):
    for i  in range(0 , len(list_num)):
        hierarchical_clustering_i = single_linkage_clustering(list_num[i])
        new_map_i = convert_from_newmap_to_oldmap(hierarchical_clustering_i)
        curr_map = attributes_array_int_then_string[i]
        index_in_order = attributes_array_by_order_database.index(curr_map)
        attributes_array_by_order_database[index_in_order] = new_map_i
        attributes_array_int_then_string[i] = new_map_i

#print(attributes_array_int_then_string)
lists_num = make_int_lists(list_num)
#print(lists_num)

make_new_int_maps(lists_num , attributes_array_int_then_string , attributes_array_by_order_database )

print(algorithm_6_test(3,[DB_test]))
#print(attributes_array_by_order_database[4])#age map
print(algorithm_6("./database",2,attributes_array_by_order_database,attributes_array_int_then_string))




