# 使用Dockerfile构建一个属于自己镜像

## Dockerfile
```
FROM ubuntu:latest

MAINTAINER atlantisfox

RUN apt-get update && \
    apt-get -y upgrade && \
    mkdir -p /home && \
    mkdir -p /home/atlantisfox && \
    mkdir -p /home/atlantisfox/downloads && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install aria2 && \
    apt-get -y install curl unzip busybox

RUN cd /home/atlantisfox/ && \
    curl -L https://github.com/ziahamza/webui-aria2/archive/master.zip > master.zip && \
    unzip master.zip

ADD aria2.conf /home/atlantisfox/aria2.conf

RUN echo

WORKDIR /home/atlantisfox
VOLUME ["/home/atlantisfox/downloads"]
EXPOSE 6800 6801

ENTRYPOINT busybox httpd -p 6801 -h /home/atlantisfox/webui-aria2-master && aria2c --conf-path=/home/atlantisfox/aria2.conf
```

## aria2.conf

```
# 用户名
rpc-user=username
# 密码
rpc-passwd=password

# 允许rpc
enable-rpc=true
# 允许所有来源, web界面跨域权限需要
rpc-allow-origin-all=true
# 允许外部访问，false的话只监听本地端口
rpc-listen-all=true
# RPC端口, 仅当默认端口被占用时修改
rpc-listen-port=6800
# 最大同时下载数(任务数), 路由建议值: 3
max-concurrent-downloads=5
# 断点续传
continue=true
# 同服务器连接数
max-connection-per-server=10
# 最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要
min-split-size=10M
# 单文件最大线程数, 路由建议值: 5
split=10
# 下载速度限制
max-overall-download-limit=0
# 单文件速度限制
max-download-limit=0
# 上传速度限制
max-overall-upload-limit=0
# 单文件速度限制
max-upload-limit=0
# 断开速度过慢的连接
#lowest-speed-limit=0

enable-http-pipelining=true

# 文件保存路径, 默认为当前启动位置
dir=/home/atlantisfox/downloads
# 文件缓存, 使用内置的文件缓存, 如果你不相信Linux内核文件缓存和磁盘内置缓存时使用, 需要1.16及以上版本
#disk-cache=0
# 另一种Linux文件缓存方式, 使用前确保您使用的内核支持此选项, 需要1.15及以上版本(?)
#enable-mmap=true
# 文件预分配, 能有效降低文件碎片, 提高磁盘性能. 缺点是预分配时间较长
#所需时间 none < falloc ? trunc « prealloc, falloc和trunc需要文件系统和内核支持
file-allocation=prealloc

# 日志等级
log-level=warn
```

## 构建镜像

构建指令如下

```
docker build -t atlantisfox/aria2 .
```

运行基于该镜像的容器

```
docker run -d -p 6800:6800 -p 6801:6801 -v /Users/binss/Downloads/aria2:/home/binss/downloads --name="aria2" binss/aria2
```