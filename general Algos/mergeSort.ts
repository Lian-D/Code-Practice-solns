function mergesort(arr: number[], low: number, high: number) {
    if (low < high) {
        let mid = Math.floor(high/2)
        let left: number[] = [];
        let right: number[] = [];

        // Clones the Arrays for the merge step
        for (let i = 0; i < mid; i++) {
            left[i] = arr[i];
        }
        for (let i = mid+1; i < high; i++) {
            right[i-(mid+1)] = arr[i];
        }

        mergesort(arr, low, mid);
        mergesort(arr, mid, high);
        return merge(left, right);
    }
}

function merge(arr1: number[], arr2: number[]) {

}