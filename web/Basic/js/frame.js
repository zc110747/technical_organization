
//IIFE 立刻调用函数表达式
(function(){

    //了解this关键字, apply方法，array的slice用法, 
    //splice插入和删除
/*    var log = {
        index: 0,
        fn: function(){
            this.index++;
            //var arr = Array.prototype.slice.apply(arguments);
            //arr.splice(0, 0, this.index, ":");
            //console.log.apply(console, arr);
            console.log.call(null, this.index, ":",  [].slice.apply(arguments));
        }
    };*/

    var log = function(){
        var index = 0;
        return function(){
            console.log.call(null, index++, ":",  [].slice.apply(arguments));
        }
    }();


    //URL通过正则匹配生成唯一字符串
    var namespace = document.URL.replace(/(#.+|\W)/g, '');
    log(namespace);


    log(typeof null, 
        typeof document.childNodes, 
        typeof document.createElement('embed'),
        typeof document.createElement('object'), 
        typeof document.createElement('applet'), 
        typeof /\d/i,
        typeof window.alert
        )

    var arr = new Array(1, 2, 3);
    log(arr instanceof Array, 
    arr.constructor == Array);  //true true
    
    log(window.constructor, 
        document.constructor, 
        document.body.constructor
        //(new ActiveXobject('Microsoft.XMLHTTP').constructor)  //IE6789 undefined
    );

    (function(){
        Array.prototype.push.call(arguments, 4);
        log(arguments);
    })(1, 2, 3);

    (function(){
        var max = Math.max.apply(null, arguments);
        log(max);
    })(2, 20, 100, 16, 25);

    (function(){
        "use strict"
        var a = window.b = 5;
    })();
    log(b);

    //添加方法
    String.prototype.repeatify = String.prototype.repeatify || function(n){
            var str = "";
            for(var i=0; i<n; i++){
                str += this;
            }
            return str;
    }
    log('hello'.repeatify(3));

    //变量和函数提升
    (function test(){
        log(a, foo()); //udefined 2

        var a = 1;
        function foo(){
            return 2;
        }
    })();   

    window.fullname = 'John Doe';
    var obj = {
        fullname: 'Colin Inrig',
        prop:{
            fullname: 'Aurelio De Rosa',
            getFullname:function(){
                return this.fullname;
            }
        }
    };
    var test = obj.prop.getFullname;
    log(obj.prop.getFullname(), test(), test.call(obj.prop));

    
    //[].forEach.call($$("*"),function(a){a.style.outline="1px solid #"+(~~(Math.random()*(1<<24))).toString(16);});
    var b = -1231;
    log(~~b);

    var arr = [], arr2 = [], arr3 = [];

        //正常写法
    for (var i=0; i<10; i++) {
        arr[i] = function () {
            console.log(i);
        }
    }//结束i=10， console.log(i), i绑定到当前值
    arr[4](); 

    for(var i=0; i<10; i++){
        arr2[i] = function(num){
            return function(){
                console.log(num)
            }
        }(i)
    }
    arr2[5]();

})();