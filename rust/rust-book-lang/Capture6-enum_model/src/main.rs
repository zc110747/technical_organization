//枚举的结构
#[derive(Debug)]
enum WorkFlowStateT {
    Init,                      //枚举值
    Standby(String),           //枚举值可以支持带类型(字符串)
    Work(i32, i32),            //枚举值包含2个类型值
    Error { error_code: u32 }, //枚举值Error
}

//枚举支持方法处理
impl WorkFlowStateT {
    fn self_match(&self) {
        Self::match_process(self);
    }

    //匹配必须穷举所有的可能性
    fn match_process(mystate: &WorkFlowStateT) {
        match mystate {
            WorkFlowStateT::Init => {
                println!("Init");
            }
            WorkFlowStateT::Standby(str) => {
                println!("{}", str);
            }
            WorkFlowStateT::Error { error_code } => {
                println!("{}", error_code);
            }
            _ => {
                //通配符
                println!("{:?}", mystate);
            }
        }
    }
}

fn main() {
    let mut state0 = WorkFlowStateT::Init;
    println!("{:?}", state0);
    WorkFlowStateT::match_process(&state0);

    state0 = WorkFlowStateT::Standby(String::from("main"));
    println!("{:?}", state0);
    WorkFlowStateT::match_process(&state0);

    state0 = WorkFlowStateT::Error {
        error_code: 10000110,
    };
    println!("{:?}", state0);
    WorkFlowStateT::match_process(&state0);
    state0.self_match();

    state0 = WorkFlowStateT::Work(5, 6);
    WorkFlowStateT::match_process(&state0);
    state0.self_match();

    //if let匹配
    if let WorkFlowStateT::Work(5, 6) = state0 {
        println!("if let equal: {:?}", state0);
    } else {
        println!("no equal: {:?}", state0);
    }

}
