function  saliencymap
maindir='../result/result_99/1fold_result/pro';
subdirpath = fullfile( maindir, '*.mat' );
dat = dir( subdirpath );               
for j = 1:length( dat )
    datpath = fullfile( maindir, dat( j ).name);
    data=load(datpath);
    data=data.data;
    data=data(:,:,2);
    [~,tempFileName,~]=fileparts(datpath);
    FB=fliplr(data);
    TB=rot90(FB,1);
    TB=(TB-min(TB(:)))/(max(TB(:))-min(TB(:)));
    map=uint8(TB*255);
    c=strfind(tempFileName,'_blob');
    name=tempFileName(1:c-1);
    imwrite(map,['../result/result_99/1fold_result/salmap/',name,'.png']);
    display(num2str(j));
        
end
end

   

   
