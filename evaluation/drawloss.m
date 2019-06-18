function drawloss
clc
clear


methods = {'train_loss','val_loss'}; 

methods_colors = distinguishable_colors(length(methods));
readpath = '../LFNet_model/LFnet_99/loss'; 

figure
hold on

for m = 1:length(methods)
    prFileName = strcat(readpath, '/', methods{m}, '.txt');
    R = load(prFileName);
    iteration = R(:, 1);
    loss = R(:, 2);
    plot(iteration, loss,'color',methods_colors(m,:),'linewidth',2);   
end 
  axis([0 160000 0 1.4]);
% 
hold off
grid on;

legend(methods, 'Location', 'Northeast');
xlabel('Iterations','fontsize',12);
ylabel('Loss','fontsize',12);
end
