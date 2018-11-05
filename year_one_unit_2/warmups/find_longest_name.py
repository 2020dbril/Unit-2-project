my_people =['ben', 'lauren', 'estelle', 'shiba']
longest=''
for x in my_people:
    if len(x) > len(longest):
        longest = x
    
print(longest)
