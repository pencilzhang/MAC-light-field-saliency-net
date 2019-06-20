# LFNet-light-field-saliency-net

We release the code of [Light Field Saliency Detection with Deep Convolutional Networks](XXXX), built on top of the  [DeepLab v2-Caffe codebase](https://bitbucket.org/aquariusjay/deeplab-public-ver2/src/master/).

## Overall network

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/framework.png" /></div>

## Architectures of three proposed LFNet variants 

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/LFNet.png" /></div>

  (a) LFNet-9 × 9. (b) LFNet-3 × 3. (c) LFnet_StarShaped. The selected viewpoints are highlighted in red.

## Installation

[Python 2.7](https://www.anaconda.com/distribution/) 

[Caffe](https://caffe.berkeleyvision.org/)

[Matlab 2016b](https://www.mathworks.com/products/matlab.html). 
Do the following two steps to make sure that the .m file can be used in Python:
- cd `matlabroot/extern/engines/python` 
- python `setup.py` install

Note: matlabroot is the root directory of MATLAB in your system.


## Data

* Dataset

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/dataset_construction.png" /></div>


<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/data_examples.png" /></div>


This project introduces a novel dataset, named Lytro illum .Using a Lytro Illum camera,
we collect 640 light fields with significant variations in terms of size, textureness, background clutter and illumination, etc.
We provide micro-lens image array, central viewing image and ground-truths. 
Please download them [here](https://drive.google.com/drive/folders/1iEuM-CO5JUgKa5-NHMXWjorAt2kBaSU3).





* Data processing

Put micro-lens image array into `data/original_data/` and put ground-truths into `data/original_GT/`.
There are 640 original images in [data/original_data/](/data/original_data), and the corresponding ground-truths are in [data/original_GT/](/data/original_GT).

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
* First go to `deeplab-public-ver2/colorname_layers.py`, then
replace the caffe_root with your caffe path in your system. 

* Download the pretrain model [here](https://drive.google.com/open?id=1ed4HmhGn50uz21wUavIkZYcYz8OjRg4l) model that initialize the backbone model.
  Create a new folder `pretrain` and place the downloaded pretrain model in this folder.
  

* There are two ways to train the network:

(1) Run `train.py` to train the LFnet_9×9 network.
If you need to train other models, you can replace 	`LFnet_99` with `LFnet_33` or `LFnet_StarShaped`
k indicates the first fold cross validation, which can be changed into 1-5.

(2) Open the terminal, switch to the caffe root directory, 
run:`/LFNet_model/LFnet_99/train_LF_net.sh`. 
Note that the file path is changed to the path of your system.



## Pretrained models
To get the pretrained models on the Illum dataset, please download form [here](https://drive.google.com/open?id=12L8nYlkMsnjUHWJm97gIkDGdTD7GxUDp).
After decompression,please put them in the three folders under the `/model/` path.



## Test

Run `test.py` to test and save the test results as a `.mat` file.

Run `/evaluation/salientmap.m` to get the final saliency map. The other `.m` files in [evaluation](	/evaluation/) are used to calculate quantitative indicators such as F,  WF,  MAE,  AP, and PR.


## Results
The saliency map of three proposed models on the Lytro illum dataset are provided [here](https://drive.google.com/open?id=1a-UiTu49rbQkJ7RYrjIayOwPaO2RGtfZ).
Visual comparison of our best LFNet variant (LFNet-9 × 9) and state-of-the-art methods on three datasets. (a) Central viewing/all-focus images. (b) Ground truth maps. 
(c) LFNet-9 × 9. (d) LFS [1]. (e) DILF [2]. (f) WSC [3]. (g) Multi-cue [4]. The first five samples are taken from the proposed Lytro Illum dataset, 
the middle three samples are taken from the HFUT-Lytro dataset, and the last two samples are taken from the LFSD dataset.

<div style="text-align:center"><img src ="https://github.com/YaMeiLiu/LFNet-light-field-saliency-net/raw/master/result.png" /></div>


## References
1. N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light field,” in IEEE Conference on Computer Vision and Pattern Recognition, 2014.
2. J. Zhang, M. Wang, J. Gao, Y. Wang, X. Zhang, and X. Wu, “Saliency detection with a deeper investigation of light field,” in International Joint Conference on Artificial Intelligence, 2015.
3. N. Li, B. Sun, and J. Yu, “A weighted sparse coding framework for saliency detection,” in IEEE Conference on Computer Vision and Pattern Recognition, 2015.
4. J. Zhang, M. Wang, L. Lin, X. Yang, J. Gao, and Y. Rui, “Saliency detection on light field: A multi-cue approach,” ACM Transactions on Multimedia Computing, Communications, and Applications, 2017.


## Citation

If you find our paper and repo useful, please cite our paper. Thanks!

```
@article{Zhang2019lfnet,
    title={Light Field Saliency Detection with Deep Convolutional Networks},
    author={Zhang, Jun and Liu, Yamei and Zhang, Shengping, Poppe, Ronald and Wang, Meng},
    journal={arXiv preprint arXiv: 2737364},
    year={2019}
}  
```

## Acknowledgement

Our light field saliency network is built on top of the  [DeepLab v2-Caffe](https://bitbucket.org/aquariusjay/deeplab-public-ver2/src/master/), 
but it could be extended to other network architectures. We thank Liang-Chieh Chen for releasing DeepLabv2-Caffe codebase.


## Contact

[Jun Zhang](mailto:zhangjun1126@gmail.com),  [Yamei Liu](mailto:liuarmg@gmail.com)

Questions can also be left as issues in the repository. We will be happy to answer them.
