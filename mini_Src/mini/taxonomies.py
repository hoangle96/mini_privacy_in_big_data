'''
Created on 2 Dec 2018
31, Private, 53042, Some-college, 10, Married-civ-spouse, Machine-op-inspct, Husband, Black, Male, 0, 0, 40, Trinadad&Tobago, <=50K
@author: yaeltu@wincs.cs.bgu.ac.il
'''
# building a taxonomy tree for each attribute
age_map = {"data" : "0-120", "children" :[{"data":[0,25], "children": [], "index":[]},{"data":[26,35], "children": [],"index":[]},{"data":[36,45], "children": [],"index":[]},
                                          {"data": [46,55], "children": [],"index":[]},{"data":[56,65], "children": [],"index":[]},{"data":[66,75], "children": [],"index":[]},
                                          {"data":[76,85], "children": [],"index":[]},{"data":[86,120], "children": [],"index":[]}]}

workclass_map = {"data" : "*", "children": 
                 [{"data" : "private", "children" :[],"index":[]}, {"data": "self-emp", "children" : 
                                                         [{"data" : "self-emp-not-inc", "children": [],"index":[]},
                                                          {"data" : "self-emp-inc", "children": [],"index":[]}
                                                          ]},
                                                          {"data" : "gov", "children":
                                                           [{"data" : "federal-gov", "children": [],"index":[]},{"data" : "local-gov", "children": [],"index":[]},{"data" : "state-gov", "children": [],"index":[]}]},
                                                          {"data": "no income", "children": [{"data" : "without-pay", "children" :[],"index":[]},{"data" : "never-worked", "children": [],"index":[]}]}]}

fnlwgt_map = {"data" : "0-10000000", "children" :
              [{"data": "0-499999", "children" :
                [{"data" : [0,124999] , "children":[],"index":[]}, {"data": [125000,249999], "children": [],"index":[]}, {"data": [250000,374999], "children" : [],"index":[]}, {"data": [375000,499999], "children" :[],"index":[]}]},
              {"data": "500000-1000000", "children":
              [{"data" : [500000,624999] , "children":[],"index":[]}, {"data": [625000,749999], "children": [],"index":[]}, {"data": [750000,874999], "children" : [],"index":[]}, {"data": [875000,10000000], "children" :[],"index":[]}]}]}

education_map = {"data" : "*", "children" : 
                 [{"data" : "academic", "children":
                   [{"data" : "bachelors", "children" : [],"index":[]},
                    {"data" : "some-college", "children" : [],"index":[]},
                    {"data" : "masters", "children" : [],"index":[]},
                    {"data" : "prof-school", "children" : [],"index":[]},
                    {"data" : "doctorate", "children" : [],"index":[]}]},
                 {"data": "assoc" , "children" : [
                     {"data": "assoc-acdm", "children": [],"index":[]}, 
                     {"data" : "assoc-voc", "children" : [],"index":[]}]},
                 {"data": "non academic", "children":[
                     {"data" : "preschool", "children" : [],"index":[]},
                     {"data" : "1st-4th", "children" : [],"index":[]},
                     {"data" : "5th-6th", "children" : [],"index":[]},
                     {"data" : "7th-8th", "children" : [],"index":[]},
                     {"data" : "9th", "children" : [],"index":[]},
                     {"data" : "10th", "children" : [],"index":[]},
                     {"data" : "11th", "children" : [],"index":[]},
                     {"data" : "12th", "children" : [],"index":[]},
                     {"data" : "hs-grad", "children" : [],"index":[]}]}]}


education_num_map = {"data": "0-50", "children" : [
    {"data": "0-8", "children" : [
        {"data" :[0,2], "children":[],"index":[]}, {"data" : [3,5], "children" : [],"index":[]},{"data" : [6,8], "children" : [],"index":[]}]},
    {"data": "9-16", "children" : [
        {"data" :[9,11], "children":[],"index":[]}, {"data" : [11,13], "children" : [],"index":[]},{"data" : [14,50], "children" : [],"index":[]}]}]}

martial_status_map = {"data" : "*", "children" : [
    {"data" : "married", "children": [
        {"data": "married-civ-spouse", "children":[],"index":[]},{"data": "married-spouse-absent", "children":[],"index":[]},{"data": "married-af-spouse", "children":[],"index":[]}]},
    {"data": "not married", "children":[
        {"data": "never-married", "children":[],"index":[]},{"data": "divorced", "children":[],"index":[]},{"data": "separated", "children":[],"index":[]},{"data": "widowed", "children":[],"index":[]}]}]}

occupation_map = {"data":"*" ,"children":[{"data":"physical" , "children":[{"data":"Craft-repair" , "children":[],"index":[]},
                                                                           {"data":"Handlers-cleaners" , "children":[],"index":[]},
                                                                           {"data": "Machine-op-inspct", "children":[],"index":[]},
                                                                           {"data": "Farming-fishing", "children":[],"index":[]},
                                                                           {"data":"Transport-moving" , "children":[],"index":[]},
                                                                           {"data": "Protective-serv", "children":[],"index":[]},
                                                                           {"data": "Armed-Forces", "children":[],"index":[]}
                                                                            ]}, 
                                           {"data":"non-physical" , "children":[{"data": "Tech-support", "children":[],"index":[]},
                                                                                {"data": "Sales", "children":[],"index":[]},
                                                                                {"data": "Exec-managerial", "children":[],"index":[]},
                                                                                {"data": "Prof-specialty", "children":[],"index":[]},
                                                                                {"data": "Adm-clerical", "children":[],"index":[]}
                                                                              
                                                                            ]},
                                           {"data":"other" , "children":[{"data": "other-service", "children":[],"index":[]},
                                                                                {"data": "Priv-house-serv", "children":[],"index":[]}
                                               ]} 
                                            ]}

relationship_map = {"data" : "*", "children" : [{"data": "family", "children": [{"data":"wife", "children":[],"index":[]},
                                                                                {"data": "husband", "children":[],"index":[]},
                                                                                {"data": "own-child", "children":[],"index":[]}]},
                                                {"data": "not family", "children": [{"data": "not-in-family","children":[],"index":[]},
                                                                                    {"data": "other-relative","children":[],"index":[]},
                                                                                    {"data": "unmarried","children":[],"index":[]}]}]}

race_map = {"data":"*", "children" : [{"data": "white", "children":[],"index":[]}, {"data" : "not white", "children": [{"data": "asian-pac-islander", "children": [],"index":[]},
                                                                                                            {"data": "amer-indian-eskimo", "children": [],"index":[]},
                                                                                                            {"data": "black", "children": [],"index":[]},
                                                                                                            {"data": "other", "children": [],"index":[]}]}]}
sex_map = {"data":"*", "children":[{"data": "male", "children":[],"index":[]},
                                   {"data": "female", "children":[],"index":[]}]}

capital_gain_map = {"tag": "gain","data" :"*", "children":[{"data": [0,0], "children":[],"index":[]},
                                             {"data": [1,1000000], "children":[],"index":[]}]}

capital_loss_map = {"tag": "loss","data" :"*", "children":[{"data": [0,0], "children":[],"index":[]},
                                             {"data": [1,1000000], "children":[],"index":[]}]}

hours_per_week_map = {"data": "0-168", "children" : [
    {"data": "0-83", "children" : [
        {"data" :[0,20], "children":[],"index":[]}, {"data" : [21,41], "children" : [],"index":[]},{"data" : [42,62], "children" : [],"index":[]},{"data" : [63,83], "children" : [],"index":[]}]},
    {"data": "84-168", "children" : [
        {"data" :[84,104], "children":[],"index":[]}, {"data" : [105,125], "children" : [],"index":[]},{"data" : [126,146], "children" : [],"index":[]},{"data" : [147,168], "children" : [],"index":[]}]}]}

native_country_map = {"data": "*", "children": [{"data": "north america", "children":[
                                                                            {"data": "united-states", "children":[],"index":[]},
                                                                            {"data": "puerto-rico", "children":[],"index":[]},
                                                                            {"data": "canada", "children":[],"index":[]},
                                                                            {"data": "cuba", "children":[],"index":[]},
                                                                            {"data": "honduras", "children":[],"index":[]},
                                                                            {"data": "jamaica", "children":[],"index":[]},
                                                                            {"data": "mexico", "children":[],"index":[]},
                                                                            {"data": "dominican-republic", "children":[],"index":[]},
                                                                            {"data": "haiti", "children":[],"index":[]},
                                                                            {"data": "guatemala", "children":[],"index":[]},
                                                                            {"data": "nicaragua", "children":[],"index":[]},
                                                                            {"data": "el-salvador", "children":[],"index":[]}]},
                                                {"data": "south america", "children":[
                                                                            {"data": "columbia", "children":[],"index":[]},
                                                                            {"data": "ecuador", "children":[],"index":[]},
                                                                            {"data": "Trinadad&Tobago", "children":[],"index":[]},
                                                                            {"data": "peru", "children":[],"index":[]}]},
                                                                            
                                                {"data": "asia", "children":[
                                                                            {"data": "india", "children":[],"index":[]},
                                                                            {"data": "japan", "children":[],"index":[]},
                                                                            {"data": "china", "children":[],"index":[]},
                                                                            {"data": "iran", "children":[],"index":[]},
                                                                            {"data": "philippines", "children":[],"index":[]},
                                                                            {"data": "vietnam", "children":[],"index":[]},
                                                                            {"data": "laos", "children":[],"index":[]},
                                                                            {"data": "taiwan", "children":[],"index":[]},
                                                                            {"data": "cambodia", "children":[],"index":[]},
                                                                            {"data": "thailand", "children":[],"index":[]},
                                                                            {"data": "hong", "children":[],"index":[]}]},
                                                {"data": "europe", "children":[
                                                                            {"data": "england", "children":[],"index":[]},
                                                                            {"data": "germany", "children":[],"index":[]},
                                                                            {"data": "greece", "children":[],"index":[]},
                                                                            {"data": "italy", "children":[],"index":[]},
                                                                            {"data": "poland", "children":[],"index":[]},
                                                                            {"data": "portugal", "children":[],"index":[]},
                                                                            {"data": "ireland", "children":[],"index":[]},
                                                                            {"data": "france", "children":[],"index":[]},
                                                                            {"data": "hungary", "children":[],"index":[]},
                                                                            {"data": "scotland", "children":[],"index":[]},
                                                                            {"data": "yugoslavia", "children":[],"index":[]},
                                                                            {"data": "holand-netherlands", "children":[],"index":[]}]},
                                                {"data": "other", "children":[
                                                                            {"data": "south", "children":[],"index":[]},
                                                                            {"data": "outlying-us(guam-USVI-etc)", "children":[],"index":[]}]}]}
income_map = {"data":"*", "children":[{"data": "<=50K", "children":[],"index":[]},
                                   {"data": ">50K", "children":[],"index":[]}]}




attributes_array_int_then_string = [age_map,fnlwgt_map, education_num_map,capital_gain_map,capital_loss_map,hours_per_week_map,
                    workclass_map,education_map, martial_status_map, occupation_map,relationship_map, race_map,
                     sex_map,native_country_map,income_map]


attributes_array_by_order_database = [age_map,workclass_map,fnlwgt_map,education_map,education_num_map,
                                      martial_status_map,occupation_map
                                    ,relationship_map,race_map,sex_map,
                                      capital_gain_map,capital_loss_map,hours_per_week_map,native_country_map,income_map]

'''
attributes_array_by_order_database = [age_map,workclass_map,fnlwgt_map,education_map,education_num_map,
                                      martial_status_map,occupation_map
                                    ,relationship_map,race_map,sex_map,
                                      capital_gain_map,capital_loss_map,hours_per_week_map
                                    ]
attributes_array_int_then_string = [age_map,fnlwgt_map, education_num_map,capital_gain_map,capital_loss_map,hours_per_week_map,
                    workclass_map,education_map, martial_status_map, occupation_map,relationship_map, race_map,
                     sex_map
                     ]
'''                                     
list_age = []
list_fnlwgt = []
list_education_num = []
list_capital_gain = []
list_capital_loss = []
list_hours_per_week = []


list_num = [list_age,
    list_fnlwgt,
    list_education_num,
    list_capital_gain,
    list_capital_loss,
    list_hours_per_week]
'''    
list_num = [list_age,
    list_fnlwgt,
    list_education_num,
    list_capital_gain]
'''   



