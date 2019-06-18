function AP
clc
clear

salpath= '../LFNet_model/LFnet_99/result/1_result/salmap';

gtpath= '../data/original_GT';



salientmappath = fullfile(salpath, '*.png' );
% GTpath = fullfile(gtpath, '*.png' );
imnames=dir(salientmappath);


imNum = length(imnames);
precision = zeros(256,1);
recall = zeros(256,1);
for i=1:imNum
    [~,name,~]=fileparts(imnames(i).name);
    Spath = fullfile( salpath, imnames(i).name);
    Gpath=fullfile( gtpath, [name,'.PNG']);
    truth_im=imread(Gpath);
    input_im=imread(Spath);
    [c,h,~]=size(truth_im);
    input_im=imresize(input_im,[c,h]);
    
    truth_im = truth_im(:,:,1);
    input_im = input_im(:,:,1);
    if max(max(truth_im))==255
        truth_im = truth_im./255;
    end
    for threshold = 0:255
        index1 = (input_im>=threshold);
        truePositive = length(find(index1 & truth_im));
        groundTruth = length(find(truth_im));
        detected = length(find(index1));
        if truePositive~=0
            precision(threshold+1) = precision(threshold+1)+truePositive/detected;
            recall(threshold+1) = recall(threshold+1)+truePositive/groundTruth;
        end
    end
    display(num2str(i));
end
precision = precision./imNum;
recall = recall./imNum;

recall = recall(end:-1:1);
precision = precision(end:-1:1);

ap = VOCap(recall,precision)
