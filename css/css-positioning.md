# Positioning Content
## Positioning With Floats
- The `float` property is versatile and can be used in a number of ways.
    - It removes an element from the normal flow of a page and positions it to the left or right of its parent element.
    - All other elements then flow around the floated element.
    - The two most used values are `left` and `right`.
- It is best utilized with `margin` and `width` to better arrange columns.

### Clearing & Containing Floats
- Because floating is not meant for laying out a page, it can sometimes negatively impact the `margin` and `padding` of nearby elements.
- To prevent this from occurring, the `clear` value can be used.
    - Its values are `left`, `right`, or `both`, and it signifies which floats to clear.
- An element after floated elements can benefit from having `clear: both;` to return the page to its normal flow.

#### Clearfix
- An alternative method is to contain floats by storing them in a parent element that acts as a container, leaving the flow completely normal outside of it.
- The CSS for that parent element is known as `clearfix`, and it is shown below:
    ```
    .group::before,
    .group::after {
        content: "";
        display: table;
    }
    .group::after {
        clear: both;
    }
    .group {
        clear: both;
        *zoom: 1;
    }
    ```
    - The pseudo-elements `::before` and `::after` dynamically generate elements above and below the element and are displayed as table-level elements.
    - The `clear: both;` in the second and third rulesets clears the floats and returns the page back to normal after the container, and it contains some trickery for old browsers.