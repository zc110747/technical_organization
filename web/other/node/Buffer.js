//支持编码格式
//ascii   --- ASCII
//utf8    --- UTF-8
//base64  --- Base64
//hex     --- 2字节编码的16进制字符串
//ucs2/utf16le    --- 2或4字节的小字节序编码的Unicode字符
//latin1/binary  --- 一字节编码的字符串的方式

//node强制buffer初始化指令 --zero-fill-buffers
//new Buffer被废弃，由buffer.from, buffer.alloc, buffer.allocUnsafe替代
let Buffer_old = function(){
    var buf = new Buffer("hello world!", "ascii");
    console.log(buf, buf.length);

    //slice共享缓存区, 父/子缓存区修改会影响到对方
    var small = buf.slice(0, 5);
    buf[0] = 0x30;
    console.log("f-change:", buf, small);
    small[0] = 0x31;
    console.log("c-change:", buf, small);

    //copy复制缓存区 
    //通过缓存区创建，缓存区可能为随机值而不是0
    var cpy = new Buffer(5); 
    console.log(cpy);   
    buf.copy(cpy, 0, 6, 11);
    console.log(cpy, cpy.toString());
}

//Buffer_old();

//Buffer新实现参考类实现
//Buffer.alloc(size, fill, endcoding);
//fill string|buffer|integer
let Buffer_new = function(){
    //const是定义指向的内存地址不会变化
    const buf1 = Buffer.alloc(5, 'a');
    const buf2 = Buffer.alloc(11, "aGVsbG8gd29ybGQ=", 'base64')
    buf1[0] = 0x62;
    console.log("alloc: ", buf1, buf2, buf2.toString(), Buffer.isBuffer(buf1));
    
    //allocUnsafe具有更高的效率，这是因为size小于等于Buffer.poolSize/2时，会使用内部快速预分配缓存池
    //而Buffer.alloc不会使用
    //Buffer.allocUnsafeSlow(size); 分配大小为size的无填充buffer
    const buf3 = Buffer.allocUnsafe(5).fill(0);
    console.log(Buffer.poolSize, buf3);
    
    let length1 = Buffer.byteLength("aGVsbG8gd29ybGQ=", 'base64');
    let length2 = Buffer.byteLength("start", "ascii")
    console.log("byte-length: ", length1, length2);
    
    //Buffer.from 
    //arrayBuffer, offset, length | string | array
    
    //TypedArray或者ArrayBuffer的.buffer属性，此时共享内存
    const arr = new Uint16Array(2);
    arr[0] = 1000;
    arr[1] = 2000;
    const buf4 = Buffer.from(arr.buffer, 0, 2); 
    console.log("from arr.buffer: ",arr, buf4);
    arr[0] = 50;
    console.log("from arr.buffer: ",arr, buf4);
    
    //compare targer>source ---- 1 其它相反
    const buf5 = Buffer.from('2324', 'ascii');
    const buf6 = Buffer.from([0x31, 0x32, 0x33, 0x35, 0x35]);
    const arr1 = [buf4, buf5, buf6];
    console.log("compare", arr1, arr1.sort(Buffer.compare), buf5.compare(buf6, 0, 3, 0, 3));
    const buf7 = Buffer.from(buf5);
    buf5[0] = 0x31;                  //拷贝，指向不同内存地址
    console.log("from: ", buf5.toString(), buf7.toString(), Buffer.isEncoding('ascii'));
    
    //concat 连接buffer流, 
    //list, length 无长度会便利数组累加获得
    //Buf.length 返回buffer块的实际长度, 而不是反应已用或者可用的内存量
    let len = buf4.length + buf5.length + buf6.length;
    const buf8 = Buffer.concat([buf4, buf5, buf6], len);
    console.log("concat:", buf8);
    
    //entries 创建[index, byte]格式的迭代器
    //keys 创建index的迭代器
    //values 创建结果的迭代器
    for(const pair of buf8.entries()){
        console.log(pair);
    }
    for(const key of buf8.keys()){
        console.log(key ,buf8[key]);
    }
    for(const value of buf8.values()){
        console.log(value);
    }
    //equals 比较相等 true/false
    //indexOf 查询满足条件字符串的首位 string/buffer/integer, byteOffser ,encoding, 无则返回-1
    //lastIndexOf 返回最后一次出现的索引
    //includes 返回型,相当于 buf.indexOf() !== -1
    const buf9 = Buffer.from('31333234', 'hex');
    console.log(buf5, buf9, buf5.equals(buf9), buf9.indexOf('3332', 'hex'), buf9.indexOf('32'), buf9.lastIndexOf('32'));

    //readDoubleBE 读取一个64位双精度值(返回大位数或者小位数)
    //readInt32BE 读取一个32位的有符号整数
    //readIntBe   读取指定长度的整数
    //offset，noAssert：起始地址，是否检查报错
    const buf10 = Buffer.from([1,2,3,4,5,6,7,8]);
    console.log(buf10, buf10.readDoubleBE(), buf10.readDoubleLE(), 
                buf10.readFloatBE(1), buf10.readFloatLE(),
                buf10.readInt16BE(0).toString(16), buf10.readInt16LE(),
                buf10.readInt32BE(0).toString(16), buf10.readInt32LE(),
                buf10.readIntBE(0, 4).toString(16),  buf10.readIntLE(0, 4, true).toString(16),
                buf10.readUInt8(0).toString(16),
                buf10.readUInt16BE(0).toString(16), buf10.readUInt16LE(),
                buf10.readUInt32BE(0).toString(16), buf10.readUInt32LE(),
                buf10.readUIntBE(0, 4).toString(16), buf10.readUIntLE(0, 4)
                );
    
    //write, writeDoubleBE, WriteDoubelLe.....与read类似
    buf10.write('write', 0 ,5, 'utf8');
    console.log('write: ',buf10);
    
    //swap16 以字节交换字节串内数据，主要用于大小端切换， buf.length必须是2的倍数
    //swap32， swap64同上
    const buf11 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
    buf11.swap16();
    console.log(buf11);
    buf11.swap32();
    console.log(buf11);
    buf11.swap64();
    console.log(buf11);
    
    const json = JSON.stringify(buf11);
    console.log(json);
    const copy = JSON.parse(json, (key, value)=>{
        return value && value.type === 'Buffer'? Buffer.from(value.data):value;
    });
    console.log(copy);
    
    const buffer = require('buffer');
    //buffer.INSPECT_MAX_BYTES buf.inspect返回最大字节, 不在Buffer上，在引入的buffer模块上
    //buffer.kMaxLength 分配给单个实例的最大内存(32位1GB, 64位2GB)
    console.log(buffer.INSPECT_MAX_BYTES, buffer.kMaxLength)
}

//Buffer_new();

module.exports.Buffer_old = Buffer_old;
module.exports.Buffer_new = Buffer_new;