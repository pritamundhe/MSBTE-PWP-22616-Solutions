import heapq

data = {
    'a':10,
    'b':30,
    'c':98,
    'd':5,
    'e':70
    }

highest_three= heapq.nlargest(3, data.values())

print("Highest 3 values are : ",highest_three)

'''
op:-
Highest 3 values are :  [98, 70, 30]
'''
