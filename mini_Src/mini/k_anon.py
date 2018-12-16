'''
Created on 13 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''

from mini.helper_funcs import generalize_S



def k_anon(database_path, cluster, relevant_indexes,attributes_array_by_order_database, lines_in_database):
    print("k_anon started")
    generalized_cluster = generalize_S(database_path, cluster, relevant_indexes,attributes_array_by_order_database)
    f= open("generalized_database.txt","w+")
    '''changed'''
    for i in relevant_indexes:
        index = find_index_in_cluster(cluster, i)
        str_new_line = ""
        for j in range(0,len(attributes_array_by_order_database)-1):
            str_new_line = str_new_line + str(generalized_cluster[index][j]) + ", "
            
        str_new_line = str_new_line + str(generalized_cluster[index][len(attributes_array_by_order_database)-1])
        #print(str_new_line)
        f.write(str_new_line)
        f.write("\n")
    
    f.close()   
    print("k_anon ended")        
def find_index_in_cluster(cluster, line_number):
    i = 0
    for item in cluster:
        if line_number in item:
            return i
        i = i + 1
    return i
        