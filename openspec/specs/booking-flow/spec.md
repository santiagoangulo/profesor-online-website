# booking-flow Specification

## Purpose

Document the end-to-end booking journey for new students to reserve their diagnostic class. This spec covers the visitor-facing booking page, the Calendly widget integration, email confirmations, and rescheduling behavior.

## Requirements

### Requirement: Free diagnostic session

The first class is a diagnostic session to assess student needs.

#### Scenario: First-time booking at no cost

- GIVEN a new visitor is on the booking page
- WHEN they complete a booking
- THEN payment information SHALL be collected per the selected pricing plan
- AND the session is confirmed

### Requirement: Booking confirmation

Upon successful booking, the user SHALL receive a confirmation email containing the Google Meet session link.

#### Scenario: Confirmation email delivery

- GIVEN a user has completed a booking
- WHEN the booking is confirmed
- THEN they SHALL receive an email with the Google Meet link
- AND the email SHALL include the scheduled date and time

### Requirement: Local timezone display

The booking calendar SHALL automatically display availability in the user's local timezone.

#### Scenario: Timezone conversion

- GIVEN a user is booking from a timezone other than Spain (CET)
- WHEN they view the calendar
- THEN the available slots SHALL be shown in their local timezone
- AND the time displayed SHALL match the user's system clock

### Requirement: Availability windows

Classes SHALL be available Monday through Saturday, from 9:00 AM to 9:00 PM (Spain/CET timezone).

#### Scenario: Viewing available hours

- GIVEN a user is on the booking page
- WHEN they view the calendar
- THEN only slots within Monday-Saturday, 9:00-21:00 Spain time SHALL be shown

### Requirement: Rescheduling with notice

Users SHALL be able to reschedule a confirmed session provided they have 24 or more hours before the scheduled time.

#### Scenario: Reschedule with adequate notice

- GIVEN a user has a confirmed booking
- WHEN they access their Calendly confirmation link
- AND the session is more than 24 hours away
- THEN they SHALL be able to select a new available time slot
- AND the original booking SHALL be automatically cancelled

#### Scenario: Reschedule denied with insufficient notice

- GIVEN a user has a confirmed booking
- WHEN they access their Calendly confirmation link
- AND the session is less than 24 hours away
- THEN the reschedule option SHALL NOT be available
- AND the user SHALL be informed of the 24-hour policy

### Requirement: Cancellation with notice

Users SHALL be able to cancel a confirmed session provided they have 24 or more hours before the scheduled time.

#### Scenario: Cancel with adequate notice

- GIVEN a user has a confirmed booking
- WHEN they access their Calendly confirmation link
- AND the session is more than 24 hours away
- THEN they SHALL be able to cancel the booking
- AND they SHALL receive a cancellation confirmation

### Requirement: Session duration

All booked sessions SHALL be 60 minutes in duration.

#### Scenario: Standard session length

- GIVEN a user has booked any session
- WHEN the booking is confirmed
- THEN the session duration SHALL be 60 minutes

## Technical Notes

- The booking widget uses Calendly inline embed at `https://calendly.com/santi-maths-teacher`
- Email confirmations and rescheduling are handled by Calendly's built-in workflow
- Google Meet links are generated automatically by Calendly upon booking
- No custom backend is required; all booking logic is managed by Calendly

## Out of Scope

- Payment processing
- Subject selection during initial booking
- Custom email sequences beyond Calendly defaults
- Integration with any CRM or student management system
