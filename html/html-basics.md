# HTML (HyperText Markup Language) Basics
- HTML is used to structure a webpage and its content.
- It is a series of elements that consist of an opening tag, content, and a closing tag:
    - `<p>Content</p>`
- It can contain an attribute, which contains extra information about the element:
    - `<p class='editor-note'>Content</p>`

## Element Nesting
- Elements can be nested inside of each other:
    - `<p>My cat is <strong>very</strong> grumpy.</p>`

## Empty Elements
- Some elements have no content, but they contain attributes that embed information.
    - `<img src='images/firefox-icon.png' alt='My test image'>`

## Basic Anatomy
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>My test page</title>
    </head>
    <body>

    </body>
    </html>
    ```
- `<!DOCTYPE html>` ensures that the document behaves correctly.
- `<html></html>` wraps all the content on the page and is known as the root element.
- `<head></head>` acts as a container for the elements that are not shown to a page's viewers.
- `<meta charset='utf-8'>` signifies that the document should use the UTF-8 charset, which includes characters from the vast majority of written languages.
- `<title></title>` sets the title that appears in the browser tab.
- `<body></body>` contains all the content that users will see.

## Essential Elements for Marking Up Text
### Headings
- HTML contains 6 heading levels `<h1>`-`<h6>`.
    ```
    <h1>My main title</h1>
    <h2>My top level heading</h2>
    <h3>My subheading</h3>
    <h4>My sub-subheading</h4>
    ```

### Paragraphs
- `<p>` elements contain paragraphs of text.
    `<p>This is a single paragraph</p>`

### Lists
- The most common lists are ordered and unordered.
    - Unordered lists have no inherit order, and they are wrapped in a `<ul>` element.
    - Ordered lists have an inherit order, and they are wrapped in an `<ol>` element.
    - Each item inside a list is placed in a `<li>` element.
    '''
    <ul>
        <li>technologists</li>
        <li>thinkers</li>
        <li>builders</li>
    </ul>
    '''

### Links
- Links make the web a web, and they are created using the `<a>` or anchor element. 
    - It takes an attribute called `href` that refers to hypertext reference.

   `<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>`

### Divs and Spans
- Divs and spans are generic elements that can contain anything.
    - `<div>`
    - `<span>`
- They are great "hook" elements that can be used for grouping related elements for styling.