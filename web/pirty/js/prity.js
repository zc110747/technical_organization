//js精粹集合
//包含原型继承, 类方法, 子类, 深度克隆
var num = 1;
var s = "Study is not work, just everytime need!";
var last_word = s.substring(s.lastIndexOf(" ")+1, s.length);
console.log((num++)+".last_word:"+last_word);

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
console.log((num++)+".简单继承:"+out)    // 1/2 = 0.5
var Op2 = new Operator(5, 1);

//类方法
out = Operator.compare(Op1, Op2);   //比较x-选择大的5
console.log((num++)+".类方法:"+out);

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

console.log((num++)+'.'+ ExtraOperator.hasOwnProperty('swap').toString());      //false
console.log((num++)+'.'+ ExtraOperator.hasOwnProperty('selfadd').toString());   //true  只显示对象本身成员，原型链上不显示

var Op3 = new ExtraOperator(1, 2);
out= Op3.div();
console.log((num++)+".子类继承:"+out);  //1/2 = 0.5

Op3.swap();
out = Op3.div();
console.log((num++)+".子类方法:"+out);  //2/1 = 2

console.log((num++)+'.'+ ExtraOperator.prototype.isPrototypeOf(Op3)) //true 检查原型是否有指定实例化对象
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

function easy_clone(obj)
{
    var result = {};
    for(var i in obj){
        result[i] = obj[i];
    }
    return result;
}


var out1 = easy_clone(Person);
console.log((num++)+".对象克隆:"+out1.address.province);                    //shang hai
out1.address.province = "shanghai";
console.log((num++)+".浅度克隆原对象:"+Person.address.province);            //克隆变量和本体未隔离 shanghai

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
console.log((num++)+".克隆对象:"+out2.address.province);
out2.address.province = "beijing";
console.log((num++)+".克隆对象:"+out2.address.province);
console.log((num++)+".深度克隆原对象:"+Person.address.province);   //克隆变量和本体未隔离
delete Person.name;
console.log((num++)+".克隆对象:"+out2.name);                       //bob         原对象和克隆对象已经隔离
console.log((num++)+".深度克隆原对象:"+Person.name);               //undefined   原对象变量已经删除

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

console.log((num++)+".原型对象:"+Operator.prototype.obj.a);
ExtraOperator.prototype.obj.a = 2;
console.log((num++)+".原型对象:"+Operator.prototype.obj.a);  //此时子类修改了父类的属性

function Alone_Operator(a, b){

}
Alone_Operator.prototype = deepClone(Operator.prototype);
Alone_Operator.prototype.a = 3;
console.log((num++)+".原型对象:"+Operator.prototype.obj.a);  //采用深度复制，未修改父类属性

//写在head之后，div之前，需要用onload包裹，表示html->dom树建立后在加载，否则会找不到
window.onload = function(){
    fade('#99ff', 'one_line', 100);
    fade('#ff7F', 'one_row', 50);
    fade('#ff14', 'two_line', 150); 
    fade('#00FF', 'two_row', 200);
    fade('#ADFF', 'two_three_row', 100);
    fade('#FF45', 'three_line', 100);
    fade('#7FFF', 'three_row', 50);
}
