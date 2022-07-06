# 兰州大学 自动评教脚本

本脚本适用于**兰州大学 评教系统**。

测试于 **2021-2022学年第二学期期末评教**，有问题请提交 issue。

## 使用教程

1. 确保已安装 **`Google Chrome`** 网页浏览器

2. 安装 **`ChromeDriver`**

   [🔗下载链接](https://chromedriver.chromium.org/downloads)

   注意：先查看 Chrome 的版本 *(设置-关于 Chrome)*，再下载对应版本的 ChromeDriver！

   解压

   将 ChromeDriver 路径添加至系统环境变量*（或者后续将脚本也放于该解压目录下）*

3. 确保已安装并配置好 **`Python`**环境，同时 pip 工具可用。

4. 安装 **`selenium`** 库

   在终端下输入 

   ```shell
   pip install selenium
   ```

5. 下载脚本

   在终端下输入 

   ```shell
   git clone git@github.com:xietao02/LZU-Automated-Teaching-Evaluation.git
   ```

6. 修改脚本内容

   -  `Semi-automatic.py` 半自动脚本，进入评教系统过后，需自行打开问卷页面，再到终端中执行相应操作。
   -  `Fully_automatic.py` 全自动脚本，运行后无需操作。

   根据需要打开相应脚本，填入自己的账号信息*（邮箱只需要前缀即可）*。

   也可以自定义问题 <u>对课程最满意的是什么？</u> 和 <u>你认为还有哪些问题需要教师在今后教学中改进和提高的？</u> 的答案。

   ```python
   #-=-=-=-=-=-=-=-=-Preprocessing-=-=-=-=-=-=-=-=-=-
   # Education Email Prefix
   Account = "txie20"
   # Password  
   Password = ""
   # Satisfaction with the course
   Satisfaction = "课程很受用，老师的讲授很生动。"
   # Areas for improvement of the course
   Improvement = "无"
   #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
   ```

7. 运行脚本

   在终端下输入

   ```shell
   python Semi-automatic.py
   ```

   或者

   ```shell
   python Fully_automatic.py
   ```

## 注意事项

❗ **本脚本仅供学习交流目的，由于不当使用造成的一切后果，本人概不负责！**

1. **本脚本不会收集个人信息**。
2. 由于网络原因，全自动脚本可能会出现漏评，可以**重新启动** 或 使用**半自动脚本**解决。
3. 使用半自动脚本时，请在自行打开评教问卷后，再转至终端输入 `y`。完成后输入 `q` 即可结束。



