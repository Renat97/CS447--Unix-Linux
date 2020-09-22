#!/usr/bin/env python3
import subprocess
import argparse
import logging
import os
import parted


parser = argparse.ArgumentParser(description='Parsing arguments for fileNames to truncate')
parser.add_argument('--file1', type=str, help='Files to truncate')
parser.add_argument('--file2', type=str, help='File to truncate')
parser.add_argument('--file3', type=str, help='File to truncate')        

# logging setup used print to log
LOG_FORMAT = '%(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)  #Use a basic config

def main(args):
    # file 1
    output = args.file1
    logging.info("{0}".format(output))
    subprocess.call('sudo truncate -s 5G /root/hw5/"{}"'.format(output), shell=True)
    subprocess.call('sudo losetup --find --show /root/hw5/"{}"'.format(output), shell=True)
    hello = subprocess.check_output('losetup --associated /root/hw5/"{}"'.format(output) +' | cut -d ' + ':' + ' -f 1',shell=True).strip()
    argument  = 'sudo parted -s ' + hello + " 'mklabel gpt mkpart lvpart1 1M 4G'"
    subprocess.call(argument, shell=True)
    print(argument)
    
    #file 2
    output2 = args.file2
    logging.info("{0}".format(output2))
    subprocess.call('truncate -s 5G /root/hw5/"{}"'.format(output2), shell=True)
    subprocess.call('losetup --find --show /root/hw5/"{}"'.format(output2), shell=True)
    hello2 = subprocess.check_output('losetup --associated /root/hw5/"{}"'.format(output2) +' | cut -d ' + ':' + ' -f 1',shell=True).strip()
    argument2 = 'sudo parted -s ' + hello2 + " 'mklabel gpt mkpart lvpart1 1M 4G'"
    subprocess.call(argument2, shell=True)
    print(argument2)
    #file 3
    output3 = args.file3
    logging.info("{0}".format(output3))
    subprocess.call('truncate -s 5G /root/hw5/"{}"'.format(output3), shell=True)
    subprocess.call('losetup --find --show /root/hw5/"{}"'.format(output3), shell=True)
    hello3 = subprocess.check_output('losetup --associated /root/hw5/"{}"'.format(output3) +' | cut -d ' + ':' + ' -f 1',shell=True).strip()
    argument3  = 'sudo parted -s ' + hello3 + " 'mklabel gpt mkpart lvpart1 1M 4G'"
    subprocess.call(argument3, shell=True)
    print(argument3)

    # raid level
    raidArg = 'mdadm -C /dev/md0 -l raid1 -n 2 ' + hello + ' ' + hello2 + ' -x 1 ' + hello3
    subprocess.call(raidArg, shell=True)
    print(raidArg)
   
   # LVM
    lvmArg = 'vgcreate vgpool /dev/md0'
    subprocess.call(lvmArg, shell=True)

    lvmArg2 = 'lvcreate -L 1G -n lv0 vgpool'
    subprocess.call(lvmArg2, shell=True)

    lvmArg3 = 'lvcreate -L 1G -n lv1 vgpool'
    subprocess.call(lvmArg3, shell=True)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
