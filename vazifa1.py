import math


def add_function(list1, list2):
    # Ikkala listning elementlarini qo'shish
    sum1 = sum(list1)
    sum2 = sum(list2)
    list3 = []
    # Agar birinchi listning yig'indisi kichik bo'lsa
    if sum1 < sum2:
        return sum1 +sum2
    elif 100<(sum2+sum1)<200 :
        return (sum2 +sum1)-100
    # for i in range(min(len(list1), len(list2))):
    #     list3.append(list1[i]+list2[i])
    # return list3

# Misollar
print(add_function([111], [222]))  # 333
print(add_function([111], [22]))   # 33
