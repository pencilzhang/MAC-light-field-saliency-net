function c=augment_addnoise(save_dir,save_GT)

Im_path = fullfile( save_dir,'*.PNG' );
Im_dat = dir( Im_path );

for i=1:length(Im_dat)
    [~,im_name,~]=fileparts(Im_dat(i).name);
    Img=imread(fullfile(save_dir,Im_dat(i).name));  
    GT=imread(fullfile(save_GT,Im_dat(i).name));
    img=imnoise(Img,'gaussian',0,0.01);
    imwrite(img,[save_dir,im_name,'_gau','.PNG']);
    imwrite(GT,[save_GT,im_name,'_gau','.PNG']);
             
end
c=3;
end