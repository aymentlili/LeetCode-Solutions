int minOperations(char* s) {
    int n = strlen(s);        
    if (n == 0) return 0;

    char mn = s[0], mx = s[0];
    int sorted = 1;
    int interiorExtreme = 0;

    for (int i = 1; i < n; i++) {
        char c = s[i];
        if (c < s[i - 1]) sorted = 0;
        if (c < mn) mn = c;
        if (c > mx) mx = c;
    }

    if (sorted) return 0;
    if (n == 2) return -1;

    if (s[0] == mn || s[n - 1] == mx) return 1;

    for (int i = 1; i < n - 1; i++) {
        if (s[i] == mn || s[i] == mx) return 2;
    }
    return 3;
}