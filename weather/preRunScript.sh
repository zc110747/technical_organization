echo "copy json file to all directory used!"
cp config.json.example weather_request/file/config.json
cp config.json.example weather_show/win_component/bin/Debug/net6.0-windows/config.json
cp config.json.example weather_show/node_component/config.json

if [ x$1 == x ]; then
    #python安装支持的运行库
    pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ schedule
    pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ paho-mqtt

    #bash安装工具
    sudo apt-get install curl

    #node安装支持库
    cd weather_show/node_component/
    npm install mqtt
    cd vue-manage-device/
    npm install
    cd ../../
else
    echo "not update script, if need, just use './preRunScript.sh' without parameter"
fi
