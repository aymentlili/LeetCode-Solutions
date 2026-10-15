int sumOddLengthSubarrays(int* arr, int arrSize) {
    int i, j=0, k=1, sum = 0;

    while (k <= arrSize) {
        for (j = 0; j + k <= arrSize; j++) {
            for (i = j; i < j + k; i ++)
                sum += arr[i];
        }
        k+=2;
        

    }
    return sum;
}
