/*
洗牌算法
思路:
1.对于已排序数组a1...an
2.取an和1...n中随机位置进行交换，此时an为随机值
3.对于剩余数组a1...a(n-1)
4.取an-1和1...n-1中随机值进行交换，此时an-1为随机值
5.以此类推，直到最后一个值结束
*/
use rand::Rng;

pub fn shuffle_test() -> Vec<u32> {
    println!("---shuffle test!---");

    let mut vector: Vec<u32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("base:{:?}", vector);

    shuffle(&mut vector);
    println!("shuffle: {:?}", vector);

    //sort
    vector.sort();
    println!("sort: {:?}", vector);

    shuffle(&mut vector);
    println!("shuffle: {:?}", vector);

    //arr shuffle
    let mut arr = [1, 2, 3, 4, 5, 6, 7];
    let size = arr.len();
    println!("base:{:?}", arr);
    shuffle_arr(&mut arr, size);
    println!("shuffle: {:?}", arr);

    vector
}

fn shuffle(vector: &mut Vec<u32>) {
    let mut index = vector.len() - 1;

    loop {
        let swap_num = rand::thread_rng().gen_range(0, index);
        vector.swap(index, swap_num);

        index -= 1;
        if index == 0 {
            break;
        }
    }
}

fn shuffle_arr<T: Copy>(arr: &mut [T], n: usize) {
    let mut index = n - 1;

    loop {
        let swap_num = rand::thread_rng().gen_range(0, index);
        arr.swap(index, swap_num);

        index -= 1;
        if index == 0 {
            break;
        }
    }
}
