# [Gold III] Haiku Formatting - 32015 

[문제 링크](https://www.acmicpc.net/problem/32015) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

많은 조건 분기, 구현, 문자열

### 제출 일자

2026년 1월 24일 18:04:05

### 문제 설명

<p>A haiku is a three-line poem in which the first and third lines contain <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> syllables each, and the second line contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container> syllables.</p>

<p>An example of a haiku is:</p>

<pre>Blue Ridge mountain road.
Leaves, glowing in autumn sun,
fall in Virginia.</pre>

<p>Write a program to examine a line of English text and and attempt to render it as a haiku. This will require counting the syllables in the words of the text, which should be done according to the following rules:</p>

<ul>
	<li>
	<p>A word consists of a non-empty, maximal string of zero or more alphabetic characters (upper and/or lower-case) followed by zero or more non-blank, non-alphabetic characters.</p>

	<ul>
		<li>
		<p>Upper/lower case distinctions are ignored for the purpose of counting syllables, but must be retained in the final output.</p>
		</li>
		<li>
		<p>Non-alphabetic characters are ignored for the purpose of counting syllables, but must be retained in the final output.</p>
		</li>
	</ul>
	</li>
	<li>
	<p>The characters 'A', 'E', 'I', 'O', 'U', and 'Y' are vowels. All other alphabetic characters are consonants.</p>

	<p>Exceptions to this rule:</p>

	<ul>
		<li>
		<p>The character sequence "QU" is considered to be a single consonant.</p>
		</li>
		<li>
		<p>The letter 'Y' is considered to be a consonant if it is immediately followed by one of the other vowels.</p>
		</li>
	</ul>
	</li>
	<li>
	<p>Every word has at least one syllable.</p>

	<p>For example, "Fly","I", "!?", and "Ssshhh!" are words of one syllable.</p>
	</li>
	<li>
	<p>Each (maximal) string of one or more consonants with at least one vowel to either side indicates a division into separate syllables.</p>

	<p>For example, "strong" has one syllable, "stronger" has <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>, and "bookkeeper" has <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>. "player" has two syllables (because the 'y', being followed by an 'e', is considered a consonant).</p>

	<p>Exceptions to this rule are:</p>

	<ul>
		<li>
		<p>An 'E' appearing as the last alphabetic character in a word is silent and should be ignored unless the next-to-last alphabetic character is an 'L' and the character immediately before that is another consonant.</p>

		<p>For example, "cake", "ale" and "pale" have one syllable. "able" has two.</p>
		</li>
		<li>
		<p>An 'ES' sequence at the end of the alphabetic sequence in a word does not add a syllable unless immediately preceded by two or more consonants.</p>

		<p>For example, "ales" and "pales" have one syllable. "witches" and "verses" have two.</p>
		</li>
	</ul>
	</li>
</ul>

### 입력 

 <p>Input will consist of a single line of text consisting of a sequence of one or more words (as defined above) separated by single blanks.</p>

<p>The total line length will not exceed <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$200$</span></mjx-container> characters.</p>

### 출력 

 <p>If the words in the input line can be divided into a haiku, then print the haiku as three lines of output.</p>

<ul>
	<li>Each line should be left-justified.</li>
	<li>A single space should separate each pair of words within a line.</li>
	<li>Upper/lower casing from the input should be preserved.</li>
	<li>Non-alphabetic characters terminating each word should be preserved.</li>
	<li>A word cannot be split across multiple lines.</li>
</ul>

<p>If the words in the input cannot be divided into a haiku, print the line of input with no changes.</p>

