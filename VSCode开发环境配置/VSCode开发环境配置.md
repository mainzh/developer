# VSCode开发环境配置



**VSCode**是一个**文本编译器**，配合**扩展**，可以方便的编辑代码



下载地址：[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)



安装勾选上    “通过Code打开”操作添加到......上下文菜单



安装扩展：

1. **Chinese(简体中文)**
2. Wisen-Translate (选装)：鼠标悬浮翻译
3. Prettier - Code formatter (选装)：格式化代码



VSCode设置：

​    `文件——首选项——设置`

1. `常用设置——自动保存：onFocusChange`
2. `搜索设置：format on：勾选format on paste、format on save`
3. `搜索设置：default formatter：选择Prettier - Code formatter`



VSCode 常用快捷键：

1、Ctrl+D：选择字符后，按 Ctrl+D，可同时选择下一个相同的字符，进行同时编辑

2、按住 alt 再按左键，可添加多个光标，进行多个位置同时编辑

3、alt+shift+上或下键，快速将该行代码复制到上一行或者下一行

4、Ctrl+F，查找替换

5、全局搜索，点击左侧搜索按钮，可以在打开的工作区搜索



---



# Git 版本控制配置



下载地址：[Git - 下载软件包 - Git 版本控制系统](https://git-scm.cn/downloads/win)



安装时：

Use Visual Studio Code as Git's default editor

adjusting the name of the initial branch in new repositories

选择 Override the default branch name for new repositories (main)



安装 Git 后，应该做的第一件事是设置 (GitHub) 用户名和电子邮件地址

https://git-scm.cn/book/en/v2/Getting-Started-First-Time-Git-Setup

    在终端中输入 GitHub 用户名、邮箱
    
        `git config --global user.name "John Doe"`
    
        `git config --global user.email johndoe@example.com`



使用`Steam++`加速 GitHub 后，使用 VSCode `源代码管理 推送` (`git`推送) 提示 SSL 证书错误的解决办法：

    点击`Steam++`加速设置--打开证书文件夹 (Steam++\AppData\Plugins\Accelerator) --复制 `SteamTools.Certificate.cer` 的文件地址
    
    在 `终端` 中输入 `git config --global "证书地址"`



替换使用`GitHub Desktop`来提交推送代码到`GitHub`上的方式

GitHub配置完Git后，可直接克隆、提交、推送GitHub仓库数据

