# Positioning Content
## Positioning with Floats
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

## Position with Inline-Block 
- The `display: inline-block` property and value can be used to layout elements next to each other.
- One concern that must be addressed is that between all inline-block elements, there is a single space between them that needs to be removed for optimal formatting.
    - In the HTML document, the space between the `</section>` of one element and the `<section>` of the next element can be removed.
        ```
        <section>
            ...
        </section><section>
            ...
        </section>
        ```
    - Alternatively, for formatting purposes, a comment can be inserted:
        ```
        <section>
            ...
        </section><!--
        --><section>
            ...
        </section>   
        ```

## Reusable Layouts
- Reusable layouts can be created to establish a grid-like effect on the page with equalivalent columns.
- For instance, to create a layout that enables three columns of equal width or two columns with the width split between them:
    ```
    .col-1-3 {
        width: 33.33%;
    }
    .col-2-3 {
        width: 66.66%;
    }

    .col-1-3,
    .col-2-3 {
        display: inline-block;
        vertical-align: top;
    }
    ```
    - `col-1-3` can be used to create three equal columns.

## Uniquely Position Elements
- To uniquely position an element, the `position` property and box offset properties--`top`, `right`, `bottom`, and `left`--can be used.
- Every element has a default `position` of `static`.

### Relative Positioning
- The `relative` value for the `position` property allows an element to appear within the normal flow of a page, and it allows it to be modified with the box offset properties.
- The element is moved relative to its initial position.
    ```
    .offset {
        left: 20px;
        position: relative;
        top: 20px;
    }
    ```
    - For instance, the above code would move the box twenty pixels from the left and top.
- Instead of moving an element beneath it down, it simply overlaps it.

### Absolute Positioning
- The `absolute` value for the `position` property means that the element does not appear within the normal flow of the document.
- It is positioned in relation to its closest relatively positioned parent element.
    - The `<body>` is the default.
- In the below example, the `<div>` would be positioned twenty pixels to the left and down twenty pixels from the top right of the `<section>`.

