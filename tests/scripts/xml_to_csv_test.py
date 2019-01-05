# Written By: Jodi Gunawan
# Date: Jan 5th, 2019
# Description:  This script tests csv file produced by xml_to_csv.py works properly

import os
import pytest

def xml_to_csv_test():
	# Run xml_to_csv script	
	os.system("python ../../scripts/data_formatting/xml_to_csv.py --train_or_test test")
	
	# Check csv file produced
	result = open("../../data/test_labels.csv").read()

	assert 'filename,width,height,class,xmin,ymin,xmax,ymax' in result
	assert 'gate_0000.jpg,1920,1080,Gate,1363,298,1916,742' in result

xml_to_csv_test()