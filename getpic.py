#coding=utf-8
import shutil 
import os,sys
import getpass
def copyFiles(sourceDir,targetDir):
	for files in os.listdir(sourceDir):
		sourceFile = os.path.join(sourceDir,files)
		targetFile = os.path.join(targetDir,files)
		if os.path.isfile(sourceFile): 
                        open(targetFile, "wb").write(open(sourceFile, "rb").read())

def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，
    #如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def rename():
	path=cur_file_dir()
	filelist = os.listdir(path)
	for files in filelist:
		Olddir=os.path.join(path,files);#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;
		filename=os.path.splitext(files)[0];#文件名
		filetype=os.path.splitext(files)[1];#文件扩展名
		if filetype == '':
			Newdir=os.path.join(path,filename+".jpg");#新的文件路径
			os.rename(Olddir,Newdir);#重命名
username = getpass.getuser()
originpath ="C:\\Users\\"+username+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
print (originpath)
copyFiles(originpath ,cur_file_dir())
rename()
