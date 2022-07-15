<html>
<head>
<title>paddles.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #ed864a;}
.s1 { color: #ebebeb;}
.s2 { color: #7ec3e6;}
.s3 { color: #ed864a; font-weight: bold;}
.s4 { color: #54b33e;}
.s5 { color: #33ccff; font-weight: bold;}
</style>
</head>
<body bgcolor="#131314">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
paddles.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>


<span class="s0">class </span><span class="s1">Paddle(Turtle):</span>
    <span class="s2"># 2.1 create paddle</span>
    <span class="s0">def </span><span class="s1">__init__(self</span><span class="s3">,</span><span class="s1">position ):</span>
        <span class="s1">super().__init__()</span>
        <span class="s1">self.shape(</span><span class="s4">'square'</span><span class="s1">)</span>
        <span class="s1">self.color(</span><span class="s4">'white'</span><span class="s1">)</span>
        <span class="s1">self.shapesize(stretch_wid=</span><span class="s5">5</span><span class="s3">, </span><span class="s1">stretch_len=</span><span class="s5">1</span><span class="s1">)</span>
        <span class="s1">self.penup()</span>
        <span class="s1">self.goto(position)</span>

    <span class="s2"># 2.2 move paddle</span>

    <span class="s0">def </span><span class="s1">go_up(self):</span>
        <span class="s1">new_y = self.ycor() + </span><span class="s5">20</span>
        <span class="s1">self.goto(self.xcor()</span><span class="s3">, </span><span class="s1">new_y)</span>

    <span class="s0">def </span><span class="s1">go_down(self):</span>
        <span class="s1">new_y = self.ycor() - </span><span class="s5">20</span>
        <span class="s1">self.goto(self.xcor()</span><span class="s3">, </span><span class="s1">new_y)</span>
</pre>
</body>
</html>