# [Gold II] 새벽의 탐정 게임 - 25208 

[문제 링크](https://www.acmicpc.net/problem/25208) 

### 성능 요약

메모리: 213504 KB, 시간: 1204 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 구현

### 제출 일자

2023년 11월 13일 16:10:40

### 문제 설명

<p>새벽의 탐정 게임은 재미있는 2인용 보드게임이다. 한 명은 탐정, 다른 한 명은 도둑 역할을 맡는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a3b202e6-a324-4752-a49b-48dcc39531df/-/preview/"></p>

<p>게임은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>행 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>열 격자 위에서 진행된다. 격자의 각 칸은 벽이 설치되어 있거나 비어있고, 역할에 관계없이 벽 위에 서거나 벽을 넘어갈 수 없다. 임의의 두 빈칸은 상하좌우로 인접한 빈칸들을 거쳐 이동할 수 있다. 다시 말해 어느 빈칸에서 출발해도 다른 모든 빈칸으로 이동할 수 있다.</p>

<p>도둑은 밤 동안 은밀하게 어떤 칸으로 이동하고, 다시 밤이 찾아오기 전엔 그 칸에서 움직일 수 없다. 탐정은 새벽이 밝아오면 단서를 모아 도둑의 위치를 밝혀내고 감옥에 가두어야 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6aee3896-2c54-4dea-874d-521f6c60f4bc/-/preview/"></p>

<p>감옥은 위 전개도를 접은 모습이다. 다시 말해, 다섯 면이 막혀있고 나머지 한 면이 뚫려있는 정육면체이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cbcb4065-a7c8-4adc-8b61-59518cea3d7f/-/preview/"></p>

<p>탐정은 자신이 있는 칸에 감옥의 뚫린 면이 바닥을 향하게 하여 놓는다. 감옥은 상하좌우 중 벽이 없는 한 방향으로 굴릴 수 있고, 그에 따라 바닥을 향하는 면이 바뀌게 된다. 즉, 이동하려는 칸의 바닥과 수직으로 접하고 있는 면이 이동 후 바닥을 향하게 된다.</p>

<p>도둑을 감옥에 가두려면, 감옥의 뚫린 면이 바닥을 향할 때 도둑이 같은 칸에 있어야 한다. 만약 막힌 면이 바닥을 향할 때 도둑이 같은 칸에 있다면 도둑은 바로 승리를 선언하고 탐정은 패배하게 된다.</p>

<p>당신은 탐정 역할이고, 도둑의 위치를 특정했다. 이제 도둑을 감옥으로 가두기만 하면 승리할 수 있다. 당신의 위치와 도둑의 위치가 주어질 때, 감옥을 최소 몇 번 굴려야 당신이 게임에서 승리할 수 있을지 알아보자.</p>

### 입력 

 <p>첫 번째 줄에 보드의 크기 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 각각 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 문자로 보드의 상태가 주어진다. 벽이 있는 칸은 <code>#</code>, 빈칸은 <code>.</code>, 탐정의 위치는 <code>D</code>, 도둑의 위치는 <code>R</code>로 주어진다.</p>

### 출력 

 <p>탐정이 승리할 수 있다면 도둑을 가두는데 필요한 최소 이동 횟수를 출력한다.</p>

<p>그렇지 않다면 -1을 출력한다.</p>

