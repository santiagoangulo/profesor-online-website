# footer Specification

## Purpose

Document the site footer structure, content, and behavior. The footer provides secondary navigation, contact information, and branding. The footer uses a unified template across all pages including the material-didactico section.

## Requirements

### Requirement: Unified footer template

The footer SHALL use a single unified 4-column template across all pages.

#### Scenario: Consistent footer across all pages

- GIVEN a visitor is on any page (main site, material-didactico index, chapter pages)
- THEN the footer SHALL display the same 4-column grid layout
- AND the footer SHALL have the same i18n support (ES/EN)

### Requirement: Footer grid layout

The footer SHALL display content in a multi-column grid.

#### Scenario: Desktop footer grid

- GIVEN a visitor is on desktop (>768px)
- THEN the footer SHALL display a 4-column grid
- AND columns SHALL be: Brand, Navigation, Subjects, Contact

#### Scenario: Tablet footer grid

- GIVEN a visitor is on tablet (481px-768px)
- THEN the footer SHALL display a 2-column grid
- AND columns SHALL stack appropriately

#### Scenario: Mobile footer grid

- GIVEN a visitor is on mobile (≤480px)
- THEN the footer SHALL display a 1-column grid
- AND columns SHALL stack vertically

### Requirement: Brand column

The footer SHALL include brand information and tagline.

#### Scenario: Brand content

- GIVEN a visitor views the footer
- THEN the brand column SHALL display:
  - Site logo (links to `/index.html`)
  - Brief description of services
  - Available in both ES and EN languages

### Requirement: Navigation column

The footer SHALL include secondary navigation links.

#### Scenario: Footer nav links

- GIVEN a visitor views the footer
- THEN the navigation column SHALL include:
  - Inicio/Home → `/index.html`
  - Servicios/Services → `/services.html`
  - Reservar clase/Book a class → `/booking.html`
  - Testimonios/Testimonials → `/testimonials.html`
  - Recursos/Resources → `/material-didactico/index.html`

### Requirement: Mathematics column

The footer SHALL include links to Mathematics areas.

#### Scenario: Mathematics links

- GIVEN a visitor views the footer
- THEN the mathematics column SHALL include:
  - Matemáticas/Mathematics → `/services.html`
  - Preparación PAU/Exam prep → `/services.html`

### Requirement: Contact column

The footer SHALL include contact information.

#### Scenario: Contact information

- GIVEN a visitor views the footer
- THEN the contact column SHALL display:
  - Email address (santi.maths.teacher@gmail.com)
  - Link to booking page
  - Google Meet badge

### Requirement: Footer bottom bar

The footer SHALL include a bottom section with copyright.

#### Scenario: Copyright display

- GIVEN a visitor views the footer
- THEN a bottom bar SHALL display:
  - Copyright notice with current year
  - Copyright text: "© {year} Profesor Online. Todos los derechos reservados."

### Requirement: Footer background

The footer SHALL have a distinct background from the main content.

#### Scenario: Footer styling

- GIVEN a visitor views the footer
- THEN the footer SHALL have:
  - Background color: `--color-surface`
  - Top border: 1px solid `--color-divider`

## Technical Implementation

- Footer template: `_includes/partials/footer.njk` (unified template)
- All links use absolute paths
- Uses CSS Grid for layout
- Responsive breakpoints: 768px and 480px

## Out of Scope

- Social media links
- Newsletter signup
- Additional footer columns
- Sticky footer behavior
