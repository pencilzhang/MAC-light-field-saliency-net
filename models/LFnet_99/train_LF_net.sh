#!/usr/bin/env sh
set -e

GLOG_logtostderr=0 GLOG_log_dir='/home/dhubel/deeplab_v2/LFNet/LFNet_model/LFnet_99/log/' ./build/tools/caffe train --solver=/home/dhubel/deeplab_v2/LFNet/LFNet_model/LFnet_99/solver_train_LF_aug.prototxt --weights=/home/dhubel/deeplab_v2/pretrain/pretrain.caffemodel --gpu=0$@
