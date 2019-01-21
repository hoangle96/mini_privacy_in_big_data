'''
Created on Jan 19, 2019

@author: user
'''
import unittest
from algorithm_4 import algorithm_4
from make_int_taxonomies import make_int_lists , make_new_int_maps

class TestAlgo_4(unittest.TestCase):
    
    def test_algo_4_first_two_of_adult(self):
        
        relevant_indexes = {1,2,3,4}
        F_cf = [{1,3},{2,4},{3,4},{1,2,3,4}]
        k = 2
        database_path = "./mini_Src/mini/dbs/test_db_cover_1"
        age_map = {'data': [38, 53], 
                   'children': [
                        {'data': [38, 39], 'children': [
                                            {'data': [39, 39], 'children': [], 'index': [1]}, 
                                            {'data': [38, 38], 'children': [], 'index': [3]}]}, 
                        {'data': [50, 53], 'children': [
                                            {'data': [50, 50], 'children': [], 'index': [2]}, 
                                            {'data': [53, 53], 'children': [], 'index': [4]}]}]}

        workclass_map = {"data" : "*", "children": 
                 [{"data" : "private", "children" :[],"index":[3,4]}, {"data": "self-emp", "children" : 
                                                         [{"data" : "self-emp-not-inc", "children": [],"index":[2]},
                                                          {"data" : "self-emp-inc", "children": [],"index":[]}
                                                          ]},
                                                          {"data" : "gov", "children":
                                                           [{"data" : "federal-gov", "children": [],"index":[]},{"data" : "local-gov", "children": [],"index":[]},{"data" : "state-gov", "children": [],"index":[1]}]},
                                                          {"data": "no income", "children": [{"data" : "without-pay", "children" :[],"index":[]},{"data" : "never-worked", "children": [],"index":[]}]}]}


        attributes_array_by_order_database = [age_map , workclass_map]
        '''
        attributes_array_int_then_string = [age_map , workclass_map]
        first_list = []
        list_num = [first_list]
        lists_num = make_int_lists(list_num,database_path,attributes_array_by_order_database,attributes_array_int_then_string)
        make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )
        print(attributes_array_by_order_database[0])
        print(attributes_array_by_order_database[1])
        '''
        expected_result = [{3,4},{1,3},{2,4}]
        cover = algorithm_4(relevant_indexes, F_cf, k, database_path,attributes_array_by_order_database)
        for item in cover :
            #print(item)
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in cover)
        
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
    def test_algo_4_multiple_1(self):
        
        relevant_indexes = {1,2,3}
        F_cf = [{1,2},{2,3},{1,2,3}]
        k = 2
        database_path = "./mini_Src/mini/dbs/test_db_multiple.txt"
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [1, 1], 'children': [], 'index': [1,2]}, 
                              {'data': [2, 2], 'children': [], 'index': [3]}]}
        
        taxonomy_second = {'data': [3, 4], 
                           'children': [
                               {'data': [3, 3], 'children': [], 'index': [1]}, 
                               {'data': [4, 4], 'children': [], 'index': [2,3]}]}
        attributes_array_by_order_database = [taxonomy_first , taxonomy_second]

        expected_result = [{1,2},{2,3}]
        cover = algorithm_4(relevant_indexes, F_cf, k, database_path,attributes_array_by_order_database)
        for item in cover :
            #print(item)
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in cover) 
    
    def test_algo_4_multiple_1_k_equal_3(self):
        
        relevant_indexes = {1,2,3}
        F_cf = [{1,2,3}]
        k = 3
        database_path = "./mini_Src/mini/dbs/test_db_multiple.txt"
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [1, 1], 'children': [], 'index': [1,2]}, 
                              {'data': [2, 2], 'children': [], 'index': [3]}]}
        
        taxonomy_second = {'data': [3, 4], 
                           'children': [
                               {'data': [3, 3], 'children': [], 'index': [1]}, 
                               {'data': [4, 4], 'children': [], 'index': [2,3]}]}
        attributes_array_by_order_database = [taxonomy_first , taxonomy_second]

        expected_result = [{1,2,3}]
        cover = algorithm_4(relevant_indexes, F_cf, k, database_path,attributes_array_by_order_database)
        for item in cover :
            #print(item)
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in cover) 
    
    def test_algo_4_multiple_2(self):
        
        relevant_indexes = {1,2,3}
        F_cf = [{1,2},{2,3},{1,2,3},{1,3}]
        k = 2
        database_path = "./mini_Src/mini/dbs/test_db_multiple_2.txt"
        taxonomy_first = {'data': [1, 2], 
                          'children': [
                              {'data': [1, 1], 'children': [], 'index': [1,2]}, 
                              {'data': [2, 2], 'children': [], 'index': [3]}]}
        taxonomy_str = {"data":"instruments", 
                        "children":[
                            {"data": "String", "children":[{"data": "guitar", "children":[],"index":[1,3]}],"index":[]},
                            {"data": "Percussion", "children":[{"data": "piano", "children":[],"index":[2]}],"index":[]}]}
        
        taxonomy_second = {'data': [3, 4], 
                           'children': [
                               {'data': [3, 3], 'children': [], 'index': [1]}, 
                               {'data': [4, 4], 'children': [], 'index': [2,3]}]}
        attributes_array_by_order_database = [taxonomy_first , taxonomy_str , taxonomy_second]

        expected_result1 = [{1,2},{2,3}]
        expected_result2 = [{1,2},{1,3}]
        expected_result3 = [{2,3},{1,3}]
        
        cover = algorithm_4(relevant_indexes, F_cf, k, database_path,attributes_array_by_order_database)
        def two_way_contain(list1 , list2):
            for item in list1 :
            #print(item)
                if not(item in list2):
                    return False
            for item in list2 :
                if not(item in list1):
                    return False 
            return True
        isLegalResult = two_way_contain(cover , expected_result1) or two_way_contain(cover , expected_result2) or two_way_contain(cover , expected_result3) 
        self.assertTrue(isLegalResult)    
if __name__ == '__main__':
    unittest.main()