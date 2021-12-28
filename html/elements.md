# Elements Reference
## Main Root
- `<html lang='en'></html>`
    - Top-level element, known as the root element, which all elements must be a descendant of.

## Metadata
- Metadata is information about the page, such as styles, scripts, and data, that help software use and render the page.
    - `<base href=''>`
        - Specifies the base URL for all relative URLs
    - `<head></head>`
        - Contains the title, scripts, and style sheets
    - `<link rel='' href=''>`
        - Specifies the relationship between the current document and an external resource
            - Used to link to css through `rel='stylesheet`
            - Used for favicon through `rel='icon'`
    - `<meta>`
        - Represents other meta-related elements
            - `<meta charset='utf-8'>`
    - `<style></style>`
        - Contains style information for a document
    - `<title></title>`
        - Defines the title shown in a page's tab

## Sectioning Root
- `<body></body>`
    - Represents the content of an HTML document

## Content Sectioning
- Content sectioning organizes the content into logical pieces.
    - `<address></address>`
        - Contains contact information for a person, group, or organization (email, address, phone number)
    - `<article></article>`
        - Represents a self-contained composition that is intended to be independently reusable (forum posts, newspaper articles, blog entries, user-submitted content, etc.)
    - `<aside></aside>` 
        - Represents content that is only indirectly related tot he document's main content (sidebars, call-out boxes)
    - `<footer></footer>`
        - Represents a footer for its nearest sectioning content or sectioning root element
        - Contains information about the author, copyright data, or related links
    - `<header></header>`
        - Represents introductory content, such as navigational aids, search forms, logos, author names, etc.
    - `<h1></h1>` through `<h6></h6>`
        - Represent levels of section headings
    - `<main></main>`
        - Represents the dominant content of the `<body>` of a document
        - Contains content that is directly related or expands upon the central topic of a document
    - `<nav></nav>`
        - Represents a section of a page whose purpose is to provide navigation links
    - `<section></section>`
        - Represents a genertic standalone section of a document that doesn't have a more specific semantic element to represent it
        - Should always have a heading

## Text Content
- Text content organizes blocks or sections of content in the `<body>`.
    - `<blockquote cite=''></blockquote>`
        - Indicates that the enclosed text is an extended quotation
    - `<dl></dl>`
        - Represents a description list that encloses terms, `<dt>`, and descriptions, `<dd>`
        - Used for a glossary or lists of key-value pairs, such as metadata
    -`<dt></dt>`
        - Specifices a term in a description list
        - Usually followed by more `<dt>` elements or a `<dd>`
    - `<dd></dd>`
        - Provides the definition or description for a `<dt>` in a `<dl>`
    - `<div></div>`
        - A generic container for flow content that is styled using CSS
    - `<figure></figure>`
        - Represents self-contained content, potentially with an optional caption
        - Contains an `<img>`, diagram, or codesnippet
        - A `<figcaption>` can be used for a caption
    - `<figcaption></figcaption>`
        - Represents a caption or legend describing the rest of the contents of a `<figure>`
    - `<hr>`
        - Represents a thematic break between paragraph-level elements
    - `<ol></ol>`
        - Represents an ordered list of items, `<li>`
        - Often rendered as a numbered list
    - `<li></li>`
        - Represents an item in an `<ol>` or an `<ul>`
    - `<ul></ul>`
        - Represents an unordered list of items, typically rendered as a bulleted list
    - `<p></p>`
        - Represents a paragraph of any structural grouping of related content
    - `<pre></pre>`
        - Represents preformatted text which is to be presented exactly as written in the HTML file
            - Whitespace is preserved


## Inline text semantics
- Inline text semantics define the meaning, structure, or style of a word, line, or text.
    - `<a href=''></a>`
        - Creates a hyperlink to other locations or webpages
    - `<abbr title=''></abbr>`
        - Represents an abbreviation or acronym
        - `title` is used to provide a description for the abbreviation
    - `<b></b>`
        - Draws a reader's attention to the element's contents that are not otherwise granted special importantance
    - `<bdi></bdi>`
        - Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text
            - Arabic, Urdu, etc.
    - `<bdo></bdo>`
        - Overrides the current directionality of text, rendering it in a different direction
    - `<br>`
        - Produces a line break in text (carriage-return)
    - `<cite></cite>`
        - Describes a reference to cited creative work
    - `<code></code>`
        - Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code
    - `<data value=''></data>`
        - Links a given piece of content with a machine-readable translation
    - `<dfn></dfn>`
        - Indicates the term being defined within the context of a definition phrase or sentence
    - `<em></em>`
        - Marks text that has stress emphasis
        - Can be nested, with each level indicating a greater degree of emphasis
    - `<i></i>`
        - Represents text set off from the original for some reason, such as idiomatic text, technical terms, etc.
    - `<kbd></kbd>`
        - Represents a span of inline text denotating textual user input from a keyboard, voice input, or an entry device
    - `<mark></mark>`
        - Represents text marked or highlighted for reference or notation purposes
    - `<q cite=''></q>`
        - Indicates that the enclosed text is a short inline quotation
    - `<s></s>`
        - Represents things that are no longer relevant or accurate
    - `<samp></samp>`
        - Represents sample output from a computer program
    - `<small></small>`
        - Represents side-comments and small print, like copyright and legal text, independent of its styled presentation
    - `<span></span>`
        - Represents a generic inline container for phrasing content, which does not inherently represent anything
        - Used for styling
    - `<strong></strong>`
        - Indicates that its contents have strong importance, seriousness, or urgency
    - `<sub></sub>`
        - Specifies inline text which should be displayed as subscript
            - Rendered with a lowered baseline using smaller text
    - `<sup></sup>`
        - Specifies inline text which is to be displayed as superscript
            - Rendered with a raised baseine using smaller text
    - `<time datetime=''></time>`
        - Represents a specific period in time
        - May include the `datetime` attribute to translate dates into machine-readable format
    - `<u></u>`
        - Represents a span of inline text which should be rendered in a way that indicates it has a non-textual annotation
            - Underline is a typical rendering
    - `<var></var>`
        - Represents the name of a variable in a mathematical expression or a programming context
    - `<wbr>`
        - Indicates a position within a text where the browser may optionally break a line

## Image and Multimedia
- `<area></area>`
    - Defines an area inside of an image map that has predefined clickable areas
- `<audio controls src=''></audio>`
    - Embeds sound content in documents
    - May contain one or more audio sources, and the browser will choose the most suitable one
- `<img src='' alt=''>`
    - Embeds an image into the document
    - The `usemap` attribute can be used with the `#name` value to use an image map
- `<map></map>`
    - Used with `<area>` elements to define an image map ( a clickable link area)
- `<track default kind='captions' srclang='' src=''/>`
    - Used as a child of `<audio>` and `<video>`
        - It can be used to specify timed text tracks that are formatted in WebVTT (`.vtt`)
    - Can be used for subtitles, captions, descriptions, etc.
- `<video controls src=''></video>`
    - Embeds a media player which supports video playback into the document

## Embedded Content
- `<embed type ='' src=''>`
    - Embeds external content
- `<iframe id='' title='' src=''></iframe>`
    - Represents nested browsing context, embedding another HTML page into the current one
- `<object type='application/pdf' data='path'></object>`
    - Represents an external resource that can be treated as an image, a nested browsing context, or a resource to be handled by a plugin
- ```<picture>
        <source srcset='' media='(min-width: 500px)'>
        <img src='' alt=''>
    </picture>
  ```
    - Contains zero or more `<source>` elements and one `<img>` element to offer alternative versions of an image for different display/device scenarios
- `<portal src=''></portal>`
    - Embeds another HTML page that cannot be interacted with
    - Offers a preview of the content of anotehr page
- `<source src='' type=''>`
    - Specificies multiple media resources for the `<picture>`, `<audio>`, and `<video>` elements

## SVG and MathML
- `<svg></svg>`
    - A container that defines a new coordinate system and viewport for SVG documents or fragments
- `<math></math>`
    - Used for math annotation

## Scripting
- To create dynamic content, scripting languages can be used.
    - `<canvas></canvas>`
        - Used for drawing graphics and animations
    - `<noscript></noscript>`
        - Defines HTML to be inserted if scripting is currently turned off
    - `<script src=''><script>`
        - Used to embed executable code or data

## Demarcating Edits
- These markings provide indications that specific parts of the text have been altered.
    - `<del></del>`
        - Represents a range of text that has been deleted from a document
    - `<ins></ins>`
        - Represents a range of text that has been added to a document

## Table Content
- `<caption></caption>`
    - Defines the caption or title of a table
- `<col></col>`
    - Defines a column within a table and is used for defining common semantics on all common cells
        - Often used in a `<colgroup>` element
- `<colgroup></colgroup>`
    - Defines a group of columns within a table
- `<table></table>`
    - Represents tabular data
- `<tbody></tbody>`
    - Represents `<tr>` elements that makeup of the body
- `<td></td>`
    - Defines a cell of a table that contains data
- `<tfoot></tfoot>`
    - Represents `<tr>` elements that makeup the footer
- `<th></th>`
    - Defines a cell of a table as a header
- `<thead></thead>`
    - Represents `<tr>` elements that makeup the header
- `<tr></tr>`
    - Defines a row of cells

## Forms
- `<button type=''><button>`
    - Represents a clickable button that is used to submit forms
- `<datalist id=''></datalist>`
    - A datalist contains a set of `<option>` elements that can be used within other inputs by utilizing the `list` attribute in an `<input>` 
- `<fieldlist></fieldlist>`
    - Used to group controls and labels
    - Click <a href='https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset'>here</a> for usage
- `<form action='' method=''></form>`
    - Represents a document section containing interactive controls for submitting information
- `<input type='' name='' id=''>`
    - Creates interactive controls for web-based forms in order to accept data from the user
- `<label for=''></label>`
    - Represents a caption for an item
- `<legend></legend>`
    - Represents a caption for a `<fieldset>`
- `<meter min='' max='' value=''></meter>`
    - Represents a scalar value within a known range
- `<optgroup label=''></optgroup>`
    - Creates a grouping of options within a `<select>`
- `<option value=''></option>`
    - Defines an item contained in a `<select>`, `<optgroup>`, or `<datalist>`
- `<output name='' for''></output>`
    - Defines a container element into which a site or app can inject the results of a calculation or outcome
- `<progress id='' max='' value=''></progress>`
    - Displays an indicator showing the completion progress of a task
- `<select name='' id=''></select>`
    - Represents a control that provides a menu of options
- `<textarea name='' id='' rows='' cols=''></textarea>`
    - Represents a multi-line plain-text editing control

## Interactive Elements
- ```
    <details>
        <summary></summary>
    </details>
  ```
    - Creates a disclosure widget that only shows information when it is toggled to an "open" state
- `<dialog></dialog>`
    - Represents a dialog box or other interactive component
- `<menu></menu>`
    - Semantic alternative to ul with items that represent a link or other command that the user can activate (experimental)
- `<summary></summary>`
    - Specifices a summary, capation, or legend for a `details` disclosure box

## Web Components
- `<slot></slot>`
    - A placeholder that can be filled with markup
- `<template></template>`
    - A mechanism for holding HTML that is not to be rendered immediately when a page is loaded