//This is for basic parameter type
#[allow(non_upper_case_globals)] //允许非大写的全局变量
fn main() {
    //整型
    //i8, u8, i16, u16
    //i32, u32, i64, u64
    //i128, u128, isize, usize
    let a: i8 = 0x1f; //16进制
    let b: u8 = b'a'; //字节
    let c: u64 = 0o77; //8进制
    let d: isize = 15_553; //分隔符
    let e: usize = 0b1111_0001; //2进制

    println!("a:{}, b:{}, c:{}, d:{}, e:{}", a, b, c, d, e);

    //常量
    pub const user: &str = "const value";
    println!("{}", user);

    //浮点型
    //f32, f64
    let mut f1: f32 = 2.5;
    f1 *= 4.0;
    println!("f1:{}", f1);
    f1 /= 2.0;
    println!("f1:{}", f1);
    f1 -= 1.0;
    println!("f1:{}", f1);
    f1 += 2.0;
    println!("f1:{}", f1);

    let f: u64 = c % 5;
    println!("f:{}", f);

    //布尔型
    //bool
    let mut b: bool = false;
    if f > 1 {
        b = true;
    }
    println!("b:{}", b);

    //字符型
    let c: char = 'z';
    println!("c:{}", c);

    //复合类型
    //元组（tuple)
    let mut t: (u8, f64, bool) = (1, 4.1, true);
    let (x, y, z) = t;
    println!("x, y, z:{}, {}, {}", x, y, z);
    t.1 = 4.2;
    t.2 = false;
    let (x, y, z) = t;
    println!("x, y, z:{}, {}, {}", x, y, z);
    println!("t:{:?}", t);

    //数组(array)
    let mut a: [u32; 4] = [1, 2, 3, 4];
    a[1] = 5;
    let b = a[3];
    println!("a:{:?}, b:{}", a, b);
}
