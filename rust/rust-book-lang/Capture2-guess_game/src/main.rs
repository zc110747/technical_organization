use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    
    //获取1~101间的随机数
    let secert_num = rand::thread_rng().gen_range(1, 101);
    println!("secert_num is {}", secert_num);

    //循环函数
    loop{
        println!("Please input your number:");
        let mut guess = String::new();
    
        //io输入值
        io::stdin().read_line(&mut guess)
                .expect("failed to read line");
        println!("you guess:{}", guess.trim());
    
        //解析字符串输入值并处理
        let guess:u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
    
        //比较
        match guess.cmp(&secert_num){
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You Win!");
                break;
            }
        }
    }

}
