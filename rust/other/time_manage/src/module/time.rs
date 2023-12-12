use chrono::prelude::*;

pub struct Timer {
    clock: i64,
}

impl Timer {
    pub fn new() -> Self {
        Self {
            clock: Local::now().timestamp_millis(),
        }
    }

    pub fn restart(&mut self) {
        self.clock = Local::now().timestamp_millis();
    }

    pub fn elapsed(&self) -> i64 {
        Local::now().timestamp_millis() - self.clock
    }
}

pub fn time_x() {
    let mut time = Timer::new();

    time.restart();
    let mut mills = Local::now().timestamp_millis();
    println!("毫秒值:{}", mills);

    mills = Local::now().timestamp_millis();
    println!("毫秒值:{}", mills);
    println!("{}", time.elapsed());
}
