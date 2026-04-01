# navigation Specification

## Purpose

Document the navigation structure and behavior of the website, including the header navigation, mobile menu, and footer navigation. The header and footer use a unified template across all pages including the material-didactico section.

## Requirements

### Requirement: Unified header template

The header SHALL use a single unified template across all pages.

#### Scenario: Consistent header across all pages

- GIVEN a visitor is on any page (main site, material-didactico index, chapter pages)
- THEN the header SHALL display the same navigation structure
- AND the header SHALL have the same i18n support (ES/EN toggle)

#### Scenario: Logo always returns to main site

- GIVEN a user clicks the site logo from any page
- THEN they SHALL be navigated to `/index.html`

### Requirement: Sticky header behavior

The header SHALL be sticky at the top of the page with scroll-aware styling.

#### Scenario: Sticky positioning

- GIVEN a visitor loads any page
- WHEN the page renders
- THEN the header SHALL have `position: sticky` and `top: 0`
- AND the header SHALL have a z-index of 100

#### Scenario: Backdrop blur

- GIVEN a visitor loads any page
- THEN the header SHALL have a semi-transparent background
- AND backdrop-filter blur SHALL be applied (14px)

#### Scenario: Shadow on scroll

- GIVEN a visitor has scrolled past 12 pixels from the top
- WHEN the page is scrolled
- THEN the header SHALL display a box shadow
- GIVEN a visitor is at the top of the page
- THEN the header SHALL NOT display a shadow

### Requirement: Header navigation

The site header SHALL contain the logo, main navigation links, and action buttons.

#### Scenario: Logo navigation

- GIVEN a user clicks the site logo
- THEN they SHALL be navigated to `/index.html`

#### Scenario: Main navigation links

- GIVEN a user is on any page
- THEN the header SHALL display the following links:
  - Inicio/Home → `/index.html`
  - Servicios/Services → `/services.html`
  - Reservar clase/Book a class → `/booking.html`
  - Testimonios/Testimonials → `/testimonials.html`
  - Recursos/Resources → `/material-didactico/index.html`

### Requirement: Active link indication

The current page link SHALL be visually indicated as active.

#### Scenario: Active page highlight via JavaScript

- GIVEN a user is on any page
- WHEN the page loads
- THEN JavaScript SHALL detect the current path
- AND the matching navigation link SHALL have the `active` class

#### Scenario: Active link styling

- GIVEN a navigation link has the `active` class
- THEN it SHALL be visually distinguished (via CSS)

### Requirement: CTA button

The header SHALL display a persistent CTA button.

#### Scenario: Header CTA placement

- GIVEN a user is on any page
- THEN a "Reservar clase" / "Book a class" button SHALL be visible in the header
- AND clicking it SHALL navigate to `/booking.html`

### Requirement: Mobile menu

A mobile menu SHALL be available on small screens.

#### Scenario: Mobile menu toggle

- GIVEN a user is on a mobile device (screen < breakpoint)
- WHEN they click the hamburger icon
- THEN the mobile menu SHALL open
- AND the hamburger icon SHALL transform to a close (X) icon
- AND body scroll SHALL be locked

#### Scenario: Mobile menu close

- GIVEN the mobile menu is open
- WHEN the user clicks the close icon
- THEN the mobile menu SHALL close
- AND body scroll SHALL be unlocked

#### Scenario: Mobile menu close on link click

- GIVEN the mobile menu is open
- WHEN the user clicks any navigation link
- THEN the mobile menu SHALL close
- AND the user SHALL be navigated to the link destination

### Requirement: Unified footer template

The footer SHALL use a single unified 4-column template across all pages.

#### Scenario: Consistent footer across all pages

- GIVEN a visitor is on any page (main site, material-didactico index, chapter pages)
- THEN the footer SHALL display the same 4-column grid layout
- AND the footer SHALL have the same i18n support

### Requirement: Accessibility

Navigation SHALL be accessible to screen readers and keyboard users.

#### Scenario: ARIA labels

- GIVEN navigation elements are present
- THEN appropriate ARIA labels SHALL be applied
- AND the menu toggle SHALL have `aria-expanded` attribute

#### Scenario: Keyboard navigation

- GIVEN a user navigates via keyboard
- THEN all navigation links SHALL be reachable via Tab
- AND the menu toggle SHALL be keyboard accessible

## Technical Implementation

- Header is in `_includes/partials/header.njk` (unified template)
- Footer is in `_includes/partials/footer.njk` (unified 4-column template)
- Navigation links use absolute paths (`/index.html`, etc.)
- Mobile menu logic is in `app.js`
- Active link detection uses `location.pathname` matching
- Scroll shadow uses `window.scrollY` with 12px threshold

## Out of Scope

- Dropdown submenus
- Mega menus
- Breadcrumb navigation
- Skip-to-content links
