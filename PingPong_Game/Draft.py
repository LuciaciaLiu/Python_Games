<html>
<head>
<title>Draft.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #7ec3e6;}
.s1 { color: #ebebeb;}
.s2 { color: #ed864a;}
.s3 { color: #ed864a; font-weight: bold;}
.s4 { color: #33ccff; font-weight: bold;}
.s5 { color: #54b33e;}
</style>
</head>
<body bgcolor="#131314">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Draft.py</font>
</center></td></tr></table>
<pre><span class="s0"># 1. create the screen</span>
<span class="s0"># 2. create and  move paddle</span>
<span class="s0"># 3. create and  move another paddle</span>
<span class="s0"># 4. create moving ball</span>

<span class="s0"># 5. detect collision with wall and bounce</span>
<span class="s0"># 6. detect collision with paddle</span>
<span class="s0"># 7. detect when paddle misses</span>

<span class="s0"># 8. scoreboard</span>


<span class="s0"># 1. create the screen</span>
<span class="s2">from </span><span class="s1">turtle </span><span class="s2">import </span><span class="s1">Turtle</span><span class="s3">, </span><span class="s1">Screen</span>
<span class="s2">import </span><span class="s1">time</span>

<span class="s1">screen = Screen()</span>
<span class="s1">screen.setup(width=</span><span class="s4">800</span><span class="s3">, </span><span class="s1">height=</span><span class="s4">600</span><span class="s1">)</span>
<span class="s1">screen.bgcolor(</span><span class="s5">'black'</span><span class="s1">)</span>
<span class="s1">screen.title(</span><span class="s5">&quot;Ping Pang Game&quot;</span><span class="s1">)</span>
<span class="s1">screen.tracer(</span><span class="s4">0</span><span class="s1">)</span>

<span class="s0"># 2.1 create paddles</span>
<span class="s1">paddle = Turtle()</span>
<span class="s1">paddle.shape(</span><span class="s5">'square'</span><span class="s1">)</span>
<span class="s1">paddle.color(</span><span class="s5">'white'</span><span class="s1">)</span>
<span class="s1">paddle.shapesize(stretch_wid=</span><span class="s4">5</span><span class="s3">, </span><span class="s1">stretch_len=</span><span class="s4">1</span><span class="s1">)</span>
<span class="s1">paddle.penup()</span>
<span class="s1">paddle.goto(</span><span class="s4">370</span><span class="s3">, </span><span class="s4">0</span><span class="s1">)</span>


<span class="s0"># 2.2 move paddles</span>
<span class="s2">def </span><span class="s1">go_up():</span>
    <span class="s1">new_y = paddle.ycor() + </span><span class="s4">20</span>
    <span class="s1">paddle.goto(paddle.xcor()</span><span class="s3">, </span><span class="s1">new_y)</span>


<span class="s2">def </span><span class="s1">go_down():</span>
    <span class="s1">new_y = paddle.ycor() - </span><span class="s4">20</span>
    <span class="s1">paddle.goto(paddle.xcor()</span><span class="s3">, </span><span class="s1">new_y)</span>


<span class="s1">screen.listen()  </span><span class="s0"># start listening</span>
<span class="s1">screen.onkey(fun=go_up</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'Up'</span><span class="s1">)</span>
<span class="s1">screen.onkey(fun=go_down</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'Down'</span><span class="s1">)</span>

<span class="s1">game_is_on = </span><span class="s2">True</span>
<span class="s2">while </span><span class="s1">game_is_on:</span>
    <span class="s1">screen.update()</span>












<span class="s1">screen.exitonclick()</span>
</pre>
</body>
</html>