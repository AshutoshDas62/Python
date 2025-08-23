"""  LIST  """
"""Lists are used to store multiple items in a single variable.A list can store strings, integers and boolean values in single list"""

list=["1", "Ashu",23,True,254,"rollno", 23, 456345]
# print(f" {type(list[2])} item is : {list[2]}")

"""If you add new items to a list, the new items will be placed at the end of the list"""
"""The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. and list allowed doublicate values"""

# PRACTICE:

# 1) indexing:
# print("index no 2 ",list[2])

# 2) slicing
# print("print index 1 to 4", list[1:5])  # list[1:5] index 1 to 5 -1(4 index)

#3) count():- the counst method count the repeation/dublication of value.
# print("no of 23 value is:", list.count(23)) # result:- no of 23 value is: 2
 
#4) index() :- shawing the indexing of given value in index parameter
# print("indexing of Ashu in list : ",list.index("Ashu")) #result :- indexing of Ashu in list : 1
# print("indexing of 23",list.index(23))  # result:-indexing of 23 : 2, List alway give first accurrence value, but how to access 23 of indexing 6. 

# # dublicate valude indexing
# print("indexing 6 of 23",list.index(23,4)) #resut:- indexing 6 of 23 6, 4 written for star searching from index 4 so for compiler 23 of 6 indexing is first occurrence

#5) insert() :- insert method helps to insert vlue in any indexing. but append method used to add values from the end of list.
# list.insert(3,"age") # 3 is index where i want to insert new item.
# list.insert(5) # TypeError: insert expected 2 arguments, got 1
# print("after insert list ", list) #result:- after inser list  ['1', 'Ashu', 23, 'age', True, 254, 'rollno', 23, 456345] 

#6) pop () :- pop method pop value by given index value in pop parameter and also pop value without parameter from the End of list
# print("before POP list: ",list)  #before POP list:  ['1', 'Ashu', 23, True, 254, 'rollno', 23, 456345]
# list.pop(3) #given index 3 
# print("List after POP: ",list)   # List after POP:  ['1', 'Ashu', 23, 254, 'rollno', 23, 456345] 
# list.pop() # pop value from end of list,
# print("POP item without paramerter : ",list) #result:-POP item without paramerter :  ['1', 'Ashu', 23, 254, 'rollno', 23]

#7) exetend () :- nothing but marging two list togather
# list2=["2nd",2] 
# list3=[23,45]
# list.extend(list2 and list3) #list after extend     ['1', 'Ashu', 23, True, 254, 'rollno', 23, 456345, 23, 45] Not successive becouse only marge list3 except list2
# print("list after extend",list) # list after extend ['1', 'Ashu', 23, True, 254, 'rollno', 23, 456345, '2nd', 2]
# # NOTE: if we write like this list.extend(list2,list3) restult:- TypeError: list.extend() takes exactly one argument (2 given)

#8) copy():- simply copy list
# 1st method
# list2=list
# print("Coppied list is list2 : ",list2) 
# 2nd method
# list2=list.copy()
# print("Coppied list is list2 : ",list2) 
#3rd method
list2=list[:] # here colon means default length of list [0 : n-1]==[:]
print("Coppied list is list2 : ",list2) 












