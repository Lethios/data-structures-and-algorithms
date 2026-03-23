fn bubble_sort(arr: &mut [i32]) {
    let n: usize = arr.len();

    for i in (0..n).rev() {
        let mut swapped: bool = false;

        for j in 0..i {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
                swapped = true;
            }
        }

        if !swapped {
            break;
        }
    }
}

fn main() {
    let mut arr: [i32; 20] = [38, 27, 43, 3, 9, 82, 10, 1, 75, 56, 14, 62, 48, 91, 23, 7, 55, 30, 18, 99];

    bubble_sort(&mut arr);
    println!("{:?}", arr);
}

