    
DB_test = {"data":"Clothing", 
           "children":[{"data": "Footwear", 
                        "children":[{"data": "Shoes", "children":[],"index":["R1","R2","R3"]},
                                    {"data": "Boots", "children":[],"index":["R4","R5"]},
                                    {"data": "Sandals", "children":[],"index":["R6"]}]},
                       
                        {"data": "Clothes", 
                         "children":[ {"data": "Shirts", "children":[],"index":[]},
                                    {"data": "Pants", "children":[],"index":[]},
                                    {"data": "Outdoors", "children":[
                                                                    {"data": "Sport-Jackets", "children":[],"index":["R8","R9","R10"]},
                                                                    {"data": "Ski-Pants", "children":[],"index":["R7"]}
                                                                    ]}        
                                    
                                    ]}
                        ]}

age_map = {"data" : "17-90", "children" :[{"data":[17,25], "children": [], "index":[]},{"data":[26,35], "children": [],"index":[]},{"data":[36,45], "children": [],"index":[]},
                                          {"data": [46,55], "children": [],"index":[]},{"data":[56,65], "children": [],"index":[]},{"data":[66,75], "children": [],"index":[]},
                                          {"data":[76,85], "children": [],"index":[]},{"data":[86,95], "children": [],"index":[]}]}
work_map = {"data" : "*", "children": 
                 [{"data" : "private", "children" :[],"index":[]}, 
                  {"data": "self-emp", "children" : 
                                                [{"data" : "self-emp-not-inc", "children": [],"index":[]}]},
                  {"data" : "gov", "children":
                                                [{"data" : "state-gov", "children": [],"index":[]}]}]}
DB_test1 = [age_map,work_map
            ]   


DB_test2 = [age_map,work_map
            ]   
 
