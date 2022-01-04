# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=dict(d1)
# d3.update(d2)
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i==x:
#           d3[i]==j+y
# print(d3)

# Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
#  {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in range(len(Data)):
#     for j in Data[i]:
#         if Data[i][j] not in b:
#             b.append(Data[i][j])
# print(b)

Count={}
word='w3resource'
# for i in word:
#     if i not in Count:
#         Count[i]=1
#     else:
#         Count[i]=Count[i]+1
# print(Count)


# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Count=0
# for i in dict.values():
#     for j in range(len(i)):
#         Count+=1
# print(Count)

d={'1':['a','b'], '2':['c','d']}
for x in d['1']:
    for y in d['2']:
        print(x + y)
   
 
 
