#[derive(Debug)]
enum ValState {
    Int(i32),
    Float(f32),
    Text(String),
}

fn vec_process() {

    //创建空的vec对象
    let mut v:Vec<i32> = Vec::new();
    println!("{:?}", v);

    v.push(0);
    v.push(1);
    v.push(2);
    v.push(3);
    println!("{:?}", v);
    v.pop();
    println!("{:?}", v);

    //用索引或者get访问vec对象
    let vref = &v[1];
    println!("{:?}", vref);
    match v.get(2) {
        Some(val) =>  println!("the value is {}", val),
        None => println!("no parameter"),
    }

    //基于vec!进行初始化
    let mut v = vec![1, 2, 3];
    println!("{:?}", v);

    //for in vec to get value
    print!("for in:");
    for val in &v {
        print!("{}, ", val);
    }
    println!("end");

     //for in vec can modify
    for i in &mut v{
        *i += 2;
    }
    println!("{:?}", v);

    //
    let v2 = vec![
        ValState::Int(3),
        ValState::Float(5.2),
        ValState::Text(String::from("test"))
    ];
    println!("{:?}", v2);

    let val2 = &v2[1];
    println!("{:?}", val2);
}

fn main() {
    vec_process();
}
