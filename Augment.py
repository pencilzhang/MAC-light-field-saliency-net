#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:51:06 2019

@author: dhubel
"""

from PIL import Image 

from PIL import ImageEnhance
import os

os.chdir('/home/dhubel/deeplab_v2/LFNet/')  #repalce your path to Augment.py
import matlab.engine
eng=matlab.engine.start_matlab()

   
def Aug1(dir,dir_GT,tempname,save_dir,save_GT):
    fullname=os.path.join(dir,tempname+'.PNG')
    fullname_GT=os.path.join(dir_GT,tempname+'.PNG')
    image = Image.open(fullname)
    GT=Image.open(fullname_GT)
    image.save(save_dir+'/'+tempname+'.PNG')
    GT.save(save_GT+'/'+tempname+'.PNG')
    #rotate.flip,crop
    c=eng.augment1(dir,dir_GT,tempname,save_dir,save_GT)
    
def Aug2(tempname,save_dir,save_GT):
    name=['','_90','_180','_crop1']
    for i in range(len(name)):
        imagename=tempname+name[i]+'.PNG'
        fullname=os.path.join(save_dir,imagename)
        fullname_GT=os.path.join(save_GT,imagename)
        image = Image.open(fullname)
        GT=Image.open(fullname_GT)
   
        enh_bri = ImageEnhance.Brightness(image)    
        brightness = 1.5    
        image_brightened = enh_bri.enhance(brightness)    
        image_brightened.save(save_dir+'/'+tempname+name[i]+'_brig.PNG')
        GT.save(save_GT+'/'+tempname+name[i]+'_brig.PNG')
  
        enh_bri = ImageEnhance.Brightness(image)    
        brightness = 0.6  
        image_brightened = enh_bri.enhance(brightness)    
        image_brightened.save(save_dir+'/'+tempname+name[i]+'_dark.PNG')
        GT.save(save_GT+'/'+tempname+name[i]+'_dark.PNG')

#Chroma enhancement   
        enh_col = ImageEnhance.Color(image)    
        color = 1.7    
        image_colored = enh_col.enhance(color)    
        image_colored.save(save_dir+'/'+tempname+name[i]+'_color.PNG')
        GT.save(save_GT+'/'+tempname+name[i]+'_color.PNG')
    
#Contrast enhancement  
        enh_con = ImageEnhance.Contrast(image)    
        contrast = 1.7    
        image_contrasted = enh_con.enhance(contrast)  
        image_contrasted.save(save_dir+'/'+tempname+name[i]+'_cont.PNG')
        GT.save(save_GT+'/'+tempname+name[i]+'_cont.PNG')
        
def Aug3(save_dir,save_GT):
    c=eng.augment2(save_dir,save_GT)
    print 'completed!!!'    

def Augment(dir_image,dir_GT,save_dir,save_GT):
    
    files = os.listdir(dir_image)
    files.sort()
    j=0
    for name in files:
        index=name.rfind('.')
        tempname=name[:index]
        Aug1(dir_image,dir_GT,tempname,save_dir,save_GT)
        Aug2(tempname,save_dir,save_GT)
        print 'already operated '+str(j)
    print 'start adding noise....'
    Aug3(save_dir,save_GT)
    
dir_image='./data/original_data/'
dir_GT='./data/original_GT/'
save_dir='./data/train/JPGImages/'
save_GT='./data/train/GT_aug/'
Augment(dir_image,dir_GT,save_dir,save_GT)
