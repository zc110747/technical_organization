mod alg_list;
mod shuffle;
mod alg_str;

fn main() {
    //洗牌算法
    shuffle::shuffle_test();

    //线性表算法
    alg_list::algorithm_list::remove_duplicate_test();

    //字符串算法
    alg_str::algorithm_str::alg_str_test();
}

