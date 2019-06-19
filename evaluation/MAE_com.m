    function mae_com
    clear all
    close all;clc;

    LFNet_model='LFNet_99';
    mae=0;
    for k=1:5

        salpath= ['../result/',LFNet_model,'/',num2str(k),'fold_result/salmap'];
        gtpath= '../data/original_GT';

        salientmappath = fullfile(salpath, '*.png' );
        imnames=dir(salientmappath);
        imNum = length(imnames);
        MAE = 0;
        %% compute MAE
        for i = 1:imNum
            [~,name,~]=fileparts(imnames(i).name);
            Spath = fullfile( salpath, imnames(i).name);
            Gpath=fullfile( gtpath, [name,'.PNG']);
            truth_im=imread(Gpath);
            input_im=imread(Spath);
            [c,h,~]=size(truth_im);
            input_im=imresize(input_im,[c,h]);

            input_im = double(input_im(:,:,1))./255;

            truth_im = double(truth_im(:,:,1));
            if max(max(truth_im))==255
                truth_im = truth_im./255;
            end
            MAE = MAE + mean2(abs(truth_im-input_im));
            display(num2str(i));
        end
        MAE = MAE/imNum;
        mae=MAE+mae;

    end
    mae=mae/5


