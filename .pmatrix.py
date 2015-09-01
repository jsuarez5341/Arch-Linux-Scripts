import numpy as np
import time
import sys

if __name__=="__main__":
    nRows=int(sys.argv[1])
    tRow=(np.random.rand(nRows)>0.5).astype(int).astype(str)
    print(tRow)
    thresh=0.7
    nulThresh=0.1
    boldOne="\033[1m1\033[0m"
    while 1:   
        for i in range(nRows):
            if tRow[i]=='0' and np.random.rand()>thresh:
                tRow[i]=' '
            elif tRow[i]=='1' and np.random.rand()>thresh:
                    tRow[i]=' '
            elif tRow[i]==boldOne:
                tRow[i]='1'
            elif tRow[i]==" " and np.random.rand()<nulThresh:
                if np.random.rand()>0.5:
                    tRow[i]='0'
                else:
                    tRow[i]=boldOne
        [print(str(itm)+"  ", end="") for itm in tRow]
        print()
        time.sleep(0.04);
