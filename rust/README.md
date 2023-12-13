# rust_study

## 基础说明

主要参考官方文档目录: <https://github.com/rust-lang/book>
另包含中文说明:<https://kaisery.github.io/trpl-zh-cn/title-page.html>
此外包含两部参考书:

- <Rust权威指南>
- <Rust编程之道>

## Cargo包管理器说明

```rust
cargo --version         查看当前版本
cargo build             编译Rust项目，生成可执行文件
cargo check             检查Rust项目内代码，不生成
cargo clean             清除项目生成文件  
cargo new [project]     创建Rust项目
cargo init [project]    在已存在文件夹创建Rust项目
cargo bench             测试编译后软件的性能
cargo update            更新lock中的依赖项cargo 
help  [cmd]             查询选项的具体功能
cargo install           编译和安装一个rust二进制包
cargo uninstall         移除一个rust二进制包
cargo run               执行Rust编译后可执行文件
cargo fmt               格式化代码，需要通过rustup component add rustfmt先安装工具
```

### 添加依赖

```rust
Cargo.toml
.....
[dependencies]

[Package] = [version]  //举例 rand="0.3.14"
```

通过cargo build或cargo update, 可更新依赖项

### 更新cargo更新源

在..\.cargo\config中添加源

```rust
[source.crates-io]
replace-with = 'tuna'

[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
```

## Rust权威指南学习

### Capture2-guess_game

```rust
    入口函数 fn main
    了解到包
        use::io;                //输入/输出
        use rand::Rng;          //生成随机数
        use std::cmp::Ordering; //比较
    match 控制流运算符
```

### Capture3-base_comp

```rust
    1.rust变量默认是不可变的,允许修改的添加mut
    2.类型
        标量(scaler)类型
            整型:i8, u8, i16, u16, i32, u32, i64, u64, isize, usize
            浮点:f32, f64
            布尔:bool
            字符:char
        复合(compound)类型
            元组:(type, type, type...)
            数组:[type; size]
    数据转换:as, parser
    3.函数
        fn, 函数体, 尾部返回值，中间返回值(return)
    5.控制流分支语句
        if, match
    6.循环语句
        loop, while, for
    7.其它
        unwrap
```

### Capture4-owner_ship

```rust
    1. 字符串类型和字符串字面量类型
       String, &str, String::new(), String::from(),
    2. 字符串类型的方法
        push_str, clone
    3. copy trait 和所有权转移
    4. 引用和借用
        &str 引用字符串字面量
        &String 引用字符串
        &mut String 可变引用
    5. 切片(不可变)
        &string_0[n..m]; 
```
