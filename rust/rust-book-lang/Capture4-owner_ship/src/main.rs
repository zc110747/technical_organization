/************************************************************
内容说明
1.所有权转移
支持Copy的trait,不会有所有权转移
    1.基础类型(整型，bool类型，字符类型，浮点类型)
    2.由上诉类型组合的元组和数组
2.引用和可变引用
    引用字面量&str
    引用字符串&String
    可变引用 &mut String
    引用的规则:
        1.在任何一段给定的时间内，只能拥有一个可变引用，且可变引用
        和不可变引用不能共存
        2.引用总是有效的
3.切片
    [n..m], n起始位置，m结束位置
    省略起始位置表示0开始，省略结束位置表示到数组末
    字符串变量，字符串字面量和数组支持切片
***************************************************************/
fn main() {
    //字符串字面量 &str
    let str0 = "String0";
    show_str_reference(str0);

    //字符串变量 String
    {
        //String::from申请变量,离开区域后释放
        let str1 = String::from("Str1");
        show_str_reference(&str1);
    }

    //push_str方法
    let mut str2 = String::from("Str2");
    str2.push_str(", add");
    show_str_reference(&str2);

    //所有权转移
    let str3 = str2;
    show_str_reference(&str3);
    //show_str(&str2); borrow of moved value: `str2`

    //复制对象clone
    let str4 = str3.clone();
    show_str_reference(&str4);
    show_str_reference(&str3);

    //基础类型
    //包含基础类型的元组支持copy trait
    let tup0: (i32, u8, f32) = (-5, 4, 3.0);
    let tup1 = tup0;
    println!("tup is {:?}, {:?}", tup0, tup1);

    //包含基础类型的数组支持copy trait
    let arr0: [u32; 4] = [1, 2, 3, 4];
    let arr1 = arr0;
    println!("arr is {:?}, {:?}", arr0, arr1);

    //ownership and function
    let mut str0 = String::from("str0");
    str0.push_str("_add");
    let str1 = show_str(str0); //所有权转移
                               //println!("str is {}", str0); //borrow of moved value: `str0`
    println!("str is {}", str1);

    //元组返回
    let (s2, len) = str_len(str1);
    println!("{} length is {}", s2, len);

    //引用和借用
    let len = str_len_ref(&s2);
    println!("{} length is {}", s2, len);

    //可变引用
    {
        let mut str = String::from("str");
        add_tail(&mut str);
        show_str_reference(&str);

        //str3在str1绑定前访问正常，绑定后访问报错
        //不能够再拥有不可变引用时，创建可变引用
        let str3 = &str;
        show_str_reference(str3);

        let str1 = &mut str;
        str1.push_str("_str1");
        show_str_reference(str1);

        //不能够将两个可变引用指向同一个变量
        //cannot borrow `str` as mutable more than once at a time
        //let str2 = &mut str;
        //str2.push_str("_str1");
    }

    //切片
    {
        let mut s = String::from("SeqString");
        s.replace_range(0..1, "a");

        let slice_arr: [&str; 5] = [&s[0..2], &s[..3], &s[3..], &s[3..s.len()], &s[..]];
        for str in slice_arr.iter() {
            println!("str is {}", str);
        }

        show_str_reference(&s[2..4]);
        //不允许,被借用到切片后，immutable
        //s.replace_range(0..1, "a");

        //数组支持切片
        let arr = ["a1", "b1", "cd"];
        let arr_s = &arr[1..];
        println!("{:?}, {:?}", arr, arr_s);
    }
}

//引用, 默认不可变
//&String仅支持字符串量
//&Str支持字符串字面量和字符串量
fn show_str_reference(s: &str) {
    println!("str value is {}", s);
}

fn show_str(s: String) -> String {
    println!("str value is {}", s);

    s //作为返回值移动到调用函数
}

fn str_len(s: String) -> (String, usize) {
    let length = s.len();

    (s, length) //通过元组返回
}

fn str_len_ref(s: &String) -> usize {
    s.len()
}

fn add_tail(s: &mut String) {
    s.push_str("_tail");
}
