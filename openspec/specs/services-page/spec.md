# services-page Specification

## Purpose

Document the structure and behavior of the services page (services.njk). This page provides detailed information about Mathematics, pricing plans, and the booking process.

## Page Structure

The services page consists of the following sections:

1. Page Hero
2. Subjects Detail Section
3. Pricing Section
4. How It Works Section

## Requirements

### Requirement: Subjects detail grid

The page SHALL display detailed Mathematics information with topics and education levels.

#### Scenario: Subject cards with topics

- GIVEN a visitor is on the services page
- THEN two subject cards SHALL be displayed: Matemáticas, Preparación PAU
- AND each card SHALL list specific topics covered
- AND each card SHALL display applicable education levels (Bachillerato, Universidad)

#### Scenario: Subject topic lists

- GIVEN a visitor views the Matemáticas card
- THEN topics SHALL include: Álgebra y funciones, Cálculo diferencial e integral, Geometría analítica, Estadística y probabilidad, Trigonometría, Números complejos

- GIVEN a visitor views the Preparación PAU card
- THEN topics SHALL include: PAU / Selectividad / EBAU, Exámenes universitarios, Oposiciones con contenido matemático, Recuperaciones y repetidores, Simulacros de examen, Estrategias de examen

### Requirement: Pricing display

The page SHALL display three pricing tiers with features and CTAs.

#### Scenario: Pricing grid

- GIVEN a visitor is on the services page
- THEN three pricing cards SHALL be displayed
- AND each card SHALL show: plan name, price per class, total price, and included features

#### Scenario: Individual class pricing

- GIVEN a visitor views the individual class pricing card
- WHEN the price is 35€ per 60-minute class
- THEN the following features SHALL be listed: 60-minute session, materials included, post-class doubt resolution, Google Meet

#### Scenario: Bundle pricing

- GIVEN a visitor views the bundle pricing card (most popular)
- WHEN the price is 29€ per class (232€ total for 8 sessions)
- THEN the following features SHALL be listed: 8 sessions, personalized study plan, monthly progress report, digital resources access, WhatsApp/email Q&A, Google Meet

#### Scenario: PAU intensive pricing

- GIVEN a visitor views the PAU intensive pricing card
- WHEN the price is 32€ per class (20-hour bundle)
- THEN the following features SHALL be listed: 20 hours of class, weekly mock exams, past exam bank, exam day strategy

### Requirement: Pricing CTA navigation

All pricing cards SHALL have CTAs that navigate to the booking page.

#### Scenario: Bundle primary CTA

- GIVEN a visitor views the bundle pricing card (featured)
- WHEN they click "Empezar ahora"
- THEN they SHALL be navigated to `/booking.html`

### Requirement: How it works section

The page SHALL explain the booking and learning process in three steps.

#### Scenario: Process steps

- GIVEN a visitor is on the services page
- THEN three numbered steps SHALL be displayed:
  1. Reserva tu clase de diagnóstico (Book diagnostic class)
  2. Primera sesión: diagnóstico y plan (First session: diagnosis and plan)
  3. Empieza a mejorar (Start improving)
- AND a "Reservar primera clase" button SHALL be displayed

### Requirement: Pricing note

The pricing section SHALL include a disclaimer about plan flexibility.

#### Scenario: Flexibility disclaimer

- GIVEN a visitor is on the services page
- THEN below the pricing grid a note SHALL be displayed
- AND the note SHALL state: "Sin letra pequeña. Se puede cambiar de plan en cualquier momento"

## Out of Scope

- Booking functionality (see `booking-flow` spec)
- Payment processing
- Subject-specific content or curriculum details
