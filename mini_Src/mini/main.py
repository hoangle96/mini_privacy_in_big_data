

from _functools import reduce
#from taxonomies import attributes_array_by_order_database
#from taxonomies import attributes_array_int_then_string
#from taxonomies import list_num
from k_anon import k_anon


from algorithm_6_7 import algorithm_6
from algorithm_4 import algorithm_4
from algorithm_2 import algorithm_2
from make_int_taxonomies import make_int_lists , make_new_int_maps
from taxonomies import taxonomies_list_and_list_nums

from tkinter import *
from tkinter import messagebox
import time

'''
print("Enter k")
k = num(input())
'''
def number_of_lines_in_db(database_path,attributes_array_by_order_database):
    #print(database_path)
    #print(attributes_array_by_order_database)
    with open(database_path, 'r') as f: 
        i = 1
        #print("algorithm_6 i : ","00")
        for line in f:
            #print("algorithm_6 i : ",i)
            line_arr = re.split(", |\\n",line)
            if ("?" in line_arr)or (len(line_arr)!=1+len(attributes_array_by_order_database) ):
                continue 
            
            #print(i)       
            i = i + 1
    f.close()
    return i-1

 

def algorithm_5(database_path, k, attributes_array_by_order_database,attributes_array_int_then_string,list_num,num_lines):
    (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string,list_num,num_lines)
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
#lists_num = make_int_lists(list_num,"./adult.data",attributes_array_by_order_database,attributes_array_int_then_string)
#make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )

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

#algorithm_5("./adult.data", 6, attributes_array_by_order_database,attributes_array_int_then_string,list_num)

    
def commandOfRun(k,num_of_first_lines, databases ,database_index,workLabel):
    database_path = databases[database_index][2]
    try:
        int(k)
    except ValueError:
        messagebox.showerror("error", "error - k is not an integer number")
        return
    try:
        int(num_of_first_lines)
    except ValueError:
        messagebox.showerror("error", "error - first number of lines is not an integer number")
        return
    
    num_of_lines_in_db = number_of_lines_in_db(database_path,taxonomies_list_and_list_nums[database_index][0])
    if (num_of_lines_in_db < int(k)):
        messagebox.showerror("error", "error - illegal k")
        return
    if(num_of_lines_in_db < int(num_of_first_lines)):
        messagebox.showerror("error", """error - database is smaller 
        than number of first lines""")
        return
    if(int(num_of_first_lines) < int(k)):
        messagebox.showerror("error", """error - number of first lines is smaller 
        than k""")
        return
    print("command executed")
    workLabel.configure(text="""
    

    WORKING ON DB NOW...""")
    workLabel.update()
    
    #time.sleep(5)
    lists_num = make_int_lists(taxonomies_list_and_list_nums[database_index][2],
                               database_path,
                               taxonomies_list_and_list_nums[database_index][0],
                               taxonomies_list_and_list_nums[database_index][1],
                               int(num_of_first_lines))
    make_new_int_maps(lists_num , 
                      taxonomies_list_and_list_nums[database_index][0], 
                      taxonomies_list_and_list_nums[database_index][1] )
    
    algorithm_5(database_path, 
                int(k), 
                taxonomies_list_and_list_nums[database_index][0],
                taxonomies_list_and_list_nums[database_index][1],
                taxonomies_list_and_list_nums[database_index][2],
                int(num_of_first_lines))
    
    workLabel.configure(text="""
    """)
    workLabel.update()
    messagebox.showinfo("completed", """k anonymization completed -
     it is in result_dbs folder""")
    return

def comandOfRadio(database_index,database_path,radioLabel):
    #print("database_index : " , database_index)
    db_size = number_of_lines_in_db(database_path,taxonomies_list_and_list_nums[database_index][0])
    txt = """
    db size : """+str(db_size)+"""
    """
    radioLabel.configure(text=txt)
    radioLabel.update()
    return 

root = Tk()

root.geometry("430x250")
Label(root, text="k-anonimity mini project").grid(row=0, column=0)

f1 = Frame(root, width= 40,height=5)
f1.grid(row=1, column=0, sticky="nsew")



f11 = Frame(f1, width=20,height=5)
f11.grid(row=0, column=0, sticky="nsew")

v = IntVar()
v.set(0)
Label(f11, 
        text="""Choose a 
Database:""",
        justify = LEFT,
        padx = 20).pack()
databases = [
    ("adult db",1 , "./dbs/adult.data"),
    ("article db(clothing)", 2 , "./dbs/test_db_clothing.txt"),
    ("tassa db(multiple)",3,"./dbs/test_db_multiple.txt"),
    ("tassa db variation(multiple_2)",4,"./dbs/test_db_multiple_2.txt"),
    ("adult 4x2 db(cover)",5,"./dbs/test_db_cover_1")
]




f12 = Frame(f1, width=20,height=5)
f12.grid(row=0, column=1, sticky="nsew")
l1 = Label(f12 ,text="""

number of 
first lines:""" )
l1.grid(row=0, column=0, sticky="nsew")
e1 = Entry(f12)
e1.grid(row=1, column=0)

l2 = Label(f12 ,text="""

""" )
l2.grid(row=2, column=0, sticky="nsew")
'''in the middle because it needs l2 reference'''
val = 0
for (name,valu,path)  in databases:
    Radiobutton(f11, 
                  text=name,
                  padx = 20, 
                  variable=v, 
                  command=lambda:comandOfRadio(v.get(),databases[v.get()][2],l2),
                  value=val).pack(anchor=W)
    val = val + 1
comandOfRadio(v.get(),databases[v.get()][2],l2)
workLabel = Label(f11 ,text="""
""")
workLabel.pack(anchor=S)



l3 = Label(f12 ,text="""k:""" )
l3.grid(row=3, column=0, sticky="nsew")
e3 = Entry(f12)
e3.grid(row=4, column=0)

f2 = Frame(root, width= 40,height=1)
f2.grid(row=2, column=0, sticky="nsew")
b = Button(f2, text="run k-anon",command=lambda:commandOfRun(e3.get(), e1.get(), databases, v.get(), workLabel))
b.pack()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=2) # not needed, this is the default behavior
root.rowconfigure(1, weight=5)
root.rowconfigure(2, weight=1)

f1.columnconfigure(0, weight=1)
#f1.rowconfigure(0, weight=0) # not needed, this is the default behavior
f1.rowconfigure(0, weight=5)

#f2.columnconfigure(0, weight=1)
#f1.rowconfigure(0, weight=0) # not needed, this is the default behavior
#f2.rowconfigure(0, weight=2)


root.mainloop()


