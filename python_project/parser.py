import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree = ET.parse("stream.xml")

root = tree.getroot()

for i in range (1,100):
	z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	print z.getchildren()[0].text, "|", z.getchildren()[1].text
