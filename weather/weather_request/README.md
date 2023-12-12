# 天气信息请求和转发
这是基于卡片linux环境下实现综合显示和应用系统，原理是从网络上下载天气信息和系统本身状态组合成json文件，然后提交到本地自建的mqtt服务器特定topic中，则其它订阅了这个topic的设备即可获取推送的json信息，将json信息转换成LVGL的图形显示，即可实现支持在各个环境下展示的系统组件，整个系统的实现包含如下组件。<br />
1. 基于mosquitto的服务器构建(本地环境自建)
2. 设备信息获取
3. 使用和风天气的API实现的天气信息获取，生成json最终数据
4. 关于mqtt的消息提交，发送到mosquitto中

## 1. 自建mqtt服务器应用
对于自建mqtt服务器，首先去官网下载linux编程包，地址: "https://mosquitto.org/download/", 选择mosquitto-2.0.18.tar.gz(后续可能会更新)，下载解压，执行如下命令编译。<br />
```bash
tar -xvf mosquitto-2.0.18.tar.gz
cd mosquitto-2.0.18
make -j4
make install
```
这里讲下编译时遇到的问题，以及解决办法。<br />
1. 提示找不到ssl相关的头文件，执行命令"sudo apt-get install libssl-dev"
2. 提示找不到cJson相关的头文件，需要到github上找到cJson的代码，下载地址:"https://github.com/DaveGamble/cJSON", 下载后在linux平台执行make&&make install执行编译安装。
如果install失败，可能是文件夹权限问题，需要make命令前加sudo，如sudo make install.安装成功后，执行命令**mosquitto -h**, 看命令是否正确执行，如果找不到，也可能是用户权限问题，需要在root权限下运行。<br />
上述执行完成后，可通过如下命令启动mqtt服务器。<br />
```bash
#生成用户配置文件，仅第一次启动执行
cp /etc/mosquitto/mosquitto.conf.example /etc/mosquitto/mosquitto.conf

#修改mosquitto.conf文件，后面会说明
vim /etc/mosquitto/mosquitto.conf

#启动mqtt服务
mosquitto -d -c /etc/mosquitto/mosquitto.conf
```
对于mqtt服务器来说，mosquitto.conf是配置文件，我们比较关注的配置项如下所示
```bash
# 指定是否能匿名登录，true是允许，false则需要指定登录的用户名和密码
# 这里因为只私有局域网实现，安全性设置成true也基本没风险
# 如果有公网映射，一定要设置成false，并指定用户名和密码
allow_anonymous true

#指定mqtt服务器工作的端口和ip地址，ip需要和本地ip一致，后续连接也会用到
listener 1883 192.168.16.52
```
如果成功启动mqtt后，且未报错，可用mqtt工具进行连接和测试，理论上此时已经能够正常工作。

## 2.获取设备信息
设备信息的获取在deive.py中基于类DeviceClass中实现，希望支持其它功能则可在此类中扩展相应的函数和变量, 执行6s的周期函数device_job, 将设备信息保存到全局变量system_info["os"]中。

## 3.基于和风天气获取天气信息
去和风天气官网"www.heweather.com"注册并实现账户，登录产品控制台可以看到自己的API信息，免费账户对于测试和我们的应用能够满足要求(六小时访问一次，理论满载一天请求8次)，这里假定完成了创建流程，已经拿到了认证key(Token),不过注意这个key需要注意保密，否则任何人都可直接使用，对于付费账户是会带来损失的。整个实现的脚本在bash_run.py中，对于天气的请求基于bash脚本实现，通过python调用此脚本执行，具体如下。<br />
1. 组合生成访问的网址:"https://devapi.qweather.com/v7/weather/now?location={0}&key={1}", location和key分别对应城市的位置和上面提到的token。
2. 通过curl命令，请求天气信息，保存成json文件。
3. 读取json文件，将需要的天气信息保存到全局变量system_info["weater"]中.

## 4.系统消息提交
系统消息的接口在mqtt_publish.py中实现，主要包含连接mqtt服务器，将转换好的json字符串，通过mqtt的指定topic发送提交，此时订阅指定topic上的数据都可以收到这个json数据，对于接收端就可以实现UI展示的处理，这一类在weather_show中实现。<br />








