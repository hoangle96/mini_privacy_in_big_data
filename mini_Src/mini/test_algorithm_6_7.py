'''
Created on Jan 19, 2019

@author: user
'''
import unittest
from mini.algorithm_6_7 import algorithm_6
from mini.make_int_taxonomies import make_int_lists , make_new_int_maps
class TestAlgo_6_7(unittest.TestCase):
    
    def test_algo_6_7_article(self):
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
        database_path = "./mini_Src/mini/dbs/test_db_clothing.txt"
        k = 3
        DB_taxonomy = {"data":"Clothing", 
                               "children":[{"data": "Footwear", 
                                            "children":[{"data": "Shoes", "children":[],"index":[]},
                                                        {"data": "Boots", "children":[],"index":[]},
                                                        {"data": "Sandals", "children":[],"index":[]}]},
                                           
                                            {"data": "Clothes", 
                                             "children":[ {"data": "Shirts", "children":[],"index":[]},
                                                        {"data": "Pants", "children":[],"index":[]},
                                                        {"data": "Outdoors", "children":[
                                                                                        {"data": "Sport-Jackets", "children":[],"index":[]},
                                                                                        {"data": "Ski-Pants", "children":[],"index":[]}
                                                                                        ]}        
                                                        
                                                        ]}
                                            ]}

        attributes_array_by_order_database = [DB_taxonomy]
        attributes_array_int_then_string = [DB_taxonomy]
        list_num = []
        expected_result = [{1,2,3},{1,2,3,4,5,6},{8,9,10},{7,8,9,10},{1,2,3,4,5,6,7,8,9,10}]
        (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string,list_num)
        #print(F_cf)
        for item in F_cf :
            #print(item)
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in F_cf)
            
        self.assertEqual(relevant_indexes , {1,2,3,4,5,6,7,8,9,10})
        self.assertEqual(lines_in_database , 10)
         
         
    def test_algo_6_7_multiple(self):
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
        database_path = "./mini_Src/mini/dbs/test_db_multiple.txt"
        k = 2
        taxonomy_first = {"tag":"first"}
        taxonomy_second = {"tag":"second"}

        attributes_array_by_order_database = [taxonomy_first , taxonomy_second]
        attributes_array_int_then_string = [taxonomy_first , taxonomy_second]
        first_list = []
        second_list = []
        list_num = [first_list , second_list]
        lists_num = make_int_lists(list_num,database_path,attributes_array_by_order_database,attributes_array_int_then_string)
        make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )
        '''
        #bug found in make list numbers from database - duplicates were not removed before making taxonomy
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [2, 2], 'children': [], 'index': [3]}, 
                              {'data': [1, 1], 'children': [
                                                            {'data': [1, 1], 'children': [], 'index': [1]}, 
                                                            {'data': [1, 1], 'children': [], 'index': [2]}
                                                            ]}]}
        taxonomy_second ={'data': [3, 4], 
                          'children': [
                                        {'data': [3, 3], 'children': [], 'index': [1]}, 
                                        {'data': [4, 4], 'children': [
                                                                    {'data': [4, 4], 'children': [], 'index': [2]}, 
                                                                    {'data': [4, 4], 'children': [], 'index': [3]}]}]}
        '''
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [1, 1], 'children': [], 'index': [1,2]}, 
                              {'data': [2, 2], 'children': [], 'index': [3]}]}
        
        taxonomy_second = {'data': [3, 4], 
                           'children': [
                               {'data': [3, 3], 'children': [], 'index': [1]}, 
                               {'data': [4, 4], 'children': [], 'index': [2,3]}]}
        #print(attributes_array_by_order_database[0]) 
        #print(attributes_array_by_order_database[1])
        
        expected_result = [{1,2},{2,3},{1,2,3}]
        (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string,list_num)
        for item in F_cf :
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in F_cf)
            
        self.assertEqual(relevant_indexes , {1,2,3})
        self.assertEqual(lines_in_database , 3)
    def test_algo_6_7_multiple_str_and_int(self):
        
        database_path = "./mini_Src/mini/dbs/test_db_multiple_2.txt"
        k = 2
        taxonomy_first = {"tag":"first"}
        taxonomy_second = {"tag":"second"}
        taxonomy_str = {"data":"instruments", 
                        "children":[
                            {"data": "String", "children":[{"data": "guitar", "children":[],"index":[]}],"index":[]},
                            {"data": "Percussion", "children":[{"data": "piano", "children":[],"index":[]}],"index":[]}]}
        attributes_array_by_order_database = [taxonomy_first ,taxonomy_str, taxonomy_second]
        attributes_array_int_then_string = [taxonomy_first , taxonomy_second,taxonomy_str]
        first_list = []
        second_list = []
        list_num = [first_list , second_list]
        lists_num = make_int_lists(list_num,database_path,attributes_array_by_order_database,attributes_array_int_then_string)
        make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )
        
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [1, 1], 'children': [], 'index': [1,2]}, 
                              {'data': [2, 2], 'children': [], 'index': [3]}]}
        
        taxonomy_second = {'data': [3, 4], 
                           'children': [
                               {'data': [3, 3], 'children': [], 'index': [1]}, 
                               {'data': [4, 4], 'children': [], 'index': [2,3]}]}
        
        expected_result = [{1,2},{2,3},{1,2,3},{1,3}]
        (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string,list_num)
        for item in F_cf :
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in F_cf)
            
        self.assertEqual(relevant_indexes , {1,2,3})
        self.assertEqual(lines_in_database , 3)         
if __name__ == '__main__':
    unittest.main()