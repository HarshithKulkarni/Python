import subprocess as s
import os
class server:

    def __init__(self):

        #s.call("google-chrome localhost",shell=True
        pass
    
    def Access(self,param):

        if(param == "finance"):
            s.call("google-chrome localhost/Finance/index.html",shell=True)
        elif(param == "data"):
            s.call("google-chrome localhost/Data/invoice.html",shell=True)
        elif(param == "market"):
            s.call("google-chrome localhost/Marketing/index.html",shell=True)
    
