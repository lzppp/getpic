#coding=utf-8
import os,sys
import getpass
def copyFiles(sourceDir,targetDir):
	for files in os.listdir(sourceDir):
		sourceFile = os.path.join(sourceDir,files)   //把目录名和文件名链接起来
		targetFile = os.path.join(targetDir,files)
def rename():
	path=os.path.dirname(os.path.realpath(__file__))
	print path
	filelist = os.listdir(path)
	for files in filelist:
		Olddir=os.path.join(path,files);#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;
		filename=os.path.splitext(files)[0];#文件名
		filetype=os.path.splitext(files)[1];#文件扩展名
		if filetype!='.py':
			Newdir=os.path.join(path,filename+"jpg");#新的文件路径
			os.rename(Olddir,Newdir);#重命名
username = getpass.getuser()
copyFiles("C:\Users\\"+username+"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets",os.path.dirname(os.path.realpath(__file__)))
rename()
