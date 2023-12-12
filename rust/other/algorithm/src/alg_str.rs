
pub mod algorithm_str{
    pub fn alg_str_test() {
        let mystr = "A man, a plan, a canal: Panama";
        println!("is palindrome:{}", check_alg_palindrome(mystr));
    
        let mystr = "race a car";
        println!("is palindrome:{}", check_alg_palindrome(mystr));
    
        let mystr = "a 1 c 1 a";
        println!("is palindrome:{}", check_alg_palindrome(mystr));
    
        let mystr = "";
        println!("is palindrome:{}", check_alg_palindrome(mystr));
    }
    
    //Valid Palindrome
    //give a string, determine if it is a palindrome.
    //only compare alphanumeric charaters. 
    fn check_alg_palindrome(val_str: &str) -> bool {
        let mut ret = true;
        let mut end: usize = val_str.len();
        if end == 0 {
            return true;
        }
    
        end -= 1;
        let low_str = <&str>::clone(&val_str).to_lowercase();
        let mut start: usize = 0;
    
        while start < end {
            let start_char = match low_str.chars().nth(start) {
                Some(x) => x,
                _ => ' ',
            };
            if !start_char.is_alphanumeric() {
                start += 1;
                continue;
            }
    
            let end_char = match low_str.chars().nth(end) {
                Some(x) => x,
                _ => ' ',
            };
            if !end_char.is_alphanumeric() {
                end -= 1;
                continue;
            }
    
            if start_char != end_char {
                ret = false;
                break;
            } else {
                start += 1;
                end -= 1;
            }
        }
    
        ret
    }
}
