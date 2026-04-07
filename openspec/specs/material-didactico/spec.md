# material-didactico Specification

## Purpose

Document the educational resources section (material-didactico) - a free resource library containing math exercises, chapters, and study materials in both Spanish and English.

## Requirements

### Requirement: Bilingual content

The material section SHALL offer content in both Spanish and English.

#### Scenario: Spanish content

- GIVEN a visitor navigates to `/material-didactico/es/`
- THEN all content SHALL be in Spanish
- AND URLs SHALL use Spanish terminology (e.g., `matematicas_1`, `capitulo01`)

#### Scenario: English content

- GIVEN a visitor navigates to `/material-didactico/en/`
- THEN all content SHALL be in English
- AND URLs SHALL use English terminology (e.g., `mathematics_1`, `chapter01`)

### Requirement: Subject organization

Materials SHALL be organized by subject and level.

#### Scenario: Mathematics 1 (Bachillerato)

- GIVEN a visitor navigates to the Spanish section
- THEN `/material-didactico/es/matematicas_1/` SHALL contain:
  - 12 chapters covering the curriculum
  - Exercise pages

#### Scenario: Mathematics for Social Sciences

- GIVEN a visitor navigates to the Spanish section
- THEN `/material-didactico/es/matematicas_ccss_1/` and `/matematicas_ccss_2/` SHALL exist
- AND contain level-appropriate content

### Requirement: Chapter structure

Each chapter SHALL contain theoretical content and examples.

#### Scenario: Chapter page content

- GIVEN a visitor views a chapter page
- THEN the page SHALL contain:
  - Chapter title and number
  - Theoretical explanations
  - Worked examples
  - Practice problems references

### Requirement: Exercises section

Each subject SHALL have an exercises section with practice problems.

#### Scenario: Exercise pages

- GIVEN a visitor navigates to the exercises section
- THEN exercise pages SHALL be available at `/exercises/` within each subject
- AND exercises SHALL be organized by chapter or topic

### Requirement: Standalone navigation

The material section SHALL have its own header and footer.

#### Scenario: Material section header

- GIVEN a visitor is in the material section (`/material-didactico/`)
- THEN a specific header SHALL be displayed
- AND it SHALL include links back to main sections

#### Scenario: Material section footer

- GIVEN a visitor is in the material section
- THEN a footer SHALL be displayed
- AND it SHALL include contact information and main site links

### Requirement: URL depth handling

The material section SHALL handle assets correctly at different URL depths.

#### Scenario: Asset path resolution

- GIVEN a page is at `/material-didactico/es/matematicas_1/capitulo01/page.html`
- THEN CSS and JS assets SHALL be loaded correctly
- AND relative paths SHALL resolve to the site root

### Requirement: Accessibility

Educational content SHALL be accessible to all users.

#### Scenario: Semantic HTML for content

- GIVEN educational content is displayed
- THEN proper heading hierarchy SHALL be used (h1, h2, h3)
- AND content SHALL be structured with semantic elements

#### Scenario: Math notation accessibility

- GIVEN mathematical formulas are displayed
- THEN they SHALL use semantic markup or alt text
- AND screen readers SHALL have some means of interpretation

## Technical Implementation

- Materials are stored in `/material-didactico/` directory
- Spanish content: `/material-didactico/es/`
- English content: `/material-didactico/en/`
- Uses 11ty for static generation
- Base template handles different asset paths for nested URLs

## Out of Scope

- Interactive exercises (currently static content)
- Answer keys or solutions
- Progress tracking
- Downloadable PDFs
- User authentication for premium content
