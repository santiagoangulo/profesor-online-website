# theme-toggle Specification

## Purpose

Document the dark/light theme toggle functionality. The site supports system preference detection and user override with persistence across sessions.

## Requirements

### Requirement: Theme detection

The system SHALL detect the user's preferred color scheme on first visit.

#### Scenario: System dark mode preference

- GIVEN a visitor loads the site for the first time
- WHEN `prefers-color-scheme: dark` is set in the browser
- THEN the site SHALL display in dark theme by default

#### Scenario: System light mode preference

- GIVEN a visitor loads the site for the first time
- WHEN `prefers-color-scheme: light` is set in the browser
- THEN the site SHALL display in light theme by default

### Requirement: Theme toggle control

Users SHALL be able to manually switch between dark and light themes.

#### Scenario: Toggle button presence

- GIVEN a user is on any page
- THEN a theme toggle button SHALL be visible in the header
- AND the toggle SHALL show an icon representing the current theme

#### Scenario: Toggle to dark theme

- GIVEN a user is viewing the site in light theme
- WHEN they click the theme toggle
- THEN the theme SHALL switch to dark
- AND the toggle icon SHALL update to show a sun icon
- AND the toggle `aria-label` SHALL update to "Cambiar a modo claro"

#### Scenario: Toggle to light theme

- GIVEN a user is viewing the site in dark theme
- WHEN they click the theme toggle
- THEN the theme SHALL switch to light
- AND the toggle icon SHALL update to show a moon icon
- AND the toggle `aria-label` SHALL update to "Cambiar a modo oscuro"

### Requirement: Theme persistence

The selected theme SHALL persist across page navigation.

#### Scenario: Theme persists on navigation

- GIVEN a user has selected dark theme
- WHEN they navigate to another page
- THEN the theme SHALL remain dark

### Requirement: CSS variable theming

Theme changes SHALL be implemented via CSS custom properties (variables).

#### Scenario: Light theme colors

- GIVEN the site is in light theme
- THEN CSS variables SHALL use light theme values
- AND `--color-bg` SHALL be `#f5f6f8`
- AND `--color-primary` SHALL be `#1e2d6e`

#### Scenario: Dark theme colors

- GIVEN the site is in dark theme
- THEN CSS variables SHALL use dark theme values
- AND `--color-bg` SHALL be `#0f1120`
- AND `--color-primary` SHALL be `#6d85e0`

### Requirement: Data-theme attribute

Theme SHALL be controlled via the `data-theme` attribute on the HTML element.

#### Scenario: Light theme data attribute

- GIVEN the site is in light theme
- THEN `<html data-theme="light">` SHALL be set

#### Scenario: Dark theme data attribute

- GIVEN the site is in dark theme
- THEN `<html data-theme="dark">` SHALL be set

### Requirement: Reduced motion preference

Theme transitions SHALL respect the `prefers-reduced-motion` media query.

#### Scenario: Disable animations when preferred

- GIVEN a user has `prefers-reduced-motion: reduce` set
- WHEN the theme is toggled
- THEN animations SHALL be disabled or minimal
- AND transitions SHALL complete instantly

## Technical Implementation

- Theme detection and toggle logic is in `app.js`
- Theme CSS variables are defined in `style.css` under `:root` and `[data-theme="dark"]`
- Default system preference detection uses `matchMedia('(prefers-color-scheme: dark)')`
- Theme state is stored via the `data-theme` attribute (not localStorage)

## Out of Scope

- Theme persistence via localStorage (relies on CSS system preference defaults)
- Per-component theme overrides
- Auto-scheduling themes (e.g., night mode at certain hours)
