struct User{
    name:String,
    age:i16,
    height:i16,
}

fn main() {
    //声明结构体对象
    let mut a_user = User{
        name: String::from("John"),
        age:  18,
        height: 150,
    };

    a_user.age = 20;
    show_user(&a_user);

    let mut b_user = create_user(String::from("Jason"));
    show_user(&b_user);

    b_user = create_user_first(String::from("Lucy"));
    show_user(&b_user);

    //借用a_user结构变量值内参数
    let c_user = User{
        name: String::from("Cloudy"),
        age: a_user.age,
        height: a_user.height,
    };
    show_user(&c_user);

    //借用a_user结构变量
    let d_user = User{
        name:String::from("Wings"),
        ..a_user
    };
    show_user(&d_user);

}


fn create_user(name: String) -> User{
    User { 
        name: name, 
        age: 24, 
        height: 174 
    }
}

fn create_user_first(name: String) -> User{
    User { 
        name,    //if know, hide 
        age: 24, 
        height: 174 
    }
}

fn show_user(user: &User){
    println!("User:{}, {}, {}", user.name, user.age, user.height);
}