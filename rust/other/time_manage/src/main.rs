use std::io;

//use module from others
mod module;
use crate::module::month::MonthDayT;
use crate::module::time::*;

#[derive(Debug)]
struct TimeProcess {
    year: u32,
    month: u32,
    day: u32,
    time_str: String,
}

impl TimeProcess {
    fn new(mystr: String) -> Self {
        let time_arr = Self::get_time_from_str(&mystr);

        assert!(
            time_arr[0] >= 1980
                && time_arr[1] <= 12
                && time_arr[2] <= Self::get_day_of_month(time_arr[0], time_arr[1]),
            "invalid time[year, month, day]: {:?}",
            time_arr
        );

        Self {
            year: time_arr[0],
            month: time_arr[1],
            day: time_arr[2],
            time_str: mystr,
        }
    }

    fn new_time(y: u32, m: u32, d: u32) -> Self {
        let time_str = format!("{}.{}.{}", y, m, d);

        Self::new(time_str)
    }

    fn show(&self) {
        println!(
            "year:{}, month:{}, day:{}, string:{}",
            self.year, self.month, self.day, self.time_str
        );
    }

    fn translate_add_day_time(&self, day: u32) -> TimeProcess {
        let mut total_day = day;
        let mut time_calc: (u32, u32, u32) = (self.year, self.month, self.day);

        let left_day_of_month = Self::get_left_day_of_month(time_calc.0, time_calc.1, time_calc.2);
        let letf_day_of_year = Self::get_left_day_of_year(time_calc.0, time_calc.1, time_calc.2);

        if total_day < left_day_of_month {
            time_calc.2 += day;
        } else if total_day < letf_day_of_year {
            total_day -= left_day_of_month;
            time_calc.2 = 0;

            loop {
                time_calc.1 += 1;
                let month_of_day = Self::get_day_of_month(time_calc.0, time_calc.1);
                if total_day < month_of_day {
                    break;
                } else {
                    total_day -= month_of_day;
                }
            }
            time_calc.2 = total_day;
        } else {
            total_day -= letf_day_of_year;
            time_calc.1 = 0;
            time_calc.2 = 0;

            loop {
                time_calc.0 += 1;
                let year_of_day = Self::get_day_of_year(time_calc.0);
                if total_day < year_of_day {
                    break;
                } else {
                    total_day -= year_of_day;
                }
            }

            loop {
                time_calc.1 += 1;
                let month_of_day = Self::get_day_of_month(time_calc.0, time_calc.1);
                if total_day < month_of_day {
                    break;
                } else {
                    total_day -= month_of_day;
                }
            }
            time_calc.2 = total_day;
        }

        TimeProcess {
            time_str: format!("{}.{}.{}", time_calc.0, time_calc.1, time_calc.2),
            year: time_calc.0,
            month: time_calc.1,
            day: time_calc.2,
        }
    }

    fn is_leap_year(y: u32) -> bool {
        let mut ret = false;
        if y % 400 == 0 || (y % 4 == 0 && y % 100 != 0) {
            ret = true;
        }

        ret
    }

    fn get_day_of_year(y: u32) -> u32 {
        let mut day = 365;

        if Self::is_leap_year(y) {
            day = 366;
        }

        day
    }

    fn get_day_of_month(y: u32, m: u32) -> u32 {
        MonthDayT::get_day_of_month(m, Self::is_leap_year(y))
    }

    fn get_left_day_of_month(y: u32, m: u32, d: u32) -> u32 {
        let day_of_month = Self::get_day_of_month(y, m);

        day_of_month - d
    }

    fn get_left_day_of_year(y: u32, m: u32, d: u32) -> u32 {
        let day_of_year = Self::get_day_of_year(y);
        let mut day = 0;
        let mut index = 1;

        while index < m {
            day += Self::get_day_of_month(y, index);
            index += 1;
        }
        day += d;

        day_of_year - day
    }

    fn get_time_from_str(my_str: &str) -> [u32; 3] {
        let mut arr: [u32; 3] = [0, 0, 0];
        let str_arr: Vec<&str> = my_str.trim().split('.').collect();

        for num in 0..str_arr.len() {
            arr[num] = str_arr[num].parse::<u32>().unwrap();
        }
        arr
    }

    fn get_start_time() -> TimeProcess {
        TimeProcess {
            year: 1980,
            month: 1,
            day: 1,
            time_str: "1980.1.1".to_string(),
        }
    }

    //from 1980-1-1
    fn get_time_from_start_day(my_str: &str) -> u32 {
        let time_arr = Self::get_time_from_str(my_str);
        let start_time = Self::get_start_time();
        let mut time_calc: (u32, u32, u32) = (start_time.year, start_time.month, start_time.day);
        let mut day = 0;

        if time_arr[0] < time_calc.0 {
            return day;
        }

        loop {
            let day_of_year = Self::get_day_of_year(time_calc.0);
            time_calc.0 += 1;
            if time_arr[0] < time_calc.0 {
                time_calc.0 = time_arr[0];
                break;
            }
            day += day_of_year;
        }

        loop {
            let day_of_month = Self::get_day_of_month(time_calc.0, time_calc.1);
            time_calc.1 += 1;
            if time_arr[1] < time_calc.1 {
                break;
            }
            day += day_of_month;
        }

        day += time_arr[2];
        day -= time_calc.2;

        day
    }

    fn get_interval_day_of_time(time0: &str, time1: &str) -> u32 {
        let day0 = Self::get_time_from_start_day(time0);
        let day1 = Self::get_time_from_start_day(time1);

        if day0 >= day1 {
            day0 - day1
        } else {
            day1 - day0
        }
    }
}

fn main() {
    let mut new_time = Timer::new();

    new_time.restart();
    println!("{}", TimeProcess::get_left_day_of_year(2022, 8, 15));

    let time = TimeProcess::new(String::from("1993.2.8"));
    time.show();

    let mut time_out = time.translate_add_day_time(10000);
    time_out.show();

    time_out = time.translate_add_day_time(10);
    time_out.show();

    time_out = time.translate_add_day_time(30);
    time_out.show();

    time_out = time.translate_add_day_time(365);
    time_out.show();

    time_out = time.translate_add_day_time(4 * 366);
    time_out.show();

    println!(
        "start day:{}",
        TimeProcess::get_time_from_start_day("1997.2.1")
    );
    println!(
        "start day:{}",
        TimeProcess::get_time_from_start_day("2020.2.10")
    );
    println!(
        "start day:{}",
        TimeProcess::get_time_from_start_day("2022.2.10")
    );

    let time = TimeProcess::new(String::from("1980.1.1"));
    let time_out = time.translate_add_day_time(6211);
    time_out.show();

    println!(
        "from start day:{}",
        TimeProcess::get_time_from_start_day("1980.3.1")
    );
    println!(
        "from start day:{}",
        TimeProcess::get_time_from_start_day("2025.11.5")
    );
    println!(
        "between day:{}",
        TimeProcess::get_interval_day_of_time("2024.1.5", "2025.1.5")
    );
    println!(
        "between day:{}",
        TimeProcess::get_interval_day_of_time("2024.11.5", "2025.11.5")
    );

    let time = TimeProcess::new_time(2012, 2, 29);
    println!("{:?}", time);

    let month = MonthDayT::new(time.month);
    println!("{:?}", month);

    println!("work time:{}", new_time.elapsed());
    time_x();

    // for month in 1..12 {
    //     println!("day:{}", MonthDayT::get_day_of_month(month as u32, true));
    // }
    //println!("day:{}", MonthDayT::get_day_of_month(13, true));
    // println!("please input time(y.m.d):");
    // let mut time = String::new();
    // io::stdin().read_line(&mut time).unwrap();
    // println!("from start day:{}", TimeProcess::get_time_from_start_day(&time));
    // println!(
    //     "between day:{}",
    //     TimeProcess::get_interval_day_of_time("1993.2.8", &time)
    // );
}
