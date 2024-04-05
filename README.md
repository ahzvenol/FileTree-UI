## FileTree-UI

### 项目功能
记录文件的名称(包括扩展名),创建时间,修改时间,大小这些基本信息

适合想要回忆自己曾经的文件都有什么的时候使用

### 使用软件
需要Python环境,node环境

克隆本仓库到本地

将py脚本放置在需要记录的目录下然后运行,这会生成一个`FileTree.json`文件

`FileTree.py`不会跳过任何东西,`FileTree_JumpSelf.py`会跳过记录脚本自己和Windows系统下自动生成的desktop.ini

`FileTree_JumpSelf_FP.py`是`FileTree_JumpSelf.py`的函数式版本,在Python中效率较低,仅一并发出,不建议使用

在本仓库根目录下运行`npm i`,之后运行`npm run serve --  --port 8888`启动Vue项目

在浏览器中访问` http://localhost:8888`,在可视化界面下将`FileTree.json`拖入指示的文件框

完毕,查看你的文件树!

### 作者的自言自语
很久以前写的项目了,后端部分算是我的代码入门,最初版本是java的,不过现在也经过层层重写了