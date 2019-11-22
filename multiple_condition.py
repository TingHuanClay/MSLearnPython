province = 'Onatrio'
tax = 0
if province == 'Alberta':
    tax = 0.5
elif province in ('Nunavut', 'Onatrio'):
    tax = 0.6
elif province == 'CC' or province == 'DD':
    tax = 0.7
    tax = 0.6
elif province == 'EE' \
     or province == 'FF':
    tax = 0.8

print(f'tax:{tax}')