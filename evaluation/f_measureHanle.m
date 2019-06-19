    function f_measureHanle

    clc
    clear
    LFNet_model='LFNet_99';
    F=0;
    for k=1:5

        salpath= ['../result/',LFNet_model,'/',num2str(k),'fold_result/salmap'];

        gtpath= '../data/original_GT';



        salientmappath = fullfile(salpath, '*.png' );

        imnames=dir(salientmappath);


        imNum = length(imnames);
        belt2=0.3;
        reca = zeros(imNum,1);
        prec = zeros(imNum,1);
        prec = zeros(imNum,1);

        for i=1:imNum
            [~,name,~]=fileparts(imnames(i).name);
            Spath = fullfile( salpath, imnames(i).name);
            Gpath=fullfile( gtpath, [name,'.PNG']);
            input_im=imread(Spath);

            truth_im=imread(Gpath);
            [c,h,~]=size(truth_im);
            input_im=imresize(input_im,[c,h]);
            truth_im = truth_im(:,:,1);
            if max(max(truth_im))==255
                label = truth_im./255;
            end
            score=input_im(:,:,1);
            thresh=2*mean(mean(score));
            sco_th0=(score)>thresh;
            sco_th=uint8(sco_th0);
            TP = length(find((label == 1) & (sco_th == 1)));
            FP = length(find((label == 0) & (sco_th == 1)));
            FN = length(find((label == 1) & (sco_th == 0)));
            if TP~=0
                reca(i,1) = TP/(TP+FN);
                prec(i,1) = TP/(TP+FP);
            end
            display(num2str(i));
        end



        %%%%%% calculate Fmeasure
        P=mean(prec);
        R=mean(reca);
        Fmeasure=((1+belt2)*P*R)/(belt2*P+R);

        F=F+Fmeasure;

    end
    F=F/5