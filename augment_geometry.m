function c=augment_geometry(dir,dir_GT,tempname,save_path,GTsave_path)
image=imread([dir,tempname,'.PNG']);
GT=imread([dir_GT,tempname,'.PNG']);

crop(image,GT,save_path,GTsave_path,tempname);
rotate(image,GT,90,save_path,GTsave_path,tempname);
rotate(image,GT,180,save_path,GTsave_path,tempname);
rotate(image,GT,270,save_path,GTsave_path,tempname);
flipp(image,GT,1,save_path,GTsave_path,tempname);
flipp(image,GT,2,save_path,GTsave_path,tempname);
c=1;

end



function crop(image,GT,save_path,GTsave_path,tempname)
[w,h,s]=size(image);
if w<h
    
    m=90;n=25;
    width=390;height=322;
    img1=imcrop(image,[m*9+1,n*9+1,(width+1)*9-1,(height+1)*9-1]);
    G1=imcrop(GT,[m+1,n+1,width,height]);
    imwrite(img1,[save_path,'/',tempname,'_crop1','.PNG']);
    imwrite(G1,[GTsave_path,'/',tempname,'_crop1','.PNG']);
	
    %% If crop the lens image array, please cancel the following two lines of comments
    m=50;n=30;
    img=imcrop(image,[m*9+1,n*9+1,(width+1)*9-1,(height+1)*9-1]);
    G=imcrop(GT,[m+1,n+1,width,height]);
	
	%% If crop the center view image,please cancel the following two lines of comments
	% img=imcrop(image,[m+1,n+1,width,height]);
    % G=imcrop(GT,[m+1,n+1,width,height]);
	
    imwrite(img,[save_path,'/',tempname,'_cr','.PNG']);
    imwrite(G,[GTsave_path,'/',tempname,'_cr','.PNG']);

else
    m=25;n=90;
    width=322;height=390;
    img1=imcrop(image,[m*9+1,n*9+1,(width+1)*9-1,(height+1)*9-1]);
    G1=imcrop(GT,[m+1,n+1,width,height]);
    imwrite(img1,[save_path,'/',tempname,'_crop1','.PNG']);
    imwrite(G1,[GTsave_path,'/',tempname,'_crop1','.PNG']);

    m=30;n=50;
	
	%% If crop the lens image array, please cancel the following two lines of comments
    img=imcrop(image,[m*9+1,n*9+1,(width+1)*9-1,(height+1)*9-1]);
    G=imcrop(GT,[m+1,n+1,width,height]);
	
    %% If crop the center view image,please cancel the following two lines of comments
    % img=imcrop(image,[m+1,n+1,width,height]);
    % G=imcrop(GT,[m+1,n+1,width,height]); 
	
    imwrite(img,[save_path,'/',tempname,'_cr','.PNG']);
    imwrite(G,[GTsave_path,'/',tempname,'_cr','.PNG']);

end


end
function rotate(image,GT,angle,save_path,GTsave_path,tempname)
img=imrotate(image,angle);
G=imrotate(GT,angle);
imwrite(img,[save_path,'/',tempname,'_',num2str(angle),'.PNG']);
imwrite(G,[GTsave_path,'/',tempname,'_',num2str(angle),'.PNG']);
end
function flipp(image,GT,num,save_path,GTsave_path,tempname)
img=flip(image,num);
G=flip(GT,num);
imwrite(img,[save_path,'/',tempname,'_',num2str(num),'.PNG']);
imwrite(G,[GTsave_path,'/',tempname,'_',num2str(num),'.PNG']);
end

