#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 20:57:14 2018

@author: dhubel
"""

import os  
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    files.sort()
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    index=name.rfind('.')
                    name=name[:index]
                    file.write(name + "\n")
                    break 
def Test():
  dir="/home/dhubel/deeplab_v2/LFNet/data/train/JPGImages"  # Replace it with your path
  outfile="/home/dhubel/deeplab_v2/LFNet/data/train/name.txt"   # Replace it with your path
  wildcard = ".PNG"
  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile) 
  ListFilesToTxt(dir,file,wildcard, 1)
  file.close() 
Test()
