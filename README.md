# djello
Let's see how far we can go with a minimal frontend: no fashionable JS or CSS frameworks, no compiling, no BEM.  Aftwerwards, we should do one in React, Bootstrap & all the trimings to compare.

[![CircleCI](https://circleci.com/gh/shangxiao/djello.svg?style=svg)](https://circleci.com/gh/shangxiao/djello)

## Features

* Modern JS features
* Query selectors
* Form validation
* Drag-n-drop
* CSS variables
* Use unicode for icons where possible
* Accessibility - no clickable divs: interact with hyperlinks or buttons
* XHR only when required - forms post their data to the server

## Possible Further Steps

* Use pytest & pytest-django
* Use factory_boy
* Make it responsive
* Split CSS, JS & HTML

## Issues Encountered

### Native DnD

The "ghost" drag image isn't very customisable. You can specify an image or an element but
the element has to be mounted on the page and visible from which the browser will take a
snapshot of what the rendered element looks like and use that as the image. The image will
be rendered with a slight transparency (Firefox is more transparent than Chrome on a Mac)
and this doesn't appear to be controllable. I was able to replicate the tilted card effect
from Trello only by cloning the source div, mounting that within a container div and then
mounting that to the body, with a negative absolute position to hide it from view. The
container was necessary in order to get the browser to capture the rotated card.

Additionally, the cursor can only be customised via [drag/drop effects]
(https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API#Define_the_drag_effect)
which isn't very useful.
