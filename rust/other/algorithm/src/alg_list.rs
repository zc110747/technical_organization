/*
study for rust and algorithm
can see: https://github.com/soulmachine/leetcode
*/
pub mod algorithm_list {

    use std::cmp::PartialEq;

    //类型题1: 删除已排序数组中的相同值
    pub fn remove_duplicate_test() {
        println!("---algorithm list test!---");

        //remove_duplicate
        let mut arr0 = [1, 1, 2, 3, 4, 5, 7, 7];
        let mut size = arr0.len();
        println!("older array:{:?}, size:{}", arr0, size);

        size = remove_duplicate(&mut arr0, size);
        let arr0 = &arr0[0..size];
        println!("remove_duplicate:{:?}, size:{}", arr0, size);

        //remove_duplicate_twice
        let mut arr0 = [1, 1, 2, 3, 3, 3, 3, 5, 5, 5, 6];
        let mut size = arr0.len();
        println!("older array:{:?}, size:{}", arr0, size);

        size = remove_duplicate_twice(&mut arr0, size);
        let arr0 = &arr0[0..size];
        println!("remove_duplicate_twice:{:?}, size:{}", arr0, size);

        //remove_duplicate_m 2
        let mut arr0 = [1, 1, 2, 3, 3, 3, 3, 5, 5, 5, 6];
        let mut size = arr0.len();
        println!("older array:{:?}, size:{}", arr0, size);

        size = remove_duplicate_m(&mut arr0, size, 2);
        let arr0 = &arr0[0..size];
        println!("remove_duplicate_m:{:?}, size:{}, m:{}", arr0, size, 2);

        //remove_duplicate_m 4
        let mut arr0 = [1, 1, 2, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 6, 7, 7];
        let mut size = arr0.len();
        println!("older array:{:?}, size:{}", arr0, size);

        size = remove_duplicate_m(&mut arr0, size, 4);
        let arr0 = &arr0[0..size];
        println!("remove_duplicate_m:{:?}, size:{}, m:{}", arr0, size, 4);
    }

    //Remove Duplicates from Sorted Array, allow once
    //no allocate extra space
    //A=[1, 1, 2] return 2, arr need be [1, 2]
    //1, 1, 2, 3, 3, 5, 7, 7, 10
    //1, x, 2, 3, x, 5, 7, x, 10
    fn remove_duplicate<T: PartialEq + Copy>(arr: &mut [T], n: usize) -> usize {
        let mut ret = 1;
        let mut index = 1;

        if n <= 1 {
            return n;
        }

        loop {
            if arr[index] != arr[ret - 1] {
                arr[ret] = arr[index];
                ret += 1;
            }

            index += 1;
            if index == n {
                break;
            }
        }

        ret
    }

    //Remove Duplicates from Sorted Array, allow twice
    //no allocate extra space
    //A=[1, 1, 2, 3, 3, 3, 3, 5] return 6, [1, 1, 2, 3, 3, 5]
    //1, 1, 2, 3, 3, 3, 3, 5
    //1, 1, 2, 3, 3, x, x, 5
    fn remove_duplicate_twice<T: PartialEq + Copy>(arr: &mut [T], n: usize) -> usize {
        let mut ret = 2;
        let mut index = 2;

        if n <= 2 {
            return n;
        }

        loop {
            if arr[index] != arr[ret - 2] {
                arr[ret] = arr[index];
                ret += 1;
            }

            index += 1;
            if index == n {
                break;
            }
        }

        ret
    }

    //Remove Duplicates from Sorted Array, allow m
    //no allocate extra space
    fn remove_duplicate_m<T: PartialEq + Copy>(arr: &mut [T], n: usize, m: usize) -> usize {
        let mut ret = m;
        let mut index = m;

        if m == 0 {
            return 0;
        }

        if n <= m {
            return n;
        }

        loop {
            if arr[index] != arr[ret - m] {
                arr[ret] = arr[index];
                ret += 1;
            }

            index += 1;
            if index == n {
                break;
            }
        }

        ret
    }

    //类型题2: 在已排序数组中查找变量
    //二分法
    //1, 2, 3, 4, 5, 6, 8
    //3 => 3
    // pub fn find_sort_test() {

    // }

    // fn solution<'N, T: PartialEq + PartialOrd + PartialOrd<&'static [N]> + Copy>(arr: &[T], n:usize, target: &[N]) -> i32
    // {
    //     let mut start = 0;
    //     let mut end = n;

    //     while start != end {
    //         let mid = start + (end - start)/2;
    //         if arr[mid] == target {
    //             return mid as i32;
    //         }
    //         if arr[start] <= arr[end] {
    //             if arr[start] <= target && arr[mid] > target  {
    //                 end = mid;
    //             }   
    //             else {
    //                 start = mid + 1;
    //             }
    //         } else {
    //             if arr[mid] <= target && arr[end-1] >= target  {
    //                 start = mid + 1;
    //             }   
    //             else {
    //                 end = mid;
    //             }
    //         }
    //     }

    //     -1
    // }
}
