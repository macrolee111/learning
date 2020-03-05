cd ..:ls       
ls     列表
psw #显示路径

cd~#返回上层

mkdir#建立文件
mkdir  desktop/all_files/0001pic

mv#移动文件
mv desptop/all_files/1.png desptop/all_files/000pic

*.#全部批量操作

curl 'www.baidu.com' #打开网页
curl -l -o desktop/baidu.html 'www.baidu.com' #下载网页源文件

curl - l -o desktop/163.txt 'www.163.com'
cat desktop/163.txt #查看文件
less desktop/163.txt #一页一页看

touch #创造文件
rm #撤销文件 永久删除
rm -i #确认删除，

mkdir#创建文件夹
mrdir#删除文件夹

nano #记事本

grep#在某一个文件里面查找有什么东西
grep aaple  apple.txt
｜ #管道，回撤上面的一个，由要做另一个命令，
｜ less
wc #数字数

curl -l ’www.163.com' | grep -c sports

man    #查看说明

diff #比较
diff a b 

mkdir #建议一个文件架
#创立文件
git  init #创建了一个仓库
git commit #更新仓库
git add #添加文件
ls -a #查看完全的列表
#替换
git log#日志
git diff -- staged #暂缓区和版本的对比
git reset --hard # 返回上一层


