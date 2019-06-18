# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:24:55 2017

@author: dhubel
"""
import numpy as np
from PIL import Image
train_dir = './data/train'
val_dir = './data/val'
train_file = '{}/{}.txt'.format(train_dir,'name')
val_file = '{}/{}.txt'.format(val_dir,'name')

indices_train = open(train_file, 'r').read().splitlines()
indices_val= open(val_file, 'r').read().splitlines()
num_train = len(indices_train)
num_val = len(indices_val)

tm_r, tm_g, tm_b = 0, 0, 0
for idx_train in indices_train:
    im_train = Image.open('{}/JPGImages/{}.PNG'.format(train_dir, idx_train))
    in_train = np.array(im_train, dtype=np.float32)
    imt_r = in_train[:, :, 0]
    imt_g = in_train[:, :, 1]
    imt_b = in_train[:, :, 2]
    imeant_r = imt_r.mean()
    imeant_g = imt_g.mean()
    imeant_b = imt_b.mean()
    tm_r += imeant_r
    tm_g += imeant_g
    tm_b += imeant_b

vm_r, vm_g, vm_b = 0, 0, 0
for idx_val in indices_val:
    im_val = Image.open('{}/JPGImages/{}.PNG'.format(val_dir, idx_val))
    in_val = np.array(im_train, dtype=np.float32)
    imv_r = in_val[:, :, 0]
    imv_g = in_val[:, :, 1]
    imv_b = in_val[:, :, 2]
    imeanv_r = imv_r.mean()
    imeanv_g = imv_g.mean()
    imeanv_b = imv_b.mean()
    vm_r += imeanv_r
    vm_g += imeanv_g
    vm_b += imeanv_b

mean_r = (tm_r+vm_r)/(num_train+num_val)
mean_g = (tm_g+vm_g)/(num_train+num_val)
mean_b = (tm_b+vm_b)/(num_train+num_val)
mean = [mean_b, mean_g, mean_r]
print(mean)
np.savetxt('./data/mean.txt', mean, fmt='%ls')

mean_npy_path = './data/mean.npy'
mean = np.ones([3,256,256], dtype=np.float)
mean[0,:,:] = mean_b
mean[1,:,:] = mean_g
mean[2,:,:] = mean_r

np.save(mean_npy_path,mean)
