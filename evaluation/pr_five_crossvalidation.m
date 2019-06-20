%% A demo code to display precision-recall curve for evaluating salient object detection algorithms
%%  five-cross validation 
function pr_five_crossvalidation

LFNet_model = 'LFnet_99';
dataset = 'illum'; % name of the dataset
methods = {'1fold_result','2fold_result','3fold_result','4fold_result','5fold_result'}; % You can add more names of methods
methods_colors = distinguishable_colors(length(methods));
savepath = '../PR_Curve/';
P=zeros(256,1);
r=zeros(256,1);
figure
hold on
for m = 1:length(methods)
    salpath= strcat('../result/',LFNet_model,'/',methods{m},'/saliencymap');
    gtpath= '../data/original_GT';%% Set your own GT path  
    [precision,recall]=pr(salpath,gtpath);
    P = P +precision;
    r=r+recall;
    plot(recall, precision,'color',methods_colors(m,:),'linewidth',2);   
    m
end


axis([0 1 0 1]);
hold off
grid on;
legend(methods, 'Location', 'SouthWest');
xlabel('Recall','fontsize',12);
ylabel('Precision','fontsize',12);

P=P./5;
r=r./5;
pr = [P'; r'];
fid = fopen([savepath dataset, '_', method, '_PRCurve.txt'],'at');
fprintf(fid,'%f %f\n',pr);
fclose(fid);
disp('Done!');


