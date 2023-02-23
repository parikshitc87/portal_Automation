import os
import shutil


def rename_file(source_file_path, destination_file_path):
	os.rename(source_file_path, destination_file_path)
	return True


def copy_file(source_file_path, destination_file_path):
	shutil.copyfile(source_file_path, destination_file_path)
	return True


def delete_file(file_path):
	os.remove(file_path)
	return True
