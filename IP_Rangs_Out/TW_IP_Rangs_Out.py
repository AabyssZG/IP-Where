#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from time import sleep
import math,sys

input_file_path1 = "delegated-apnic-latest.txt"
output_file_path1 = "TW_Rang.txt"

with open(input_file_path1, "r", encoding="utf-8") as input_file1, \
     open(output_file_path1, "w", encoding="utf-8") as output_file1:
    for line in input_file1:
        if line.startswith("TW|ipv4"):
            output_file1.write(line)
    print("[+] 筛选基本行成功，输出为TW_Rang.txt")

input_file_path2 = "TW_Rang.txt"
output_file_path2 = "TW_Rangs.txt"

with open(input_file_path2, "r", encoding="utf-8") as input_file2, \
     open(output_file_path2, "w", encoding="utf-8") as output_file2:
    for line in input_file2:
        parts = line.split("|")[2:4]
        output_file2.write("|".join(parts) + "\n")
    print("[+] 筛选基本列成功，输出为TW_Rangs.txt")

input_file_path3 = "TW_Rangs.txt"
output_file_path3 = "TW_IP_Rangs.txt"

with open(input_file_path3, "r", encoding="utf-8") as input_file3, \
     open(output_file_path3, "w", encoding="utf-8") as output_file3:
    for line in input_file3:
        number_part = line.split("|")[1]
        replacement = 32 - math.floor(math.log2(int(number_part)))
        output_file3.write(line.replace("|" + number_part, "/" + str(replacement) + "\n"))
    print("[+] 成功导出香港分配网段，输出为TW_IP_Rangs.txt")