import sys
import os
import time
import difflib

file1 = open("streamdata.csv","r")
file2 = open("streamdata3.csv","r")
diff = difflib.context_diff(file1.readlines(), file2.readlines())
#delta = ''.join(x[2:] for x in diff if x.startswith('- '))
delta = ''.join(diff)
print delta
