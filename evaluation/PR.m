function [precision,recall]=PR(salpath,gtpath)

% 
% salpath= '../LFNet_model/LFnet_99/result/1_result/salmap';
% % 
% gtpath= '/media/dhubel/24c82cc9-d084-41b1-8f8c-ed0d81eb1acb/allresult/GT/illum/GT';



salientmappath = fullfile(salpath, '*.png' );

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
% figure,plot(recall,precision);
% grid on;

% recal = recall(end:-1:1);
% preci = precision(end:-1:1);
% 
% ap = VOCap(recal,preci)



% xlabel('Recall')
% ylabel('Precision')
% legend(method)
% axis([0 1 0 1]);


% pr = [precision;recall];

% fid = fopen([savepath dataset, '_', method, '_PRCurve.txt'],'at');
% fprintf(fid,'%f %f\n',pr);
% fclose(fid);
% disp('Done!');
end
