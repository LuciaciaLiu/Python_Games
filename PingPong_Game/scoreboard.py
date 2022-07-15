<html>
<head>
<title>scoreboard.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #ed864a;}
.s1 { color: #ebebeb;}
.s2 { color: #33ccff; font-weight: bold;}
.s3 { color: #ed864a; font-weight: bold;}
.s4 { color: #54b33e;}
</style>
</head>
<body bgcolor="#131314">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
scoreboard.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>


<span class="s0">class </span><span class="s1">Scoreboard(Turtle):</span>
    <span class="s0">def </span><span class="s1">__init__(self):</span>
        <span class="s1">super().__init__()</span>
        <span class="s1">self.goto(</span><span class="s2">30</span><span class="s3">, </span><span class="s2">270</span><span class="s1">)</span>
        <span class="s1">self.color(</span><span class="s4">'white'</span><span class="s1">)</span>
        <span class="s1">self.penup()</span>

        <span class="s1">self.l_score = </span><span class="s2">0</span>
        <span class="s1">self.r_score = </span><span class="s2">0</span>
        <span class="s1">self.hideturtle()</span>
        <span class="s1">self.update_scoreboard()</span>


    <span class="s0">def </span><span class="s1">update_scoreboard(self):</span>
        <span class="s1">self.clear()</span>
        <span class="s1">self.goto(-</span><span class="s2">100</span><span class="s3">, </span><span class="s2">200</span><span class="s1">)</span>
        <span class="s1">self.write(self.l_score</span><span class="s3">, </span><span class="s1">align=</span><span class="s4">'center'</span><span class="s3">, </span><span class="s1">font=(</span><span class="s4">'Arial'</span><span class="s3">, </span><span class="s2">80</span><span class="s3">, </span><span class="s4">'normal'</span><span class="s1">))</span>
        <span class="s1">self.goto(</span><span class="s2">100</span><span class="s3">, </span><span class="s2">200</span><span class="s1">)</span>
        <span class="s1">self.write(self.r_score</span><span class="s3">, </span><span class="s1">align=</span><span class="s4">'center'</span><span class="s3">, </span><span class="s1">font=(</span><span class="s4">'Arial'</span><span class="s3">, </span><span class="s2">80</span><span class="s3">, </span><span class="s4">'normal'</span><span class="s1">))</span>

    <span class="s0">def </span><span class="s1">l_point(self):</span>
        <span class="s1">self.l_score += </span><span class="s2">1</span>
        <span class="s1">self.update_scoreboard()</span>

    <span class="s0">def </span><span class="s1">r_point(self):</span>
        <span class="s1">self.r_score += </span><span class="s2">1</span>
        <span class="s1">self.update_scoreboard()</span></pre>
</body>
</html>