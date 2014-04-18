#!/usr/bin/python
import os, threading
i=30
for j in range(i):
		cmd = "curl http://localhost:9981/test"+str(j+1)+" -X PUT ;ab -n 1 -c 1 -u ./output10M http://localhost:9981/test"+str(j+1)+"/output10M > ./result/SME_test_"+str(i)+"_"+str(j+1)
		print cmd
		threading.Thread(target=os.system, args=(cmd,)).start()
