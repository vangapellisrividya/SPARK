'''	
@Author: Srividya
@Title : using cached function in sparkcontext 
'''
from pyspark import SparkContext 
if __name__ == "__main__":
   try:
      sc = SparkContext("local", "Cache app") 
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
      # Persist this RDD with the default storage level (MEMORY_ONLY) ,can also check if the RDD is cached or not.
      words.cache() 
      caching = words.persist().is_cached 
      print()
      print("----------------------------------------")
      print("Words got chached > %s" % (caching))
   except Exception as e:
        print(e)
