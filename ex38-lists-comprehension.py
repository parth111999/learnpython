#more examples to lists comprehension

vec = [-4, -2, 0, 2, 4]
vecDoubled = [x*2 for x in vec]
print(">>> vec", vec)
print(">>> vecDoubled", vecDoubled)

#filter negative numbers
vecFiltered = [x for x in vec if x >= 0]
print(">>> vecFiltered", vecFiltered)

#apply functions to all the elements
vecFunctioned = [abs(x) for x in vec]
print(">>> vecFunctioned",vecFunctioned)

#apply a method to each element
freshFruit = ['     banana',"   loganberry","passion fruit","apples   ","oranges"]

print(">>>> freshFruit", freshFruit)

freshFruitCleaned = [fruit.strip() for fruit in freshFruit]
print(">>> freshFruitCleaned", freshFruitCleaned)

#create a list of 2-tuple like (number, square)
squaresTuple = [(x,x**2) for x in range(500)]
print("squaresTuple", squaresTuple)

#how to flatten a list:
    #Traditional method:

myTwoDList = [[1,2,3],[4,5,6],[7,8,9]]
myFlatList = []
for elem in myTwoDList:
    for num in elem:
        myFlatList.append(num)

print(myFlatList)

    #with list comprehension

myFlatList2 = [num for elem in myTwoDList for num in elem]
print(myFlatList2)
