data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

unique_val=set()
for d in data:
    for value in d.values():
        unique_val.add(value)

print("Unique values : ",unique_val)

'''
op:-
Unique values :  {'S001', 'S005', 'S009', 'S007', 'S002'}
'''
