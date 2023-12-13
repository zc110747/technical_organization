(function(context){
//多对象杂糅 source无数量限制
//[].slice.call或Array.protype.call 将对象转为数组
function mix(target, source){ //最后参数如果为bool型，由此决定是否覆写 false不覆盖 true覆盖
    var args = [].slice.call(arguments), i=1, key, 
        ride = typeof args[args.length-1] == "boolean"?args.pop():true;
    if(args.length === 1){
        target = !(this.widow) ? this : {};
    }
    while((source = args[i++])){
        for(key in source){
            if(ride || !(key in target)){   //用于处理相同对象是否覆盖
                target[key] = source[key];
            }
        }
    }
    return target;
}

var device = {
    ID: 12,
    main_port: 80,
};

var ex_device = {
    ID: 16,
    distance: 10,
    slave_port: 20,
};

mix(ex_device, device); 
console.log(ex_device);

//ES6支持块级作用域 函数本身的作用域，在其所在的块级作用域之内
//而ES6中，不管会不会进入if代码块，其内部声明的函数皆不会影响到作用域的外部
function func() { console.log('I am outside!'); }
(function () {
  if(true) { //声明为false时，出错
    // 重复声明一次函数f
    function func() { console.log('I am inside!'); }
  }

  func();
}());

func();

const PI = 3;

//对于对象和数组,const仅限制地址，不限制其内容
const foo = {data:2015};
foo.data = 2016;
console.log(foo);             //{data:2016} 定义只限制地址，内容可修改

//深度冻结 不允许添加属性和变量
var constantize = (obj) => {
  Object.freeze(obj);
  Object.keys(obj).forEach( (key, value) => {
    if ( typeof obj[key] === 'object' ) {
      constantize( obj[key] );
    }
  });
};

constantize(foo);
foo.data = 2017;
foo.time = 11;
console.log(foo);           //{data:2016} 常规模式下修改不起作用   

const fre = Object.freeze({data:2015});
fre.data = 2016;
delete fre.data;
console.log(fre);           //{data:2015} 常规模式下修改不起作用

const arr = [];
arr[0] = 10;
arr[1] = 12;
console.log(arr);           //[10, 12]

//ES6允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构
var [a, b, c] = [1, 2, 3];
console.log(a+''+b+''+c);   //123

var [x,,z] = [1, 2, 3];
console.log(x+''+z);        //13

var [head, ...tail] = [1, 2, 3, 4];
console.log(head);        //1
console.log(tail);        //[2, 3, 4]

var [x,y,z = 0] = [1, 2];
console.log(x+''+y+''+z); //120

//对象的属性没有次序，变量必须与属性同名，才能取到正确的值
var {bar, feo} = { feo: "aaa", bar: "bbb" };
console.log(feo) // "aaa"
console.log(bar) // "bbb"

console.log("\u0030");
console.log("\uD842\uDFB7");
console.log("\u{20BB7}");


var e = context.getElementsByTagName("div");
var s = '𠮷a';
console.log(s.codePointAt(0)); // 134071
console.log(s.codePointAt(1)); // 57271

console.log(s.charCodeAt(2));  // 97

}(document));

//.map处理Array数组
var arr = new Array(10);
var index = 0;
var roots = arr.push(index).map(function(value){
    index++;
})