import idautils
def main():
	
	KEYWORDS   = 'error'
	cursorList = []
	real_names = []
	addresses  = []
	names      = idautils.Names()

	print "========= Welcome to Finder ========="
	print "KEYWORDS = " + KEYWORDS

	# Populate the two above lists with their respective data from the list of tuples returned by idautils.Names()
	for n in names:
		real_names.append(n[1]) # real_names[30] ------> addresses[30]
		addresses.append(n[0])
		
	# search for a 'start' name in the names list and if it is there, set cursor to the address of beginning of it
	for rn in real_names:
		if rn.lower().find(KEYWORDS.lower()) != -1:
			cursorList.append(addresses[int(real_names.index(rn))])
			print "FOUND: " + rn

	temp = -1

	for cursor in cursorList:
		myFunc = idaapi.get_func(cursor)
		if myFunc:
			print "--------------------------------------------------------------------------------------------------------------------"
			print "Function Name = " + idaapi.get_func_name(cursor)
			print "--------------------------------------------------------------------------------------------------------------------"
			while cursor < myFunc.endEA:
				print "%s" % idc.GetDisasm(cursor)
				if idc.GetMnem(cursor) == 'call' and idc.GetMnem(idc.prev_head(cursor)) == 'jmp':
					idc.MakeComm(cursor, 'This is a call after a jump!')
				cursor = idc.next_head(cursor,myFunc.endEA) # MaxEA()
		else:
			print "Can't find index :	"
			print cursor

	print "========= Finder Ends ========="

if __name__ == "__main__":
    main()