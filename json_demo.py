"""
    You can create a JSON object from a Dictionary object 
"""
def create_JSON(dict):
    return json.dumps(dict)


person_dict = {'first': 'Clay', 'last':'Hsiao'}
person_dict['country'] = 'Taiwan'
# List in Json
language_list = ['Taiwanese', 'English', 'Chinese (Mandarine)']
person_dict['languages'] = language_list

person_json = create_JSON(person_dict)
print(person_json)
print()

# nested Json
staff_dict = {}
staff_dict['Developer'] = person_dict
staff_json = create_JSON(staff_dict)
print(staff_json)