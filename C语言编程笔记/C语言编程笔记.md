

[菜鸟教程 - 学的不仅是技术，更是梦想！ (runoob.com)](https://www.runoob.com/)

[菜鸟教程在线编辑器 (runoob.com)](https://www.runoob.com/try/runcode.php?filename=helloworld&type=c)

C程序设计_谭浩强 清华大社

CPrimer_Plus.6[Zh]_人邮社



# C语言开发环境配置

## 编辑器

用VSCode来创建代码文件

安装扩展：

​    (1) C/C++    (功能：IntelliSense 智能提示、debugging 调试、 code browsing 代码浏览)

​    (2) cmake (选装)

​    (3) cmake tools (选装)



## 编译器

用来将代码文件生成计算机可执行的二进制文件

最常用的免费可用的编译器是 GNU 的 gcc 编译器适合于 C/C++ 编程语言。

Windows 上的安装 **MinGW-w64**

* 下载地址:  https://sourceforge.net/projects/mingw-w64/files/

  下载：x86_64-posix-sjlj

* 解压缩到相应的目录，添加D:\_Tool_\C\MinGW-w64\bin 目录到系统环境变量中 **PATH** 

验证gcc：Win+R，输入cmd，确认，输入"gcc -v"，回车，弹出"gcc version"信息，表示安装成功



## 其他程序

**cmake**

用来生成构建系统的工具，从而可以使用不同的编译器和工具链

下载地址：[Download CMake](https://cmake.org/download/)

下载：Binary distributions : Windows x64 ZIP



## 编码方式 Encoding

UTF-8 : 国际通用 (推荐使用)

Chinese BIG5 (Traditional) : 中文繁体

Chinese GB2312 (Simplified) : 中文简体



## VS Code 配置C/C++ 多文件编译和调试 (手动)

安装VS Code 、MinGW-w64、安装扩展C/C++    (以c_cpp_Template模板项目为例)

1、生成源代码

​    在工程文件夹下，创建一个包含所有函数的mian.c文件

2、编译不带调试信息

​    在“终端——新建终端”，输入编译“gcc .\main.c -o project”，输入运行“.\project.exe”，输入查看大小“ls”

3、模块化编程

​    再将main.c中的功能函数模块化为不同的.c、.h文件

4、编译带调试信息

​    在“终端——新建终端”，输入编译且包含调试信息“gcc -g .\main.c .\add.c -o project”，输入运行“.\project.exe”，输入查看大小“ls”

​    gcc “.c文件”    编译

​    gcc -g “.c文件”    编译且包含调试信息

​    gcc -o “项目名称”    编译产生的可执行程序文件重命名

​    ls    查看项目目录下的文件的信息  (模式、最后写入时间、大小、名称)

​    .\\"项目名称.exe"    运行可执行程序文件

5、调试

​    点击左侧“调试和运行”，选择“创建launch.json文件”，选择调试器“C++ (GDB/LLDB)”，选择“添加配置”，选择“C/C++：(gdb)启动”

配置"configurations":下的

​    (1)"program":    “输入程序名称，例如\${}”  改为  "${workspaceFolder}\\Project.exe",

​        表示调试的可执行程序的名称

​    (2)"miDebuggerPath":    “/path/to/gdb”  改为  "D:\\\_Tool_\\C\\MinGW-w64\\bin\\gdb.exe",

​        表示调试的目录

​    (3)"preLaunchTask": "C/C++: gcc.exe 生成活动文件"

​        表示调试前进行的操作指令

​        因此时多文件编译是在终端手动调用gcc命令，没有用到"preLaunchTask"自动进行，所以需要注释掉，在命令行前加“//”或者Ctrl+Shift

Ctrl+S 保存配置

​    在代码行前新增断点，选择“逐过程、单步调试、单步跳出”等验证



## VS Code 配置C/C++ 多文件编译和调试 (自动)

安装VS Code 、MinGW-w64、安装扩展C/C++    (以c_cpp_gcc_Template模板项目为例)

1、生成源代码

   新建项目文件夹、main.c文件、其他的.c.h文件

2、配置“.vscode”文件夹

​    选择.c 文件，“Ctrl+Shift+P”，在 > 后输入 "C/C++"，选择 "C/C++：编辑配置(UI)"    (若没有此选项，可从新安装低版本的C/C++扩展)

​    在“C/C++配置”中设置：

​        (1)配置名称：添加配置c、cpp

​        (2)编译器路径：

​                c语言：D:\_Tool_\C\MinGW-w64\bin\gcc.exe

​                c++语言：D:/\_Tool_/C/MinGW-w64/bin/g++.exe

​        (3)IntelliSense 模式：选择gcc-x64 (legacy)

​    编译器路径、IntelliSense 模式需要设置在对应的配置名称下

​    关闭“C/C++配置”界面

​    VScode资源管理器中项目树中新增了“.vscode文件夹”

​        其中“c_cpp_properties.json”就是“C/C++配置”设置参数

3、配置“tasks.json”文件，用于调试前的操作

​    选择.c 文件，选择“终端——配置任务”

​         c语言：选择“C/C++：gcc.exe生成活动文件”

​        c++语言：选择“C/C++：g++.exe生成活动文件”

​        在“.vscode文件夹”中新增了“tasks.json”

​        (1)c语言：将 "-g", 后面的 "\${file}", 改为 "${workspaceFolder}\\\\*.c", 

​            c++语言：将 "-g", 后面的 "\${file}", 改为 "${workspaceFolder}\\\\*.cpp", 

​            表示编译当前工作目录下的所有.c文件或者.cpp文件

​        (2)将 "-o", 后面的 "\${fileDirname}\\\\​\${fileBasenameNoExtension}.exe" 改为 "${workspaceFolder}\\\Objects\\\Project.exe" 

​            表示将编译产生的程序文件Project.exe存储在工作目录下的Objects文件夹

​        Ctrl+S 保存配置

4、编译main.c文件

​    选择main.c文件，选择“终端——运行生成任务”

​    若是c语言就选择“C/C++：gcc.exe构建和调试活动文件”

​    若是c++语言就选择“C/C++：g++.exe构建和调试活动文件”

​    显示“生成已成功完成”

​    点击右下方的+旁边的向下符号，选择“PowerShell”启动“终端”，在“PS E:\0.Project\c_cpp_Template>”后输入“.\Objects\Project.exe”(可使用TAB键补全)，回车，得到结果

​    或者点击右上角的“Run C/C++ File”，可直接在“终端”显示结果

5、调试

点击左侧“调试和运行”，选择“创建launch.json文件”，选择调试器“C++ (GDB/LLDB)”，选择“添加配置”，选择“C/C++：(gdb)启动”

配置"configurations":下的

​    (1)"program":    “输入程序名称，例如\${}”  改为  "${workspaceFolder}\\Objects\\Project.exe",

​        表示调试的可执行程序的名称

​    (2)"miDebuggerPath":    “/path/to/gdb”  改为  "D:\\_Tool_\\C\\MinGW-w64\\bin\\gdb.exe",

​        表示调试的目录

​    (3)"preLaunchTask": "C/C++: gcc.exe 生成活动文件"

​        表示调试前进行的操作指令

​    Ctrl+S 保存配置

​    在代码行前新增断点，选择“逐过程、单步调试、单步跳出”等验证



## VS Code 配置C/C++ 多文件编译和调试 (cmake)

安装VS Code 、MinGW-w64、cmake、安装扩展C/C++、扩展cmake、扩展cmake tools    (以c_cpp_cmake_Template模板项目为例)

1、生成源代码

   新建项目文件夹、main.c文件、其他的.c.h文件    (以c_cpp_gcc_Template模板项目为例)

2、创建CMakeLists.txt

​    在项目树空白处双击，建立新文件，命名为“CMakeLists.txt”，输入以下代码

    cmake_minimum_required(VERSION 3.10)  # Adjust the version as needed
    
    project(Project)  #定义项目的名称
    
    add_executable(Project main.c add.c)  #定义项目，以及编译的源文件（用空格隔开）
​    配置cmake：“Ctrl+Shift+P”，在 > 后输入 "CMake:Configuer"，选择编译器 "GCC 8.1.0"

在“终端”中输入“cd .\build”  表示进入当前项目的build路径下

在“终端”中输入“cmake ..”  验证cmake架构是否正常

​    —— Configuer done

​    —— Generating done

​    —— Build files have been writen to:    出现以上三条提示表示cmake架构创建正常

当将项目的目录发生变化时，需先删除build文件夹，重新配置cmake：“Ctrl+Shift+P”......



当不采用系统生成“build”目录，而是自己生成时，(先删除系统生成的“build”目录)

在“终端”中输入“cd ..”    表示进入当前目录

在“终端”中输入“mkdir build”    表示创建“build”文件夹

在“终端”中输入“cd build”    表示进入当前项目的build路径下

在“终端”中输入“cmake ..”     验证cmake架构是否正常

​    当Check for working CXX compiler：... CL.EXE，表示调用了微软MSVC编译器 (安装了VS时)

​    此时使用“ cmake -G “MinGW Makefiles” .. ”代替“ cmake .. ” 即可 (仅第一次时使用，后面仍可用“ cmake .. ”)

​    使用前需先清除“ cmake .. ”创建的build目录，使用 "rm *"，选择 A全是，输入“ls”，确认build文件被清除

​    此时Check for working CXX compiler：... gcc.exe，表示调用了gcc编译器

3、编译

在“终端”中输入“make”  (Linux)  ;  “mingw32-make.exe”  (Windows)

​    编译并链接add_executable()函数定义的文件，在buil目录下生成最终的编译后的可执行文件

4、调试

点击左侧“调试和运行”，选择“创建launch.json文件”，选择调试器“C++ (GDB/LLDB)”，选择“添加配置”，选择“C/C++：(gdb)启动”

配置"configurations":下的

​    (1)"program":    “输入程序名称，例如\${}”  改为  "${workspaceFolder}\\build\\Project.exe",

​        表示调试的可执行程序的名称

​    (2)"miDebuggerPath":    “/path/to/gdb”  改为  "D:\\\_Tool_\\C\\MinGW-w64\\bin\\gdb.exe",

​        表示调试的目录

​    (3)"preLaunchTask": "C/C++: gcc.exe 生成活动文件"

​        表示调试前进行的操作指令

​        因此时多文件编译是在终端手动调用cmake命令，没有用到"preLaunchTask"自动进行，所以需要注释掉

​    Ctrl+S 保存配置

​    在代码行前新增断点，选择“逐过程、单步调试、单步跳出”等验证

5、配置“tasks.json”文件，用于调试前的操作

​    “Ctrl+Shift+P”，在 > 后输入配置任务 "Tasks:Configuer Task"，选择“Create tasks.json file from template”

​    或者将“launch.json文件”中的"preLaunchTask": "C/C++: gcc.exe 生成活动文件"后面部分改动一下，比如删除“文件”

​    选择main.c，按F5启动调试，选择配置任务“Configuer Task”，选择“C/C++: gcc.exe 生成活动文件”，生成的是单文件调试的tasks.json

​    若使用gcc命令编译调试，可参考c_cpp_gcc_Template模板项目

将cmakelists的过程写入“tasks.json”文件，并将最终的操作"Build"名称，写到“launch.json文件”的"preLaunchTask":后

当执行调试“launch”时，首先执行"preLaunchTask"，即“tasks.json”文件中的操作



参考：

1、【基于VSCode的C/C++环境搭建，多文件编译，CMake，json调试配置 | Windows篇】 https://www.bilibili.com/video/BV13K411M78v/?share_source=copy_web&vd_source=86b5f625abf15dd7c7c74bfc5efc38d5

2、【VS Code 配置C/C++多文件编译和调试（初学一劳永逸版）】 https://www.bilibili.com/video/BV1SF411m7Tc/?share_source=copy_web&vd_source=86b5f625abf15dd7c7c74bfc5efc38d5