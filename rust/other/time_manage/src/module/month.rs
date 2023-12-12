#[derive(Debug)]
pub enum MonthDayT {
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December,
    None,
}

impl MonthDayT {
    //no leap year
    pub fn get_day(&self, is_leap: bool) -> u32 {
        let mut day: u32 = 0;

        match self {
            MonthDayT::January => day = 31,
            MonthDayT::February => {
                if is_leap {
                    day = 29;
                } else {
                    day = 28;
                }
            }
            MonthDayT::March => day = 31,
            MonthDayT::April => day = 30,
            MonthDayT::May => day = 31,
            MonthDayT::June => day = 30,
            MonthDayT::July => day = 31,
            MonthDayT::August => day = 31,
            MonthDayT::September => day = 30,
            MonthDayT::October => day = 31,
            MonthDayT::November => day = 30,
            MonthDayT::December => day = 31,
            _ => (),
        }

        day
    }

    pub fn new(month: u32) -> MonthDayT {
        match month {
            1 => MonthDayT::January,
            2 => MonthDayT::February,
            3 => MonthDayT::March,
            4 => MonthDayT::April,
            5 => MonthDayT::May,
            6 => MonthDayT::June,
            7 => MonthDayT::July,
            8 => MonthDayT::August,
            9 => MonthDayT::September,
            10 => MonthDayT::October,
            11 => MonthDayT::November,
            12 => MonthDayT::December,
            _ => MonthDayT::None,
        }
    }

    pub fn get_day_of_month(month: u32, is_leap: bool) -> u32 {
        assert!(month <= 12, "invalid month: {:?}", month);

        let month_t = Self::new(month);

        month_t.get_day(is_leap)
    }
}
