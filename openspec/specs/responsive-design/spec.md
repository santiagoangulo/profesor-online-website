# responsive-design Specification

## Purpose

Document the responsive design approach and breakpoints used across the website to ensure a consistent experience across devices.

## Requirements

### Requirement: Fluid typography

Text sizes SHALL scale smoothly across viewport widths using `clamp()`.

#### Scenario: Font scaling

- GIVEN the base font size is defined
- WHEN the viewport width changes
- THEN font sizes SHALL scale proportionally
- AND text SHALL remain readable at all breakpoints
- AND no horizontal scrolling SHALL occur due to text overflow

### Requirement: Fluid spacing

Spacing SHALL scale proportionally with viewport width.

#### Scenario: Section padding scales

- GIVEN a section has padding defined with `clamp()`
- WHEN the viewport width changes
- THEN the padding SHALL scale smoothly between min and max values

### Requirement: Mobile breakpoint

The site SHALL adapt layout for screens 768px and below.

#### Scenario: Navigation collapses to hamburger menu

- GIVEN a user is on a mobile device (width ≤ 768px)
- WHEN the page loads
- THEN the horizontal navigation links SHALL be hidden
- AND a hamburger menu toggle SHALL be visible

#### Scenario: Mobile menu fullscreen overlay

- GIVEN a user is on a mobile device (width ≤ 768px)
- WHEN the hamburger menu is opened
- THEN the menu SHALL cover the full viewport
- AND navigation links SHALL be displayed vertically and centered

#### Scenario: Footer grid collapses

- GIVEN a user is on a mobile device (width ≤ 768px)
- WHEN viewing the footer
- THEN the footer grid SHALL display in 2 columns (768px)
- OR 1 column (480px)

### Requirement: Tablet breakpoint

The site SHALL provide optimized layout for tablet devices.

#### Scenario: Tablet navigation

- GIVEN a user is on a tablet device (width 481px-768px)
- WHEN viewing the navigation
- THEN the horizontal navigation SHALL be visible
- AND the CTA button SHALL be hidden

### Requirement: Desktop breakpoint

The site SHALL provide full layout for desktop screens.

#### Scenario: Full navigation display

- GIVEN a user is on a desktop device (width > 768px)
- WHEN viewing the navigation
- THEN all navigation links SHALL be visible
- AND the CTA button SHALL be visible

#### Scenario: Footer full grid

- GIVEN a user is on a desktop device (width > 768px)
- WHEN viewing the footer
- THEN the footer grid SHALL display in 4 columns

### Requirement: Container max-width

Content SHALL be constrained to readable widths.

#### Scenario: Default container width

- GIVEN a visitor is on a wide screen
- THEN content SHALL be contained within `--content-wide` (1200px)
- AND centered with auto margins

#### Scenario: Narrow container

- GIVEN a section uses `.container--narrow`
- THEN content SHALL be contained within `--content-default` (960px)

### Requirement: Touch targets

Interactive elements SHALL have adequate touch target sizes on mobile.

#### Scenario: Minimum touch target size

- GIVEN a user is on a mobile device
- WHEN tapping interactive elements (buttons, links)
- THEN the touch target SHALL be at least 44x44 pixels

### Requirement: Scroll behavior

Pages SHALL have smooth scroll behavior with adequate scroll padding.

#### Scenario: Scroll padding for sticky header

- GIVEN a page has a sticky header
- WHEN scrolling to anchor links
- THEN the scroll position SHALL account for the header height
- AND content SHALL not be hidden behind the header

### Requirement: Image responsiveness

Images SHALL scale appropriately and maintain aspect ratio.

#### Scenario: Responsive images

- GIVEN an image is displayed on the page
- WHEN the viewport width changes
- THEN the image SHALL scale down proportionally
- AND `height: auto` SHALL be set to maintain aspect ratio

## Technical Implementation

- Breakpoints: 768px (tablet/mobile) and 480px (small mobile)
- Fluid sizing uses CSS `clamp()` function
- Container widths defined as CSS variables in `style.css`
- Scroll padding: `scroll-padding-top: var(--space-16)` on `html`

## Out of Scope

- Print styles
- Landscape mobile optimizations
- PWA/standalone mode
- Device-specific CSS for notched displays
