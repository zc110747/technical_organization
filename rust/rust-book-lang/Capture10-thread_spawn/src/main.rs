use std::thread;
use std::time::Duration;
use std::sync::mpsc;
use std::sync::{Mutex, Arc};

/*
std::thread 定义管理线程的各种函数
std::sync    
*/
fn main() {
    thread_sample();

    thread_mpsc();

    thread_sync();
}

//thread sample
//1.thread的创建接口thread::spawn
//2.move获取外部的数据
//3.join等待执行完毕
fn thread_sample() {
    let mut str_usr = String::from("Usr Str ");

    let handler = thread::spawn(move || {
        str_usr.push_str("Thread Push!");
        println!("{}", str_usr);

        for i in 1..5 {
            print!("num in thread:{}! ", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..3 {
        print!("num in main:{}! ", i);
        thread::sleep(Duration::from_millis(1));
    }

    handler.join().unwrap();
}

//thread_mpsc
//1.mpsc创建rx和tx通道
//2.send和recv进行通道发送和接收数据
//3.clone复制发送通道，实现多个发送
fn thread_mpsc() {
    let (tx, rx) = mpsc::channel();
    let tx_cl = tx.clone();

    let handler1 = thread::spawn(move || {
        tx.send(String::from("hi from thread")).unwrap();
    });

    let handler2 = thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx_cl.send(val).unwrap();
        }
    });

    //in this place already move
    //str_usr.push_str("main push!");
    let myrecv =  rx.recv().unwrap();
    println!("from mpsc:{}", myrecv);
    
    for recv in rx {    
        println!("loop:{}", recv);
    }

    handler1.join().unwrap();
    handler2.join().unwrap();
}

//use mutex to sync data
fn thread_sync() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handler = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        }); 
        handles.push(handler);
    }

    for handler in handles {
        handler.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}