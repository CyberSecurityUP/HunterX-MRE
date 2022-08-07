import os
import sys
import argparse
from sys import path
sys.path.insert(1, 'tools/')
import disasmain
import sections
import recolocations
import md5
import pes

print("Created by Joas")
print("")
print("python3 main.py -h")

my_parser = argparse.ArgumentParser(description='Enter the name of the file')
my_parser.add_argument('--disasmain', '-d',
                     type=str)
my_parser.add_argument('--sections', '-s',
                     type=str)
my_parser.add_argument('--recolocations', '-r',
		     type=str)
my_parser.add_argument('--md5',
		     type=str)
my_parser.add_argument('--pes',
                     type=str)
args = my_parser.parse_args()
       

if args.disasmain:
	disasmain.func1()
elif args.sections:
	sections.func2()
elif args.recolocations:
	recolocations.func3()
elif args.md5:
	md5.func4()
elif args.pes:
	pes.func5()
