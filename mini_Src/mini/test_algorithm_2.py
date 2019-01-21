'''
Created on Jan 20, 2019

@author: user
'''
import unittest
from algorithm_2 import algorithm_2

class TestAlgo_2(unittest.TestCase):
    
    def test_algo_2_simple(self):
                    
        #self.assertEqual(1 , 1)
        #self.assertTrue(True)
        
        k = 2
        cover = [{1,2,3}]
        expected_result = [{1,2,3}]
        
        cluster = algorithm_2(k, cover)
        
        self.assertEqual(cluster, expected_result)
      
    def test_algo_2_simple_2(self):
        
        k = 2
        cover = [{1,2},{1,2,3}]
        
        
        expected_result = [{1,2,3}]
        
        cluster = algorithm_2(k, cover)
        
        self.assertEqual(cluster, expected_result)
        
    def test_algo_2_presentation_example(self):
        
        k = 2
        cover = [{1,5},{3,4},{1,2,5}]
        

        expected_result = [{1,2,5},{3,4}]
        
        cluster = algorithm_2(k, cover)
        
        for item in cluster :
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in cluster)
        
    def test_algo_2_k_equal_3(self):
        
        k = 3
        #check if changing the order in the cover matters
        cover = [{1,2,3,7,8},{4,5,6},{1,2,3}]
        

        expected_result = [{1,2,3,7,8},{4,5,6}]
        
        cluster = algorithm_2(k, cover)
    
        for item in cluster :
            self.assertTrue(item in expected_result)
        for item in expected_result :
            self.assertTrue(item in cluster)
    
    def test_algo_2_k_equal_3_all_intersecting(self):
        
        k = 3
        cover = [{1,2,3,4,7,8},{4,5,6},{1,2,3}]
        

        expected_result1 = [{1,2,3},{4,5,6,7,8}]
        expected_result2 = [{1,2,3,7,8},{4,5,6}]
        cluster = algorithm_2(k, cover)
    
        def two_way_contain(list1 , list2):
            for item in list1 :
                if not(item in list2):
                    return False
            for item in list2 :
                if not(item in list1):
                    return False 
            return True
        isLegalResult = two_way_contain(cluster , expected_result1) or two_way_contain(cluster , expected_result2) 
        self.assertTrue(isLegalResult) 
          
if __name__ == '__main__':
    unittest.main()