'''	
@Author: Srividya
@Title : using reduce function in sparkcontext 
'''
from pyspark import SparkContext
from operator import add
if __name__ == "__main__":
    try:
        sc = SparkContext("local", "Reduce app")
        nums = sc.parallelize([1, 2, 3, 4, 5])
        # After performing the specified commutative and associative binary operation, the element in the RDD is returned. 
        # here importing add package from the operator and applying it on ‘num’ to carry out a simple addition operation.
        adding = nums.reduce(add)
        print()
        print("----------------------------------------")
        print("Adding all the elements -> %i" % (adding))
    except Exception as e:
            print(e)
