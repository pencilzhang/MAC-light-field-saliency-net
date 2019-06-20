    %% A demo code to display precision-recall curve for evaluating salient object detection algorithms
    function drawPR
    clear all;%close all;
    dataset = 'illum'; % Name of the dataset

    %methods = {'LFS','ijcai15','WSC','tomm17','LFnet_99'}; % You can add more names of methods separated by comma
    methods = {'LFnet_99'};
    methods_colors = distinguishable_colors(length(methods));
    readpath = '../pr_curve/';

    %% Load PRCurve.txt and draw PR curves
    figure
    hold on

    for m = 1:length(methods)
        prFileName = strcat(readpath,dataset, '_', methods{m}, '_PRCurve.txt');
        R = load(prFileName);
        precision = R(:, 1);
        recall = R(:, 2);
        plot(recall, precision,'color',methods_colors(m,:),'linewidth',2);
    end
    axis([0 1 0 1]);
    %
    hold off
    grid on;
    % set(gca,'lineWidth',2)
    legend(methods, 'Location', 'SouthWest');
    xlabel('Recall','fontsize',12);
    ylabel('Precision','fontsize',12);
    end
