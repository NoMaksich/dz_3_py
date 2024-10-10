elements = [1,2,3,3,3,3,4,4,4,5,5,5]

duplicates = []

for i in elements:
    if elements.count(i) > 1 and i  not in duplicates:
        duplicates.append(i)
        
print(duplicates)