typedef struct {
    long long time;
    int index;
} Node;

typedef struct {
    Node* data;
    int size;
} MinHeap;

static void heapPush(MinHeap* h, Node value) {
    int i = h->size++;
    h->data[i] = value;

    while (i > 0) {
        int p = (i - 1) / 2;

        if (h->data[p].time < h->data[i].time ||
            (h->data[p].time == h->data[i].time &&
             h->data[p].index <= h->data[i].index))
            break;

        Node tmp = h->data[i];
        h->data[i] = h->data[p];
        h->data[p] = tmp;
        i = p;
    }
}

static Node heapPop(MinHeap* h) {
    Node result = h->data[0];
    h->size--;

    if (h->size == 0)
        return result;

    h->data[0] = h->data[h->size];

    int i = 0;

    while (1) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        int best = i;

        if (l < h->size &&
            (h->data[l].time < h->data[best].time ||
             (h->data[l].time == h->data[best].time &&
              h->data[l].index < h->data[best].index)))
            best = l;

        if (r < h->size &&
            (h->data[r].time < h->data[best].time ||
             (h->data[r].time == h->data[best].time &&
              h->data[r].index < h->data[best].index)))
            best = r;

        if (best == i)
            break;

        Node tmp = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = tmp;
        i = best;
    }

    return result;
}

static int findNext(int* parent, int x) {
    if (parent[x] != x) {
        parent[x] = findNext(parent, parent[x]);
    }
    return parent[x];
}

static void update(int* tree, int n, int i, int delta) {
    for (i++; i <= n; i += i & -i) {
        tree[i] += delta;
    }
}

static int query(int* tree, int i) {
    int sum = 0;
    for (i++; i > 0; i -= i & -i) {
        sum += tree[i];
    }
    return sum;
}

static int kth(int* tree, int n, int k) {
    int idx = 0;
    int bit = 1;

    while ((bit << 1) <= n) {
        bit <<= 1;
    }

    for (; bit > 0; bit >>= 1) {
        int next = idx + bit;

        if (next <= n && tree[next] < k) {
            idx = next;
            k -= tree[next];
        }
    }

    return idx;
}

int* busiestServers(int k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize) {
    (void)loadSize;

    MinHeap heap;
    heap.data = malloc(k * sizeof(Node));
    heap.size = 0;

    int* server = calloc(k, sizeof(int));
    int* tree = calloc(k + 1, sizeof(int));

    for (int i = 0; i < k; i++) {
        update(tree, k, i, 1);
    }

    int available = k;

    for (int i = 0; i < arrivalSize; i++) {
        long long arr = arrival[i];
        int l = load[i];

        while (heap.size > 0 && heap.data[0].time <= arr) {
            Node node = heapPop(&heap);
            update(tree, k, node.index, 1);
            available++;
        }

        if (available == 0) {
            continue;
        }

        int start = i % k;
        int before = start > 0 ? query(tree, start - 1) : 0;

        int rank = before < available ? before + 1 : 1;
        int s = kth(tree, k, rank);

        update(tree, k, s, -1);
        available--;

        heapPush(&heap, (Node){arr + l, s});
        server[s]++;
    }

    int max_ = 0;

    for (int i = 0; i < k; i++) {
        if (server[i] > max_) {
            max_ = server[i];
        }
    }

    int count = 0;

    for (int i = 0; i < k; i++) {
        if (server[i] == max_) {
            count++;
        }
    }

    int* res = malloc(count * sizeof(int));
    int pos = 0;

    for (int i = 0; i < k; i++) {
        if (server[i] == max_) {
            res[pos++] = i;
        }
    }

    *returnSize = count;

    free(heap.data);
    free(server);
    free(tree);

    return res;
}