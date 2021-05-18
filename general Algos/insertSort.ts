
function insertSort(arr: number[]) {
    for (let i = 0; i < arr.length; i++) {
        let key = arr[i];
        let comparisonIndex = i - 1;

        while (comparisonIndex >= 0 && arr[comparisonIndex] > key) {
            arr[comparisonIndex+1] = arr[comparisonIndex];
            comparisonIndex = comparisonIndex - 1;
        }
        arr[comparisonIndex+1] = key;
    }
    return arr;
}

console.log(insertSort([7,6,5,4,3,2,1]));
