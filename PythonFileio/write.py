# with open('test.txt', 'r') as rf:
# 	with open('testcopy.txt', 'w') as wf:

# 		for line in rf:
# 			wf.write(line)
# i = ["jennie.jpg","jennie1,jpg"]
# with open(i, 'rb') as rf:
# 	with open(i,'wb')as wf:

# 		for line in rf:
# 			wf.write(line)

with open('jennie.jpg', 'rb') as rf:
	with open('jennie_copy.png', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)

		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)