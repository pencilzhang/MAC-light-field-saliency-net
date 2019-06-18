# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:44:14 2017

@author: dmarr
"""
#from pylab import*
caffe_root='/home/dhubel/deeplab_v2/deeplab-public-ver2/'   # Replace the caffe_root with your caffe path in your system
import sys
sys.path.insert(0,caffe_root + 'python')
import caffe
import numpy as np
import os
import time
os.chdir('/home/dhubel/deeplab_v2/deeplab-public-ver2/')  # Replace the caffe_root with your caffe path in your system
os.getcwd

caffe.set_device(0)
caffe.set_mode_gpu()

LFNet_model='LFnet_99'
k=1
record_val_loss=True


f=open('../LFNet_model/'+LFNet_model+'/train_LF.prototxt','r+')
s=f.read()
f.seek(0,0)
index=s.rfind('split')
c=s[index:index+23]
index1=c.rfind(',')
f.write(s.replace(s[index+11:index+index1-2],'train'+str(k)))
f.close()

if record_val_loss:
   f=open('../LFNet_model/'+LFNet_model+'/val_LF.prototxt','r+')
   s=f.read()
   f.seek(0,0)
   index=s.rfind('split')
   c=s[index:index+23]
   index1=c.rfind(',')
   f.write(s.replace(s[index+11:index+index1-2],'val'+str(k)))
   f.close() 
   
   f=open('../LFNet_model/'+LFNet_model+'/solver_train_LF.prototxt','r+')
   w=open('../LFNet_model/'+LFNet_model+'/solver_train_LF_aug.prototxt','w+')
   s=f.read()
   f.seek(0,0) 
   if 'test_' not in s:
       print 'Please add test network in solver_train_LF.prototxt....'
       
   if '#test_'in s and 'test_' in s:
      
      s=s.replace('#test_','test_')
   ind=s.rfind('model/')
   ind1=s.rfind('train"')
   ind3=s.rfind('GPU')
   w.write(s[:ind]+'model/'+str(k)+s[ind1:])
   f.close()
   w.close()
else:
   f=open('../LFNet/LFNet_model/'+LFNet_model+'/solver_train_LF.prototxt','r+')
   w=open('../LFNet/LFNet_model/'+LFNet_model+'/solver_train_LF_aug.prototxt','w+')
   s=f.read()
   f.seek(0,0)    
   if '#test_'not in s and 'test_' in s:
     s=s.replace('test_','#test_')
   ind=s.rfind('model/')
   ind1=s.rfind('train"')
   w.write(s[:ind]+'model/'+str(k)+s[ind1:])
   f.close()
   w.close()

   
   
caffemodel='../LFNet/Pretraining_model/train_iter_20000.caffemodel'
solver=caffe.SGDSolver('../LFNet/LFNet_model/'+LFNet_model+'/solver_train_LF_aug.prototxt')
solver.net.copy_from(caffemodel)
#solver.test_nets[0].copy_from(caffemodel)

max_iter = 160000


if not record_val_loss:

          
    solver.step(max_iter)
else:
    loss_PATH='../LFNet/LFNet_model/'+LFNet_model+'/loss/'

    train_loss = []
    val_loss = []
    test_iter = 128        
    test_interval = 500    
    start=time.time()

    for it in range(max_iter//20):
        traloss=0
        for i in range(20):  
            solver.step(1)   
            traloss1=solver.net.blobs['loss'].data*1
            traloss=traloss1+traloss
        tloss=traloss/20
        train_loss.append(str((it+1)*20)+'     '+str(tloss))
        end1=time.time()
        print( end1-start )
        print ('Iteration',(it+1)*20,'train_loss=',tloss)
        if (it+1)*20 %test_interval==0:
            valloss=0
            for test_it in range(test_iter):
                solver.test_nets[0].forward()
                valloss1=solver.test_nets[0].blobs['loss'].data*1
                valloss=valloss1+valloss
            vloss=valloss/test_iter
            val_loss.append(str((it+1)*20)+'     '+str(vloss))
            end1=time.time()
            print (end1-start )
            print ('Iteration',(it+1)*20,'val_loss=',vloss )

    np.savetxt(loss_PATH+'train_loss.txt', train_loss, fmt='%ls')
    np.savetxt(loss_PATH+'val_loss.txt', val_loss, fmt='%ls')
