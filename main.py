#coding=utf-8

import os
# print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))


import argparse
from os import path, listdir, makedirs

from ncmdump import dump

parser = argparse.ArgumentParser(description='用于将网易云专属的ncm音乐格式转换为mp3/flac')
parser.add_argument('file', type=str, help='传入包含ncm的文件夹或ncm文件', nargs='+')

args = parser.parse_args()

#获得传入的参数
# print(args)

# ' '.join(opts.dmp)
fileordir = ' '.join(args.file)

file_list = []
if path.isdir(fileordir):
    dir_str = fileordir
    for file in listdir(dir_str):
        if file.endswith(".ncm"):
            file_list.append(dir_str+"/"+file)
if path.isfile(fileordir):
    file_list.append(fileordir)



makedirs("output", exist_ok=True)

for file in file_list:
    print("processing", file)
    dump(file, output_dir="./output/")
