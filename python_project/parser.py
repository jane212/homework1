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

for i in range (0,length):
	x = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	print x.getchildren()[0].text, "|", x.getchildren()[1].text

