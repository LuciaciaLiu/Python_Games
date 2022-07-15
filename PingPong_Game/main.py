<html>
<head>
<title>main.py</title>
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
main.py</font>
</center></td></tr></table>
<pre><span class="s0"># 1. create the screen</span>
<span class="s2">from </span><span class="s1">turtle </span><span class="s2">import </span><span class="s1">Turtle</span><span class="s3">, </span><span class="s1">Screen</span>
<span class="s2">from </span><span class="s1">paddles </span><span class="s2">import </span><span class="s1">Paddle</span>
<span class="s2">from </span><span class="s1">ball </span><span class="s2">import </span><span class="s1">Ball</span>
<span class="s2">import </span><span class="s1">time</span>
<span class="s2">from </span><span class="s1">scoreboard </span><span class="s2">import </span><span class="s1">Scoreboard</span>


<span class="s1">screen = Screen()</span>
<span class="s1">screen.setup(width=</span><span class="s4">800</span><span class="s3">, </span><span class="s1">height=</span><span class="s4">600</span><span class="s1">)</span>
<span class="s1">screen.bgcolor(</span><span class="s5">'black'</span><span class="s1">)</span>
<span class="s1">screen.title(</span><span class="s5">&quot;Ping Pang Game&quot;</span><span class="s1">)</span>
<span class="s1">screen.tracer(</span><span class="s4">0</span><span class="s1">)</span>

<span class="s1">r_paddle = Paddle((</span><span class="s4">374</span><span class="s3">,</span><span class="s4">0</span><span class="s1">))</span>
<span class="s1">l_paddle = Paddle((-</span><span class="s4">384</span><span class="s3">,</span><span class="s4">0</span><span class="s1">))</span>
<span class="s1">ball = Ball()</span>
<span class="s1">scoreboard = Scoreboard()</span>

<span class="s1">screen.listen()  </span><span class="s0"># start listening</span>
<span class="s1">screen.onkey(fun=r_paddle.go_up</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'Up'</span><span class="s1">)</span>
<span class="s1">screen.onkey(fun=r_paddle.go_down</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'Down'</span><span class="s1">)</span>

<span class="s1">screen.onkey(fun=l_paddle.go_up</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'w'</span><span class="s1">)</span>
<span class="s1">screen.onkey(fun=l_paddle.go_down</span><span class="s3">, </span><span class="s1">key=</span><span class="s5">'s'</span><span class="s1">)</span>

<span class="s0"># 4. create moving ball</span>
<span class="s1">game_is_on = </span><span class="s2">True</span>

<span class="s2">while </span><span class="s1">game_is_on:</span>
    <span class="s1">time.sleep(</span><span class="s4">0.1</span><span class="s1">)</span>
    <span class="s1">screen.update()</span>
    <span class="s1">ball.ball_move()</span>
    <span class="s0"># 5. detect collision with wall and bounce</span>
    <span class="s2">if </span><span class="s1">ball.ycor() &gt; </span><span class="s4">280 </span><span class="s2">or </span><span class="s1">ball.ycor() &lt; -</span><span class="s4">280</span><span class="s1">:  </span><span class="s0"># bounce</span>
        <span class="s1">ball.bounce_y()</span>
    <span class="s0"># 6. detect collision with paddle</span>
    <span class="s2">if </span><span class="s1">ball.distance(r_paddle) &lt; </span><span class="s4">50 </span><span class="s2">and </span><span class="s1">ball.xcor()&gt;</span><span class="s4">340 </span><span class="s2">or </span><span class="s1">ball.distance(l_paddle) &lt; </span><span class="s4">50 </span><span class="s2">and </span><span class="s1">ball.xcor() &lt; -</span><span class="s4">350</span><span class="s1">:</span>
        <span class="s1">ball.bounce_x()</span>

    <span class="s0"># 7. detect when paddle misses</span>
    <span class="s2">if </span><span class="s1">ball.xcor() &gt; </span><span class="s4">370</span><span class="s1">:</span>
        <span class="s1">ball.reset_position()</span>
        <span class="s1">scoreboard.l_point()</span>

    <span class="s2">if </span><span class="s1">ball.xcor() &lt; -</span><span class="s4">380</span><span class="s1">:</span>
        <span class="s1">ball.reset_position()</span>
        <span class="s1">scoreboard.r_point()</span>

    <span class="s0"># 8. scoreboard</span>








</pre>
</body>
</html>