from elftools.elf.elffile import ELFFile
import argparse
import os
import sys

#my_parser = argparse.ArgumentParser(description='Enter the name of the file you')
#my_parser.add_argument('-d',
#                     metavar='file',
#                     type=str,
#                     help='Select File')
#args = my_parser.parse_args()
#input_d = args.d
        #file = input("Name file: ")
#if not os.path.isdir(input_d):
 #       print('The file specified does not exist')
def func2():
#coding: Non-ASCII
	file2 = input("Name file: ")
	try:
        	print("Analysis Completed")
	except FileNotFoundError:
        	print("Oops!  That was no valid number.  Try again...")
	with open(file2, 'rb') as f: #change the file name to what you are performing reverse engineering
    		e = ELFFile(f)
    		for section in e.iter_sections():
	        	print(hex(section['sh_addr']), section.name)
if __name__ == '__main__':
    func2()
