'''	
@Author: Aishwarya
@Date: 2022-02-2
@Title : using map function in sparkcontext 
'''
#########################################################################################
from pyspark import SparkContext
if __name__ == "__main__":
   try:
      sc = SparkContext("local", "Map app")
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
      # A new RDD is returned by applying a function to each element in the RDD
      # a key value pair and map every string with a value of 1
      words_map = words.map(lambda x: (x, 1))
      mapping = words_map.collect()
      print()
      print("----------------------------------------")
      print("Key value pair -> %s" % (mapping))
   except Exception as e:
            print(e)