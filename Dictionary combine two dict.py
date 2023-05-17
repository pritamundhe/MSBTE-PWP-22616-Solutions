d1={
    'a':100,
    'b':200,
    'c':300
}
d2={
    'a':300,
    'b':200,
    'c':400
}
d3=d1.copy()
for i in d2:
    if i in d1:
        d3[i]=d3[i]+d2[i]
    else:
        d3[i]=d2[i]
        
print(d3)

    '''
    op:-
    
    {'a': 400, 'b': 400, 'c': 700}
    '''
