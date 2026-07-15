<div align="center">
  <h1>📏 Unit Converter: Meters & Kilometers</h1>
  <p>A simple Python script that converts distances in both directions: meters to kilometers and kilometers to meters.</p>
</div>

<hr />

<h2>🛠️ Technologies Used</h2>
<ul>
  <li><strong>Language:</strong> Python 3</li>
  <li><strong>Libraries:</strong> None (uses only built-in Python features)</li>
</ul>

<h2>✨ Features</h2>
<ul>
  <li>↔️ <strong>Two-Way Conversion:</strong> Converts both meters to kilometers and kilometers to meters.</li>
  <li>🎯 <strong>Simple Menu:</strong> Lets the user choose the desired conversion type.</li>
  <li>⚠️ <strong>Error Handling:</strong> Uses <code>try-except</code> to handle invalid numeric input gracefully.</li>
  <li>⚡ <strong>Lightweight:</strong> Fast, minimal, and easy to run in any Python environment.</li>
</ul>

<h2>🚀 Installation</h2>
<ol>
  <li>Make sure Python 3 is installed on your system.</li>
  <li>Save the script as <code>Meters to kilometers.py</code>.</li>
  <li>Open a terminal or command prompt.</li>
  <li>Run the file with the following command:</li>
</ol>

<pre><code>python "Meters to kilometers.py"</code></pre>

<h2>⚙️ How It Works</h2>
<p>
The program first asks the user to choose a conversion mode:
</p>
<ul>
  <li><strong>1</strong> → Meters to kilometers</li>
  <li><strong>2</strong> → Kilometers to meters</li>
</ul>
<p>
Then it asks for a numeric value and performs the selected conversion.
If the entered value is not a valid number, the program displays an error message.
</p>

<h2>📥 Input & Output</h2>

<h3>Example 1: Meters to Kilometers</h3>
<p><strong>Input:</strong></p>
<pre><code>Select Convert. 1.Meters to kilometers  2.Kilometer to meter
Choose:1
meter:5000</code></pre>

<p><strong>Output:</strong></p>
<pre><code>Kilometer: 5.0</code></pre>

<h3>Example 2: Kilometers to Meters</h3>
<p><strong>Input:</strong></p>
<pre><code>Select Convert. 1.Meters to kilometers  2.Kilometer to meter
Choose:2
meter:5</code></pre>

<p><strong>Output:</strong></p>
<pre><code>meter: 5000.0</code></pre>

<h3>Example 3: Invalid Input</h3>
<p><strong>Input:</strong></p>
<pre><code>Choose:1
meter:abc</code></pre>

<p><strong>Output:</strong></p>
<pre><code>Error: The entered value is not a valid number.</code></pre>
