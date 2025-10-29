# [Gold V] Encyclopedia - 8374 

[문제 링크](https://www.acmicpc.net/problem/8374) 

### 성능 요약

메모리: 80880 KB, 시간: 1176 ms

### 분류

자료 구조, 그리디 알고리즘, 스택

### 제출 일자

2025년 10월 29일 19:49:21

### 문제 설명

<p>Little John loves reading Bytean encyclopedia. He is especially fascinated with the colorful illustrations the book contains. Bytean encyclopedia consists of many independent parts. Once in a while some new pages are printed. John's parents then add them to a binder containing all previous pages of the encyclopedia. In order to protect encyclopedia's pages from getting dirty, John's parents put each of them into a separate transparent shirt.</p>

<p>One day John dropped the book on the floor - all shirts fell out of the binder and all pages fell out of the shirts. Luckily, nothing got lost (neither pages nor shirts) and the number of pages is still equal to the number of shirts. John picked up all elements from the floor and put all of them together, forming a stack. He wants to put all elements back into the binder. Firstly, he needs to reorder pages and shirts in the stack so that pages are interleaved by shirts. John can't read, so the order of pages is not an issue for him. The only important thing is that all pages should be located back in shirts.</p>

<p>In each move John can swap positions of two consecutive elements in the stack. He finishes the process of reording when pages and shirts occur in the stack alternately.</p>

<p>Help Little John and calculate how many swap operations of consecutive elements in the stack are necessary to perform the desired reordering.</p>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input the description of the stack,</li>
	<li>calculates how many swap operations are required to order elements of Bytean encyclopedia,</li>
	<li>writes the result to the standard output.</li>
</ul>

### 입력 

 <p>The first line of the standard input contains one integer <em>n</em> (1 ≤ <em>n</em> ≤ 1 000 000) representing the number of pages (which is also equal to the number of shirts) in the Bytean encyclopedia.</p>

<p>The following lines contain the description of the stack: 2 · <em>n</em> non-negative integers. The <em>i</em>-th number describes <em>i</em>-th element on the stack and is equal 0, if that element is a shirt. Otherwise it is a positive number not grater than 1 000 000 000.</p>

<p>Description of the stack contains the same number of zeros as positive numbers. Encyclopedia is not perfect and pages numbers might repeat.</p>

### 출력 

 <p>One integer should be written to the standard output - the minimal number of swap operations that have to be performed to put Bytean encyclopedia back together.</p>

