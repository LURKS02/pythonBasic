
# dictionary =========================
# dic = {인덱스 : 값}
dict = {"idx1" : 1, "idx2" : 2, "idx3" : 3}
dict2 = {"idx4" : 4, "idx5" : 5}
keys = dict.keys()
print(dict)
print(keys)

dictlist = []
dictlist.append(dict)
dictlist.append(dict2)
print(dictlist)

dictlist[1]["idx6"] = 6
print(dictlist)