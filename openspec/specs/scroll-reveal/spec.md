# scroll-reveal Specification

## Purpose

Document the scroll-triggered reveal animation behavior. Elements fade in and slide up as they enter the viewport, creating a smooth, staggered content appearance.

## Requirements

### Requirement: Reveal animation trigger

Elements with the `reveal` class SHALL animate when they enter the viewport.

#### Scenario: Initial state

- GIVEN an element has the `reveal` class
- WHEN the page loads
- THEN the element SHALL have `opacity: 0` and `transform: translateY(20px)`

#### Scenario: Triggered state

- GIVEN an element has the `reveal` class
- WHEN the element enters the viewport
- THEN the element SHALL have `opacity: 1` and `transform: none`

### Requirement: Staggered timing

Multiple reveal elements SHALL animate with a staggered delay.

#### Scenario: Stagger delay

- GIVEN multiple reveal elements are visible in the viewport
- WHEN the first element animates
- THEN subsequent elements SHALL animate with 80ms delay between each
- AND the formula is `delay = index * 80ms`

### Requirement: Intersection threshold

Reveal animations SHALL trigger when elements cross a visibility threshold.

#### Scenario: Threshold configuration

- GIVEN an element with the `reveal` class
- WHEN the element is 10% visible in the viewport
- THEN the reveal animation SHALL trigger
- AND the threshold SHALL be 0.1

#### Scenario: Root margin

- GIVEN an element with the `reveal` class
- WHEN the element is near the bottom of the viewport
- THEN the animation SHALL trigger before the element reaches the exact threshold
- AND the root margin SHALL be `0px 0px -40px 0px`

### Requirement: Single animation trigger

Reveal animations SHALL only trigger once per element.

#### Scenario: No re-animation

- GIVEN an element has already animated (has `visible` class)
- WHEN the element scrolls out of view and back in
- THEN the animation SHALL NOT replay
- AND the observer SHALL unobserve the element after triggering

### Requirement: Reveal container

Elements SHOULD be wrapped in a container that allows the animation to work.

#### Scenario: Reveal class placement

- GIVEN a section contains multiple elements
- WHEN the section enters the viewport
- THEN each element with the `reveal` class SHALL animate independently
- AND the animation delay SHALL be relative to element position in DOM

## Technical Implementation

- Uses IntersectionObserver API
- Reveal elements have `.reveal` class
- CSS transition: `opacity 0.6s`, `transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)`
- Delay calculated in JS based on element index
- Observer created with threshold: 0.1, rootMargin: '0px 0px -40px 0px'

## Out of Scope

- Scroll progress indicators
- Parallax effects
- Animation on scroll direction
- Disabling animations (see `responsive-design` spec for reduced-motion)
