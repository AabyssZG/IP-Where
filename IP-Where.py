#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

import ipaddress
from tqdm import tqdm

logo0 = r'''
                                             ,, 
`7MMF'`7MM"""Mq.     `7MMF'     A     `7MF'`7MM 
  MM    MM   `MM.      `MA     ,MA     ,V    MM 
  MM    MM   ,M9        VM:   ,VVM:   ,V     MMpMMMb.  .gP"Ya `7Mb,od8 .gP"Ya  
  MM    MMmmdM9          MM.  M' MM.  M'     MM    MM ,M'   Yb  MM' "',M'   Yb 
  MM    MM               `MM A'  `MM A'      MM    MM 8M""""""  MM    8M"""""" 
  MM    MM                :MM;    :MM;       MM    MM YM.    ,  MM    YM.    , 
.JMML..JMML.               VF      VF      .JMML  JMML.`Mbmmd'.JMML.   `Mbmmd' 
                    +------------------------------+
                    + github.com/AabyssZG/IP-Where +  @AabyssZG
                    +------------------------------+   [+] V1.1
'''
print(logo0)

def check_ip(ip_to_check, ip_ranges):
    try:
        ip_address = ipaddress.ip_address(ip_to_check)
        for ip_range in ip_ranges:
            network = ipaddress.ip_network(ip_range.strip(), strict=False)
            if ip_address in network:
                return True
        return False
    except ValueError:
        return False

def read_IPs(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def read_IP_ranges(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def write_file(ips, output):
    with open(output, "w") as file:
        file.write("\n".join(ips))

ips_path = input("请输入原始IP文件名 >>> ")
ip_ranges_path = input("请输入需要匹配的IP段文件名 >>> ")
output = "True_IPs.txt"

ips_to_check = read_IPs(ips_path)
ip_ranges = read_IP_ranges(ip_ranges_path)

matched_ips = []

with tqdm(total=len(ips_to_check), desc="Checking IPs") as pbar:
    for ip in ips_to_check:
        if check_ip(ip, ip_ranges):
            matched_ips.append(ip)
        pbar.update(1)

write_file(matched_ips, output)