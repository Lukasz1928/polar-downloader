import os
import shutil
import zipfile

location = 'D:\\Desktop\\polar'
temp_location = f'{location}\\tmp'
download_location = f'{location}\\download'
files_location = f'{location}\\files'


def prepare_location():
    shutil.rmtree(location)
    os.makedirs(location)
    os.makedirs(temp_location)
    os.makedirs(download_location)
    os.makedirs(files_location)


def clean_up():
    shutil.rmtree(location)


def unzip_files():
    files = os.listdir(download_location)
    for idx, file in enumerate(files, 1):
        with zipfile.ZipFile(f'{download_location}\\{file}', "r") as zip_ref:
            zip_ref.extractall(temp_location)
        unpacked_file = f'{temp_location}\\{os.listdir(temp_location)[0]}'
        dst_file = f'{files_location}\\{idx}.tcx'
        shutil.copyfile(unpacked_file, dst_file)
        os.remove(unpacked_file)
