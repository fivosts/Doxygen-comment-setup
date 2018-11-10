#!/usr/bin/python2
import subprocess, os
import sys

def register_file(source_path):

	source_name = source_path
	if "/" in source_path:
		source_name = source_path.split("/")[-1]

	register_list = []
	register_list.append("/*! \\file " + source_name + "\n")
	register_list.append("*\t \\brief <Add brief description>\n")
	register_list.append("*\n")
	register_list.append("*\t <Add detailed description>\n")
	register_list.append("*/\n")

	return register_list

def modify_source(source_path):
	print source_path
	try:
		source_file = open(source_path, "r+")
	except IOError:
		print source_path + " could not be opened"

	source_file_list = register_file(source_path)  ## Insert header file info
	for line in source_file:
		print line
		source_file_list.append(line)
	print source_file_list

	#insert here functions to add function/class/struct data

	try:
		source_file.seek(0)
		source_file.truncate()
		for line in source_file_list:
			source_file.write(line)
	except IOError:
		print source_path + " could not be written"

	try:
		for line in source_file_list:
			source_file.close()
	except IOError:
		print source_path + " could not be closed"

	return

def search_dir(item, prev_path):
	# print prev_path  + item
	# print os.path.isdir(prev_path+item)

	if os.path.isfile(prev_path + item):

		file_extension = (prev_path + item).split(".")[-1]
		if file_extension in ["c", "cpp", "cc", "cxx", "h", "hpp"]:
			modify_source(prev_path + item)
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