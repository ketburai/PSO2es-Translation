#!/usr/bin/python
# coding=utf8
import re
import os
import pprint
import simplejson
import sys

counterr = 0
bufout = "000.0%:0FILE"
os.chdir(os.getcwd() + "/json")
invalid_json_files = []
json_files = [f for f in os.listdir('.') if re.match(r'.*\.txt', f)]
for files in json_files:
    with open(files) as json_file:
        try:
            countin = 0
            countout = 0
            djson = simplejson.load(json_file)
            for rmid in djson:
                countin += 1
		#pprint.pprint(rmid)
                if (("en_text" in rmid) and (rmid["en_text"] != "")):
                       countout += 1
            #print ("%s/%s" % (countin, countout))
            if (countin):
                countper = "{:06.1%}".format(float(countout)/float(countin))
                bufout += '\n{0}:{1}'.format(countper,files)
            else:
                bufout += '\n{0}:{1}'.format("0NULL ",files)
        except ValueError as e:
            print("%s: %s") % (files, e)
            invalid_json_files.append(files)

counterr += len(invalid_json_files)
if counterr != 0:
    sys.exit("=============\nJSON files with issues: %d" % count)
else:
    print bufout
