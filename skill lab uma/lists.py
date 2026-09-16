# list comprehension

# list1=[x for x in range(10)]
# print(list1)

# list2=[x**2 for x in range(5)]
# print(list2)

# list3=[x for x in range(21) if x%2==0]
# print(list3)

# list4=[x for x in range(51) if x%2==0 and x%5==0]
# print(list4)

scores=[25,41,29,18,11,38,29,33,50,48,47,44,36,25,22]
toppers=[x for x in scores if x>=45]
print(toppers)
low_achievers=[x for x in scores if x<=30]
print(low_achievers)