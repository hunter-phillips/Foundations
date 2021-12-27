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
<table class="standard-table no-markdown">
  <thead>
    <tr>
      <th scope="col">Selector</th>
      <th scope="col">Example</th>
      <th scope="col">Learn CSS tutorial</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Type_selectors">Type selector</a></td>
      <td><code>h1 {&nbsp; }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors#type_selectors">Type selectors</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Universal_selectors">Universal selector</a></td>
      <td><code>* {&nbsp; }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors#the_universal_selector">The universal selector</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Class_selectors">Class selector</a></td>
      <td><code>.box {&nbsp; }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors#class_selectors">Class selectors</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/ID_selectors">id selector</a></td>
      <td><code>#unique { }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors#id_selectors">ID selectors</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Attribute_selectors">Attribute selector</a></td>
      <td><code>a[title] {&nbsp; }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Attribute_selectors">Attribute selectors</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Pseudo-classes">Pseudo-class selectors</a></td>
      <td><code>p:first-child { }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#what_is_a_pseudo-class">Pseudo-classes</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Pseudo-elements">Pseudo-element selectors</a></td>
      <td><code>p::first-line { }</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#what_is_a_pseudo-element">Pseudo-elements</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Descendant_combinator">Descendant combinator</a></td>
      <td><code>article p</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators#descendant_selector">Descendant combinator</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Child_combinator">Child combinator</a></td>
      <td><code>article &gt; p</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators#child_combinator">Child combinator</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/Adjacent_sibling_combinator">Adjacent sibling combinator</a></td>
      <td><code>h1 + p</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators#adjacent_sibling">Adjacent sibling</a></td>
    </tr>
    <tr>
      <td><a href="/en-US/docs/Web/CSS/General_sibling_combinator">General sibling combinator</a></td>
      <td><code>h1 ~ p</code></td>
      <td><a href="/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators#general_sibling">General sibling</a></td>
    </tr>
  </tbody>
</table>

