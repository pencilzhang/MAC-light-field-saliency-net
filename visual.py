#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:03:17 2019

@author: dhubel
"""

caffe_root='/home/dhubel/deeplab_v2/deeplab-public-ver2/' # Replace the caffe_root with your caffe path in your system
import sys
sys.path.insert(0,caffe_root + 'python')
import caffe
import numpy as np
from scipy import misc
import pylab as py
import scipy.io as scio

import matplotlib.pyplot as plt
import os
os.chdir('/home/dhubel/deeplab_v2/deeplab-public-ver2/') # Replace the caffe_root with your caffe path in your system
os.getcwd

caffe.set_device(0)
caffe.set_mode_gpu()


caffemodel_m='../LFNet_model/LFnet_99/model/train_iter_160000.caffemodel'
net_test = caffe.Net('../LFNet_model/LFnet_99/train_LF.prototxt',  
                caffemodel_m,  
                caffe.TEST) 




def vis_square(data,name):  
 
        data = (data - data.min()) / (data.max() - data.min())  
       

        n = int(np.ceil(np.sqrt(data.shape[0])))  
        padding = (((0, n ** 2 - data.shape[0]),  
                   (0, 1), (0, 1))                 
                   + ((0, 0),) * (data.ndim - 3))  
        data = np.pad(data, padding, mode='constant', constant_values=1)  
  
        # tile the filters into an image  
        data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))  
        data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])  
        plt.figure()
        plt.imshow(data)
        plt.axis('off')
        plt.show()
        misc.toimage(data,cmin=0.0,cmax=1).save('   '+name+'.jpg')
        dataNew = '  /'+name+'.mat'

        scio.savemat(dataNew, {'data':data})

net_test.forward()   

       
##  visual feature map
name='conv3_1'
feat = net_test.blobs[name].data[0]
vis_square(feat,name)
      
### visual convolution kernel

#name='LF_conv1_1'
#feat = net_test.params[name][0].data
#vis_square(feat.transpose(0, 2, 3, 1),name)

