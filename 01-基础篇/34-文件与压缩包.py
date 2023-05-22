# coding: utf-8
# @Author: 小飞有点东西

# shutil模块
import shutil

# 拷贝文件的状态信息,如:atime, mtime, ctime等,(只拷贝状态信息,b.txt必须存在)
shutil.copystat('data/a.txt', 'data/b.txt')

# 拷贝文件的权限(只拷贝a.txt的权限,b.txt必须存在)
shutil.copymode('data/a.txt', 'data/b.txt')

# 拷贝文件
shutil.copyfileobj(open('data/a.txt', 'r'), open('data/z.txt', 'w'))
shutil.copyfile('data/a.txt', 'data/z.txt')
shutil.copy('data/a.txt', 'data/z.txt')  # 拷贝文件以及权限
shutil.copy2('data/a.txt', 'data/z.txt')    # 拷贝文件以及状态信息

# 拷贝文件夹,ignore的意思是排除
shutil.copytree('data', 'data2', ignore=shutil.ignore_patterns('*.py', 'user*'))

# 移动文件/文件夹,如果移动的路径相同,只是名字不同,则相当于重命名
shutil.move('data', 'data1')

# 创建压缩包(压缩包种类，“zip”, “tar”, “bztar”，“gztar”)
shutil.make_archive("path", 'zip', root_dir='data')


# zipfile模块
import zipfile

# 压缩
zf = zipfile.ZipFile('path.zip', 'w')    # 创建一个压缩包
zf.write('data/a.txt')  # 需要加到压缩包的文件
zf.write('data/b.txt')  # 需要加到压缩包的文件
zf.close()   # 关闭压缩包

# 解压
zf = zipfile.ZipFile('path.zip', 'r')   # 打开一个压缩包
zf.extractall(path='test')  # 解压包内所有文件,并指定解压路径
zf.close()  # 关闭压缩包


# tarfile模块
import tarfile

# 压缩
tar = tarfile.open('path.tar', 'w')  # 创建一个压缩包
tar.add('data/a.txt', arcname='a.txt')  # 将文件添加到压缩包并命名
tar.add('data/b.txt', arcname='b1.txt')  # 将文件添加到压缩包并命名
tar.close()  # 关闭压缩包

# 解压
tar = tarfile.open('path.tar', 'r')  # 打开一个压缩包
tar.extractall(path='test')  # 解压包内所有文件,并指定解压路径
tar.close()  # 关闭压缩包
