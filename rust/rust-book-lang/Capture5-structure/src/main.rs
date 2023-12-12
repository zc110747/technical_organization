/************************************************************
内&容说明
1.结构体struct
***************************************************************/

#[derive(Debug)]
struct User {
    name: String,
    email: String,
    phone: String,
    age: u16,
    active: bool,
}

#[derive(Debug)]
struct UserS<'a> {
    name_s : &'a str,
}

#[derive(Debug)]
struct Rgb(u8, u8, u8);

//实现结构体的方法
impl Rgb {
    fn new(r:u8, g:u8, b:u8) -> Self{
        Self(r, g, b)
    }

    fn show(&self) {
        println!("{}, {}, {}", self.0, self.1, self.2);
    }

    fn update_r(&mut self, r:u8){
        self.0 = r;
    }
}

fn main() {
    //结构体初始化和修改
    {
        let mut user0 = User {
            name: String::from("123"),
            email: String::from("123@xx.com"),
            phone: String::from("14550129515"),
            age: 24,
            active: true,
        };
        println!("{:?}", user0);

        user0.active = false;
        println!("{:?}", user0);
    }

    //简化初始化
    {
        let user = build_user(String::from("123"), 
                            String::from("123@xx.com"), false);
        show_user(&user);

        //对象可以使用其它变量进行赋值,发生move,原变量不能访问
        let name_str = String::from("test");
        let user1 = User {
            name: name_str,
            email: String::from("test@xx.com"),
            phone: String::from("14550129515"),
            age: 24,
            active: true,
        };
        show_user(&user1);
        //println!("{}", name_str);

        //借用初始化, 在借用初始化时，user的内部参数已经move，后续不能访问
        let user2 = User {
            active:true,
            ..user
        };
        show_user(&user2);
        //show_user(&user);  //borrow of partially moved value: `user
    }   

    //生命周期标注
    {
        let user_s = UserS{
            name_s: "UserS",
        };
        println!("{:?}, {}", user_s, user_s.name_s);
    }

    //元组结构体
    {
        //impl 添加方法
        let black = Rgb(0xff, 0xff, 0xff);
        println!("{:?}", black);
        black.show();

        //解构结构体
        let mut red = Rgb::new(0xff, 0x00, 0x00);
        let Rgb {
            0 : r,
            1 : g,
            2 : b,
        } = red;
        println!("{}, {}, {}", r, g, b);

        red.update_r(0xf1);
        red.show();
    }

}

//打印属性值
fn show_user(user: &User)
{
    println!("User {{ name: {}, email: {}, phone: {}, age: {}, active: {} }}",
    user.name, user.email, user.phone, user.age, user.active);
}

fn build_user(name: String, email: String, active:bool) -> User{
    User {
        name,
        email,
        phone: String::from("1234567890"),
        age:16,
        active,
    }
}