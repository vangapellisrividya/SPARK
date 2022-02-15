'''	
@Author: Srividya
@Title : using accumulator function in sparkcontext 
'''
from pyspark import SparkContext 
if __name__ == "__main__":

   sc = SparkContext("local", "Accumulator app") 
   # Accumulator variables are used for aggregating the information through associative and commutative operation
   num = sc.accumulator(10) 
   def f(x): 
      global num 
      num+=x 
   rdd = sc.parallelize([20,30,40,50]) 
   rdd.foreach(f) 
   result = num.value 
   print()
   print("----------------------------------------")
   print("Accumulated value is = %i" % (result))
