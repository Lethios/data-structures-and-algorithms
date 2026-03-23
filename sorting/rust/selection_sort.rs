fn selection_sort(arr: &mut [i32]) {
    let n: usize = arr.len();

    for i in 0..n-1 {
        let mut min_idx: usize = i;

        for j in i+1..n {
            if arr[j] < arr[min_idx] {
                min_idx = j;
            }
        }

        if min_idx != i {
            arr.swap(i, min_idx);
        }
    }
}

fn main() {
    let mut arr: [i32; 20] = [38, 27, 43, 3, 9, 82, 10, 1, 75, 56, 14, 62, 48, 91, 23, 7, 55, 30, 18, 99];

    selection_sort(&mut arr);
    println!("{:?}", arr);
}
