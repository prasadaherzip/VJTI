#include <iostream>
#include <unistd.h>     // for sleep
#include <sys/mman.h>   // for mmap
#include <cstring>      // for memset


int main() {
    std::cout << "Step 1: Program started. PID = " << getpid() << "\n";
    std::cout << "Pause 1: Press Enter to continue...\n";
    std::cin.get();

    // At this point, measure VSZ and RSS using: ps -p <PID> -o vsz,rss
    // Also explore /proc/<PID>/status and /proc/<PID>/smaps for detailed memory.

    // Step 2: Memory map one anonymous page (4KB on most systems)
    size_t page_size = sysconf(_SC_PAGESIZE);
    void* addr = mmap(NULL, page_size, PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (addr == MAP_FAILED) {
        perror("mmap");
        return 1;
    }
    
    std::cout << "Step 2: Mapped a new anonymous page at " << addr << "\n";
    std::cout << "Pause 2: Press Enter to continue...\n";
    std::cin.get();

    // Measure VSZ and RSS again here with ps and /proc.

    // Step 3: Write data to the mapped page
    std::cout << "Step 3: Writing to the mapped page...\n";
    memset(addr, 0xABC, page_size); // Touch the page to commit it

    std::cout << "Pause 3: Press Enter to exit...\n";
    std::cin.get();
    sleep(10);
    // Final measurement of VSZ and RSS.

    // Cleanup
    munmap(addr, page_size);
    return 0;
}