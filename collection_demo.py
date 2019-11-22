"""
Dictionary is defined by '{}'
"""
dictionary_1 = {}
dictionary_1['first'] = 'Clay'
dictionary_1['last'] = 'Hsiao'

dictionary_2 = {'first':'Sharon'}
dictionary_2['last'] = 'Chang'


"""
List is defined by '[]'
"""
list_1 = [dictionary_1, dictionary_2]
list_1.append({'first':'Ruth', 'last':'Hsiao'})

"""
List can store objects with 'Different Type'
"""
list_1.append(100)

"""
List can insterted new object at specific index
"""
list_1.insert(1, "String Value is fine")
print(list_1)



"""
List can retrieved by ranges
"""
sublist = list_1[0:2]

print(sublist)