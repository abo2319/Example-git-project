# # 2-1
# S=str('homework')
# S=S.replace("o", "p")
# print(S)

# # 2-2
# S=str('homework')
# print(S[1:5])

# # 2-3
# S=str('homework')
# S=S.replace("o", ",")
# print(S)

# 3-1
school = ([('Chiao', 'NCTU'), ('Yang', 'NYU'), ('CY', 'NCYU'), ('Tsing', 'NTHU')])
a={}
for item in school:
    a[item[0]]=item[1]
print(a)

# # 3-2
# school = ([('Chiao', 'NCTU'), ('Yang', 'NYU'), ('CY', 'NCYU'), ('Tsing', 'NTHU')])
# a={}
# for item in school:
#     a[item[0]]=item[1]
# print(a['Chiao'])


# # 3-3
# school = ([('Chiao', 'NCTU'), ('Yang', 'NYU'), ('CY', 'NCYU'), ('Tsing', 'NTHU')])
# a={}
# for item in school:
#     a[item[0]]=item[1]
# del a['Tsing']
# print(a)


# # 4-1
# vvv=['Python', 'Java', 'C', 3.8, 8, 1.0, True, ('A', 100, True, 'B')]
# a=[type(item) for item in vvv]
# print (a)

# # 4-2
# vvv=['Python', 'Java', 'C', 3.8, 8, 1.0, True, ('A', 100, True, 'B')]
# a=[]
# for item in vvv:
#     if type(item)==tuple:
#         a=list(item)
# print(a)


# # 4-3
# vvv=['Python', 'Java', 'C', 3.8, 8, 1.0, True, ('A', 100, True, 'B')]
# a=list(vvv)
# a.extend(['homework'])
# print(a)


# # 5-1
# nn = [78, 56, 73, 4, 125, 800]
# nn=sorted(nn)
# print(nn)


# # 5-2
# nn = [78, 56, 73, 4, 125, 800]
# bb = [1, 2, 3, 4, 5]
# a = set(nn).intersection(set(bb))
# print(a)

# # 5-3
# nn = [78, 56, 73, 4, 125, 800]
# bb = [1, 2, 3, 4, 5]
# a = set(nn).union(set(bb))
# print(a)


# # 6-1
# A = 123
# B ='blockhead'
# C = [1332, 'Freeze ',23]
# a = str(A)+B+C[1]
# print(a)

# # 6-2
# A = 123
# B ='blockhead'
# C = [1332, 'Freeze ',23]
# C = [123 if i==1332 else 'blockhead' if i==23 else i for i in C]
# print(C)