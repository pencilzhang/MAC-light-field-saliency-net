#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:19:43 2018

@author: dhubel
"""

caffe_root ='/home/dhubel/deeplab_v2/deeplab-public-ver2/' # replace caffe_root to your system

import sys
sys.path.insert(0, caffe_root + 'python')

import caffe
from caffe import layers as L, params as P
import os
os.chdir(caffe_root)
param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)]
def conv_relu(bottom, nout, ks=3, stride=1, pad=1,param=param):
    conv = L.Convolution(bottom, kernel_size=ks, stride=stride,
        num_output=nout, pad=pad, 
        param=param,
        weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0))
    return conv, L.ReLU(conv, in_place=True)

def conv_relu_dia(bottom, nout, ks=3, stride=1, pad=1,dilation=1):
    conv = L.Convolution(bottom, kernel_size=ks, stride=stride,
        num_output=nout, pad=pad,dilation=dilation,
        param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)],
        weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0))
    return conv, L.ReLU(conv, in_place=True)

def max_pool(bottom, ks=3, stride=2, pad=1):
    return L.Pooling(bottom, pool=P.Pooling.MAX, kernel_size=ks, stride=stride,pad=pad)

def cn_LF(split):
    n = caffe.NetSpec()
    pydata_params = dict(split=split, mean=(88.386, 99.768,107.622),
            seed=1337)
    if split == 'train':
        pydata_params['train_dir'] = '../data/train'
        pylayer = 'TrainDataLayer'
    else:
        pydata_params['val_dir'] = '../data/val'
        pylayer = 'ValDataLayer'
    n.data, n.label = L.Python(module='colorname_layers', layer=pylayer,
            ntop=2, param_str=str(pydata_params))
    
      
    # the base net
    
    n.LF_conv1_1=L.Convolution(n.data, kernel_size=9, stride=9, num_output=64,
        param=[dict(lr_mult=10, decay_mult=1), dict(lr_mult=20, decay_mult=0)],
        weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0))
    n.LF_relu1_1=L.ReLU(n.LF_conv1_1, in_place=True)
    n.conv2, n.relu2 = conv_relu(n.LF_relu1_1, 64,param=[dict(lr_mult=10, decay_mult=1), dict(lr_mult=20, decay_mult=0)])
    n.drop2= L.Dropout(n.relu2,  dropout_ratio=0.1,in_place=True)
    n.conv1_2, n.relu1_2 = conv_relu(n.drop2, 64)
    n.drop1_2= L.Dropout(n.relu1_2,  dropout_ratio=0.1,in_place=True)
    n.pool1 = max_pool(n.drop1_2)
    
    n.conv2_1, n.relu2_1 = conv_relu(n.pool1, 128)
    n.drop2_1= L.Dropout(n.relu2_1,  dropout_ratio=0.1,in_place=True)
    n.conv2_2, n.relu2_2 = conv_relu(n.drop2_1, 128)
    n.drop2_2= L.Dropout(n.relu2_2,  dropout_ratio=0.1,in_place=True)

    n.pool2 = max_pool(n.drop2_2)

    n.conv3_1, n.relu3_1 = conv_relu(n.pool2, 256)
    n.drop3_1= L.Dropout(n.relu3_1,  dropout_ratio=0.2,in_place=True)
    n.conv3_2, n.relu3_2 = conv_relu(n.drop3_1, 256)
    
    n.drop3_2= L.Dropout(n.relu3_2,  dropout_ratio=0.2,in_place=True)
    
    n.conv3_3, n.relu3_3 = conv_relu(n.drop3_2, 256)
    n.drop3_3= L.Dropout(n.relu3_3,  dropout_ratio=0.2,in_place=True)
    n.pool3 = max_pool(n.drop3_3)

    n.conv4_1, n.relu4_1 = conv_relu(n.pool3, 512)
    n.drop4_1= L.Dropout(n.relu4_1,  dropout_ratio=0.2,in_place=True)
    
    n.conv4_2, n.relu4_2 = conv_relu(n.drop4_1, 512)
    n.drop4_2= L.Dropout(n.relu4_2,  dropout_ratio=0.2,in_place=True)
    
    n.conv4_3, n.relu4_3 = conv_relu(n.drop4_2, 512)
    n.drop4_3= L.Dropout(n.relu4_3,  dropout_ratio=0.2,in_place=True)
    
    n.pool4 = max_pool(n.drop4_3, stride=1)

    n.conv5_1, n.relu5_1 = conv_relu_dia(n.pool4, 512, pad=2,dilation=2)
    n.drop5_1= L.Dropout(n.relu5_1,  dropout_ratio=0.3,in_place=True)
    
    n.conv5_2, n.relu5_2 = conv_relu_dia(n.drop5_1, 512, pad=2, dilation=2)
    n.drop5_2= L.Dropout(n.relu5_2,  dropout_ratio=0.3,in_place=True)
    
    n.conv5_3, n.relu5_3 = conv_relu_dia(n.drop5_2, 512, pad=2, dilation=2)
    n.drop5_3= L.Dropout(n.relu5_3,  dropout_ratio=0.3,in_place=True)
    
    n.pool5 = max_pool(n.drop5_3, stride=1)

    
    #hole=6
    n.fc6_1, n.relu6_1 = conv_relu_dia(n.pool5, 1024, pad=6,dilation=6)
    n.drop6_1= L.Dropout(n.relu6_1,  dropout_ratio=0.5,in_place=True)
    n.fc7_1, n.relu7_1 = conv_relu(n.relu6_1, 1024, ks=1, pad=0)
    n.drop7_1= L.Dropout(n.relu7_1,  dropout_ratio=0.5,in_place=True)
    n.fc8_1=L.Convolution(n.drop7_1,kernel_size=1, num_output=2, weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0),
                            param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)])
    
    #hole=12
    n.fc6_2, n.relu6_2 = conv_relu_dia(n.pool5, 1024, pad=12,dilation=12)
    n.drop6_2= L.Dropout(n.relu6_2,  dropout_ratio=0.5,in_place=True)
    n.fc7_2, n.relu7_2 = conv_relu(n.relu6_2, 1024, ks=1, pad=0)
    n.drop7_2= L.Dropout(n.relu7_2,  dropout_ratio=0.5,in_place=True)
    n.fc8_2=L.Convolution(n.drop7_2,kernel_size=1, num_output=2, weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0),
                            param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)])
    
    #hole=18
    n.fc6_3, n.relu6_3 = conv_relu_dia(n.pool5, 1024, pad=18,dilation=18)
    n.drop6_3= L.Dropout(n.relu6_3,  dropout_ratio=0.5,in_place=True)
    n.fc7_3, n.relu7_3 = conv_relu(n.relu6_3, 1024, ks=1, pad=0)
    n.drop7_3= L.Dropout(n.relu7_3,  dropout_ratio=0.5,in_place=True)
    n.fc8_3=L.Convolution(n.drop7_3,kernel_size=1, num_output=2, weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0),
                            param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)])
    
    #hole=24
    n.fc6_4, n.relu6_4 = conv_relu_dia(n.pool5, 1024, pad=24,dilation=24)
    n.drop6_4= L.Dropout(n.relu6_4,  dropout_ratio=0.5,in_place=True)
    n.fc7_4, n.relu7_4 = conv_relu(n.relu6_4, 1024, ks=1, pad=0)
    n.drop7_4= L.Dropout(n.relu7_4,  dropout_ratio=0.5,in_place=True)
    n.fc8_4=L.Convolution(n.drop7_4,kernel_size=1, num_output=2, weight_filler=dict(type='xavier'), bias_filler=dict(type='constant', value=0),
                            param=[dict(lr_mult=1, decay_mult=1), dict(lr_mult=2, decay_mult=0)])
    
    n.fc8= L.Eltwise(n.fc8_1, n.fc8_2,n.fc8_3,n.fc8_4,
                     operation=P.Eltwise.SUM)
    

    
    n.fc8_shrink=L.Interp(n.fc8,interp_param=dict(zoom_factor=8 ))
    n.socre=L.Crop(n.fc8_shrink,n.label);
#    
    n.loss = L.SoftmaxWithLoss(n.socre, n.label, loss_param=dict(ignore_label=255))
    
    return n.to_proto()

def make_net():
    with open('../LFNet_model/LFnet_99/train_LF.prototxt', 'w') as f:
        f.write(str(cn_LF('train')))

    with open('../LFNet_model/LFnet_99/val_LF.prototxt', 'w') as f:
        f.write(str(cn_LF('val')))

if __name__ == '__main__':
    make_net()
