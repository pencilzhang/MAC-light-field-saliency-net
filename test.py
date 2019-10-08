# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:44:14 2017

@author: dmarr
"""

caffe_root='/home/dhubel/deeplab_v2/deeplab-public-ver2/'
import sys
sys.path.insert(0,caffe_root + 'python')
import caffe
import os
os.chdir('/home/dhubel/deeplab_v2/deeplab-public-ver2/')
os.getcwd

caffe.set_device(0)
caffe.set_mode_gpu()

MAC_model='MACblock_99'
k=1

caffemodel='../models/'+MAC_model+'model/'+str(k)+'train_iter_160000.caffemodel'

net_test = caffe.Net('../models/'+MAC_model+'/test.prototxt',  
                caffemodel,  
                caffe.TEST) 
test_iter =  128   

for it in range(test_iter):
    net_test.forward()

    print(it)
