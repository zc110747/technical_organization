var name = "Teny";
var someone = {
            name: "Bob",
            family: 0,

            information:{
                age : 15,
                work: "student",
                showInfo:function(){
                    log("age: "+someone.information.age, "work: "+someone.information.work);
                }
            },
            increment:function(inc){
                this.family += typeof inc == 'number'? inc:1;
            },
            showName:function(){
                        log(this.name);
                    }
};
var other = {
    name: "Tom",
    showName: someone.showName
};

other.showName();                       //Tom 此时this指向other

var show = someone.showName;
show();                                 //此时this指向全局对象window Teny

var theone = someone;
theone.name = "Candy";                  //修改属性内变量
theone.information.hobby = "music";     //对于非对象本身参数，会将该属性添加到对象中

theone.showName();                      //Candy 此时this指向someone
someone.showName();                     //Candy 对象不拷贝，只能引用
someone.information.showInfo();
log("hobby: "+someone.information.hobby, typeof someone.name, typeof someone.information.age);

if(someone.hasOwnProperty("name"))
{
    log("object has type name!");   //检查对象是否包含某属性
}

delete theone.name;                 //删除对象的某种属性，但是不会影响到原型
if(!someone.hasOwnProperty("name"))
{
    log("object delete type name!");
}

someone.increment(2);   //方法调用方式，this绑定指定对象someone
log(someone.family);      //值为2

var add = function(a, b){
    return (a+b);
};
someone.addfamily = function()
{
    that = this;
    var helper = function(){
            that.family = add(2,3);  //闭包调用
    };
    helper();                        //函数方式调用时，this被绑定到全局对象，则不会修改当前参数
}
someone.addfamily();
log(someone.family);


//新建一个构造器(了解即可，不建议使用)
var Quo = function(string)
{
    this.status = string;
}
//添加公共方法 get_status
Quo.prototype.get_status = function(){
    return this.status;
}
//构造一个Quo实例
var myQuo = new Quo('confused');
log(myQuo.get_status());

var tarray = [3, 4];
var sum = add.apply(null, tarray);
log(sum);

var statusobject = {
    status : 'Apply test'
};
var status = Quo.prototype.get_status.apply(statusobject);
log(status); //类似与引用，借用其它对象的方法，此时this指针绑定的是statusobject

//函数被调用时，会附送多余的参数arguments，因此无特定参数函数是允许的
var sum = function(){
    var i, sum = 0;
    for(i=0; i<arguments.length; i+=1)
    {
        sum+= arguments[i];
    }
    return sum;
}
log(sum(1,2,3,4));  //输出10

//对象添加方法
Function.prototype.method = function (name, func){
    if(!this.prototype[name])   //避免添加到已有的方法上面去，需要限定
    {
        this.prototype[name] = func;
        return this;
    }
}

Number.method('integer', function(){
    return Math[this<0? 'ceil' : 'floor'](this);
});
log((-10/3).integer() + "</br>");

String.method('trim', function(){
    return this.replace(/^\s+$/g, '');    //正则表达式去除空格
})
log("  trim test  ",  "-"+"trim test  ".trim()+";");

//函数作用域，处处可见
var myobject = function(){
    var value = 0;
    return {
        increment: function(inc){
            value += typeof inc === 'number'? inc:1;
            },
        getValue: function(){
             return value;
        }
    }
}();
myobject.increment(2);
log(myobject.getValue());

//js精粹集合
//包含原型继承, 类方法, 子类, 深度克隆
var s = "Study is not work, just everytime need!";
var last_word = s.substring(s.lastIndexOf(" ")+1, s.length);
log("last_word:"+last_word);

function InsertDataToLabal(id, data)
{
    var d =document.getElementById(id);
    d.innerHTML = d.innerHTML + "<br>" +data;
}

function Operator(a, b) {
    this.x = a;
    this.y = b;
}
Operator.prototype.plus = function Operator_plus(){
    return this.x + this.y;
}
Operator.prototype.minus = function Operator_minus(){
    return this.x - this.y;
}
Operator.prototype.plus = function Operator_plus(){
    return this.x * this.y;
}
Operator.prototype.div = function Operator_div(){
    return this.y != 0? this.x/this.y: alert("division error!");
}
Operator.compare = function Operator_compare(a, b){
    return a.plus > b.plu? a.x:b.x;
}
Operator.prototype.obj = {a:1};

//简单原型继承 Op1对象继承了Operator的公共方法
var Op1 = new Operator(1, 2);
var out = Op1.div();
log("简单继承:"+out)    // 1/2 = 0.5
var Op2 = new Operator(5, 1);

//类方法
out = Operator.compare(Op1, Op2);   //比较x-选择大的5
log("类方法:"+out);

function ExtraOperator(a, b){
    Operator.apply(this, arguments);
}

//临时构造函数实现原型和子类隔离
function F(a, b){

};
F.prototype = Operator.prototype;

//子类的继承
//ExtraOperator.prototype = new Operator();
//ExtraOperator.prototype = Operator.prototype;  //父类和子类共享原型, 此时修改子类原型会改变父类的继承原型。
ExtraOperator.prototype = new F();
ExtraOperator.prototype.constructor = ExtraOperator;
ExtraOperator.prototype.swap = function(){
    this.x = this.x + this.y;
    this.y = this.x - this.y;
    this.x = this.x - this.y;
}
ExtraOperator.selfadd = function()
{
    this.x++;
    this.y++;
}
log(ExtraOperator.hasOwnProperty('swap').toString(), ExtraOperator.hasOwnProperty('selfadd').toString());

var Op3 = new ExtraOperator(1, 2);
out= Op3.div();
log("子类继承:"+out);  //1/2 = 0.5

Op3.swap();
out = Op3.div();
log("子类方法:"+out, ExtraOperator.prototype.isPrototypeOf(Op3));

//共享原型时有效，采用new Operator时无效
//Op2.swap();
//var out5 = Op2.div();
var Person = {
    name: "bob",
    age : "18",
    address: {
        province:"beijing"
    },
    favorite: {
        reading:"English"
    }
}



var out1 = easy_clone(Person);
log("对象克隆:"+out1.address.province);                    //shang hai
out1.address.province = "shanghai";
log("浅度克隆原对象:"+Person.address.province);            //克隆变量和本体未隔离 shanghai

function easy_clone(obj)
{
    var result = {};
    for(var i in obj){
        result[i] = obj[i];
    }
    return result;
}

//判断是对象还是数组，避免克隆后导致结构变化(数组->对象 对象<-数组)
function isClass(obj){
    if(obj == null) return "NULL";
    if(obj == undefined) return "Undefined";
    return Object.prototype.toString.call(obj).slice(8, -1);
}

function deepClone(obj){
    var result;
    var objClass = isClass(obj);
    //确定result的类型
    if(objClass==="Object"){
        result={};
    }else if(objClass==="Array"){
        result=[];
    }else{
        return obj;
    }
    for(key in obj){
        var copy=obj[key];
        if(isClass(copy)=="Object"){
            result[key]=arguments.callee(copy);//递归调用
        }else if(isClass(copy)=="Array"){
            result[key]=arguments.callee(copy);
        }else{
            result[key]=obj[key];
        }
    }
    return result;
}

var out2 = deepClone(Person);
log("克隆对象:"+out2.address.province);
out2.address.province = "beijing";
log("克隆对象:"+out2.address.province, "深度克隆原对象:"+Person.address.province);
delete Person.name;
log("克隆对象:"+out2.name, "深度克隆原对象:"+Person.name);

//递归实现渐变色
var fade = function(color, node, time){
var level = 1;
var status = 0;
var n_id = document.getElementById(node);
var step = function(){
    var hex = level.toString(16);
    n_id.style.backgroundColor = color + hex + hex;
    if(status == 0){
        level += 1;
        if(level == 15)
        {
            status = 1;
        }
    }
    if(status == 1){
        level -= 1;
        if(level == 0)
        {
            status = 0;
        }
    }
    setTimeout(step, time);
};
    setTimeout(step, time);
};

log("原型对象:"+Operator.prototype.obj.a);
ExtraOperator.prototype.obj.a = 2;
log("原型对象:"+Operator.prototype.obj.a);  //此时子类修改了父类的属性

function Alone_Operator(a, b){

}
Alone_Operator.prototype = deepClone(Operator.prototype);
Alone_Operator.prototype.a = 3;
log("原型对象:"+Operator.prototype.obj.a);  //采用深度复制，未修改父类属性

//闭包实例
var quote = function(status){
    return {
        get_status:function(){
        return status;
        }
    };
};
var myquo = quote("amazed");
log(myquo.get_status());

//用构造函数定义方法
function Operator_add() {return this.begin + this.after;}
function Operator_minus() {return this.begin - this.after;}
function Operator_plus() {return this.begin * this.after;}
function Operator_div() {return this.begin / this.after;}
function Operator(a, b)
{
    this.begin = a;
    this.after = b;

    this.add = Operator_add;
    this.minus = Operator_minus;
    this.plus = Operator_plus;
    this.div = Operator_div;
}

var Op = new Operator(2, 2);
var a = Op.add();                //2+2=4
log(a);

//用原型继承实现上述过程
function math_minus() {return this.begin - this.after;}
function math_plus() {return this.begin * this.after;}
function math_div() {return this.begin / this.after;}
function math_compare(a, b){
    return a.begin<b.begin?a:b;
}
function math(a, b)
{
    this.begin = a;
    this.after = b;
}

new math(0, 0);                     //创建并舍弃初始的math对象
math.prototype.minus = math_minus;  //添加原型对象公有方法minus
var c = new math(8, 2);
c.div = math_div;                   //添加对象私有方法div
var out = c.div();                  //8/2=4
log(out);
var out = c.minus();                //8-2=6
log(out);

math.prototype.plus = math_plus;    //添加原型对象公有方法plus
out = c.plus();                     //8*2=16
log(out);

//类方法
var d = new math(6, 2);
math.compare = math_compare;
var e = math.compare(c, d);
log(e.begin);
        //out = d.div();                      //出错 div是对象c的私有属性

//写在head之后，div之前，需要用onload包裹，表示html->dom树建立后在加载，否则会找不到
window.onload = function(){
    fade('#00DD', document.body);
}

 //递归实现渐变色
var fade = function(color, node){
    var level = 1;
    var status = 0;
    var step = function(){
        var hex = level.toString(16);
        node.style.backgroundColor = color + hex + hex;
        if(status == 0){
            level += 1;
            if(level == 15)
            {
                status = 1;
            }
        }
        if(status == 1){
            level -= 1;
            if(level == 0)
            {
                status = 0;
            }
        }
        setTimeout(step, 100);
    };
    setTimeout(step, 100);
};

