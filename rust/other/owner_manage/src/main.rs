
fn main() {

    //move and clone
    let s0:String = String::from("start");
    let s1 = s0;
    let s2 = s1.clone();

    //println!("{s0}"); //error, s0 have been moved
    println!("s1:{s1}, s2:{s2}");

    ownership_change(s1);
    //println!("{s1}, {s2}"); //error, s2 have been moved

    let s3 = get_ownership(s2);
    println!("s3:{s3}");
    let s4 = format!("format, {s3}");
    println!("s4:{s4}");

    let s5 = (s4.clone(), s4.len());
    println!("s5:{:?}", s5);

    //copy trait
    //整型，布尔型，浮点型，
    //字符型，元组，数组
    let x:char  = 'a';
    let y = x;
    println!("{x}, {y}");

    //{:?} shows compositon type
    //{:#?} shows compositon type with wrap
    let a:[i16;2] = [1, 2];
    let a1 = a;
    println!("{:#?}, {:?}", a, a1);

    let t:(u8, u16, [i32;2]) = (1, 5, [2, 4]);
    let t1 = t;
    println!("{:?}, {:?}", t, t1);

    //reference
    //&, not get ownership
    let u0 = get_length(&(s5.0));
    println!("s5:{:?}, u0:{u0}", s5);

    let mut s6 = s5.0.clone();
    println!("{s6}, {:?}", s5);

    //referenece mut var
    //1.in each timer, only one valid mutable reference
    //2.reference must be valid
    let s7 = &mut s6;
    println!("s7:{s7}");

}

fn ownership_change(s:String){
    println!("s:{s}")
}

fn get_ownership(s:String) -> String{

    let s2 = String::from(" Get");
    s + &s2
}

fn get_length(s : &String) -> usize{
    s.len()
}