#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Tool to dump in IANA RR DNS parameters in JSON or Python dict format 
#
# Software is free software released under the "Modified BSD license"
#
# Copyright (c) 2013 Alexandre Dulaunoy - a@foo.be

import argparse
import csv
import json
import codecs
import urllib.request

#IANA format (CSV) is TYPE,Value,Meaning,Reference,Template,Registration Date
ianarrurl = "http://www.iana.org/assignments/dns-parameters/dns-parameters-4.csv"

argParser = argparse.ArgumentParser(description='Dump IANA DNS parameters in various formats')
argParser.add_argument('-d', action='store_true', help='Python dict')
argParser.add_argument('-j', action='store_true', default=True, help='JSON output (default format)')
argParser.add_argument('-i', action='store_false', default=True, help='Disable integer value RR check')
argParser.add_argument('-v', action='store_true', help='Verbose output')
args = argParser.parse_args()


rrset=[row for row in csv.DictReader(codecs.iterdecode(urllib.request.urlopen(ianarrurl),'utf-8'),fieldnames = ( "Type","Value","Meaning","Reference","Template","Registration Date" ))]

if args.i:
	rri = []
	for rr in rrset[1:]:
		if rr['Value'].isdigit():
			rri.append(rr)
	rrset=rri
else:
	rrset=rrset[1:]

if args.d:
	print (rrset)

if args.j:
	jsonout = json.dumps( rrset )
	print (jsonout)
