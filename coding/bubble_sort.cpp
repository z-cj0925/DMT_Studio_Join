// 数字媒体技术社团 2026 招新 · 二选一（编程与算法方向）
// 题目：用冒泡排序把 8 3 6 2 7 1 按从小到大排序
// 作者：紫菜卷

#include <iostream>
#include <utility>   // std::swap

int main() {
    int arr[] = {8, 3, 6, 2, 7, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    // 外层循环：一共需要 n-1 轮
    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;   // 记录本轮有没有发生过交换

        // 内层循环：从左到右两两比较
        // 每轮结束后末尾的 i+1 个数已经排好，所以比较范围减 i
        for (int j = 0; j < n - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {   // 前面比后面大 → 交换
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        // 如果一整轮都没交换过，说明已经有序，可以提前结束
        if (!swapped) {
            break;
        }
    }

    // 输出结果
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << (i == n - 1 ? '\n' : ' ');
    }

    return 0;
}
