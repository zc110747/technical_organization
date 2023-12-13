
//replace+正则替换
var str="ww;ss;ss";
str = str.replace(/;/g, ";");
log(str);

//对象特点
var a = {n:1};
var b = a;
a.x = a = {n:2};
log(a, b);

function getBit(val,bit){
    /*1 return true; 0 return false*/
    return ((val & (0x1 << bit)) >> bit)==1;
}

function setBit(val,bit){
    return val | (0x1 << bit);
}

function clearBit(val,bit){
    var a=255;
    for(var i=0;i<=bit;i++){
        a=a<<1;
        if(i>0)a++;
    }
    return val & a;
}

function reverseBit(val,bit){
    if(getBit(val,bit)) 
        return clearBit(val,bit);
    else 
        return setBit(val,bit);
}

var mib_tbl = {
    mib25:  "00",
    mib84:  "c0a800a0c0a800a9c0a8"+
            "0001ffffff003bfc7f62"+
            "80d40000000002006375"+
            "31763100",
    mib63:  "00000000000000000000"+
            "00000000000000000000"+
            "000000000000000000"
};

var device_status = {
    LocalIpaddr:["192", "168", "0", "160"],
    RemoteIpaddr:["192", "168", "0", "169"],
    NetMask:["192", "168", "0", "1"],
    GateWay:["255", "255", "255", "0"],
    LocalMac:["3b", "fc", "7b", "62", "80", "d4"],
    RemoteMac:["00", "00", "00", "00", "00", "00"],
    FrameLength:"4",
    BuffDepth:"2",
    LocalPort:"30000",
    RemotePort:"30000",
};

var device_config = {
    LocalIpaddr:["192", "168", "0", "160"],
    RemoteIpaddr:["192", "168", "0", "169"],
    NetMask:["192", "168", "0", "1"],
    GateWay:["255", "255", "255", "0"],
    LocalMac:["3b", "fc", "7b", "62", "80", "d4"],
    BuffDepth:"14",
    FrameLength:"2",
    LocalPort:"30000",
    RemotePort:"30000",
    LocolReset:"0",
    RemoteReset:"0",
    SetStatus:[0xff, 0x01]
}

log(device_status.LocalIpaddr[0]);

function get_string(first, last)
{
    return parseInt(mib_tbl.mib84.substring(first, last), 16).toString(10);
}

function get_mib_process(mib){
    var i;
    switch(mib)
    {
        case 84:
            var str = mib_tbl.mib84;
            for(i=0; i<4; i++)
            {
                device_status.LocalIpaddr[i] = get_string(i*2, i*2+2);
                device_status.RemoteIpaddr[i] = get_string(i*2+8, i*2+10);
                device_status.NetMask[i] = get_string(i*2+16, i*2+18);
                device_status.GateWay[i] = get_string(i*2+24, i*2+26);
            }
    
            for(i=0; i<6; i++)
            {
                device_status.LocalMac[i] = str.substring(2*i+32, 2*i+34);
                device_status.RemoteMac[i] = str.substring(2*i+44, 2*i+46);
            }

            device_status.FrameLength = get_string(56, 57);
            device_status.BuffDepth = get_string(57, 58);
            device_status.LocalPort = get_string(58, 62);
            device_status.RemotePort = get_string(62, 66);
        break;
        default:
        break;
    }
}

function pad(str, n) {  
    var len = str.length;  
    while(len < n) {  
        str = "0" + str;  
        len++;  
    }  
    return str;  
}  

function IntToString(src, index)
{
    return pad(parseInt(src, 10).toString(16), index);
}

function set_mib_process(mib){
    switch(mib)
    {
        case 25:
            mib_tbl.mib25[0] = device_config.RemoteReset;
            mib_tbl.mib25[1] = device_config.LocalReset;
            break;
        case 63:
            var remove = '';
            var i;
            for(i=0; i<2; i++)
            {
                remove += IntToString(device_config.SetStatus[i], 2);
            }
            for(i=0; i<4; i++){
                remove += IntToString(device_config.LocalIpaddr[i], 2);
            }
            for(i=0; i<4; i++){
                remove += IntToString(device_config.RemoteIpaddr[i], 2);
            }
            for(i=0; i<4; i++){
                remove += IntToString(device_config.NetMask[i], 2);
            }
            for(i=0; i<4; i++){
                remove += IntToString(device_config.GateWay[i], 2);
            }
            remove += device_config.LocalMac.join('');
            remove += IntToString(device_config.BuffDepth, 1);
            remove += IntToString(device_config.FrameLength, 1);
            remove += IntToString(device_config.LocalPort, 4);
            remove += IntToString(device_config.RemotePort, 4);
            log(remove);
            mib_tbl.mib63 = remove;
            break;
        default:
        break;
    } 
}


set_mib_process(63);
log(mib_tbl.mib63);

var x='110';
var data = parseInt(x, 10).toString(16);
log(data);