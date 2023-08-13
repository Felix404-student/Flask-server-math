# Flask-server-math
Simple Python/Flask server implemntation for using URL query parameters

<div class="section" id="step-zero-setup-your-environment">
<h2>Step Zero: Setup Your Environment</h2>
<p>It will be more convenient if you always have an “environmental variable”
that sets <cite>FLASK_ENV</cite> to “development”, so you don’t have to do that
every time you open a new terminal window.</p>
<p>You can configure this in your <cite>~/.bash_profile</cite>. To confirm, open up this file in VSCode:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>code ~/.bash_profile
</pre></div>
</div>
<p>Add the following line to it, if you don’t have this line already included:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span> <span class="nv">FLASK_ENV</span><span class="o">=</span>development
</pre></div>
</div>
<p><strong>Close this terminal window and open a new one.</strong></p>
<p>Test that this works like this:</p>
<pre class="console literal-block">
$ <span class="cmd">echo $FLASK_ENV</span>
development
</pre>
</div>
<div class="section" id="set-up-your-project">
<h2>Set Up Your Project</h2>
<p>Download the starter code. You’ll get a directory with two directories
in it:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">flask</span><span class="o">-</span><span class="n">greet</span><span class="o">-</span><span class="n">calc</span><span class="o">/</span>
  <span class="n">greet</span><span class="o">/</span>
  <span class="n">calc</span><span class="o">/</span>
</pre></div>
</div>
<p>At the top level of this (inside <cite>flask-greet-calc</cite>), create a
virtual environment:</p>
<pre class="console literal-block">
$ <span class="cmd">python3 -m venv venv</span>
</pre>
<p>Start using your venv:</p>
<pre class="console literal-block">
$ <span class="cmd">source venv/bin/activate</span>
(env) $
</pre>
<p>Install Flask:</p>
<pre class="console literal-block">
(env) $ <span class="cmd">pip3 install flask</span>
...
</pre>
<p>Make a “requirements.txt” file in this directory with a listing of
all the software needed for this project:</p>
<pre class="console literal-block">
(env) $ <span class="cmd">pip3 freeze &gt; requirements.txt</span>
</pre>
<p>(you can look at that file with <code class="docutils literal notranslate"><span class="pre">cat</span> <span class="pre">requirements.txt</span></code>)</p>
</div>
<div class="section" id="set-up-git">
<h2>Set Up Git</h2>
<p>We want you to add this project to Git, so let’s make our project
a Git repository:</p>
<pre class="console literal-block">
(env) $ <span class="cmd">git init</span>
</pre>
<p>Then, since we <strong>don’t</strong> want the <cite>venv/</cite> folder put into Git (or
send to GitHub), put it in a file called <cite>.gitignore</cite> (notice the
leading dot!). Inside that file should be this line:</p>
<div class="literal-block-wrapper docutils container" id="id1">
<div class="code-block-caption"><span class="caption-text">.gitignore</span></div>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>venv/
</pre></div>
</div>
</div>
<p>(which means “ignore all folders named <cite>venv/</cite> anywhere here and below,
as far as git is concerned”)</p>
<p>You should test that Git is ignoring this file by making sure it doesn’t
appear as an untracked file in <cite>git status</cite>:</p>
<pre class="console literal-block">
(env) $ <span class="cmd">git status</span>
</pre>
</div>
<div class="section" id="greet">
<h2>Greet</h2>
<p>In the <cite>greet</cite> folder, Make a simple Flask app that responds to these
routes with simple text messages:</p>
<dl class="docutils">
<dt><cite>/welcome</cite></dt><dd>Returns “welcome”</dd>
<dt><cite>/welcome/home</cite></dt><dd>Returns “welcome home”</dd>
<dt><cite>/welcome/back</cite></dt><dd>Return “welcome back”</dd>
</dl>
<p>Once you’ve finished this, run the tests for it:</p>
<pre class="console literal-block">
$ <span class="cmd">python3 -m unittest test.py</span>
</pre>
</div>
<div class="section" id="calc">
<h2>Calc</h2>
<p>Build a simple calculator with Flask, which uses URL query parameters
to get the numbers to calculate with.</p>
<p>Make a Flask app that responds to 4 different routes. Each route does a math
operation with two numbers, <cite>a</cite> and <cite>b</cite>,  which will be passed in as URL
GET-style query parameters.</p>
<dl class="docutils">
<dt><cite>/add</cite></dt><dd>Adds <cite>a</cite> and <cite>b</cite> and returns result as the body.</dd>
<dt><cite>/sub</cite></dt><dd>Same, subtracting <cite>b</cite> from <cite>a</cite>.</dd>
<dt><cite>/mult</cite></dt><dd>Same, multiplying <cite>a</cite> and <cite>b</cite>.</dd>
<dt><cite>/div</cite></dt><dd>Same, dividing <cite>a</cite> by <cite>b</cite>.</dd>
</dl>
<p>For example, a URL like <cite>http://localhost:5000/add?a=10&amp;b=20</cite> should return
a string response of exactly <strong>30</strong>.</p>
<p>Write the routes for this but <strong>don’t hardcode the math operation in your
route function</strong> directly.
Instead, we’ve provided helper functions for this in the file <cite>operations.py</cite>:</p>
<div class="literal-block-wrapper docutils container" id="id2">
<div class="code-block-caption"><span class="caption-text">calc/operations.py</span></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="sd">&quot;&quot;&quot;Basic math operations.&quot;&quot;&quot;</span>

<span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Add a and b.&quot;&quot;&quot;</span>
    
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="k">def</span> <span class="nf">sub</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Substract b from a.&quot;&quot;&quot;</span>

    <span class="k">return</span> <span class="n">a</span> <span class="o">-</span> <span class="n">b</span>

<span class="k">def</span> <span class="nf">mult</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Multiply a and b.&quot;&quot;&quot;</span>

    <span class="k">return</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span>

<span class="k">def</span> <span class="nf">div</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Divide a by b.&quot;&quot;&quot;</span>

    <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>
</pre></div>
</div>
</div>
<p>Import and use these in your routes.</p>
<p>After you’ve tried out your app, run the unit tests:</p>
<pre class="console literal-block">
$ <span class="cmd">python3 -m unittest test.py</span>
</pre>
</div>
<div class="section" id="further-study">
<h2>Further Study</h2>
<p>You probably have a lot of code duplication in your <cite>calc</cite> routes, given
that you’re doing such similar things in each.</p>
<p>Make a single route/view function that can deal with 4 different kinds of URLs:</p>
<ul class="simple">
<li><cite>/math/add</cite></li>
<li><cite>/math/sub</cite></li>
<li><cite>/math/mult</cite></li>
<li><cite>/math/div</cite></li>
</ul>
<p>You can write this in one function with one route by using a route parameter
for the actual operation (“add”, “sub”, etc).</p>
<p>As an extra-bonus, see if you can find a way to do this in the route without
a whole series of if/elif statements. One good way is to use a dictionary
to map operation names to the functions that do the underlying math.</p>
</div>
</div>
