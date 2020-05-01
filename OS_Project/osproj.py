import docx2txt
import urllib.request

def best_fit(process_memory,memory_space):
	process_memory1 = [int(x) for x in process_memory]
	memory_space1 = [int(x) for x in memory_space]
	remaining_memory1=[0,0,0,0,0]
	i=0
	print("PROCESS BEST FIT !!!! :")
	while True:
		if i < len(process_memory1):
			j=0
			for pro in memory_space1:
				if i<len(process_memory1) and j<len(memory_space1) and process_memory1[i] != -1 and process_memory1[i]<pro and process_memory1[i]+100 > pro:
					if i == len(process_memory1)-1 and process_memory1[i]<max(memory_space1):
						remaining_memory1[4]=max(memory_space1)-process_memory1[i]
						process_memory1[i]=-1
						print("\tprocess P{} ----> memory B{}".format(i+1,memory_space1.index(max(memory_space1))+1))
						i += 1
						break
					remaining_memory1[j]=pro-process_memory1[i]
					j += 1
					process_memory1[i]=-1
					print("\tprocess P{} ----> memory B{}".format(i+1,memory_space1.index(pro)+1))
					i += 1
				else:
					j += 1
				
		else:
			break
	infrag = sum(remaining_memory1)				
	print("INTERNAL FRAGMENTATION : {} ".format(infrag))

def first_fit(process_memory,memory_space):
	process_memory2 = [int(x) for x in process_memory]
	memory_space2 = [int(x) for x in memory_space]
	remaining_memory2,mem=[0,0,0,0,0],[0,0,0,0,0]
	i,extfrag=0,0
	print("\nPROCESS FIRST FIT !!!! :")
	for i in range(len(process_memory2)):
		j=0
		for memory in memory_space2:
			if i < len(process_memory2) and j<len(memory_space2) and process_memory2[i] < memory and process_memory2[i] != -1 and mem[j]!=-1:
				#print("{}---->{}".format(process_memory2[i],memory))
				remaining_memory2[j] = memory - process_memory2[i]
				process_memory2[i],mem[j] = -1,-1
				print("\tprocess P{} ----> memory B{}".format(i+1,memory_space2.index(memory)+1))
			else:
				j += 1
	for i in process_memory2:
		if i != -1:
			print("\tprocess P{} is not allocated \n".format(process_memory2.index(i)+1))
	for i in range(len(memory_space2)):
		if remaining_memory2[i] == 0:
			extfrag += memory_space2[i]						
	infrag = sum(remaining_memory2)				
	print("INTERNAL FRAGMENTATION : {} ".format(infrag))
	print("EXTERNAL FRAGMENTATION : {} ".format(extfrag))					

def next_fit(process_memory,memory_space):
	process_memory3 = [int(x) for x in process_memory]
	memory_space3 = [int(x) for x in memory_space]
	remaining_memory3=[0,0,0,0,0]
	i,j,extfrag=0,0,0
	print("\nPROCESS NEXT FIT !!!! :")
	for memory in memory_space3:
		if i < len(process_memory3) and j<len(memory_space3) and process_memory3[i] < memory and process_memory3[i] != -1:
			#print("{}---->{}".format(process_memory3[i],memory))
			remaining_memory3[j] = memory - process_memory3[i]
			process_memory3[i] = -1
			print("\tprocess P{} ----> memory B{}".format(i+1,memory_space3.index(memory)+1))
			i += 1
			j += 1
		else:
			j += 1
	for i in process_memory3:
		if i != -1:
			print("\tprocess P{} is not allocated \n".format(process_memory3.index(i)+1))
	for i in range(len(memory_space3)):
		if remaining_memory3[i] == 0:
			extfrag += memory_space3[i]				
	infrag = sum(remaining_memory3)				
	print("INTERNAL FRAGMENTATION : {} ".format(infrag))					
	print("EXTERNAL FRAGMENTATION : {} ".format(extfrag))
	
def worst_fit(process_memory,memory_space):
	process_memory4 = [int(x) for x in process_memory]
	memory_space4 = [int(x) for x in memory_space]
	ms = [int(x) for x in memory_space]
	remaining_memory4,mem=[0,0,0,0,0],[0,0,0,0,0]
	i,extfrag=0,0
	print("\nPROCESS WORST FIT !!!! :")
	for i in range(len(process_memory4)):
		for memory in memory_space4:
			if i < len(process_memory4) and memory == max(ms) and process_memory4[i] != -1 and process_memory4[i] < memory:
				#print("{}---->{}".format(process_memory4[i],memory))
				remaining_memory4[ms.index(max(ms))] = memory - process_memory4[i]
				process_memory4[i] = -1
				ms[ms.index(max(ms))] = -1
				print("\tprocess P{} ----> memory B{}".format(i+1,memory_space4.index(memory)+1))
				i += 1
	for i in process_memory4:
		if i != -1:
			print("\tprocess P{} is not allocated \n".format(process_memory4.index(i)+1))
	for i in range(len(memory_space4)):
		if remaining_memory4[i] == 0:
			extfrag += memory_space4[i]
	infrag = sum(remaining_memory4)				
	print("INTERNAL FRAGMENTATION : {} ".format(infrag))
	print("EXTERNAL FRAGMENTATION : {} ".format(extfrag))
	
def memory_allocation(mem_data):
	data=[]
	for x in mem_data:
		data.extend(x.split())
	data="".join(data)
	process_memory,memory_space = [],[]
	for i in range(len(data)):
		if i is 2 or i is 7 or i is 12 or i is 17:
			process_memory.append(data[i:i+3:])
		if i is 22 or i is 27 or i is 32 or i is 37 or i is 42:
			memory_space.append(data[i:i+3:])
	
	while True:
		print("\n\n\n\n\n\n\n SIMULATION OF MEMORY ALLOCATION ALGORITHM\n\n")
		print(" Enter : 1 ---> BEST FIT \t 2 ---> FIRST FIT \t 3 ---> NEXT FIT \t 4 ---> WORST FIT \t 5 ---> EXIT : ")
		ch = int(input(" Enter the Number : "))
		if ch == 1:
			best_fit(process_memory,memory_space)
		elif ch == 2:
			first_fit(process_memory,memory_space)
		elif ch == 3:
			next_fit(process_memory,memory_space)
		elif ch == 4:
			worst_fit(process_memory,memory_space)			
		elif ch == 5:
			print("EXIT FROM MEMORY ALLOCATION!!!")
			break
		else:
			print("WHOOPSSS.......INVALID INPUT!!!")	

def fifo(data2,size):
	f = -1
	hit = 0
	page_faults = 0
	_page_ = []
	for i in range(size):
		_page_.append(-1)

	for i in range(len(data2)):
		flag = 0
		for j in range(size):
			if(_page_[j] == data2[i]):
				flag = 1
				break

		if flag == 0:
			f = (f+1) % size
			_page_[f] = data2[i]
			page_faults += 1
			print("\n\t\t{} ---> ".format(data2[i]))
			for j in range(size):
				if _page_[j] != -1:
					print("\n\t\t\t\t\t->{}".format(_page_[j]))
				else:
					print("\n\t\t\t\t\t-> -")
		else:
			print("\n\t\t{} ---> HIT!!!".format(data2[i]))
			hit += 1
	print("\n Total page faults : {} ---- Total Hits : {} ".format(page_faults,hit))

def lru(data2,size):
    x,hit = 0,0
    page_faults = 0
    _page_ = []
    for i in range(size):
        _page_.append(-1)

    for i in range(len(data2)):
        flag = 0
        for j in range(size):
            if(_page_[j] == data2[i]):
                flag = 1
                break

        if flag == 0:
            if _page_[x] != -1:
                min = 999
                for k in range(size):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(_page_[k] == data2[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            _page_[x] = data2[i]
            x = (x+1) % size
            page_faults += 1
            print("\n\t\t{} --->".format(data2[i]))
            for j in range(size):
                if _page_[j] != -1:
                    print("\n\t\t\t\t\t->{}".format(_page_[j]))
                else:
                    print("\n\t\t\t\t\t-> -")
        else:
            print("\n\t\t{} ---> HIT".format(data2[i]))
            hit += 1
    print("\n Total page faults : {} ---- Total Hits : {} ".format(page_faults,hit))

def optimal(data2,size):
	x,hit = 0,0
	page_faults = 0
	_page_ = []
	for i in range(size):
		_page_.append(-1)

	for i in range(len(data2)):
		flag = 0
		for j in range(size):
			if(_page_[j] == data2[i]):
				flag = 1
				break

		if flag == 0:
			if _page_[x] != -1:
				max = -1
				for k in range(size):
					flag = 0
					j =  i
					while j<len(data2):
						j += 1
						if j < len(data2) and (_page_[k] == data2[j]):
							flag = 1
							break
					if (flag == 1 and max < j):
						max = j
						x = k

			_page_[x] = data2[i]
			x = (x+1) % size
			page_faults += 1
			print("\n\t\t{} --->".format(data2[i]))
			for j in range(size):
				if _page_[j] != -1:
					print("\n\t\t\t\t\t->{}".format(_page_[j]))
				else:
					print("\n\t\t\t\t\t-> -")
		else:
			print("\n\t\t{} ---> HIT".format(data2[i]))
			hit += 1
	print("\n Total page faults : {} ---- Total Hits : {}".format(page_faults,hit))

def page_replacement(page):
	data2 = []
	for x in page:
		if x.isnumeric():
			data2.extend(x.split())
	data2 = "".join(data2)	
	data2 = [int(x) for x in data2]

	while True:
		print("\n\n\n\n\n\n\n SIMULATION OF PAGE REPLACEMENT ALGORITHM\n\n")
		print(" Enter : 1 ---> FIFO \t 2 ---> LRU \t 3 ---> OPTIMAL \t 4 ---> EXIT : ")
		ch = int(input(" Enter the Number : "))
		if ch != 4:
			size = int(input("\n Enter page frame size : "))
		if ch == 1:
			fifo(data2,size)
		elif ch == 2:
			lru(data2,size)
		elif ch == 3:
			optimal(data2,size)
		elif ch == 4:
			print("EXIT FROM PAGE REPLACEMENT!!!")
			break
		else:
			print("WHOOPSSS.......INVALID INPUT!!!")	

def main():
	mem_data = docx2txt.process("memory allocation strategies.docx")
	page = urllib.request.urlopen("file:///C:/python-practice/project/os%20project/MINI%20PROJECT%20INPUT%20FILES/FIFO%20OPTIMAL%20LRU%20LFU.html").read().decode("utf8")
	print("\n\n\n\n\n\n\n*********************************************************************************************************************************************************\n\n\n\n\n\n\n")
	print("\n\n\n\n\n\n\n             ------------               !!!!!!OS PROJECT!!!!!               ---------------                         \n\n")
	while True:
		print("\n\n\n\n\n\n\n*********************************************************************************************************************************************************\n\n\n\n\n\n\n")
		print(" Enter : 1 ---> MEMORY ALLOCATION \t 2 ---> PAGE REPLACEMENT \t 3 ---> EXIT : ")
		ch = int(input(" Enter the Number : "))
		if ch == 1:
			memory_allocation(mem_data)
		elif ch ==2:
			page_replacement(page)
		elif ch == 3:
			print("THANK YOU FOR YOUR TIME!!!")
			break
		else:
			print("WHOOOPPPSSS......INVALID INPUT!!!!")	
main()	