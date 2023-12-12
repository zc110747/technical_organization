
//1, 2
(function(arr){
    if(arr.length == 0){
        arr[0] = 1;
    }

    while(arr.length != 0){
        console.log(arr.shift());
    }
}([1, 2]));

//1, 2, 5
(function(){
    var test = (function(a) {
         this.a = a;   
         return function(b) {
              return this.a + b;
         }
     } (function(a, b) {
         return a;
    }(1, 2))); 

    console.log(test(4));
}());

var htm = "", i;
for(i=0; i<10; i++){
    htm += ('<ul><li>' + i + '<li><ul>');
}
console.log(htm);

array = [1, 4, 5, 6];
array = array.sort(function(){
    return Math.random() - 0.5;
});
console.log(array);

//使用gulp自动构建工具

//正则表达式

