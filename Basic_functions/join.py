'''	
@Author: Srividya
@Title : using join function in sparkcontext 
'''
from pyspark import SparkContext
if __name__ == "__main__":
    try:
        sc = SparkContext("local", "Join app")
        x = sc.parallelize([("spark", 1), ("hadoop", 4)])
        y = sc.parallelize([("spark", 2), ("hadoop", 5)])
        # It returns RDD with a pair of elements with the matching keys and all the values for that particular key.
        joined = x.join(y)
        final = joined.collect()
        print()
        print("----------------------------------------")
        print( "Join RDD -> %s" % (final))
    except Exception as e:
            print(e)
