#Bloom filter
from pybloom import BloomFilter
from random import randrange
import numpy.random as nprnd

#### How does it work for a range of numbers?
f = BloomFilter(capacity=10000, error_rate=0.001)
[f.add(x) for x in range(10000)]
sum = 0
for i in range(10000):
    #print(i in f)
    sum = sum + (i in f)
print("Accuracy for range of numbers",(sum/10000)*100)
#### How does it work for random numbers?
f = BloomFilter(capacity=10000, error_rate=0.001)
randomNumbers = nprnd.randint(10000000, size=10000)
[f.add(x) for x in randomNumbers]
sum = 0
for i in range(10000):
    #print(i in f)
    sum = sum + (i in f)
print("Accuracy for random numbers",(sum/10000)*100)


#Locally sensityve hash function
from lshash import LSHash
lsh = LSHash(6, 8)
lsh.index([1,2,3,4,5,6,7,8])
lsh.query([6.8], num_results=None, distance_func="euclidean")
