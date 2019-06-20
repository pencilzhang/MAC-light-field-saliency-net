#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:51:06 2019

@author: dhubel
"""

from PIL import Image 

from PIL import ImageEnhance
import os

os.chdir('/home/dhubel/deeplab_v2/LFNet/')
import matlab.engine
eng=matlab.engine.start_matlab()

   
def Aug_geometric(dir,dir_GT,tempname,save_dir,save_GT):  ## Geometric transformation
    fullname=os.path.join(dir,tempname+'.PNG')
    fullname_GT=os.path.join(dir_GT,tempname+'.PNG')
    image = Image.open(fullname)
    GT=Image.open(fullname_GT)
    image.save(save_dir+'/'+tempname+'.PNG')
    GT.save(save_GT+'/'+tempname+'.PNG')
    #Rotate.flip,crop
    c=eng.augment_geometry(dir,dir_GT,tempname,save_dir,save_GT)
    
def Aug_color(tempname,save_dir,save_GT):#Change brightness, chroma, contrast
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
        
def Aug_addnoise(save_dir,save_GT):##add noise
    c=eng.augment_addnoise(save_dir,save_GT)
    print 'completed!!!'    

def Augment(dir_image,dir_GT,save_dir,save_GT):
    
    files = os.listdir(dir_image)
    files.sort()
    j=0
    for name in files:
        index=name.rfind('.')
        tempname=name[:index]
        Aug_geometric(dir_image,dir_GT,tempname,save_dir,save_GT)
        Aug_color(tempname,save_dir,save_GT)
        print 'already operated '+str(j)
    print 'start adding noise....'
    Aug_addnoise(save_dir,save_GT)
    
dir_image='./data/original_data/'
dir_GT='./data/original_GT/'
save_dir='./data/train/JPGImages/'
save_GT='./data/train/GT_aug/'
Augment(dir_image,dir_GT,save_dir,save_GT)
