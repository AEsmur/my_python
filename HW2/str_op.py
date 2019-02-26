s = 'У лукоморья 123 дуб зелёный 456'
'''№1'''
print(s.index('я'))
'''№2'''
print(s.count('у'))
'''№3'''
if s.isalpha() == False:
    print(s.upper())
'''№4'''
if len(s) > 4:
    print(s.lower())
'''№5'''
print('О' + s[1:])
