# [Silver IV] 상현이의 물리학및실험1 실험 대작전 - 33257 

[문제 링크](https://www.acmicpc.net/problem/33257) 

### 성능 요약

메모리: 56452 KB, 시간: 196 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 5월 14일 23:19:42

### 문제 설명

<p>물리학및실험1을 수강하고 있는 상현이는 단일 물질로 이루어진 $N$개의 추의 밀도를 측정했다. 각 추는 $1$부터 $N$까지의 번호가 붙어있고, $i$번 추의 밀도는 $D_i$이다. 이때 밀도를 이용하여 $N$개의 추를 구성하고 있는 물질의 개수를 알아내고자 한다. 하지만 밀도 측정이 정확하지 않아 두 추의 밀도 차가 오차 범위 $E$ 미만이라면 두 추는 같은 물질로 이루어졌다고 판단한다. (예를 들어, 오차 범위가 $2$라면 밀도가 $10$, $11$, $12$, $13$, $14$, $15$인 추들은 모두 같은 물질로 만들어졌다고 판단한다.)</p>

<p>이번에는 상현이가 밤을 새지 않도록 그를 도와 $N$개의 추를 구성하고 있는 물질의 개수를 출력하는 프로그램을 작성하자!</p>

### 입력 

 <p>첫 번째 줄에 두 개의 정수 $N$$(1 \le N \le 2 \times 10^5)$과 $E$$(1 \le E \le 10^9)$이 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄에 $N$개의 정수 $D_1, D_2, \cdots, D_N$이 공백으로 구분되어 주어진다. $(1 \le D_i \le 10^9)$</p>

### 출력 

 <p>$N$개의 추를 구성하고 있는 물질의 개수를 출력한다.</p>

