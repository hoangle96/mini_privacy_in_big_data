'''
Created on Jan 20, 2019

@author: user
'''
import unittest
from hierarchical_clustering import single_linkage_clustering
class Test_Hierarchical_Clustering(unittest.TestCase):
    
    def test_hierar_clust_simple(self):
                    
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
        
        lst_nums = [10]
        taxonomy = single_linkage_clustering (lst_nums)
        expected_result = {"data":[10] , "children":[] , "index":[] }
        self.assertEqual(taxonomy , expected_result)
    
    def test_hierar_clust_1(self):
                    
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
        
        lst_nums = [1,2]
        taxonomy = single_linkage_clustering (lst_nums)
        expected_result = {"data":[1,2],"children":[
                                                    {"data":[1] , "children":[] , "index":[]},
                                                    {"data":[2] , "children":[] , "index":[]}]  }
        self.assertEqual(taxonomy , expected_result)
         
    def test_hierar_clust_2(self):
        
        lst_nums = [1,2,9,10]
        taxonomy = single_linkage_clustering (lst_nums)
        expected_result = {"data":[1,2,9,10] , "children":[
                                    {"data":[1,2],"children":[
                                                    {"data":[1] , "children":[] , "index":[]},
                                                    {"data":[2] , "children":[] , "index":[]}]  } ,
                                    {"data":[9,10],"children":[
                                                    {"data":[9] , "children":[] , "index":[]},
                                                    {"data":[10] , "children":[] , "index":[]}]  }
                                                           ]}
        self.assertEqual(taxonomy , expected_result)
     
    def test_hierar_clust_3(self):
        
        lst_nums = [1,2,9,10,100]
        taxonomy = single_linkage_clustering (lst_nums)
        expected_result = {"data":[1,2,9,10,100] ,"children":[
                                   {"data":[1,2,9,10] , "children":[
                                            {"data":[1,2],"children":[
                                                            {"data":[1] , "children":[] , "index":[]},
                                                            {"data":[2] , "children":[] , "index":[]}]  } ,
                                            {"data":[9,10],"children":[
                                                            {"data":[9] , "children":[] , "index":[]},
                                                            {"data":[10] , "children":[] , "index":[]}]  }
                                                                   ]},
                                    {"data":[100] , "children":[] , "index":[]}
                                                             ]}
                            
        self.assertEqual(taxonomy , expected_result)         
if __name__ == '__main__':
    unittest.main()