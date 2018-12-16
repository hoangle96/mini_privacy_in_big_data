
import re
from _functools import reduce
from mini.taxonomies import attributes_array_by_order_database
from mini.taxonomies import attributes_array_int_then_string
from mini.taxonomies import list_num
from mini.helper_funcs import remove_nodes_under_k,map_iterator_int,map_iterator_str, generalize_S
from mini.k_anon import k_anon


from mini.algorithm_6_7 import algorithm_7,algorithm_6
from mini.algorithm_6_7 import algorithm_6_test
from mini.algorithm_4 import algorithm_4
from mini.algorithm_2 import algorithm_2
from mini.test_taxonomies import *
import copy

from mini.hierarchical_clustering import single_linkage_clustering
from mini.hierarchical_clustering import num


def convert_from_newmap_to_oldmap(map_num):
    if map_num["children"] == []:
        num = map_num["data"][0]
        return {"data":[num,num] , "children":[],"index":[]}
    else:
        minVal = min(map_num["data"])
        maxVal = max(map_num["data"])
        return {"data":[minVal , maxVal] , 
                "children":list(map(convert_from_newmap_to_oldmap , map_num["children"])) }


def make_int_lists(list_num , database_path,attributes_array_by_order_database):
    with open(database_path, 'r') as f: 
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
                    list_num[index_of_int].append(num(line_arr[j]))   
            i = i + 1
    f.close()
    return list_num

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

#print(attributes_array_int_then_string)

#print(lists_num)

#make_new_int_maps(lists_num , attributes_array_int_then_string , attributes_array_by_order_database )
'''
print("Enter k")
k = num(input())
'''
#print(algorithm_6_test(3,[DB_test]))
#print(attributes_array_by_order_database[4])#age map
'''
def algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string):
    step 1
    with open(database_path) as f: 
        i = 1
        relevant_indexes = set()
        for line in f:
            line_arr = re.split(", |\\n",line)
            if "?" in line_arr:
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                if attributes_array_int_then_string.index(current_row) in range(0,1):
                    map_iterator_int(line_arr[j],i,current_row)
                else:
                    map_iterator_str(line_arr[j],i,current_row)
            relevant_indexes.add(i)        
            i = i + 1
    f.close()
            
    step 2
    list(map(lambda n:remove_nodes_under_k(n,k),attributes_array_by_order_database))
     steps 5-9
    attributes_map = {"data": "root", "children": attributes_array_by_order_database}
    processed = []
    F_cf = []
    F_cf = algorithm_7(attributes_map, k, processed,F_cf)
    return (F_cf, relevant_indexes)
  '''  

def algorithm_5(database_path, k, attributes_array_by_order_database):
    (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string)
    #print("****F_cf : ****"  )
    #for item in F_cf :
    #    print(item)
    union_fcf = reduce(lambda a , b : a | b , F_cf)
    if(union_fcf != relevant_indexes):
        print("error occured - can not produce k-anonimity ")
        f= open("errorfcf","w+")
        for item in F_cf:
            f.write(str(item))
            f.write("\n")
        f.write("relevant_indexes : \n")
        f.write(str(relevant_indexes))
        f.write("\n")
        f.close()
        return
    else:
        f= open("fcf","w+")
        for item in F_cf:
            f.write(str(item))
            f.write("\n")
        f.write("relevant_indexes : \n")
        f.write(str(relevant_indexes))
        f.write("\n")
        f.close()
    #print("relevant_indexes : ")
    #print(relevant_indexes)
    
    cover = algorithm_4(relevant_indexes, F_cf,k, database_path,attributes_array_by_order_database)
    cluster = algorithm_2(k,cover)
    k_anon(database_path, cluster, relevant_indexes,attributes_array_by_order_database, lines_in_database)
    
   
    
  
'''
list_num = [list_age]
lists_num = make_int_lists(list_num)    
make_new_int_maps(lists_num , DB_test1, DB_test2 )
(F_cf, relevant_indexes) = algorithm_6("./database",k,DB_test1,DB_test2)
print(F_cf)
print(algorithm_4(relevant_indexes, F_cf, k, "./database",DB_test1))
'''


#lists_num = make_int_lists(list_num,"./adult.data",attributes_array_by_order_database)
#make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )

'''
def write_to_file(attributes_array_by_order_database):
    f= open("attributes_taxonomies_num_lines","w+")
    def write_in_iter_rec(item ,f , space_num):
        f.write("\n")
        f.write(" "*space_num)
        f.write(str(item["data"]))
        write_to_file_rec(item , f , space_num+1)
        
    def write_to_file_rec(root , f , space_num):
        if root["children"] == []:
            f.write(" "*space_num)
            f.write("leaf : ")
            f.write(str(root["data"]))
        else:
            f.write("\n")
            f.write(" "*space_num)
            f.write(str(root["data"]))
            list(map(lambda item : write_in_iter_rec(item , f , space_num+1) , root["children"] ))
            
    write_to_file_rec({"data": "root", "children": attributes_array_by_order_database} , f , 0)
    f.close()
    
write_to_file(attributes_array_by_order_database)
'''
'''
(F_cf, relevant_indexes, i) = algorithm_6("./adult.data",3,attributes_array_by_order_database,attributes_array_int_then_string)
print("F_cf: ")
for item in F_cf:
    print(item)
'''
'''
cover = algorithm_4(relevant_indexes, F_cf, k, "./adult.data",attributes_array_by_order_database)
print("cover: ", cover)
cluster = algorithm_2(k,cover)
print("cluster: ", cluster)
'''

algorithm_5("./adult.data", 200, attributes_array_by_order_database)





