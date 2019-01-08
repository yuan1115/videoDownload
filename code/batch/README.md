### 说在前面

为下载的的的的YouTube上的视频，所以你必须能够  科学上网            

#### 环境

* 安装python3+,安装包request,Pysocks,client,you-get,youtube-dl
* 安装you-get：pip3 install you-get
* 测试 you-get -s 127.0.0.1:1080 --debug -i 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
* youtube-dl安装：pip3 install youtube-dl
* 添加ffmpeg/bin到环境变量(以便自动合成音视频)
* 添加aria2c到环境变量（多线程加速下载工具）

#### 目录说明

* mp4 存放下载视频的目录
* vList.txt 存放视频地址，一行一个  
* class.txt 存放播放列表url，格式：'url;列表名称;视频总数;需要下载的格式（默认1080p，137表示1080，136表示720，135表示480的MP4格式）