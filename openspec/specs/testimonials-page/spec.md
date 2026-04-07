# testimonials-page Specification

## Purpose

Document the structure and behavior of the testimonials page (testimonials.njk). This page showcases student success stories to build trust and credibility with potential students.

## Page Structure

The testimonials page consists of the following sections:

1. Page Hero
2. Statistics Strip
3. Testimonials Masonry Grid
4. CTA Section

## Requirements

### Requirement: Statistics strip

A statistics strip SHALL display key metrics about teaching performance.

#### Scenario: Stats display

- GIVEN a visitor is on the testimonials page
- THEN four statistics SHALL be displayed in a horizontal strip:
  - 150+ alumnos formados (students taught)
  - 98% tasa de satisfacción (satisfaction rate)
  - 5.0 valoración media (average rating with stars)
  - +2.3 puntos de mejora media en notas (average grade improvement)

#### Scenario: Stats layout

- GIVEN a visitor is on the testimonials page
- THEN the stats SHALL be displayed in a row
- AND they SHALL be separated by vertical dividers
- AND the section SHALL have a surface background color

### Requirement: Page hero

The hero section SHALL introduce the testimonials section.

#### Scenario: Hero content

- GIVEN a visitor is on the testimonials page
- THEN the hero SHALL display:
  - Section label: "Testimonios"
  - Headline: "Resultados reales, alumnos reales"
  - Subtitle with student count claim (150+ students improved)

### Requirement: Testimonials masonry grid

Testimonials SHALL be displayed in a responsive masonry-style grid.

#### Scenario: Three-column layout

- GIVEN a visitor is on the testimonials page on desktop
- THEN testimonials SHALL be displayed in 3 columns
- AND each column SHALL contain multiple testimonial cards

#### Scenario: Testimonial card content

- GIVEN a testimonial card is displayed
- THEN the card SHALL include:
  - 5-star rating
  - Quote text
  - Author name
  - Author level and location (e.g., "2º Bachillerato · Sevilla")

#### Scenario: Featured testimonial

- GIVEN a visitor is on the testimonials page
- THEN one testimonial SHALL be visually distinguished as "featured"
- AND the featured card SHALL have larger typography and a quote mark decoration

#### Scenario: Minimum testimonial count

- GIVEN a visitor is on the testimonials page
- THEN at least 9 testimonials SHALL be displayed across the three columns

### Requirement: Testimonial quote content

Testimonial quotes SHALL reflect real student outcomes and experiences.

#### Scenario: Quote variety

- GIVEN testimonials are displayed
- THEN quotes SHALL represent:
  - Students who passed exams after failing
  - Students who achieved high grades (8.5, 9.6)
  - Parents of students
  - University students
  - Exam preparation students (PAU, oposiciones)

#### Scenario: Geographic diversity

- GIVEN testimonials are displayed
- THEN authors SHALL represent multiple Spanish cities
- AND some testimonials SHALL represent international students (Latin America)

### Requirement: CTA section

A CTA section SHALL encourage visitors to book after reading testimonials.

#### Scenario: Success story CTA

- GIVEN a visitor has scrolled past testimonials
- THEN a CTA box SHALL be displayed
- AND the headline SHALL be: "¿Quieres ser el próximo caso de éxito?"
- AND a "Reservar ahora" button SHALL be displayed

## Out of Scope

- Booking functionality (see `booking-flow` spec)
- Testimonial submission or moderation
- Verification of testimonial authenticity
- Video testimonials
