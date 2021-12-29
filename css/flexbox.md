# <a href='https://css-tricks.com/snippets/css/a-guide-to-flexbox/'>Flexbox</a>
## Flex Containers and Flex Items
- Flexbox is a toolbox of properties that can be used to position elements. 
- Some properties belong to the `flex container` and others to the `flex items`.
    <img src='https://cdn.statically.io/gh/TheOdinProject/curriculum/495704c6eb6bf33bc927534f231533a82b27b2ac/html_css/v2/foundations/flexbox/imgs/03.png'>
    - A `flex container` contains the `display: flex` property and value.
    - A `flex item` has the `flex` property.
- `Flex items` can also be `flex containers`:
    <img src='https://cdn.statically.io/gh/TheOdinProject/curriculum/495704c6eb6bf33bc927534f231533a82b27b2ac/html_css/v2/foundations/flexbox/imgs/04.png'>

## Flex Properties
<img src='https://cdn.statically.io/gh/TheOdinProject/curriculum/495704c6eb6bf33bc927534f231533a82b27b2ac/html_css/v2/foundations/flexbox/imgs/10.png'>

- `flex` is shorthand for three properties that can be set on a `flex item`.
    - `flex: <flex-grow> <flex-shrink> <flex-basis>`
    - When `flex: 1` is set, it is interpreted as `flex: 1 1 0`.
- They affect how flex items size themselves.

### flex-grow
- `flex-grow` is used as the flex item's "growth factor."
    - If the value for all the items is 1, they will all be the same.
    - If one of the values is 2, it will be 2x larger than the other values.

### flex-shrink
- `flex-shrink` sets the flex item's "shrink factor."
    - If the value is 1, all flex items will shrink equally.
    - If an item is 0, it will not shrink.
    - Higher numbers mean that an item will shrink at a higher rate than normal.

### flex-basis
- `flex-basis`sets the initial size of a flex item.
    - Any growing or shrinking starts from this baseline.
- Using `auto` tells the items to check for a width declaration and the item will be set to that value.
- Using `0%` sets the initial value to 0, and all items will proportionately grow to fill in the space.


## Flex Axes
- There are two axes for flex containers:
    - The Main Axis
    - The Cross Axis
- The direction of the `main axis`is set by the `flex-direction` property, which can either be `row` (left-to-right), `column` (top-to-bottom), `row-reverse` (right-to-left) or `column-reverse` (bottom-to-top). The `cross axis` is perpendicular in each respective case.
    - When it is set to `row`, `flex-basis` refers to `width`, but it refers to `height` when set to `column`.
- It is worth noting that block-level elements default to the full width of their parent, and they default to the height of their content, and where there is no content, the height is 0.
- When `flex-direction` is set to column, the `height` of the container needs to be set or else the `flex` shorthand property cannot be used because the basis for the flex-items will be a height of 0, which fills up the container's default of 0.
- Alternatively, the height of the flex item can be set and the `flex-basis` can be set to `auto`.

## <a href='https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container'>Axes Alignment</a>
- `flex: 1` makes each flex item grow to fill available space.
- `justify-content` aligns items across the main axis.
    - `space-between`- equal amounts of space between the items; no edge
    - `space-around` - equal space on both sides of all items; combines middle
    - `space-evenly` - equal space on sides and middle
    - `flex-start` - everything to starting side
    - `flex-end` - everything to ending side
    - `center` - center items
- `align-items` aligns items along the cross axis.
    - `stretch` - items stretch to the height of the flex container
    - `flex-start` - items align at the start
    - `flex-end` - items align at the end
    - `center` - items center
- `gap` adds a specified space between flex items
    - it is similar to adding a margin to the items
- `align-self` aligns a single flex item
    - same values as `align-items` plus `auto`

## flex-wrap
- `flex-wrap` has a default value of `nowrap`.
- Setting it to `wrap` means that items, given a width, will be pushed to the next line if they are too large for their container instead of autosizing.

## flex-flow
- `flex-flow` is a combination of `flex-direction` and `flex-wrap`.
    - `flex-flow: <flex-direction> <flex-wrap>`

## Use Cases
- A common pattern for navigation is to have a list of items displayed as a horizontal bar.
- Another common use is for form controls with inputs and buttons.