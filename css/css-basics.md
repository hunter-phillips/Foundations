# CSS (Cascading Style Sheets) Basics
- CSS is a style sheet language that is used for decorating and styling an HTML document.

## Creating and Connecting CSS to HTML
- A CSS file should be saved under the name `style.css` in a directory named `styles`.
- In the `<head>` of the HTML file, add a link to the CSS file:
    `<link rel='stylesheet' href='styles/style.css'>`

## Anatomy of a CSS ruleset
```
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```
- A ruleset contains to three parts:
    1. Selector: Defines the element to be styled
        - p, div, img, etc.
    2. Property: Specifies which properties to style
        - color, width, border, etc.
    3. Property Value: Sets the value of a property
        - red, 500px, solid, black, etc.

## Types of Selectors
<table>
  <thead>
    <tr>
      <th>Selector</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Type selector</td>
      <td><code>h1 {&nbsp; }</code></td>
    </tr>
    <tr>
      <td>Universal selector</td>
      <td><code>* {&nbsp; }</code></td>
    </tr>
    <tr>
      <td>Class selector</td>
      <td><code>.box {&nbsp; }</code></td>
    </tr>
    <tr>
      <td>id selector</td>
      <td><code>#unique { }</code></td>
    </tr>
    <tr>
      <td>Attribute selector</td>
      <td><code>a[title] {&nbsp; }</code></td>
    </tr>
    <tr>
      <td>Pseudo-class selectors</td>
      <td><code>p:first-child { }</code></td>
    </tr>
    <tr>
      <td>Pseudo-element selectors</td>
      <td><code>p::first-line { }</code></td>
    </tr>
    <tr>
      <td>Descendant combinator/td>
      <td><code>article p</code></td>
    </tr>
    <tr>
      <td>Child combinator</td>
      <td><code>article &gt; p</code></td>
    </tr>
    <tr>
      <td>Adjacent sibling combinator</td>
      <td><code>h1 + p</code></td>
    </tr>
    <tr>
      <td>General sibling combinator</td>
      <td><code>h1 ~ p</code></td>
    </tr>
  </tbody>
</table>

