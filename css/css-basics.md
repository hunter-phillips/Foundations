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
<a href='https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#reference_table_of_selectors'>MDN Selectors</a>

## Specificity 
- When an element has multiple, conflicting declaration targeting it, specificity determines which values to use.
- From most to least specific:
    1. ID Selector
    2. Class Selector
    3. Type Selector
- If two items have the same amount of specificity, whichever comes second will appear.

## Fonts
### Font Properties
| Property     | Options                       | Description                          | Example                                |
|--------------|-------------------------------|--------------------------------------|----------------------------------------|
| font-family  | Times, sans-serif, etc.       | change the font family               | `font-family: Times, serif;`           |
| font-style   | normal, oblique, italics      | change text                          | `font-style: normal;`                  |
| font-variant | normal, small-caps            | display font in normal or small caps | `font-variant: small-caps;`            |
| font-weight  | 1-1000; normal, bold          | specify the weight of the font       | `font-weight: bold;`                   |
| font-size    | large; larger; px; em; rem; % | modify the size of font              | `font-size: 12px;`                     |

### Add Custom Font From Google
- Go to <a href='https://fonts.google.com/'>Google Fonts</a> and select the fonts.
- Copy the `<link>` of the selected families and paste them into the `<head>`.
    ```
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet"> 
    ```

## Color and Background Properties
| Property            | Options                          | Description                                   | Example                                   |
|---------------------|----------------------------------|-----------------------------------------------|-------------------------------------------|
| color               | rgb, hex, names, rgba, etc.      | change the color of text                      | `color: #000080;`                         |
| background-color    | ibid.                            | changes the background color of an element    | `background-color: white;`                |
| background-image    | absolute or relative link        | changes the background image of an element    | `background-image: url(/images/foo.gif);` |
| background-repeat   | repeat-x; repeat-y; no-repeat    | determines how a background image is repeated | `background-repeat: repeat-x'`            |
| background-position | top; bottom; left; right; center | initial position of the background image      | `background-position: center;`            |

## Text Properties
| Property        | Options                                        | Description                                            | Example                      |
|-----------------|------------------------------------------------|--------------------------------------------------------|------------------------------|
| word-spacing    | em, rem, px, etc.                              | changes the spacing between words                      | `word-spacing: 0.4em;`       |
| letter-spacing  | ibid.                                          | sets the amount of space between characters            | `letter-spacing: 0.1em;`     |
| text-decoration | underline, overline, line-through, blink, none | decorates the text                                     | `text-decoration: none;`     |
| vertical-align  | baseline, middle, top, bottom, etc.            | vertically aligns inline elements relative to a parent | `vertical-align: middle;`    |
| text-transform  | capitalize, uppercase, lowercase; none         | changes capitalization of text                         | `text-transform: uppercase;` |
| text-align      | left, center, right, justify                   | aligns text horiztonally                               | `text-align: center;`        |