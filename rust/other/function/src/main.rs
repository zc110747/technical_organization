fn main() {
    //函数
    show_func();

    //带参数的函数
    para_func(5);
    
    //带返回值的函数
    let m = para_re_func(6);
    println!("m:{m}");       //catch the variable

    //表达式返回
    let mut u2 = {
        let x=3;
        x+1
    };
    println!("u2:{u2}");

    //判断语句
    //if...else if...else
    //if...else
    let b1:i32 = 5;
    if b1 == 5 {
        u2 += 1;
        println!("b1 is {b1}, u2:{u2}");
    }
    else if b1 > 6 {
        u2 = 0;
        println!("b1 is {b1}, u2:{u2}");
    }
    else {
        println!("others");
    }
    
    //for if/else, need equal type, otherwise will error
    let a:i32 = if u2>5 {5} else {6};  
    println!("a:{a}");
    
    //循环语句
    //loop
    let mut counter = 0;
    let result= loop {
        counter += 1;
        
        if counter > 5{
            break "counter:{counter}";
        }      
    };
    println!("result:{result}");

    //loop lable
    counter = 0;
    'external_label: loop{
        let mut index = 0;
        println!("counter:{counter}");
        loop{
            println!("index:{index}");

            if index == 1 {
                break;
            }

            if counter == 2 {
                break 'external_label;
            }
        
            index += 1;
        }

        counter += 1;
    }

    //while
    while counter > 0 {
        println!("while counter:{counter}");
        counter -= 1;
    }

    //for
    let t1:[u16;4] = [2, 5, 7, 9];
    for u in t1 {
        println!("u:{u}");
    }

    for u in t1.iter().enumerate() {
        println!("u:{}, {}", u.1, t1[u.0]);
    }

}

//1.basic
fn show_func() {
    println!("call show func!");
}

//2.with parameter
fn para_func(i:i32){
    println!("i:{}", i);
}

//3.with return
fn para_re_func(i:i32) -> i32{
    let x:i32 = i*i;
    
    x + 1  //返回值不能带;号
}

