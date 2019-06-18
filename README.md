# LFNet-light-field-saliency-net
## Installation:
Install Python2 and Make caffe with python2 wrapper. Detailed description can refer to these two URLs：https://blog.csdn.net/ruotianxia/article/details/78331964 and https://github.com/BVLC/caffe

Then install MATLAB2016b, Do the following to make sure that the .m file can be used in Python

1、cd "matlabroot/extern/engines/python"  

2、python setup.py install

Note: matlabroot is the root directory of MATLAB in your system

## Data:
There are 640 original images in /Data/original_data, and the corresponding GT is in /Data/original_GT.

Run Python Augment.py for data enhancement

Convert GT to the label that can be entered into the caffe network by running the following command Under the your path to convert_labels.py:

`./convert_labels.py ./data/train/GT_aug/ ./data/train/name.txt ./data/train/annotations/`

Copy the label to the val/annotations/:
`cp ./data/train/annotations/* ./data/val/annotations/`

Copy the original images to the val/JPGImages/:
`cp ./Data/original_data/* ./data/val/JPGImages/`

Put the train data and test data in /Data/train/, this experiment uses 5-fold cross-validation, the picture name index has been put into the .txt file according to 5-fold cross-validation.

for example, train1.txt indicates the train data used in the first experiment in the 5-fold cross-validation. 

The corresponding val1.txt represents the test data used in the first experiment in the 5-fold cross-validation.

## training:
First find colorname_layers.py in `deeplab-public-ver2/`

Replace the caffe_root with your caffe path in your system

* Method 1:

Run `train.py` to train.

The current example is the first experiment of the LFnet_9×9 network. If you need to train other models, you can change the following parameters:

LFNet_model='LFnet_99', replace LFnet_99 with LFnet_33 or LFnet_StarShaped

k=1, indicating the first fold cross validation, which can be changed to 1-5

* Method 2:

Open the terminal, switch to the caffe root directory, 

run:`/LFNet_model/LFnet_99/train_LF_net.sh`, and note that the file path in train_LF_net.sh is changed to the path of your system.

## test:

Run `test.py` in` /LFNet` to test and save the test results as a .mat file.

Run` /F_PR_MAE/salientmap.m` to get the final saliency map. The other .m files in /F_PR_MAE are used to calculate quantitative indicators F, WF, MAE, AP and PR.

## Results:

Visual comparison of our best LFNet variant (LFNet-9 × 9) and state-of-the-art methods on three datasets. (a) Central viewing/all-focus images. (b) Ground truth maps. (c) LFNet-9 × 9. (d) LFS [1]. (e) DILF [2]. (f) WSC [3]. (g) Multi-cue [4]. The first five samples are taken from the proposed Lytro Illum dataset, the middle three samples are taken from the HFUT-Lytro dataset, and the last two samples are taken from the LFSD dataset.

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/SaliencyMap.png" /></div>

## References
1. N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light field,” in IEEE Conference on Computer Vision and Pattern Recognition, 2014.
2. J. Zhang, M. Wang, J. Gao, Y. Wang, X. Zhang, and X. Wu, “Saliency detection with a deeper investigation of light field,” in International Joint Conference on Artificial Intelligence, 2015.
3. N. Li, B. Sun, and J. Yu, “A weighted sparse coding framework for saliency detection,” in IEEE Conference on Computer Vision and Pattern Recognition, 2015.
4. L. Wang, H. Lu, X. Ruan, and M.-H. Yang, “Deep networks for saliency detection via local estimation and global search,” in IEEE Conference on Computer Vision and Pattern Recognition, 2015, pp. 3183–3192.
