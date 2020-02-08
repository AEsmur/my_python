names = ['John', 'Paul', 'George', 'Ringo']
filtered = list(filter((lambda x: x == 'John' or x == 'Paul'), names))
print(filtered)
