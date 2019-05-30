获取透明售房网的数据

http://www.tmsf.com/index.jsp

git下载和使用

yum install git -y

git config --global user.name "wzl"

git config --global user.email "921756080@qq.com"

ssh-keygen -t rsa -C "921756080@qq.com"

cat ~/.ssh/id.pub把公钥复制到github setting sshkey

git init

git remote add origin10 git@github.com:wzlsgit/house.git

git push -u origin10 master

#docker build -t 'flaskip' .

windows客户端提交

git add .

git commit -m "增加realip和demo文档修改"

git push
