# LFNet-light-field-saliency-net

We release the code of [Light Field Saliency Detection with Deep Convolutional Networks](XXXX), built on top of the  [DeepLab v2-Caffe codebase](https://bitbucket.org/aquariusjay/deeplab-public-ver2/src/master/).

## Overall network

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/framework.png" /></div>

## Architectures of three proposed LFNet. 

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/LFNet.png" /></div>

  (a) LFNet-99. (b) LFNet-33. (c) LFnet_StarShaped. The selected viewpoints are highlighted in red.

## Installation

[Python 2.7](https://www.anaconda.com/distribution/) 

[Caffe](https://caffe.berkeleyvision.org/)

[Matlab 2016b](https://www.mathworks.com/products/matlab.html). 
Do the following two steps to make sure that the .m file can be used in Python
- cd `matlabroot/extern/engines/python` 
- python `setup.py` install

Note: matlabroot is the root directory of MATLAB in your system


## Data
There are 640 original images in [data/original_data](/data/original_data), and the corresponding ground-truths are in [data/original_gt](/data/original_gt).

Run python `augment.py` for data augmentation.

Convert GT to the label that can be entered into the Caffe network by running:
`./convert_labels.py ./data/train/GT_aug/ ./data/train/name.txt ./data/train/annotations/`

Copy the label to the [val/annotations/](	/data/val/annotations/):
`cp ./data/train/annotations/* ./data/val/annotations/`

Copy the original images to the [val/JPGImages/](/data/val/JPGImages/):
`cp ./data/original_data/* ./data/val/JPGImages/`

Put the train data and test data in [data/train/](/data/train/).
We use 5-fold cross-validation, the image index has been put into the .txt file according to 5-fold cross-validation.
For example, train1.txt indicates the train data used in the 1st-fold experiment. 
The corresponding val1.txt represents the test data used in the 1st-fold experiment.

## Train
First go to `deeplab-public-ver2/colorname_layers.py`, then
replace the caffe_root with your caffe path in your system. 

There are two ways to train the network:
* Method 1):

Run `train.py` to train the LFnet_9×9 network.
If you need to train other models, you can replace 	`LFnet_99` with `LFnet_33` or `LFnet_StarShaped`
k indicates the first fold cross validation, which can be changed into 1-5.

* Method 2):

Open the terminal, switch to the caffe root directory, 
run:`/LFNet_model/LFnet_99/train_LF_net.sh`. 
Note that the file path is changed to the path of your system.


## Test

Run `test.py` to test and save the test results as a `.mat` file.

Run `/evaluation/salientmap.m` to get the final saliency map. The other `.m` files in [evaluation](	/evaluation/) are used to calculate quantitative indicators such as F,  WF,  MAE,  AP, and PR.


## Results

Visual comparison of our best LFNet variant (LFNet-9 × 9) and state-of-the-art methods on three datasets. (a) Central viewing/all-focus images. (b) Ground truth maps. (c) LFNet-9 × 9. (d) LFS [1]. (e) DILF [2]. (f) WSC [3]. (g) Multi-cue [4]. The first five samples are taken from the proposed Lytro Illum dataset, the middle three samples are taken from the HFUT-Lytro dataset, and the last two samples are taken from the LFSD dataset.

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/result.png" /></div>


## References
1. N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light field,” in IEEE Conference on Computer Vision and Pattern Recognition, 2014.
2. J. Zhang, M. Wang, J. Gao, Y. Wang, X. Zhang, and X. Wu, “Saliency detection with a deeper investigation of light field,” in International Joint Conference on Artificial Intelligence, 2015.
3. N. Li, B. Sun, and J. Yu, “A weighted sparse coding framework for saliency detection,” in IEEE Conference on Computer Vision and Pattern Recognition, 2015.
4. L. Wang, H. Lu, X. Ruan, and M.-H. Yang, “Deep networks for saliency detection via local estimation and global search,” in IEEE Conference on Computer Vision and Pattern Recognition, 2015, pp. 3183–3192.

## Citation

If you find our paper and repo useful, please cite our paper. Thanks!

```
@article{Zhang2019lfnet,
    title={Light Field Saliency Detection with Deep Convolutional Networks},
    author={Zhang, Jun and Liu, Yamei and Zhang, Shengping, Poppe, Ronald and Wang, Meng},
    journal={arXiv preprint arXiv:XXXX},
    year={2019}
}  
```

## Acknowledgement

Our light field saliency network is built on top of the  [DeepLab v2-Caffe](https://bitbucket.org/aquariusjay/deeplab-public-ver2/src/master/), but it could be extended to other network architectures. We thank Liang-Chieh Chen for releasing DeepLabv2-Caffe codebase.
