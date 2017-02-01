import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree = ET.parse("stream.xml")

root = tree.getroot()

z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()

length = len(z)

f = open('streamdata.csv','w')

for i in range (1,length):
	x = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	content = x.getchildren()[0].text+","+x.getchildren()[1].text+"\n"
	f.write(content)


f.close()
