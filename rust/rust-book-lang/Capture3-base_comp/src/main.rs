use std::cmp::Ordering;
/************************************************************
内容说明
1.rust变量
    let, let mut, const
2.类型
基础数据类型
    整型:i8, u8, i16, u16, i32, u32, i64, u64, isize, usize
    浮点:f32, f64
    布尔:bool
    字符:char
复合数据类型
    元组:(type, type, type...)
    数组:[type; size]
数据转换
    as: 基础类型互相转换
        let f:f32 = 1.5; let a = f as u32 + 1;
    parser
3.语法关键字
    匹配 match
    判断 if, if let
    循环 loop, while, for
4.函数
    fn, 函数体, 返回
5.错误处理
    unwrap
***************************************************************/

const GLOBAL: u32 = 5;

fn main() {
    let mut x = "5";
    println!("x is {}", x);

    x = "6";
    println!("x is {}", x);

    let x: u32 = x.trim().parse().unwrap_or(0);
    println!("x is {}", x);

    //match类型switch的功能
    match x.cmp(&GLOBAL) {
        Ordering::Less => println!("Less"),
        Ordering::Equal => println!("Equal"),
        Ordering::Greater => println!("Great"),
    };

    //match and option<val>
    let value = Some(0);
    match value {
        Some(x) => println!("Some is {}", x),
        _=> println!("none"),
    };
    println!("value is {:?}", value);

    //if let
    if let Some(val) = value {
        println!("val is {}", val);
    }
    
    //while let
    let mut value = Some(0);
    while let Some(i) = value {
        if i > 9 {
            println!("Great than 9");
            value = None;
        }
        else {
            print!("i is {}; ", i);
            value = Some(i+1);
        }
    }
    println!("{:?}", value);

    //lambda
    let s = "hello ".to_string();
    let join = | i:&str | { s + i};
    println!("{}", join("world!"));

    //unwrap使用默认的error处理
    let x = "3";
    let x = x.parse::<u32>().unwrap();
    println!("x is {}", x);

    //as
    let f: f32 = 4.5;
    let f1 = f + 3.0;
    let f2 = f1 * (x as f32);
    println!("f1 is {}, f2 is {}", f1, f2);
    let b1 = true;
    let b2 = 1 + b1 as u32;
    println!("b2 is {}", b2);
    let f = 3.5;
    let c = f as u32 + 1;
    println!("c is {}", c);   

    //tuple
    let tup: (i32, u16, &str) = (5, 6, "test");
    let (x1, y1, z1) = tup;
    println!("x1 is {}, y1 is {}, z1 is {}", x1, y1, z1);
    println!("tup:{}, {}, {}", tup.0, tup.1, tup.2);

    //array具有相同的数据类型
    let mut ary: [i32; 5] = [1, 2, 3, 4, 6];
    println!("ary is {:?}", ary);
    ary[0] = 5;
    println!("ary is {:?}", ary);
    let array_d = &ary[1..3];

    show_value(ary[3], "ary[3]");
    show_value(array_d[1], "array_d[1]");
    show_value(add_value(3, 5) as i32, "x");

    //返回值
    let x = {
        let y = 5;
        y + 1
    };
    show_value(x, "x");

    //match控制流 with if
    let y = match x {
        x if x < 5 => {
            println!("small");
            x + 1
        }
        x if x == 5 => {
            println!("equal");
            x
        }
        x if x > 5 => {
            println!("big");
            x - 1
        }
        _ => {
            println!("no process");
            0
        }
    };
    show_value(y, "y");

    //loop
    let mut index = 0;
    let result = loop {
        show_value(ary[index], "arr");
        index += 1;
        if index == ary.len() {
            break index;
        }
    };
    show_value(result as i32, "result");

    //while
    index = 0;
    while index < ary.len() {
        show_value(ary[index], "arr");
        index += 1;
    }

    //for
    for value in ary.iter() {
        println!("value is {}", value);
    }

    for num in (1..5).rev() {
        println!("num:{}, ary is {}", num, ary[num]);
    }
}

//1.input
fn show_value(x: i32, s: &str) {
    println!("{} value is {}", s, x);
}

//2.with return
fn add_value(x: i32, y: i32) -> u32 {
    if y > 0 {
        return y as u32;
    } 

    (x + y) as u32
}
