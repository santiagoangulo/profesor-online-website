# i18n Specification

## Purpose

Document the internationalization (i18n) behavior of the website. The site supports two languages: Spanish (ES) as the primary language and English (EN) as the secondary language. All user-facing text can be toggled between these languages across all pages including the material-didactico section.

## Requirements

### Requirement: Language detection

The system SHALL detect the user's preferred language on first visit.

#### Scenario: Browser language detection

- GIVEN a new visitor loads any page
- WHEN the browser language starts with "es"
- THEN the site SHALL default to Spanish (ES)
- WHEN the browser language does not start with "es"
- THEN the site SHALL default to English (EN)

### Requirement: Language persistence

The selected language SHALL persist across page navigation and sessions.

#### Scenario: Language stored in localStorage

- GIVEN a user selects a language
- THEN the selection SHALL be saved to localStorage under key `lang`
- AND on subsequent page loads, the saved language SHALL be applied

#### Scenario: Language persists across all pages

- GIVEN a user is viewing the site in Spanish
- WHEN they navigate to any other page (including material-didactico sections and chapters)
- THEN the site SHALL remain in Spanish

### Requirement: Language toggle

Users SHALL be able to switch between Spanish and English via a toggle control.

#### Scenario: Toggle control location

- GIVEN a user is on any page (main site or material-didactico)
- THEN a language toggle SHALL be visible in the header
- AND the toggle SHALL show "ES" and "EN" buttons

#### Scenario: Switching to English

- GIVEN a user is viewing the site in Spanish
- WHEN they click the "EN" button
- THEN all translatable elements SHALL display English text
- AND the "EN" button SHALL show as active
- AND the "ES" button SHALL show as inactive

#### Scenario: Switching to Spanish

- GIVEN a user is viewing the site in English
- WHEN they click the "ES" button
- THEN all translatable elements SHALL display Spanish text
- AND the "ES" button SHALL show as active
- AND the "EN" button SHALL show as inactive

### Requirement: No language flash on load

The language SHALL be applied before the page is painted to avoid visual flash.

#### Scenario: Synchronous language application

- GIVEN a user loads any page
- WHEN the page renders
- THEN the correct language SHALL be applied immediately
- AND there SHALL be no visible flash of incorrect language

### Requirement: Translatable elements

All text content SHALL be available in both Spanish and English.

#### Scenario: Translatable text attributes

- GIVEN an element has translatable content
- THEN it SHALL have both `data-es` and `data-en` attributes
- AND the `data-es` attribute SHALL contain the Spanish text
- AND the `data-en` attribute SHALL contain the English text

#### Scenario: Text content switches

- GIVEN a user is viewing a page in Spanish
- WHEN they switch to English
- THEN the element's innerHTML SHALL be replaced with the `data-en` value
- GIVEN a user is viewing a page in English
- WHEN they switch to Spanish
- THEN the element's innerHTML SHALL be replaced with the `data-es` value

### Requirement: HTML lang attribute

The HTML document's lang attribute SHALL reflect the current language.

#### Scenario: Lang attribute update

- GIVEN a user switches languages
- THEN the `<html>` element's `lang` attribute SHALL be updated
- AND it SHALL match the current language code ("es" or "en")

### Requirement: Page title translation

Page titles SHALL be translated when the language changes.

#### Scenario: Title translation

- GIVEN a page has a translatable title
- WHEN a user switches languages
- THEN the `<title>` element SHALL be updated with the translated version

### Requirement: Dark/light theme

Theme selection SHALL NOT affect language preference.

#### Scenario: Theme independent of language

- GIVEN a user selects English and dark theme
- WHEN they switch back to Spanish
- THEN the theme SHALL remain dark
- AND the language SHALL be Spanish

## Technical Implementation

- Language detection and switching logic is in `app.js`
- The `setLang(lang)` function handles all language switching
- Language is initialized immediately on page load via IIFE to prevent flash
- LocalStorage key: `lang`
- Default browser detection: `navigator.language.startsWith('es')`
- All translatable text uses `data-es` and `data-en` attributes
- Header and footer templates use absolute paths to ensure consistent behavior across all URL depths

## Out of Scope

- URL-based language routing (e.g., `/en/booking.html`)
- Language-specific SEO meta tags
- Translation of dynamically generated content
- RTL language support
