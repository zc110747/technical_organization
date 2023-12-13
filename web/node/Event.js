
const Event_process = function(){
    
    const EventEmitter = require("events");
    class MyEmitter extends EventEmitter{};
    
    //ES6 箭头函数 this/arguments指向父作用域
    const myEmitter = new MyEmitter(); 
    this.a = 10;
    
    //newListener注册监听器事件, 会在每个监听器注册时执行
    myEmitter.on('newListener', ()=>{
        console.log("new Listener");    
    });
    myEmitter.on('removeListener', ()=>{
        console.log("remove Listener");    
    });
    
    //emitter.on的别名
    myEmitter.addListener('event', (a)=>{ 
        console.log('event---事件触发!', a, this.a, global.a, arguments[0]);
    });
    
    //监听器异步执行
    //setImmediate 异步实现
    //listenerCount 返回监听块的统计 listeners 返回监听事件块的副本
    //EventEmitter.defaultMaxListeners 默认允许注册的最大事件
    //setMaxListeners/getMaxListeners 获得和设置允许注册的最大事件
    myEmitter.on('event', (a, b)=>{
       setImmediate(()=>{
         console.log("异步 %d, %d", a, b);
         console.log("lister count: ", myEmitter.listenerCount("event"), myEmitter.listeners("event"));
         console.log("default lister count: ", EventEmitter.defaultMaxListeners);
         myEmitter.setMaxListeners(myEmitter.getMaxListeners() + 1);
         console.log("getMaxListeners: ", myEmitter.getMaxListeners());
         
       }); 
    });
    
    //this指向事件实例
    //once --- 事件最多被调用一次, 触法时，先注销监听器, 再指向回调函数
    myEmitter.once('usr', function(){
        console.log('usr ---事件触发!', arguments[0], this);
    })
    
    
    myEmitter.on('error', (err)=>{
        setImmediate(()=>{
            console.log(err);
        });
    });
    
    //正常事件按照顺序添加
    //prependListener, prependOnceListener将事件插入到开头
    myEmitter.prependListener("event", ()=>{
        console.log("prependListener!");    
    });
    
    myEmitter.prependOnceListener("event", ()=>{
        console.log("Once PrependListener!");    
    });
    //emit同步调用注册的事件, 并执行
    myEmitter.emit('event', 1, 2);
    myEmitter.emit('usr', 1);
    myEmitter.emit('usr', 1);
    myEmitter.emit('error', new Error('whoops!'));
    
    //移除指定的eventName监听器
    myEmitter.removeAllListeners('event');
    
    //列出触发器已注册的事件数组
    console.log(myEmitter.eventNames()); 
    //removeListener和removeAllListeners在最后一个执行监听器执行完之前不会从emit中移除
    const callback = (stream)=>{
        console.log("回调");
    }
    myEmitter.on('event', callback);
    myEmitter.emit('event');
    myEmitter.removeListener('event', callback);
    console.log(myEmitter.eventNames());
    
    
    
}

Event_process(0);