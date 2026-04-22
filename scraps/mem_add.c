#include <stdio.h>
#include <stdint.h>

int main() {
    int x = 10;
    int ptr = 0x1000;

    // Decimal (by casting)
    uintptr_t decimal_addr = (uintptr_t)ptr;
    printf("Decimal: %llu\n", (unsigned long long)decimal_addr);

    return 0;
}
