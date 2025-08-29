# [Gold II] Cow Frisbee - 24492 

[문제 링크](https://www.acmicpc.net/problem/24492) 

### 성능 요약

메모리: 62528 KB, 시간: 308 ms

### 분류

자료 구조, 스택

### 제출 일자

2025년 8월 29일 17:33:29

### 문제 설명

<p>Farmer John's $N$ cows ($N \leq 3 \times 10^5)$ have heights $1, 2, \ldots, N$. One day, the cows are standing in a line in some order playing frisbee; let $h_1 \ldots h_N$ denote the heights of the cows in this order (so the $h$'s are a permutation of $1 \ldots N$).</p>

<p>Two cows at positions $i$ and $j$ in the line can successfully throw the frisbee back and forth if and only if every cow between them has height lower than $\min(h_i, h_j)$.</p>

<p>Please compute the sum of distances between all pairs of locations $i<j$ at which there resides a pair of cows that can successfully throw the frisbee back and forth. The distance between locations $i$ and $j$ is $j-i+1$.</p>

### 입력 

 The first line of input contains a single integer $N$. The next line of input
contains $h_1 \ldots h_N$, separated by spaces.

### 출력 

 <p>Output the sum of distances of all pairs of locations at which there are cows that can throw the frisbee back and forth. Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long long" in C/C++).</p>

