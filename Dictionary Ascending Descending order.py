D={
    'apple':4,
    'banana':7,
    'orange':5,
    'grape':1
}

asc=dict(sorted(D.items(), key=lambda x:x[1]))

desc=dict(sorted(D.items(),key=lambda x:x[1], reverse=True))

print("Ascending Order : ",asc)
print("Descending order : ",desc)

'''
op:-
Ascending Order :  {'grape': 1, 'apple': 4, 'orange': 5, 'banana': 7}
Descending order :  {'banana': 7, 'orange': 5, 'apple': 4, 'grape': 1}
'''
