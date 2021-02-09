fn main() {
    let mut x: [u8; 7] = [20, 10, 25, 15, 88, 41, 66];
    for n in 0..x.len() {
        let mut min = n;
        let a:u8 = x[n];
        for j in n+1..x.len() {
            if x[min] > x[j] {
                min = j;
            }
        }
        x[n] = x[min];
        x[min] = a;
    }
    print!("{:#?}", x);
}


        // x = [15, 30, 23, 22, 33] -> x = [23, 30, 15, 22, 33]
        // a = 3  b = 5
        // c = b                n = x[0]  x[n] = 10, x[min] = 10
        // b = a                x[0] = x[2]
        // a = c                x[2] = n
        // b = a                