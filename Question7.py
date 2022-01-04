dict=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
b=[]
for i in range(len(dict)):
  for j in dict[i]:
    if  dict[i][j] not in b:
      b.append(dict[i][j])
print(b)




# dict = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
# list =[] # create empty list
# for val in dict.values(): 
#   if val in list: 
#     continue 
#   else:
#     list.append(val)

# print (list)