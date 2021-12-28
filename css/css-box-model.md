# The Box Model
- Everything on a webpage, at its simplest, is a rectangular box.
<img href='https://cdn.statically.io/gh/TheOdinProject/curriculum/main/foundations/html_css/the-box-model/imgs/boxes.png'>

## Display: Block and Inline Boxes
### Block
- Elements with a display type of `block` will:
    - Break onto a new line
    - Padding, margin, and border cause other elements to be pushed away
    - Width and height are respected
    - Box fills the entire space available in its container
- `<h1>` and `<p>` are examples.
### Inline
- Elements with an outer display type of `inline` will:
    - Not break onto a new line
    - Width and height properties do not apply
    - Vertical padding, margins, and borders will apply but will not cause other inline boxes to move away
    - Horiztonal padding, margins, and borders will apply and will cause other inline boxes to move away
- `<a>`, `<span>`, and `<em>` are examples.
### Inline-Block
- Elements with `display: inline-block` will:
    - Not break onto a new line
    - Width and height properties are respected
    - Padding, margin, and border cause other elements to be pushed away


## Breaking Down the Box Model
<img href='https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model/box-model.png'>
- There are four main components of a box:
    - `content`: area where content is displayed that can be sized using `width` and `height`
    - `padding`: increases the space between the border of a box and the content inside of it
    - `border`: adds space between the padding and the margin
    - `margin`: increases the space between a box and any others that sit next to it
- When two elements are next to each other, the largest margin is used because they collapse into each other.
    - If both elements had a margin of 60px, the total margin between them is only 60px, not 120px.
- If the `box-sizing` property is set to `border-box`, the total height and width of the entire box will be whatever `height` and `width` are set to.

## Margin Properties
| Property      | Description                                                                          | Example                                                             |
|---------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| margin-top    | sets the top margin                                                                  | `margin-top: 5px;`                                                  |
| margin-right  | sets the right margin                                                                | `margin-right: 50%;`                                                |
| margin-bottom | sets the bottom margin                                                               | `margin-bottom: 3em;`                                               |
| margin-left   | sets the left margin                                                                 | `margin-left: 1rem;`                                                |
| margin        | set top/bottom and left/right<br>set all margins<br>set top, right, left, and bottom | `margin: 2em 4em;`<br>`margin: 5px;`<br>`margin:  1em 2em 3em 4em;` |

- To horiztonally center an element, set its `width` and then use the following margin: 
    - `margin: 0 auto;`
## Padding Properties
| Property      | Description                                                                          | Example                                                             |
|---------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| padding-top    | sets the top padding                                                                  | `padding-top: 5px;`                                                  |
| padding-right  | sets the right padding                                                                | `padding-right: 50%;`                                                |
| padding-bottom | sets the bottom padding                                                               | `padding-bottom: 3em;`                                               |
| padding-left   | sets the left padding                                                                 | `padding-left: 1rem;`                                                |
| padding        | set top/bottom and left/right<br>set all paddings<br>set top, right, left, and bottom | `padding: 2em 4em;`<br>`padding: 5px;`<br>`padding:  1em 2em 3em 4em;` |

## Border Properties
| Property            | Description                                                                                        | Example                                                    |
|---------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| border-width        | sets the width of all of the borders<br>sets the width of the top, right, bottom, and left borders | `border-width: 5px;`<br>`border-width: 10px 5px 10px 5px;` |
| border-color        | color the border                                                                                   | `border-color: #000000;`                                   |
| border-style        | sets the style of the border (none; dotted; dashed; solid; double)                                 | `border-style: dotted;`                                    |
| border-&lt;side&gt; | sets the width, color, and style of the top, right, bottom, or left border                         | `border-left: 5px red double;`                             |
| border              | sets the width, color, and style of all the borders                                                | `border: 5px red double;`                                  |

