# students = [{
#     'name':'serah',
#     'age':30,
#     'country':'Canada',
#     'contact':'587-664-9511'
#     },
#     {
#     'name':'mayowa',
#     'age':10,
#     'country':'Nigeria',
#     'contact':'0703-017-9683'
#     }
#     ]

# for student in students:
#     print (student['name'], student['age'],sep=': ')
# from datetime import datetime,timedelta
# now= datetime.now()
# print("Today's date is: "+ str(now))
# futuredate = now + timedelta(days=25)
# print("Date after 25 days: " + str(futuredate))

import numpy as np
# l1 = [3,1,8,7,9]
# a1 = np.array(l1)
# a1
# a2 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=object)

# [[1,2,3], [4,5,6], [7,8,9]]
# print(a1.shape, a1.ndim)
# print(a2.shape, a2.ndim)
# customers = np.array(['Bob', 'John', 'Miller', 'Bob', 'Sammy', 'Samuel', 'Tony', 'Amanda', 'Bob'])
# # print(customers,customers.ndim, customers.shape)
# data = np.random.randint(1,100, size=(9,4))
# transactions = np.array(data)
# print(transactions)
# slice = transactions[customers=='Bob', :]
# print(slice)

# import statistics
# print(statistics.mean([40,40]))

import sys
print("hello,my name is",sys.argv[1])