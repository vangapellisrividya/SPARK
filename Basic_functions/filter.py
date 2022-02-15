'''	
@Author: Srividya
@Title : using cached filter in sparkcontext 
'''
from pyspark import SparkContext
if __name__ == "__main__":
   try:
      sc = SparkContext("local", "Filter app")
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
      # A new RDD is returned containing the elements, which satisfies the function inside the filter
      words_filter = words.filter(lambda x: 'spark' in x)
      filtered = words_filter.collect()
      print()
      print("----------------------------------------")
      print("Fitered RDD -> %s" % (filtered))
   except Exception as e:
            print(e)
