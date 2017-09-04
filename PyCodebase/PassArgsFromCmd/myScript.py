import os
import sys  # reads a list of arguments off the batch file, starting with the script name

scriptName = sys.argv[0] # script name is captured first, always
index = (len(sys.argv)-1) # env argument is last in the list
env = sys.argv[index] 

print("This is the name of the script: %s" % (scriptName))
print("This is the Environment: %s" % (env))