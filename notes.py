# r = 123_456 + 1_000_000
# print(r)
# s = 'this is a string message'
# i = 10
# f = 33.5
# b = True
# print(s)
# print(type(s))

# testimony = '"I did nothing!" he said. "Not that either! Or the other thing."'
# print(testimony)

# s2 = 'Hello, Python!' # string is a sequence of characters
# print([c for c in s2]) # c 只是 variable

# l=[]
# for c in s2:
#     l.append(c)
# print(l)




# name = "Henny" # strings 字串不可改變
# print(name[0])
# print(name.replace('H', 'P'))
# print(name) # name 還是 Henny


# year = 2020
# event = 'COVID-19'
# # s = f'Results of the {year} {event}' # f' 大括號 結合 py3.6版之後
# s = 'Results of the {} {}'.format(year, event)
# print(s)


# Homework1



school = ([('Chiao', 'NCTU'), ('Yang', 'NYU'), ('CY', 'NCYU'), ('Tsing', 'NTHU')])
# a = {a[0]:a[1] for a in school}
# print(a)

# a={}
# for item in school:
#     a[item[0]]=item[1]
#     print(item[0])
#     print(item[1])
#     print(a)
# print(a)

# school_dict={}
# for item in school:    
#     school_dict[item[0]]=item[1]
# print(school_dict)

# vvv=['Python', 'Java', 'C', 3.8, 8, 1.0, True, ('A', 100, True, 'B')]
# a=[]
# for item in vvv:
#     if type(item)==tuple:
#         a=list(item)
# print(a)


# # 5-1
# nn = [78, 56, 73, 4, 125, 800]
# nn=sorted(nn)
# print(nn)

# # 5-2
# nn = [78, 56, 73, 4, 125, 800]
# bb = [1, 2, 3, 4, 5]
# a = set()
# a = set(nn).intersection(set(bb)) 
# print(a)

# # 5-3
# nn = [78, 56, 73, 4, 125, 800]
# bb = [1, 2, 3, 4, 5]
# a = set()
# a = set(nn).union(set(bb))
# print(a)


# nn = [78, 56, 73, 4, 125, 800]
# bb = [1, 2, 3, 4, 5]

# nn.sort()
# print(nn)
# a = set(nn)|set(bb)
# print(a)





