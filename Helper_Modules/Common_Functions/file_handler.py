import os
import shutil


def rename_file(source_file, destination_file):
	# Specify the current file path and name
	current_file_path = '/path/to/current/file.txt'

	# Specify the new file path and name
	new_file_path = '/path/to/new/file.txt'

	# Rename the file
	os.rename(current_file_path, new_file_path)
	return destination_file


def copy_file(source_path, destination_path):
	# Specify the source file path and name
	source_file_path = '/path/to/source/file.txt'

	# Specify the destination file path and name
	destination_file_path = '/path/to/destination/file.txt'

	# Copy the file
	shutil.copyfile(source_file_path, destination_file_path)
	return destination_path
