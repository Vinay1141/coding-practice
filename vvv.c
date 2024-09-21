#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct triangle {
    int a;
    int b;
    int c;
    double area;
};
typedef struct triangle triangle;
double calculate_area(int a, int b, int c) {
    double p = (a + b + c) / 2.0;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}
int sort_by_area(triangle* tr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (tr[j].area > tr[j + 1].area) {
                // Swap the triangles
                triangle temp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp;
            }
        }
    }
    return 0;  
}
int main() {
    int n, rc;
    scanf("%d", &n);
    triangle *tr = malloc(n * sizeof(triangle));
    for (int i = 0; i < n; i++) {
        scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
        tr[i].area = calculate_area(tr[i].a, tr[i].b, tr[i].c);
    }
    rc = sort_by_area(tr, n);

    for (int i = 0; i < n; i++) {
        printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
    }
    free(tr);

    return rc;
}
