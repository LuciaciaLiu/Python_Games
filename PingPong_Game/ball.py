<html>
<head>
<title>ball.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #ed864a;}
.s1 { color: #ebebeb;}
.s2 { color: #54b33e;}
.s3 { color: #33ccff; font-weight: bold;}
.s4 { color: #ed864a; font-weight: bold;}
.s5 { color: #7ec3e6;}
</style>
</head>
<body bgcolor="#131314">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
ball.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>


<span class="s0">class </span><span class="s1">Ball(Turtle):</span>
    <span class="s0">def </span><span class="s1">__init__(self):</span>
        <span class="s1">super().__init__()</span>
        <span class="s1">self.shape(</span><span class="s2">'circle'</span><span class="s1">)</span>
        <span class="s1">self.color(</span><span class="s2">'white'</span><span class="s1">)</span>
        <span class="s1">self.penup()</span>
        <span class="s1">self.goto(</span><span class="s3">0</span><span class="s4">, </span><span class="s3">0</span><span class="s1">)</span>
        <span class="s1">self.x_move = </span><span class="s3">10</span>
        <span class="s1">self.y_move = </span><span class="s3">10</span>
        <span class="s1">self.move_speed = </span><span class="s3">0.2</span>

    <span class="s5"># 4. create moving ball</span>
    <span class="s0">def </span><span class="s1">ball_move(self):</span>
        <span class="s1">new_x = self.xcor() + self.x_move</span>
        <span class="s1">new_y = self.ycor() + self.y_move</span>
        <span class="s1">self.goto(new_x</span><span class="s4">, </span><span class="s1">new_y)</span>

    <span class="s0">def </span><span class="s1">bounce_y(self):</span>
        <span class="s1">self.y_move *= -</span><span class="s3">1</span>
        <span class="s1">self.move_speed * </span><span class="s3">0.8</span>

    <span class="s0">def </span><span class="s1">bounce_x(self):</span>
        <span class="s1">self.x_move *= -</span><span class="s3">1</span>

    <span class="s0">def </span><span class="s1">reset_position(self):</span>
        <span class="s1">self.goto(</span><span class="s3">0</span><span class="s4">,</span><span class="s3">0</span><span class="s1">)</span>
        <span class="s1">self.bounce_x()</span>

</pre>
</body>
</html>