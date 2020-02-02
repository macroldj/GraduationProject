#!/usr/bin/env bash
# 初始化部署环境
# CentOS 7.6 64位 镜像安装云主机(注意进行配置自己的密码)
# 0. 基础源配置

# 1. docker
yum install -y docker
systemctl daemon-reload
systemctl restart docker.service

# 2. git
# git 相关的配置请参考
yum install -y git
git config --global user.name "macroldj"
git config --global user.email "macroldj@163.com"
ssh-keygen -t rsa -C "macroldj@163.com"

#3. pip 安装y
yum install python3-pip - y
pip3 install --upgrade pip

#4. 安装docker-compose
pip3 install docker-compose

# 5. 创建必要目录
mkdir workspace

# shellcheck disable=SC2164
cd workspace
git clone git@github.com:macroldj/GraduationProject.git
# shellcheck disable=SC2164
cd GraduationProject
bash run.sh start