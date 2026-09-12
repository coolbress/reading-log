---
name: Reading Log
description: A personal ledger of finished books, styled as a bank passbook.
colors:
  cover-navy: "#1b2540"
  cover-navy-dark: "#0d0f18"
  cover-ink: "#f3efe4"
  cover-ink-dark: "#ece6d4"
  cover-ink-muted: "#a9a493"
  cover-ink-muted-dark: "#8f8a78"
  page-ivory: "#f3efe4"
  page-plum-dark: "#241f2b"
  ink: "#1c1f2e"
  ink-dark: "#ece6d4"
  ink-muted: "#5b5445"
  ink-muted-dark: "#a89f8a"
  rule: "#d9cfb8"
  rule-dark: "#3a3446"
  gold: "#7c5e22"
  gold-dark: "#d9ab52"
  gold-strong: "#8a6a1f"
  gold-strong-dark: "#e6bd6c"
  button-fg: "#f8f4e9"
  button-fg-dark: "#1c1720"
typography:
  label:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0.1em to 0.16em, uppercase"
  body:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  title:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.9rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  mono:
    fontFamily: "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
    fontSize: "0.82rem to 0.85rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
rounded:
  none: "0px"
  hairline: "2px"
spacing:
  xs: "0.35rem"
  sm: "0.6rem"
  md: "1.05rem"
  lg: "1.5rem"
  xl: "2.75rem"
  xxl: "3.5rem"
components:
  button-primary:
    backgroundColor: "{colors.gold-strong}"
    textColor: "{colors.button-fg}"
    rounded: "{rounded.hairline}"
    padding: "0.75rem 1.6rem"
  input-underline:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.4rem 0.1rem"
---

# Design System: Reading Log

## Overview

**Creative North Star: "The Passbook Ledger"**

A finished book is recorded the way a bank teller stamps a deposit: entered once, dated, numbered, never edited. The page is built as a physical passbook — a navy cover band with a torn perforation tearing away into an ivory ledger page, a deposit-slip form, and a running ledger of stamped entries. There are no cards, no colored side-borders, no serif type, and no decorative gradients standing in for texture; the only ornament is the ledger itself: hairline rules, tabular gold entry numbers, and mono-set dates.

This is a single-user, single-template product (per PRODUCT.md): one self-contained `index.html`, no framework, no build step, no external assets. The passbook world is expressed entirely in system fonts and CSS custom properties, confirmed for WCAG AA contrast in both light and dark `prefers-color-scheme`.

**Key Characteristics:**
- Navy cover band torn away from an ivory ledger page via a perforation seam
- Gold ink reserved for entry numbers and the one primary action
- System sans for labels (tracked uppercase) and system mono for tabular dates/numbers
- Hairline rules divide ledger rows; no cards, no borders-as-color-coding
- New entries stamp into place with a brief scale+rotate animation, skipped under reduced motion

## Colors

Deep navy cover, ivory ledger page, and a single gold stamp accent — restrained enough that gold reads as a deliberate rarity, not a theme color.

### Primary
- **Gold Stamp** (`#7c5e22`, strong variant `#8a6a1f`): the accent ink. `--gold` marks ledger entry numbers; `--gold-strong` is reserved for the primary button and input focus state. The strong variant was corrected from `#a67a2a` to `#8a6a1f` in light mode during finish review to bring the button's text contrast to AA (~4.6:1); dark mode's `#e6bd6c` was untouched.

### Neutral
- **Cover Navy** (`#1b2540`, dark-mode `#0d0f18`): the header band background, evoking a passbook's embossed cover.
- **Cover Ink** (`#f3efe4`, dark-mode `#ece6d4`): text on the navy cover band.
- **Page Ivory** (`#f3efe4`, dark-mode `#241f2b`): the ledger page background.
- **Ink** (`#1c1f2e`, dark-mode `#ece6d4`): primary body/entry text on the page.
- **Ink Muted** (`#5b5445`, dark-mode `#a89f8a`): labels, dates' companion text, secondary entry lines (author).
- **Rule** (`#d9cfb8`, dark-mode `#3a3446`): hairline dividers between ledger rows and the dashed binding rule.

### Named Rules
**The One Ink Rule.** Gold is the only accent color in the system; it appears on entry numbers and the primary action only, never as a background fill, border, or decorative wash.

## Typography

**Body/Label Font:** System sans (`-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`)
**Mono Font:** System mono (`ui-monospace, "SF Mono", Menlo, Consolas, monospace`)

**Character:** No custom webfonts — the no-external-assets constraint makes the system stack itself the typeface. Sans carries prose and tracked-uppercase labels; mono is reserved for anything tabular (dates, entry numbers), giving the ledger a register-book rhythm.

### Hierarchy
- **Title** (700, 1.9rem, tight `-0.01em` tracking): the "Reading Log" cover heading.
- **Body** (400, 1rem): entry titles/authors and form input text.
- **Label** (600, 0.72rem, 0.1em–0.16em uppercase tracking): section headers ("New entry"), field labels, ledger column headers — the ledger-header register voice.
- **Mono/Tabular** (400, 0.82–0.85rem, tabular-nums): entry numbers (gold) and finished-on dates (muted ink).

### Named Rules
**The No Serif Rule.** Type is system-sans or system-mono only; no serif face appears anywhere in the system, keeping the passbook register plain rather than literary.

## Layout

Single-column passbook capped at `40rem` (`.passbook`), centered, full-height. Three vertical zones: cover band, deposit-slip form, ledger — each with generous top/bottom padding (`2.75rem`–`3.25rem`) rather than internal card padding. Ledger rows use a fixed three-column grid (`2.75rem` number / `5.5rem` date / flexible entry) that holds at all widths. At `640px` and above, the ledger gains a `1px dashed` left-edge binding rule (`--rule`) with `1.25rem` left padding — the stitched-binding detail retreats below that width rather than cramping mobile.

## Elevation & Depth

Flat throughout. No shadows anywhere in the stylesheet; depth is conveyed by the navy/ivory value contrast between the cover band and the page, plus the perforation seam (a repeating radial-gradient of small circles) marking where the "torn" deposit slip separates from the cover.

## Shapes

Square-cornered by default (`border-radius: 0` on inputs); the one exception is the primary button at a bare `2px` radius, barely softening the corner. Inputs are borderless except for a single `1px` bottom rule that thickens to `2px` gold on focus — an underline field, not a boxed one. The cover's lower edge is perforated (a repeating dot pattern) rather than a straight or gradient edge, the system's one recurring non-rectangular silhouette.

## Components

### Buttons
- **Shape:** Near-square, `2px` radius.
- **Primary:** `--gold-strong` background, `--button-fg` text, `0.75rem 1.6rem` padding, `700` weight, `0.85rem` uppercase with `0.04em` tracking. Only one button exists in the system ("Stamp it in").
- **Hover / Focus:** Hover dims to `0.92` opacity; active scales to `0.97`; focus-visible shows a `2px` solid outline in `--focus-on-page`, offset `3px`. Transition disabled under `prefers-reduced-motion`.

### Inputs / Fields
- **Style:** Transparent background, no border box, single `1px` bottom rule in `--rule`, no radius.
- **Focus:** Bottom rule switches to `--gold-strong` and thickens to `2px`; no glow or box-shadow.
- **Labels:** Uppercase, tracked, muted-ink, sit above each field (deposit-slip style), not floating or inline.

### Ledger Row (signature component)
The passbook's core repeating unit: a three-column grid row (gold tabular entry number, mono date, title+author stack) separated by a hairline bottom rule, with no card wrapper or background change between rows. The newest entry (`.is-new`) plays a one-shot 0.4s "stamp-in" animation (opacity 0→1, scale 1.06→1, rotate -1.2deg→0, `cubic-bezier(0.2, 0.9, 0.3, 1)`), replaced with no animation under `prefers-reduced-motion: reduce`.

### Cover / Perforation Seam (signature component)
The navy cover band's bottom edge carries a `radial-gradient`-based perforation (small ivory circles repeating on a `1.1rem × 1rem` tile), simulating a torn deposit-slip edge between the cover and the ledger page below.

## Do's and Don'ts

### Do:
- **Do** keep gold (`--gold` / `--gold-strong`) limited to entry numbers, focus states, and the single primary action.
- **Do** set tabular/numeric content (dates, entry numbers) in the system mono stack with `font-variant-numeric: tabular-nums`.
- **Do** use uppercase tracked system-sans labels (`0.72rem`, `600`, `0.1–0.16em` tracking) for field labels and section/column headers.
- **Do** separate ledger rows with hairline `--rule` borders instead of cards or background shading.
- **Do** gate any new entrance animation behind a `prefers-reduced-motion: reduce` fallback, matching the stamp-in treatment.

### Don't:
- **Don't** introduce cards or boxed containers; the ledger row and the cover band are the only surface treatments this world uses.
- **Don't** use colored side-borders to signal state or category; the system's only border color is the neutral `--rule` hairline (plus gold on input focus).
- **Don't** add kicker or eyebrow labels above headings — flagged and removed by the design detector during this build; not a device this world uses, so it is not carried forward as a pattern.
- **Don't** introduce serif type anywhere; the type system is system-sans + system-mono only, also flagged and corrected during this build.
- **Don't** use repeating-gradient decoration as a generic texture; the one repeating radial-gradient in the system is the cover's perforation seam, a specific structural detail, not a decorative motif to reuse elsewhere.
- **Don't** add a new external font, icon set, or build-step dependency; PRODUCT.md fixes this as a standing constraint, not a per-surface choice.
