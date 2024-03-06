def retrue(t):
    return all(t)

tuple_1 = (True, True, False, True)
tuple_2 = (True, True, True, True)
tuple_3 = (False, False, False, False)
print(retrue(tuple_1)) 
print(retrue(tuple_2)) 
print(retrue(tuple_3)) 