#!/usr/bin/python2
import subprocess, os
import sys

def modify_source(source_path):
	print source_path
	pass

def search_dir(item, prev_path):
	# print prev_path  + item
	# print os.path.isdir(prev_path+item)

	if os.path.isfile(prev_path + item):
		file_extension = (prev_path + item).split(".")[-1]
		
		if file_extension in ["c", "cpp", "cc", "cxx", "h", "hpp"]:
			modify_source(prev_path + item)
			pass
		pass
	elif os.path.isdir(prev_path + item):
		for dir in os.listdir(prev_path + item):
			search_dir("/" + dir, prev_path + item)


	return

if __name__ == '__main__':

	dir_list = sys.argv
	del dir_list[0]
	if os.path.basename(__file__) in dir_list: 
		dir_list.remove(os.path.basename(__file__))
	# for i in range(1, len(sys.argv)):
		# if 
		# dir_list.append(sys.argv[i])
		# print sys.argv[i]

	for item in dir_list:
		if item[-1] == "/":
			item = item[:-1]
		search_dir(item, "")