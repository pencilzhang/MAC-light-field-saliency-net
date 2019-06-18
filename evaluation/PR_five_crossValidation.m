%% A demo code to display precision-recall curve for evaluating salient object detection algorithms
%%  five-cross validation 
function PR_five_crossValidation

method = 'LFnet_99';
dataset = 'illum'; % name of the dataset
methods = {'1_result','2_result','3_result','4_result','5_result'}; % you can add more names of methods
methods_colors = distinguishable_colors(length(methods));
savepath = '../PR_Curve/';
P=zeros(256,1);
r=zeros(256,1);
%% load PRCurve.txt and draw PR curves
figure
hold on
for m = 1:length(methods)
    salpath= ['../LFNet_model/',method,'/result/',methods{m},'/salmap'];
    gtpath= '../data/original_GT';%% set your own GT path
    
    
    [precision,recall]=PR(salpath,gtpath);
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


