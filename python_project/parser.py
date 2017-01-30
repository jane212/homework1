import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree = ET.parse("stream.xml")

root = tree.getroot()

f = open('streamdata.csv','w')

for i in range (1,100):
	z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	content = z.getchildren()[0].text+","+z.getchildren()[1].text
	f.write(content)
	f.write('\n')

f.close()
