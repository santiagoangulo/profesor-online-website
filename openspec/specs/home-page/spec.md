# home-page Specification

## Purpose

Document the structure and behavior of the landing page (index.njk). The home page serves as the primary entry point for potential students, providing an overview of services, teaching method, and social proof through testimonials and statistics.

## Page Structure

The home page consists of the following sections, in order:

1. Hero Section
2. Subjects Strip
3. About/Method Section
4. Testimonials Preview
5. CTA Section

## Requirements

### Requirement: Hero section

The hero section SHALL display the primary value proposition and CTAs.

#### Scenario: Hero content display

- GIVEN a visitor loads the home page
- WHEN the page renders
- THEN the hero SHALL display: headline, subtitle, and two CTA buttons
- AND the hero SHALL show a visual representation of an online class session

#### Scenario: Formula accent pills

- GIVEN a visitor views the hero section
- THEN three formula pills SHALL be displayed above the headline
- AND they SHALL display: "E = mc²", "∫ f(x)dx", "F = ma"
- AND they SHALL reinforce the math/science branding

#### Scenario: Hero visual card stack

- GIVEN a visitor views the hero section
- THEN a card stack visual SHALL be displayed on the right side (desktop)
- AND the stack SHALL include:
  - Floating session card showing next session info
  - Main board visual with equation examples
  - Floating progress card showing student progress

#### Scenario: Primary CTA navigation

- GIVEN a visitor clicks the primary CTA ("Reservar clase")
- THEN they SHALL be navigated to `/booking.html`

#### Scenario: Secondary CTA navigation

- GIVEN a visitor clicks the secondary CTA ("Ver servicios")
- THEN they SHALL be navigated to `/services.html`

### Requirement: Hero trust indicators

The hero section SHALL display trust indicators including student count, satisfaction rate, and platform badge.

#### Scenario: Trust stats display

- GIVEN a visitor is on the home page
- THEN the hero SHALL display: 150+ students, 98% satisfaction, 5-star rating
- AND the hero SHALL display a Google Meet platform badge

### Requirement: Subjects strip

The subjects section SHALL display Mathematics and exam preparation as the main offerings.

#### Scenario: Subject cards display

- GIVEN a visitor is on the home page
- THEN two subject cards SHALL be displayed: Matemáticas, Preparación de exámenes
- AND each card SHALL display an icon and brief description

### Requirement: Method section

The method section SHALL explain the teaching approach with a three-step process.

#### Scenario: Method steps

- GIVEN a visitor is on the home page
- WHEN they view the method section
- THEN three numbered steps SHALL be displayed: Diagnóstico inicial, Plan personalizado, Seguimiento continuo
- AND each step SHALL include a brief explanation

### Requirement: Testimonials preview

The home page SHALL display a preview of student testimonials with a link to full testimonials.

#### Scenario: Testimonial cards

- GIVEN a visitor is on the home page
- THEN three testimonial cards SHALL be displayed
- AND each card SHALL show: star rating, quote, author name, and author level/location

#### Scenario: View all testimonials

- GIVEN a visitor clicks "Ver todos los testimonios"
- THEN they SHALL be navigated to `/testimonials.html`

### Requirement: CTA section

The CTA section SHALL encourage visitors to book their diagnostic class.

#### Scenario: Final CTA display

- GIVEN a visitor scrolls to the CTA section
- THEN a prominent booking button SHALL be displayed
- AND the section SHALL emphasize "Primera clase de diagnóstico"

## Out of Scope

- Booking functionality (see `booking-flow` spec)
- Pricing details (see `services-page` spec)
- Full testimonials page (see `testimonials-page` spec)
