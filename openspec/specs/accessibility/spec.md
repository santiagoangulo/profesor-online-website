# accessibility Specification

## Purpose

Document the accessibility features and compliance of the website. The site should be usable by all visitors, including those using assistive technologies.

## Requirements

### Requirement: Semantic HTML

Pages SHALL use semantic HTML elements for proper document structure.

#### Scenario: Proper heading hierarchy

- GIVEN a visitor views any page
- THEN headings SHALL follow a logical order (h1 → h2 → h3)
- AND there SHALL be only one h1 per page
- AND headings SHALL not skip levels

#### Scenario: Semantic landmarks

- GIVEN a visitor views any page
- THEN the page SHALL include proper landmark elements:
  - `<header>` for the site header
  - `<main>` for the main content
  - `<footer>` for the site footer

### Requirement: Keyboard navigation

The site SHALL be fully navigable via keyboard.

#### Scenario: Focus indicators

- GIVEN a user navigates via Tab key
- THEN focused elements SHALL show a visible focus indicator
- AND the indicator SHALL be: 2px solid primary color with 3px offset

#### Scenario: Tab order

- GIVEN a user navigates via keyboard
- THEN the tab order SHALL follow the logical reading order
- AND interactive elements SHALL be reachable in sequence

### Requirement: ARIA attributes

Interactive elements SHALL have appropriate ARIA attributes.

#### Scenario: Button labels

- GIVEN a button has no visible text
- THEN an `aria-label` SHALL describe the button's purpose
- AND the label SHALL be in the current language

#### Scenario: Expanded state

- GIVEN a toggle button changes state
- THEN `aria-expanded` SHALL reflect the current state
- AND `aria-label` SHALL update if the purpose changes

#### Scenario: Navigation landmarks

- GIVEN navigation elements are present
- THEN `role="list"` SHALL be used on `<ul>` navigation lists
- AND `aria-label` SHALL identify navigation sections

### Requirement: Color contrast

Text SHALL maintain sufficient contrast ratios.

#### Scenario: Body text contrast

- GIVEN text is displayed on a background
- THEN the contrast ratio SHALL be at least 4.5:1 for normal text
- AND 3:1 for large text (18px+ or 14px bold)

#### Scenario: Interactive elements contrast

- GIVEN buttons or links are displayed
- THEN the text contrast SHALL be at least 4.5:1

### Requirement: Screen reader support

Content SHALL be accessible to screen reader users.

#### Scenario: Decorative images

- GIVEN an image is purely decorative
- THEN `aria-hidden="true"` SHALL be applied
- OR the image SHALL have an empty `alt` attribute

#### Scenario: Linked images

- GIVEN an image is inside a link
- THEN the link text SHALL describe the destination
- AND the image may be decorative

### Requirement: Language-specific accessibility

Content SHALL be accessible in both supported languages.

#### Scenario: Language attribute

- GIVEN the page content is in Spanish
- THEN `<html lang="es">` SHALL be present
- GIVEN the page content is in English
- THEN `<html lang="en">` SHALL be present

### Requirement: Error identification

Forms and interactive elements SHALL clearly identify errors.

#### Scenario: Error messaging

- GIVEN an error occurs in user input
- THEN the error message SHALL be visible
- AND the error message SHALL be programmatically associated with the input

## Technical Implementation

- Focus styles in `base.css` with `:focus-visible`
- ARIA attributes applied in templates
- Language toggle updates `<html lang>` attribute
- Responsive breakpoints handle mobile accessibility

## Out of Scope

- Skip navigation links
- ARIA live regions for dynamic content
- Multi-step form accessibility
- Video/audio accessibility
