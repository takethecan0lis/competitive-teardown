---
name: product-explorer
description: Guides first-hand exploration of an app, website, or desktop software for a competitive teardown, including driving an iPhone app through iPhone Mirroring on a Mac, guided handoffs to the user, and a strict safety protocol (create-and-cancel, never save, buy, or change real data). Use during a teardown's exploration step, or when the user says "click through the app", "walk the app", "map every screen", "explore the menus", "use iPhone Mirroring", or "screen share the iPhone".
---

# Product Explorer

Explore the product first-hand with the user, in the main conversation. Map every reachable screen, open every create and edit form without saving, capture copy and options, and hand the user anything only they should do. Read `references/safety-protocol.md` before the first action and follow it without exception.

## Objective and benefit

- **Objective:** This skill aims to map every screen of a product safely, with the tester's account left exactly as it was found.
- **Benefit:** You get a coverage count of screens visited over screens found, with the forms, options and copy recorded, and no saved, bought or sent changes on your account or phone.
- **Why it is worth having:** First-hand evidence of what a product actually does is hard to get from the outside, and a strict create-and-cancel rule lets you collect it without risking real data.

Adopted, not measured: no result has been measured yet.

## Ask first

Before any exploration, ask the user, one question at a time, in this order:
1. Is the account a real account or a test account? Default: a test account. If it is real, apply the tighter rules in the safety protocol and say so.
2. How will the product be reached (web, desktop, iPhone Mirroring, recordings)? This is the user's choice; offer no default beyond the product's own platform.

## 1. Set up

1. Confirm the access mode with the user:
   - **Website or web app:** use the built-in browser or Claude in Chrome (follow that browser's skill). Read pages as text first; screenshot only when layout matters.
   - **Desktop software:** use computer use (load the computer-use skill and request access to the app).
   - **iPhone app:** use iPhone Mirroring on the user's Mac through computer use. Follow `references/iphone-mirroring.md`.
   - **Android app:** ask the user for screen recordings or a mirroring tool they already use; no direct control.
2. Confirm the account is a trial or test account where possible, and note what real data it holds. Tighten the protocol if real data is present.
3. Create `evidence/sessions/session-plan.md` (sessions, goals, deadlines such as trial end) and open `evidence/sessions/session-NN-notes.md`. Record app version and build on the first screen that shows it.

## 2. Build the coverage checklist (MAP tree)

Start `docs/<product>/02-product-map.md` as a tree of MAP IDs: every tab, menu item, settings page, sheet, and modal. Mark each node unvisited, visited, or blocked (with reason: paywall, needs data, needs another account, needs a set time). Report coverage as visited over total. "Spider everything" means driving this number toward 100 percent and explaining the remainder.

## 3. Explore each node

For every node:
1. Navigate there and capture: title, every visible label and option, default values, empty states, help text, upsell placement, and the exact tone of the copy (short excerpts only).
2. Scroll to the end. Open every disclosure, menu, and info icon.
3. For every object type the user can create (project, document, folder, tag, reminder, and so on): open the **new** form, record every field, its type, required or optional, defaults, and limits, then **cancel without saving**.
4. For every object type: open **edit** on at least one existing item, record the fields and any destructive options (delete, archive), then back out without saving.
5. Record settings and configuration options exhaustively, including notification types.
6. Log the node as visited in the MAP tree and the session notes.

## 4. Guided handoff (when the user must act)

Use `references/guided-handoff.md`. Hand off for: sign-ins and passwords, any typing the tool cannot do, anything that saves or changes real data, purchases, time-of-day moments (scheduled reminders, notifications, events), and screen recordings. The pattern is always: navigate to the exact screen and leave it open, tell the user in one or two lines what to tap or type and why, wait for "done", capture the result.

## 5. Real moments and recordings (full depth)

Schedule tasks the user performs at the moment they naturally occur (first open of the day, a scheduled reminder, completing an onboarding flow start to finish, an event day). Ask for a screen recording when timing matters. To read a recording: extract scene-change frames with ffmpeg, build contact sheets, then sample uniformly to catch gradual scrolls. Record structure and product copy only; never the user's entries, notifications, or lock-screen content.

## 6. Participant notes

Keep `evidence/sessions/participant-notes.md`. Record the user's confusion ("I couldn't find where to add a note"), reactions ("this feels cluttered"), and workarounds as REPORTED evidence with the session and step. These often become the most valuable findings.

## 7. Close each session

Update the MAP coverage, list new open questions with owners, note any protocol incidents and how they were reversed, and tell the user what is covered and what the next session needs.

## What this does not verify

- That every screen was reached; blocked nodes (paywall, missing data, other people) stay listed as blocked, not as covered.
- That the account is unchanged beyond what the session notes record; an unseen change is possible, so check the account yourself afterward.
- Behavior at other times, on other devices or for other account types; it records only what the session showed.
