'''
Created on Jan 17, 2019

@author: user
'''
import unittest
from mini.helper_funcs import map_iterator_int,map_iterator_str,sum_of_supports,set_of_supports
from mini.helper_funcs import remove_nodes_under_k
from mini.helper_funcs import number_of_leaves , generalize_S

class TestHelper(unittest.TestCase):

    def test_map_iterator_int_leaf(self):
        root = {"data":[9,11] ,"children":[] ,"index":[] }
        value = 10
        i = 1
        map_iterator_int(value,i,root)
        self.assertTrue(i in root["index"] )
        root = {"data":[10,10] ,"children":[] ,"index":[] }
        value = 10
        i = 2
        map_iterator_int(value,i,root)
        self.assertTrue(i in root["index"] )
    def test_map_iterator_int_inner_node(self):
        root = {"data":[9,11] ,"children":
                                [{"data":[9,10] , "children":[] , "index":[]},
                                 {"data":[11,11] , "children":[] , "index":[]}
                                 ] ,"index":[] }
        value = 10
        i = 1
        map_iterator_int(value,i,root)
        self.assertTrue(i in root["children"][0]["index"] )
        
        root = {"data":[9,11] ,"children":
                                [{"data":[9,9] , "children":[] , "index":[]},
                                 {"data":[10,10] , "children":[] , "index":[]},
                                 {"data":[11,11] , "children":[] , "index":[]}
                                 ] ,"index":[] }
        value = 10
        i = 1
        map_iterator_int(value,i,root)
        self.assertTrue(i in root["children"][1]["index"] )
        
    def test_map_iterator_str_leaf(self):
        root = {"data":"atlantic" ,"children":[] ,"index":[] }
        value = "atlantic"
        i = 1
        map_iterator_str(value,i,root)
        self.assertTrue(i in root["index"])
    def test_map_iterator_str_inner_node(self):
        root = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[] , "index":[]},
                                 {"data":"atlantic" , "children":[] , "index":[]},
                                 {"data":"indian" , "children":[] , "index":[]}
                                 ] }
        value = "indian"
        i = 1
        map_iterator_str(value,i,root)
        self.assertTrue(i in root["children"][2]["index"] )
    
    def test_sum_of_supports_leaf(self):
        node = {"data":[9,11] ,"children":[] ,"index":[1 , 2] }
        summ = sum_of_supports(node)
        self.assertEqual(summ, 2)    
    def test_sum_of_supports_inner_node(self):
        node = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[] , "index":[1 ,2]},
                                 {"data":"atlantic" , "children":[] , "index":[3]},
                                 {"data":"indian" , "children":[] , "index":[4,5,6,11]}
                                 ] }
        summ = sum_of_supports(node)
        self.assertEqual(summ, 7)
    
    def test_set_of_supports_leaf(self):
        node = {"data":[9,11] ,"children":[] ,"index":[1 , 2] }
        set_of_sup = set_of_supports(node)
        self.assertEqual(set_of_sup, {1,2})        
    def test_set_of_supports_inner_node(self):
        node = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[] , "index":[1 ,2]},
                                 {"data":"atlantic" , "children":[] , "index":[3]},
                                 {"data":"indian" , "children":[] , "index":[4,5,6,11]}
                                 ] }
        set_of_sup = set_of_supports(node)
        self.assertEqual(set_of_sup, {1,2,3,4,5,6,11})   
    def test_remove_nodes_under_k_leaf(self):
        node = {"data":[9,11] ,"children":[] ,"index":[1 , 2] }
        k = 3
        remove_nodes_under_k(node,k)
        self.assertTrue(node['isDeleted'])
        node = {"data":[9,11] ,"children":[] ,"index":[1 , 2] }
        k = 2
        remove_nodes_under_k(node,k)
        self.assertTrue((not('isDeleted' in node)) or (node['isDeleted'] == False))        
    def test_remove_nodes_under_k_inner_node(self):
        node = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[
                                                {"data":"coral sea" , "children":[] , "index":[10]}
                                                ] , 
                                  "index":[1 ,2]},
                                 {"data":"atlantic" , "children":[] , "index":[3]},
                                 {"data":"indian" , "children":[] , "index":[4,5,6,11]}
                                 ] }
        k = 3
        remove_nodes_under_k(node,k)
        self.assertTrue((node['isDeleted'] is None) or (node['isDeleted'] == False))
        self.assertTrue(node["children"][0]['isDeleted'])
        self.assertTrue((not('isDeleted' in node["children"][0]["children"][0])) or (node["children"][0]["children"][0]['isDeleted'] == False))
        self.assertTrue(node["children"][1]['isDeleted'])
        self.assertTrue((not('isDeleted' in node["children"][2])) or (node["children"][2]['isDeleted'] == False))

    def test_number_of_leaves_leaf(self):
        node = {"data":[9,11] ,"children":[] ,"index":[1 , 2] }
        num = number_of_leaves(node)
        self.assertEqual(num, 1)        
    def test_number_of_leaves_inner_node(self):
        node = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[] , "index":[1 ,2]},
                                 {"data":"atlantic" , "children":[] , "index":[3]},
                                 {"data":"indian" , "children":[] , "index":[4,5,6,11]}
                                 ] }
        num = number_of_leaves(node)
        self.assertEqual(num, 3)
    
    def test_generalize_S(self):
        
        database_path = "./mini_Src/mini/dbs/test_db_helper.txt"
        S = [{1,2},{2,3}]
        relevant_indexes ={1,2,3}
        nodeoceans = {"data":"oceans" ,"children":
                                [{"data":"pacific" , "children":[] , "index":[3]},
                                 {"data":"atlantic" , "children":[] , "index":[]},
                                 {"data":"indian" , "children":[] , "index":[1,2]}
                                 ] }
        nodenums = {"data":[10,30] ,"children":
                                [{"data":[10,19] , "children":[] , "index":[1]},
                                 {"data":[20,29] , "children":[] , "index":[2]},
                                 {"data":[30,30] , "children":[] , "index":[3]}
                                 ] }
        attributes_array_by_order_database = [nodenums,nodeoceans]
        generalized_records = generalize_S(database_path, S, relevant_indexes,attributes_array_by_order_database)
        self.assertEqual(generalized_records[0][0] ,{"10" , "20" } )
        self.assertEqual(generalized_records[0][1] ,{"indian"} )
        self.assertEqual(generalized_records[1][0] ,{"20" , "30" } )
        self.assertEqual(generalized_records[1][1] ,{"indian" , "pacific"} )
        
if __name__ == '__main__':
    unittest.main()