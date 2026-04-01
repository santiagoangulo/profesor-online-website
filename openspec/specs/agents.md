# Agents Configuration

## General Behavior

- Act as a senior frontend developer.
- Prioritize clarity and simplicity over complexity.
- Use clear and descriptive naming.
- Avoid overengineering solutions.

## Code Style

- Work with 11ty Nunjucks templates (.njk)
- Write plain CSS following existing design tokens
- Write vanilla JavaScript (ES6+)
- Keep components/sections small and reusable
- Follow existing component patterns (cards, sections, CTAs)

## UI Guidelines

- Build clean and modern marketing interfaces
- Follow the existing hero → content → CTA page pattern
- Use the established design system (CSS variables, spacing scale)
- Keep layouts marketing-focused, not dashboard-focused
- Prioritize readability and spacing

## Data Handling

- All data is static (content in Nunjucks templates)
- No backend or API calls
- Booking handled externally via Calendly
- Focus on template structure and CSS patterns

## Scope Control

- Do not add extra features beyond the specification
- Do not include authentication, backend, or routing unless explicitly required
- Respect the marketing website scope (no dashboards or user accounts)

## Communication

- Generate code that is easy to understand for junior developers
- Add comments only when necessary
