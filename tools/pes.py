import pefile

def func5():
	file = input("Select File: ")
	pe = pefile.PE(file)
	print("e_magic : " + hex(pe.DOS_HEADER.e_magic)) # Prints the e_magic field of the DOS_HEADER
	print("e_lfnew : " + hex(pe.DOS_HEADER.e_lfanew)) # Prints the e_lfnew field of the DOS_HEADER
if __name__ == '__main__':
	func5()
