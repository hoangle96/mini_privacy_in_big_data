

from _functools import reduce
from mini.taxonomies import attributes_array_by_order_database
from mini.taxonomies import attributes_array_int_then_string
from mini.taxonomies import list_num
from mini.k_anon import k_anon


from mini.algorithm_6_7 import algorithm_6
from mini.algorithm_4 import algorithm_4
from mini.algorithm_2 import algorithm_2
from mini.make_int_taxonomies import make_int_lists , make_new_int_maps
from mini.test_taxonomies import *


'''
print("Enter k")
k = num(input())
'''

def algorithm_5(database_path, k, attributes_array_by_order_database,attributes_array_int_then_string,list_num):
    (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string,list_num)
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
    

''' build numbers taxonomies by the algorithm of hierarchical clustering '''
lists_num = make_int_lists(list_num,"./adult.data",attributes_array_by_order_database,attributes_array_int_then_string)
make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )

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

algorithm_5("./adult.data", 6, attributes_array_by_order_database,attributes_array_int_then_string,list_num)





