# Tolkz Speakers USA — Static Site Build Report

Built: Fri Nov 20, 2026 · Location: `~/workspace/working/tolkz-site/`
Regenerate any time with `python3 build.py` (all copy lives in that file).

## Pages built (6)

| Page | Contents |
|---|---|
| `index.html` | Hero with Oliver stage photo; three services (Book a Speaker / Get Represented / Train & Certify via TIPS); featured speakers strip (Oliver + 3 roster speakers); 4-step "How Booking Works"; booking CTA band |
| `about.html` | Company story (adapted from the old site's own About copy via Wayback); US LLC formed March 31, 2026; vision — best speakers bureau for African and African-American speakers; address of record 3387 Brownlow Ave, St Louis Park, MN 55426; Founder & CEO section on Oliver Nshom with portrait |
| `speakers.html` | Full roster: 23 cards (Oliver + 22 approved speakers) with name, professional title, location; booking note; apply CTA |
| `become-a-speaker.html` | Full application form (basic info, profile, experience, media links, availability & fees, terms checkbox) modelled on the old `/become-a-speaker.php` form; submits via FormSubmit AJAX to ceo@tolkzspeakers.com with on-page success/error states and a clear email fallback note |
| `academy.html` | TIPS Academy: CES $495 (4 wks) → CPS $1,495 (8–12 wks) → CPTC $2,995 (12–16 wks); Complete Pathway $3,995 (vs $4,985 separately); 70%/70% assessment standard; founding cohorts begin January 11, 2027; links to https://tipscampus.com and https://www.tipstexas.org/academy.html; **no buy buttons** (selection-first — CTAs route to Contact); CANASA described only as a *proposed* partnership, mirroring the canonical wording on the TIPS site |
| `contact.html` | ceo@tolkzspeakers.com (bureau/corporate); speaking@olivernshom.com (speaking & coaching inquiries about Oliver); +1 (507) 319-5381; address of record; booking/application guidance cards |

Design: self-contained static HTML, inline CSS per page, Google Fonts only (Fraunces + Inter), deep navy + gold premium bureau theme, mobile-responsive, skip-link + ARIA labels, consistent nav/footer on every page (footer: © 2026 Tolkz Speakers USA, address, ceo@tolkzspeakers.com, www.tolkzspeakers.com). Company voice throughout; "Tolkz" spelling verified on all pages.

## Speakers included — and their source

**Source for the whole roster:** the approved-speakers spreadsheet sent by Abraham Thompson on Oct 22, 2026 ("Fwd: Approved Tolkz Speakers", file `speakers_approved_2025-11-14`), retrieved from Gmail for this build. Names, professional titles and locations are reproduced from that list:

Oliver Nshom (Founder & Featured Speaker) · Ly Smith · Ebot Patience Ojong · Klieng Glory · Bamu Kingsley Tabifor · Njei Kingsly Achiri · Yokwei Promise Kenkoh · Kelvin Mumba · Terence Musong Ndifor · Sai Ramachandran · Mirabel Nugi Kanjo · Ishimwe Solange · Ernest Marvellous Kumi · Denise Bowles · Nsahlar Didier Yinkfu · Dr. Joybert Javnyuy · Bryan Turkel · Rob Kalwarowsky · Melanie Puemedji · Karen Attyah · Amengwo Mbah Dilan · Fonyuy Catherine Limnyuy · Fiona Luma Tankoh

Roster decisions made during the build:
- The sheet lists Kelvin Mumba twice (Kelvin Elias Mumba / Kelvin Mumba, two different emails, both Lusaka) — merged into **one** roster entry combining both listed titles.
- For Denise Bowles, Bryan Turkel and Rob Kalwarowsky, the sheet's "Professional Title" column actually contains a talk title — displayed on their cards as "Signature talk: …" rather than as a job title.
- **No testimonials were carried over.** The old codebase (~/workspace/working/tolkz-edit/) and the July 2025 Wayback homepage contain testimonial quotes, but the two sources contradict each other and the quotes could not be independently verified, so they were left out per the no-invented-claims rule. The old site's template statistics ("10K+ events hosted", "5K+ speakers") were likewise **not** used.
- The three upcoming events Oliver listed for the old site on Oct 22, 2026 (Yaoundé Nov 27, Savannah, Buea Dec 5) were **not** added — circumstances have since changed (Nov 27 stand-in proposal; Dec 5 is the CANASA convention) and the page spec did not call for an events section.

## Assets used

- `images/oliver-nshom.jpg` — Oliver's navy-suit portrait (from `~/workspace/your_files/brand-photos/oliver-navy-suit-portrait.jpg`), used on About, the roster card and the home featured strip.
- `images/oliver-stage.jpg` — Oliver delivering a keynote (from `~/workspace/your_files/brand-photos/oliver-keynote-stage-blue.jpg`), home hero.
- All other roster speakers are shown with a designed gold-initial monogram tile — **no photos were invented or borrowed**. `~/workspace/working/tolkz-headshots/` was empty, and no headshot files matching the approved roster exist in the workspace headshot folders (those hold CANASA convention speakers, a different roster). When real headshots for roster speakers are supplied, drop them into `images/` and swap the monogram block for an `<img>` in `build.py`.

## ⚠️ Action required — FormSubmit activation

The application form posts to `https://formsubmit.co/ajax/ceo@tolkzspeakers.com`. **The very first real submission triggers a FormSubmit activation email to ceo@tolkzspeakers.com — Oliver must click the activation link in that email** before applications will be delivered. Until activation, submitters will see the form's error/fallback message directing them to email ceo@tolkzspeakers.com directly, so no application is silently lost.

## Could not verify / not done

- No deployment performed — this deliverable is the site files only. Pointing www.tolkzspeakers.com at this static site (new Vercel project or other static host under Oliver's control, plus DNS) is a separate step; the old Next.js deployment remains paused under the developer's Vercel.
- Ernest Marvellous Kumi's listed title is simply "President" (of an unnamed organisation) — reproduced as listed; Oliver may want to confirm/expand it.
- Sai Ramachandran's contact email on the sheet (`tolkz@ramachandr.in`) was already flagged in October as possibly truncated — not used on the site (no speaker emails are published), noted here only for the record.
- Form fields mirror the old form's fee ranges and experience bands exactly as archived.
