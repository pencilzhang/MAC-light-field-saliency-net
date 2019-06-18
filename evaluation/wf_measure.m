function wf_measure
clc
clear

salpath= '../models/LFnet_99/result/1_result/salmap';

gtpath= '../data/original_GT';

salientmappath = fullfile(salpath, '*.png' );
imnames=dir(salientmappath);

imNum = length(imnames);
belt2=0.3;
reca = zeros(imNum,1);
prec = zeros(imNum,1);
for i=1:imNum
    [~,name,~]=fileparts(imnames(i).name);
    Spath = fullfile( salpath, imnames(i).name);
    Gpath=fullfile( gtpath, [name,'.PNG']);
    truth_im=imread(Gpath);
    truth_im = truth_im(:,:,1);
    input_im=imread(Spath);
    [c,h,~]=size(truth_im);
    input_im=imresize(input_im,[c,h]);
    score=input_im(:,:,1);
    score=double(score);
    if max(max(score))>1
        score=double(score./255);
    end
    if max(max(truth_im))==255
        label=(truth_im)>128;
    end
    [R,P]= WFb(score,label);
    reca(i,1) = R;
    prec(i,1) = P;
    display(num2str(i));
end
P=mean(prec)
R=mean(reca)
WFmeasure=((1+belt2)*P*R)/(eps+belt2*P+R)
    
end  
    
    
    
    
    function [R,P]= WFb(FG,GT)
    % WFb Compute the Weighted F-beta measure (as proposed in "How to Evaluate
    % Foreground Maps?" [Margolin et. al - CVPR'14])
    % Usage:
    % Q = FbW(FG,GT)
    % Input:
    %   FG - Binary/Non binary foreground map with values in the range [0 1]. Type: double.
    %   GT - Binary ground truth. Type: logical.
    % Output:
    %   Q - The Weighted F-beta score
    
    %Check input
    Beta=0.3;
    if (~isa( FG, 'double' ))
        error('FG should be of type: double');
    end
    if ((max(FG(:))>1) || min(FG(:))<0)
        error('FG should be in the range of [0 1]');
    end
    if (~islogical(GT))
        error('GT should be of type: logical');
    end
    
    dGT = double(GT); %Use double for computations.
    
    
    E = abs(FG-dGT);
    % [Ef, Et, Er] = deal(abs(FG-GT));
    
    [Dst,IDXT] = bwdist(dGT);
    %Pixel dependency
    K = fspecial('gaussian',7,5);
    Et = E;
    Et(~GT)=Et(IDXT(~GT)); %To deal correctly with the edges of the foreground region
    EA = imfilter(Et,K);
    MIN_E_EA = E;
    MIN_E_EA(GT & EA<E) = EA(GT & EA<E);
    %Pixel importance
    B = ones(size(GT));
    B(~GT) = 2-1*exp(log(1-0.5)/5.*Dst(~GT));
    Ew = MIN_E_EA.*B;
    
    TPw = sum(dGT(:)) - sum(sum(Ew(GT)));
    FPw = sum(sum(Ew(~GT)));
    
    R = 1- mean2(Ew(GT)); %Weighed Recall
    P = TPw./(eps+TPw+FPw); %Weighted Precision
    
%     Q = (2)*(R*P)./(eps+R+P); %Beta=1;
%     Q = (1+Beta)*(R*P)./(eps+R+(Beta.*P));
    end