import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

url_str = "http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorData?MSG_TrafficDetectorDataRequest=string%20HTTP/1.1"
request = urllib2.Request(url_str, headers = {"Accept":"text/xml"})
contents = urllib2.urlopen(request).read()
root = ET.fromstring(contents)
with open("streamdata_all.csv","w") as f:
        for child in root[2][0][3]:
                content = child[0].text+","+child[1].text+"\n"
                f.write(content)
