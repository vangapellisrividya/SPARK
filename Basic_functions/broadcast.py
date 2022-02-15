'''	
@Author: Srividya
@Title : using broadcast function in sparkcontext 
'''
from pyspark import SparkContext 

if __name__ == "__main__":
    try:

        sc = SparkContext("local", "Broadcast app") 
        # Broadcast variables are used to save the copy of data across all nodes. 
        # This variable is cached on all the machines and not sent on machines with tasks.
        words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"]) 
        data = words_new.value 
        print()
        print("----------------------------------------")
        print("Stored data -> %s" % (data) )
        elem = words_new.value[2] 
        print ("Printing a particular element in RDD -> %s" % (elem))
    except Exception as e:
        print(e)
