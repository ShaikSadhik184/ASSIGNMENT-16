tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1[1])
list1[0] = 222
tuple2 = tuple([tuple1[0], tuple(list1), tuple1[2], tuple1[3]])

print(tuple2)
