import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree = ET.parse("stream.xml")

root = tree.getroot()

z = root[2][0][3].getchildren()

length = len(z)

with open("streamdata.csv","w") as f:
	for i in range (0,length):
		x = root[2][0][3].getchildren()[i]
		content = x[0].text+","+x[1].text+"\n"
		f.write(content)
