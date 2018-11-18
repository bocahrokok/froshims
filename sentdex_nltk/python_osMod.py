import os

curDir = os.getcwd()
print(curDir)

os.mkdir('NewDirTest')

import time
time.sleep(2)
os.rename('newDirTest','New Dir terbaru asu!')


