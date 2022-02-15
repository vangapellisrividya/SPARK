'''	
@Author: Srividya
@Title : using count function in sparkcontext 
'''
from pyspark import SparkContext
if __name__ == "__main__":
   try:
      sc = SparkContext("local", "count app")
      words = sc.parallelize (
         ["scala", 
         "java", 
         "hadoop", 
         "spark", 
         "akka",
         "spark vs hadoop", 
         "pyspark",
         "pyspark and spark"]
      )
      #Number of elements in the RDD is returned.
      counts = words.count()
      print()
      print("----------------------------------------")
      print("Number of elements in RDD = %i" % (counts))
   except Exception as e:
         print(e)
