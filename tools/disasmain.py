from elftools.elf.elffile import ELFFile
from capstone import *
import argparse
import os
import sys

#my_parser = argparse.ArgumentParser(description='Enter the name of the file you want to reverse engineer')
#my_parser.add_argument('-d',
 #                    metavar='file',
  #                   type=str,
   #                  help='Select File')
#args = my_parser.parse_args()
#input_d = args.d
#	file = input("Name file: ")
#if not os.path.isdir(input_d):
 	#print('The file specified does not exist')
def func1():
	file = input("Name file: ")
#	try:
 #               print("Analysis Completed")
  #    	except FileNotFoundError:
   #             print("Oops!  That was no valid file.  Try again...")
	with open(file, 'rb') as f:   #change the file name to what you are performing reverse engineering
    		elf = ELFFile(f)
    		code = elf.get_section_by_name('.text')
    		ops = code.data()                 # returns a bytestring with the opcodes
    		addr = code['sh_addr']            # starting address of `.text`
    		md = Cs(CS_ARCH_X86, CS_MODE_64)
    		for i in md.disasm(ops, 0x7aa):    # looping through each opcode
        		print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")

if __name__ == '__main__':
    func1()
