'''
Created on 12 Dec 2018

@author: yaeltu@wincs.cs.bgu.ac.il
'''
from __future__ import division
import re
import random
from _functools import reduce
from mini.algorithm_6_7 import algorithm_6
from mini.taxonomies import attributes_array_by_order_database,\
    attributes_array_int_then_string
from mini.helper_funcs import number_of_leaves

import sys
from numpy.core.test_rational import rational


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

def cost_function(generalized_record,attributes_array_by_order_database):
    summ = 0;
    r = len(attributes_array_by_order_database)
    for j in range(0,r):
        up = len(generalized_record[j]) - 1
        down = number_of_leaves(attributes_array_by_order_database[j]) - 1
        outcome = up / down
        summ = summ + outcome
    
    output = (1/r) * summ
    return output
    
def denumerator(S,D,E,k):
    d_without_e = D - E
    s_intersection_d_without_e = S & d_without_e
    min_val = min([len(s_intersection_d_without_e), 2*k -1])
    return min_val


        
def algorithm_4(relevant_indexes, F_cf, k, database_path,attributes_array_by_order_database):
    curr_cover= list()
    covered_records = set()
    minVal = sys.maxsize
    minS = set()
    S_R = set()
    ratio = sys.maxsize
    while(covered_records != relevant_indexes):
        #for item in F_cf:
        generalized_records = generalize_S(database_path, F_cf, relevant_indexes,attributes_array_by_order_database)
        ratios = list(map(lambda itemgen,itemfcf: (sys.maxsize,itemfcf) if denumerator(itemfcf, relevant_indexes, covered_records, k) == 0 else ((cost_function(itemgen,attributes_array_by_order_database) / denumerator(itemfcf, relevant_indexes, covered_records, k)),itemfcf),  generalized_records,F_cf))    
        (minVal, minS) = reduce(lambda tup1,tup2: (tup1[0],tup1[1]) if tup1[0] < tup2[0] else (tup2[0], tup2[1]), ratios)
        if(len(minS) <= (2*k -1)):
            S_R = minS
        elif len(minS & (relevant_indexes - covered_records)) >= (2*k -1):
            S_R = set(random.sample(minS & (relevant_indexes - covered_records), 2*k -1))
        else:
            max_val = max(k,len(minS & (relevant_indexes - covered_records)))
            S_R = minS & (relevant_indexes - covered_records) | set(random.sample(minS, max_val - len(minS & (relevant_indexes - covered_records))))
        covered_records = covered_records | S_R
        curr_cover.append(S_R)
    return curr_cover
        
            
            
            
            
            
    
    
    