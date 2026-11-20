#!/usr/bin/env python3
"""Build script for the Tolkz Speakers USA static site.
Generates six self-contained HTML pages with shared inline CSS, nav and footer.
Source of truth for facts: see BUILD-REPORT.md.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
:root{
  --navy:#081527; --navy-2:#0c2140; --navy-3:#123058;
  --gold:#c9a24b; --gold-2:#e6cb7e; --gold-deep:#a07f2c;
  --cream:#f7f3ea; --paper:#fffdf8; --ink:#16222e; --muted:#5b6b7a;
  --line:#e3dcc9; --radius:14px;
  --shadow:0 10px 30px rgba(8,21,39,.14);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:var(--ink);background:var(--paper);line-height:1.65;font-size:16.5px}
h1,h2,h3,.display{font-family:'Fraunces',Georgia,'Times New Roman',serif;font-weight:600;line-height:1.15;color:var(--navy)}
a{color:var(--gold-deep)}
img{max-width:100%;display:block}
.wrap{max-width:1140px;margin:0 auto;padding:0 22px}
.skip{position:absolute;left:-999px;top:0;background:var(--gold);color:var(--navy);padding:10px 16px;z-index:99;font-weight:600}
.skip:focus{left:10px;top:10px}
/* Header */
.topbar{background:var(--navy);color:#cfd9e4;font-size:.85rem}
.topbar .wrap{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;padding-top:7px;padding-bottom:7px}
.topbar a{color:var(--gold-2);text-decoration:none}
header.site{background:var(--navy-2);position:sticky;top:0;z-index:50;box-shadow:0 2px 14px rgba(0,0,0,.25)}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.wordmark{text-decoration:none;line-height:1}
.wordmark .wm-name{font-family:'Fraunces',Georgia,serif;font-size:1.9rem;font-weight:700;letter-spacing:.06em;color:#fff}
.wordmark .wm-name em{font-style:normal;color:var(--gold)}
.wordmark .wm-sub{display:block;font-size:.62rem;letter-spacing:.42em;color:var(--gold-2);font-weight:600;margin-top:3px}
nav.main{display:flex;gap:4px;flex-wrap:wrap;align-items:center}
nav.main a{color:#e8edf3;text-decoration:none;font-weight:500;font-size:.98rem;padding:9px 13px;border-radius:8px}
nav.main a:hover{background:rgba(201,162,75,.16);color:#fff}
nav.main a[aria-current="page"]{color:var(--gold-2);box-shadow:inset 0 -2px 0 var(--gold)}
.btn{display:inline-block;background:linear-gradient(180deg,var(--gold-2),var(--gold));color:var(--navy);font-weight:700;text-decoration:none;padding:12px 24px;border-radius:10px;border:1px solid var(--gold-deep);box-shadow:0 4px 14px rgba(160,127,44,.35)}
.btn:hover{filter:brightness(1.06)}
.btn.ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.55);box-shadow:none}
.btn.ghost:hover{border-color:var(--gold-2);color:var(--gold-2)}
.btn.navy{background:var(--navy);color:#fff;border-color:var(--navy)}
.btn.small{padding:9px 18px;font-size:.95rem}
/* Hero */
.hero{background:radial-gradient(1100px 480px at 85% -10%,var(--navy-3),transparent),linear-gradient(160deg,var(--navy) 0%,var(--navy-2) 60%,#0a1c33 100%);color:#eef2f7;padding:74px 0 66px}
.hero .kicker{color:var(--gold-2);letter-spacing:.32em;font-size:.78rem;font-weight:700;text-transform:uppercase}
.hero h1{color:#fff;font-size:clamp(2.3rem,5.2vw,3.7rem);margin:16px 0 18px;max-width:16em}
.hero h1 em{font-style:italic;color:var(--gold-2)}
.hero p.lede{font-size:1.18rem;color:#c9d5e1;max-width:44em}
.hero .cta-row{display:flex;gap:14px;flex-wrap:wrap;margin-top:30px}
.hero-grid{display:grid;grid-template-columns:1.25fr .9fr;gap:44px;align-items:center}
.hero-photo{border-radius:18px;overflow:hidden;border:1px solid rgba(201,162,75,.5);box-shadow:var(--shadow)}
.hero-photo img{width:100%;height:100%;object-fit:cover;aspect-ratio:4/3}
.hero-photo figcaption{background:rgba(8,21,39,.92);color:#d7dee7;font-size:.86rem;padding:10px 14px}
/* Sections */
section.block{padding:64px 0}
section.block.alt{background:var(--cream)}
.sec-head{max-width:46em;margin-bottom:34px}
.sec-head .kicker{color:var(--gold-deep);letter-spacing:.3em;font-size:.75rem;font-weight:700;text-transform:uppercase}
.sec-head h2{font-size:clamp(1.7rem,3.4vw,2.4rem);margin:10px 0 10px}
.sec-head p{color:var(--muted);font-size:1.06rem}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px;box-shadow:0 3px 12px rgba(8,21,39,.05)}
.card h3{font-size:1.28rem;margin-bottom:8px}
.card p{color:var(--muted)}
.card .icon{width:46px;height:46px;border-radius:12px;background:var(--navy);color:var(--gold-2);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:1.3rem;margin-bottom:16px}
.steps{counter-reset:step;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.step{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px;position:relative}
.step::before{counter-increment:step;content:counter(step,decimal-leading-zero);font-family:'Fraunces',serif;font-size:1.6rem;color:var(--gold);font-weight:700;display:block;margin-bottom:8px}
.step h3{font-size:1.12rem;margin-bottom:6px}
.step p{color:var(--muted);font-size:.97rem}
/* Speakers */
.sp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:22px}
.sp-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:0 3px 12px rgba(8,21,39,.05);display:flex;flex-direction:column}
.sp-photo{aspect-ratio:1/1;overflow:hidden;background:var(--navy-2)}
.sp-photo img{width:100%;height:100%;object-fit:cover}
.sp-mono{aspect-ratio:1/1;background:linear-gradient(150deg,var(--navy-2),var(--navy));display:flex;align-items:center;justify-content:center}
.sp-mono span{font-family:'Fraunces',serif;font-size:3rem;color:var(--gold-2);border:2px solid rgba(201,162,75,.55);border-radius:50%;width:104px;height:104px;display:flex;align-items:center;justify-content:center;letter-spacing:.04em}
.sp-body{padding:20px 22px 24px}
.sp-body h3{font-size:1.16rem;margin-bottom:5px}
.sp-body .title{color:var(--gold-deep);font-weight:600;font-size:.95rem;margin-bottom:6px}
.sp-body .loc{color:var(--muted);font-size:.9rem}
.sp-body .talk{color:var(--muted);font-size:.94rem;font-style:italic}
.badge{display:inline-block;background:var(--gold);color:var(--navy);font-size:.7rem;font-weight:800;letter-spacing:.14em;padding:4px 10px;border-radius:99px;text-transform:uppercase;margin-bottom:10px}
/* CTA band */
.cta-band{background:linear-gradient(150deg,var(--navy),var(--navy-2));color:#e8edf3;border-radius:20px;padding:44px 40px;display:flex;justify-content:space-between;gap:26px;align-items:center;flex-wrap:wrap}
.cta-band h2{color:#fff;font-size:1.8rem;margin-bottom:8px}
.cta-band p{color:#c2cedd;max-width:34em}
/* Tables / pricing */
.price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.price-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:30px;box-shadow:0 3px 12px rgba(8,21,39,.05)}
.price-card.featured{border:2px solid var(--gold);background:linear-gradient(180deg,#fffdf4,#fff)}
.price-card .lvl{color:var(--gold-deep);font-weight:800;letter-spacing:.18em;font-size:.75rem;text-transform:uppercase}
.price-card h3{font-size:1.3rem;margin:8px 0 4px}
.price-card .price{font-family:'Fraunces',serif;font-size:2.1rem;color:var(--navy);margin:10px 0}
.price-card .price small{font-size:.95rem;color:var(--muted);font-family:'Inter',sans-serif}
.price-card ul{list-style:none;margin:14px 0 20px}
.price-card li{padding:6px 0 6px 24px;position:relative;color:var(--muted);font-size:.98rem}
.price-card li::before{content:"—";position:absolute;left:0;color:var(--gold)}
/* Forms */
form.app{background:#fff;border:1px solid var(--line);border-radius:18px;padding:34px;box-shadow:var(--shadow)}
form.app fieldset{border:none;margin-bottom:28px}
form.app legend{font-family:'Fraunces',serif;font-size:1.25rem;color:var(--navy);font-weight:600;margin-bottom:14px;padding-bottom:6px;border-bottom:2px solid var(--gold);width:100%}
.f-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.f-field{display:flex;flex-direction:column;gap:6px}
.f-field.full{grid-column:1/-1}
.f-field label{font-weight:600;font-size:.93rem;color:var(--navy)}
.f-field label .req{color:#b3261e}
.f-field input,.f-field select,.f-field textarea{font:inherit;padding:11px 13px;border:1px solid #c8cfd6;border-radius:9px;background:#fff;color:var(--ink)}
.f-field input:focus,.f-field select:focus,.f-field textarea:focus{outline:2px solid var(--gold);outline-offset:1px;border-color:var(--gold-deep)}
.f-field .hint{font-size:.83rem;color:var(--muted)}
.check{display:flex;gap:10px;align-items:flex-start;font-size:.95rem}
.check input{margin-top:4px;width:18px;height:18px;accent-color:var(--gold-deep)}
.form-status{border-radius:10px;padding:14px 18px;margin-top:18px;display:none}
.form-status.ok{display:block;background:#e9f6ec;border:1px solid #2e7d32;color:#1b4d20}
.form-status.err{display:block;background:#fdecea;border:1px solid #b3261e;color:#7a130d}
.note{background:var(--cream);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:10px;padding:16px 20px;color:#4c4433}
/* Contact cards */
.contact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.contact-grid .card a{font-weight:600}
/* Footer */
footer.site{background:var(--navy);color:#b9c6d4;margin-top:0}
footer.site .wrap{padding-top:46px;padding-bottom:26px}
.foot-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:30px;margin-bottom:30px}
footer.site h3{color:#fff;font-size:1.05rem;margin-bottom:12px;font-family:'Inter',sans-serif;letter-spacing:.04em}
footer.site a{color:#d7dee7;text-decoration:none}
footer.site a:hover{color:var(--gold-2)}
footer.site ul{list-style:none}
footer.site li{margin:7px 0}
.foot-bottom{border-top:1px solid rgba(255,255,255,.14);padding-top:18px;font-size:.88rem;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
/* Responsive */
@media (max-width:920px){
  .hero-grid{grid-template-columns:1fr}
  .grid3,.price-grid,.contact-grid{grid-template-columns:1fr 1fr}
  .steps{grid-template-columns:1fr 1fr}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:600px){
  .grid3,.grid2,.price-grid,.contact-grid,.steps,.f-grid,.foot-grid{grid-template-columns:1fr}
  section.block{padding:44px 0}
  .hero{padding:52px 0 46px}
  form.app{padding:24px 18px}
  .cta-band{padding:32px 24px}
}
"""

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("speakers.html", "Speakers"),
    ("become-a-speaker.html", "Become a Speaker"),
    ("academy.html", "TIPS Academy"),
    ("contact.html", "Contact"),
]

def header(current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<a class="skip" href="#main">Skip to main content</a>
<div class="topbar"><div class="wrap">
  <span>Tolkz Speakers USA &middot; St Louis Park, Minnesota</span>
  <span><a href="tel:+15073195381">+1 (507) 319-5381</a> &middot; <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a></span>
</div></div>
<header class="site"><div class="wrap">
  <a class="wordmark" href="index.html" aria-label="Tolkz Speakers USA — home">
    <span class="wm-name">TOLK<em>Z</em></span>
    <span class="wm-sub">SPEAKERS USA</span>
  </a>
  <nav class="main" aria-label="Main navigation">{links}<a class="btn small" href="contact.html">Book a Speaker</a></nav>
</div></header>"""

FOOTER = """<footer class="site"><div class="wrap">
  <div class="foot-grid">
    <div>
      <h3>Tolkz Speakers USA</h3>
      <p>A U.S. speakers bureau representing African and African-American voices — and the speakers who carry their messages to the world.</p>
      <p style="margin-top:10px;">3387 Brownlow Ave<br>St Louis Park, MN 55426, USA</p>
    </div>
    <div>
      <h3>Explore</h3>
      <ul>
        <li><a href="about.html">About Tolkz</a></li>
        <li><a href="speakers.html">Speaker Roster</a></li>
        <li><a href="become-a-speaker.html">Become a Speaker</a></li>
        <li><a href="academy.html">TIPS Academy</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Contact</h3>
      <ul>
        <li>Bureau &amp; corporate: <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a></li>
        <li>Speaking &amp; coaching inquiries: <a href="mailto:speaking@olivernshom.com">speaking@olivernshom.com</a></li>
        <li>Phone: <a href="tel:+15073195381">+1 (507) 319-5381</a></li>
        <li>Web: <a href="https://www.tolkzspeakers.com">www.tolkzspeakers.com</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <span>&copy; 2026 Tolkz Speakers USA. All rights reserved.</span>
    <span>Inspire. Connect. Transform.</span>
  </div>
</div></footer>"""

def page(filename, title, description, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Tolkz Speakers USA</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""

# ---------------------------------------------------------------- roster data
# Source: approved-speakers list sent by Abraham Thompson, Oct 22, 2026
# (spreadsheet "speakers_approved_2025-11-14"). Names, titles and locations are
# reproduced from that list. The two Lusaka entries for Kelvin Mumba (two
# different emails) are merged into one roster entry.
# talk = the sheet's "Professional Title" entry is a signature talk title.
ROSTER = [
    # name, title, location, talk_title_or_None
    ("Ly Smith", "Mindset Thought Leader", "Nevada, USA", None),
    ("Ebot Patience Ojong", "Motivational Speaker", "Yaoundé, Cameroon", None),
    ("Klieng Glory", "Author, Poet & Leadership Practitioner", "Bamenda, Cameroon", None),
    ("Bamu Kingsley Tabifor", "Visual Communications Specialist & Strategic Thinker", "Yaoundé, Cameroon", None),
    ("Njei Kingsly Achiri", "Corporate Strategy & Leadership Speaker — driving business growth and entrepreneurial excellence", "Yaoundé, Cameroon", None),
    ("Yokwei Promise Kenkoh", "Leadership Speaker", "Yaoundé, Cameroon", None),
    ("Kelvin Mumba", "Transformational Leadership Expert · Orator & Thought Leader", "Lusaka, Zambia", None),
    ("Terence Musong Ndifor", "Sales & Small Business Consultant", "Limbe, Cameroon", None),
    ("Sai Ramachandran", "The Polymathic Connector", "Bangalore, India", None),
    ("Mirabel Nugi Kanjo", "Life Coach, Therapist & Trauma Healing Specialist", "Canada", None),
    ("Ishimwe Solange", "Gospel Singer, Youth Empowerment Advocate & Inspirational Speaker", "Kigali, Rwanda", None),
    ("Ernest Marvellous Kumi", "President", "Accra, Ghana", None),
    ("Denise Bowles", None, "Ilkeston, Derbyshire, England", "I Wanna Tell You My Story"),
    ("Nsahlar Didier Yinkfu", "Medical Doctor & Holistic Healer", "Bamenda, Cameroon", None),
    ("Dr. Joybert Javnyuy", "Global Speaker & Trainer · Enterprise Strategist & Consultant · Value Extraction & Monetization Architect · Author", "Houston, USA", None),
    ("Bryan Turkel", None, "Austin, USA", "From Autopilot to Aligned: Reclaiming Purpose in a Disconnected World"),
    ("Rob Kalwarowsky", None, "Edmonton, Canada", "Achieve Your Goals: Secrets of Olympic Gold Medalists"),
    ("Melanie Puemedji", "Leadership & Personal Development Speaker, Jurist, Lecturer, Coach & Writer", "Yaoundé, Cameroon", None),
    ("Karen Attyah", "Brand Strategist helping brands reach the 50+ audience", "Los Angeles, USA", None),
    ("Amengwo Mbah Dilan", "Leadership Speaker", "Douala, Cameroon", None),
    ("Fonyuy Catherine Limnyuy", "Personal Development & Motivational Speaker", "Yaoundé, Cameroon", None),
    ("Fiona Luma Tankoh", "Personal Growth Speaker", "Yaoundé, Cameroon", None),
]

# Verified headshots: each file is the speaker's own photo from the legacy
# Tolkz platform records (production DB headshot_path / codebase-paired
# testimonial images in the old tolkz repo). Speakers not listed here have
# no verifiable photo on file and keep the monogram tile.
PHOTOS = {
    "Ebot Patience Ojong": "images/ebot-patience-ojong.jpg",
    "Melanie Puemedji": "images/melanie-puemedji.jpg",
    "Dr. Joybert Javnyuy": "images/joybert-javnyuy.jpg",
    "Amengwo Mbah Dilan": "images/amengwo-mbah-dilan.jpg",
    "Fonyuy Catherine Limnyuy": "images/fonyuy-catherine-limnyuy.jpg",
    "Fiona Luma Tankoh": "images/fiona-luma-tankoh.jpg",
}

def initials(name):
    parts = [p for p in name.replace("Dr.", "").split() if p]
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()

def speaker_card(name, title, location, talk=None, photo=None, badge=None):
    if photo:
        media = f'<div class="sp-photo"><img src="{photo}" alt="Portrait of {name}"></div>'
    else:
        media = f'<div class="sp-mono" aria-hidden="true"><span>{initials(name)}</span></div>'
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    title_html = f'<p class="title">{title}</p>' if title else ""
    talk_html = f'<p class="talk">Signature talk: &ldquo;{talk}&rdquo;</p>' if talk else ""
    return f"""<article class="sp-card">{media}<div class="sp-body">{badge_html}<h3>{name}</h3>{title_html}{talk_html}<p class="loc">{location}</p></div></article>"""

OLIVER_CARD = speaker_card(
    "Oliver Nshom",
    "Founder &amp; CEO · Keynote Speaker, Team-Building Trainer &amp; Coach",
    "Minneapolis, USA",
    photo="images/oliver-nshom.jpg",
    badge="Founder &amp; Featured Speaker",
)

# ---------------------------------------------------------------- index.html
INDEX_BODY = """
<section class="hero"><div class="wrap"><div class="hero-grid">
  <div>
    <p class="kicker">Tolkz Speakers USA</p>
    <h1>Voices that <em>move rooms.</em><br>Speakers the world remembers.</h1>
    <p class="lede">Tolkz Speakers USA is a U.S. speakers bureau built to put African and African-American voices on the stages where decisions are made — and to connect event organizers with speakers who inform, inspire and transform their audiences.</p>
    <div class="cta-row">
      <a class="btn" href="contact.html">Book a Speaker</a>
      <a class="btn ghost" href="become-a-speaker.html">Join the Roster</a>
    </div>
  </div>
  <figure class="hero-photo">
    <img src="images/oliver-stage.jpg" alt="Oliver Nshom, Founder and CEO of Tolkz Speakers USA, delivering a keynote address on stage">
    <figcaption>Oliver Nshom — Founder &amp; CEO, Tolkz Speakers USA</figcaption>
  </figure>
</div></div></section>

<section class="block"><div class="wrap">
  <div class="sec-head">
    <p class="kicker">What Tolkz Does</p>
    <h2>One bureau. Three ways to work with us.</h2>
    <p>Tolkz markets and brands speakers globally, helping them secure paid speaking engagements nationally and internationally — and gives organizers a trusted desk to book from.</p>
  </div>
  <div class="grid3">
    <div class="card">
      <div class="icon" aria-hidden="true">1</div>
      <h3>Book a Speaker</h3>
      <p>Conferences, corporate events, churches, schools and summits: tell the bureau about your event and Tolkz will match it with the right voice from its roster — and handle the booking conversation end to end.</p>
      <p style="margin-top:14px;"><a href="speakers.html"><strong>Browse the roster &rarr;</strong></a></p>
    </div>
    <div class="card">
      <div class="icon" aria-hidden="true">2</div>
      <h3>Get Represented</h3>
      <p>Speakers with a message and a mission can apply to join the Tolkz roster. Approved speakers are profiled to organizers and positioned for paid engagements in the United States and internationally.</p>
      <p style="margin-top:14px;"><a href="become-a-speaker.html"><strong>Apply to join &rarr;</strong></a></p>
    </div>
    <div class="card">
      <div class="icon" aria-hidden="true">3</div>
      <h3>Train &amp; Certify</h3>
      <p>Through the Texas Institute of Public Speaking (TIPS), Tolkz connects speakers to professional certification — CES, CPS and CPTC — so skill is not just claimed, it is credentialed.</p>
      <p style="margin-top:14px;"><a href="academy.html"><strong>Explore the TIPS Academy &rarr;</strong></a></p>
    </div>
  </div>
</div></section>

<section class="block alt"><div class="wrap">
  <div class="sec-head">
    <p class="kicker">Featured Speakers</p>
    <h2>From the Tolkz roster</h2>
    <p>A selection of the voices Tolkz represents — from the bureau's founder to speakers across the United States, Cameroon and beyond.</p>
  </div>
  <div class="sp-grid">
    """ + OLIVER_CARD + """
    """ + speaker_card("Dr. Joybert Javnyuy", "Global Speaker &amp; Trainer · Enterprise Strategist &amp; Consultant", "Houston, USA", photo="images/joybert-javnyuy.jpg") + """
    """ + speaker_card("Ly Smith", "Mindset Thought Leader", "Nevada, USA") + """
    """ + speaker_card("Melanie Puemedji", "Leadership &amp; Personal Development Speaker, Jurist, Lecturer, Coach &amp; Writer", "Yaoundé, Cameroon", photo="images/melanie-puemedji.jpg") + """
  </div>
  <p style="margin-top:26px;"><a class="btn navy" href="speakers.html">See the Full Roster</a></p>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head">
    <p class="kicker">How Booking Works</p>
    <h2>From first inquiry to standing ovation</h2>
  </div>
  <div class="steps">
    <div class="step"><h3>Tell us about your event</h3><p>Share your date, audience, theme and budget range through the contact page or by email.</p></div>
    <div class="step"><h3>Get matched</h3><p>The bureau recommends the speakers on the roster who fit your audience and your goals.</p></div>
    <div class="step"><h3>Confirm the booking</h3><p>Fees, travel and terms are agreed in writing — clearly, before anyone commits.</p></div>
    <div class="step"><h3>Your speaker delivers</h3><p>Tolkz stays in the loop through the event, so organizers and speakers are both supported.</p></div>
  </div>
  <div class="cta-band" style="margin-top:44px;">
    <div>
      <h2>Planning an event?</h2>
      <p>Put a voice on your stage that your audience will talk about long after the lights go down.</p>
    </div>
    <a class="btn" href="contact.html">Start a Booking Inquiry</a>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- about.html
ABOUT_BODY = """
<section class="hero"><div class="wrap">
  <p class="kicker">About Us</p>
  <h1>The bureau behind the <em>voices.</em></h1>
  <p class="lede">Tolkz Speakers USA is a U.S.-registered speakers bureau committed to marketing and branding speakers globally — helping them secure paid speaking engagements nationally and internationally.</p>
</div></section>

<section class="block"><div class="wrap">
  <div class="grid2">
    <div>
      <div class="sec-head" style="margin-bottom:18px;">
        <p class="kicker">Who We Are</p>
        <h2>Built in the United States. Reaching the world.</h2>
      </div>
      <p>Tolkz Speakers USA is a United States limited liability company, formed on March 31, 2026, with its address of record at 3387 Brownlow Ave, St Louis Park, MN 55426.</p>
      <p style="margin-top:14px;">The bureau's platform connects aspiring and professional speakers with opportunities to showcase their voices, starting in the U.S. and Cameroon. Through curated events, coaching and exposure to international stages, Tolkz empowers speakers to build influence and grow their speaking careers.</p>
      <p style="margin-top:14px;">Tolkz also works alongside the Texas Institute of Public Speaking (TIPS), the certification body founded by Tolkz's founder, so that the speakers it represents can back their talent with recognized professional credentials.</p>
    </div>
    <div class="card" style="align-self:start;">
      <h3>Our Vision</h3>
      <p>To be the best speakers bureau for African and African-American speakers — the bureau the world calls first when it wants those voices on its stages.</p>
      <h3 style="margin-top:22px;">What We Stand For</h3>
      <p>Credibility before visibility. Tolkz documents what it claims, vets the associations it makes, and holds a simple standard: no claim beyond its proof.</p>
      <h3 style="margin-top:22px;">Where We Work</h3>
      <p>Headquartered in Minnesota, USA, with speakers and partners across the United States, Cameroon, Africa and the wider diaspora.</p>
    </div>
  </div>
</div></section>

<section class="block alt"><div class="wrap">
  <div class="hero-grid">
    <figure class="hero-photo" style="box-shadow:var(--shadow);">
      <img src="images/oliver-nshom.jpg" alt="Portrait of Oliver Nshom, Founder and CEO of Tolkz Speakers USA">
      <figcaption style="background:var(--navy);color:#d7dee7;font-size:.86rem;padding:10px 14px;">Oliver Nshom — Founder &amp; CEO</figcaption>
    </figure>
    <div>
      <div class="sec-head" style="margin-bottom:16px;">
        <p class="kicker">The Founder</p>
        <h2>Oliver Nshom — Founder &amp; CEO</h2>
      </div>
      <p>Oliver Nshom has been a professional speaker for more than 17 years. After a 2023 breakthrough invitation to speak in Singapore, his stages have extended to the United States, Spain, India and beyond.</p>
      <p style="margin-top:14px;">He is the founder of CANASA, the Cameroon National Speakers Association, and of the Texas Institute of Public Speaking (TIPS), which delivers the CES, CPS and CPTC professional speaker certifications. He founded Tolkz Speakers USA to build the bureau he believes African and African-American speakers deserve: one that markets them seriously, brands them professionally and puts them on paid stages around the world.</p>
      <p style="margin-top:14px;">For speaking and coaching inquiries about Oliver directly, write to <a href="mailto:speaking@olivernshom.com">speaking@olivernshom.com</a>. For bureau and corporate matters, write to <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a>.</p>
      <p style="margin-top:20px;"><a class="btn navy" href="speakers.html">Meet the Roster</a></p>
    </div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- speakers.html
_roster_cards = "\n    ".join(
    speaker_card(name, title, loc, talk=talk, photo=PHOTOS.get(name))
    for (name, title, loc, talk) in ROSTER
)
SPEAKERS_BODY = """
<section class="hero"><div class="wrap">
  <p class="kicker">Speaker Roster</p>
  <h1>Meet the <em>Tolkz</em> speakers</h1>
  <p class="lede">The approved speakers represented by Tolkz Speakers USA — leadership speakers, coaches, authors, strategists and storytellers across the United States, Cameroon, Africa and the diaspora.</p>
  <div class="cta-row">
    <a class="btn" href="contact.html">Book a Speaker</a>
    <a class="btn ghost" href="become-a-speaker.html">Apply to Join the Roster</a>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sp-grid">
    """ + OLIVER_CARD + """
    """ + _roster_cards + """
  </div>
  <div class="note" style="margin-top:34px;">
    <strong>Booking a speaker:</strong> every engagement is arranged through the bureau. Tell Tolkz about your event — date, audience, theme and budget — at <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a> or via the <a href="contact.html">contact page</a>, and the bureau will confirm availability and terms in writing.
  </div>
  <div class="cta-band" style="margin-top:34px;">
    <div>
      <h2>Your voice belongs on this roster?</h2>
      <p>Applications are reviewed by the bureau. If your message and mission fit, Tolkz will be in touch.</p>
    </div>
    <a class="btn" href="become-a-speaker.html">Apply as a Speaker</a>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- become-a-speaker.html
BECOME_BODY = """
<section class="hero"><div class="wrap">
  <p class="kicker">Join as a Speaker</p>
  <h1>Share your expertise <em>with the world.</em></h1>
  <p class="lede">Apply to join the Tolkz Speakers USA roster. Approved speakers are profiled to event organizers and positioned for paid speaking engagements in the United States and internationally.</p>
</div></section>

<section class="block"><div class="wrap">
  <div class="grid3" style="margin-bottom:38px;">
    <div class="card"><h3>Be seen</h3><p>Your profile is presented to organizers looking for credible voices for conferences, corporate events, churches, schools and summits.</p></div>
    <div class="card"><h3>Be branded</h3><p>Tolkz helps speakers present themselves professionally — title, topics, biography and media that organizers can trust.</p></div>
    <div class="card"><h3>Be booked</h3><p>The bureau fields inquiries, confirms terms in writing and supports both speaker and organizer through the engagement.</p></div>
  </div>

  <form class="app" id="speaker-application" novalidate>
    <fieldset>
      <legend>Basic Information</legend>
      <div class="f-grid">
        <div class="f-field">
          <label for="f-name">Full Name <span class="req" aria-hidden="true">*</span></label>
          <input id="f-name" name="Full Name" type="text" autocomplete="name" required>
        </div>
        <div class="f-field">
          <label for="f-email">Email Address <span class="req" aria-hidden="true">*</span></label>
          <input id="f-email" name="Email" type="email" autocomplete="email" required>
        </div>
        <div class="f-field">
          <label for="f-phone">Phone Number</label>
          <input id="f-phone" name="Phone" type="tel" autocomplete="tel">
        </div>
        <div class="f-field">
          <label for="f-location">Country &amp; City of Residence <span class="req" aria-hidden="true">*</span></label>
          <input id="f-location" name="Location" type="text" placeholder="e.g. Houston, USA" required>
        </div>
        <div class="f-field">
          <label for="f-website">Website (if applicable)</label>
          <input id="f-website" name="Website" type="url" placeholder="https://">
        </div>
        <div class="f-field">
          <label for="f-social">Social Media Links</label>
          <input id="f-social" name="Social Media Links" type="text" placeholder="LinkedIn, Instagram, YouTube…">
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Speaker Profile</legend>
      <div class="f-grid">
        <div class="f-field full">
          <label for="f-title">Professional Title <span class="req" aria-hidden="true">*</span></label>
          <input id="f-title" name="Professional Title" type="text" placeholder="e.g. Leadership Speaker &amp; Author" required>
        </div>
        <div class="f-field full">
          <label for="f-topics">Your Top Speaking Topics <span class="req" aria-hidden="true">*</span></label>
          <input id="f-topics" name="Speaking Topics" type="text" placeholder="e.g. Leadership, Credibility, Youth Empowerment" required>
        </div>
        <div class="f-field full">
          <label for="f-bio">Short Bio (100–200 words) <span class="req" aria-hidden="true">*</span></label>
          <textarea id="f-bio" name="Short Bio" rows="5" required></textarea>
          <span class="hint">This is the biography organizers will read first. Write it in the third person.</span>
        </div>
        <div class="f-field full">
          <label for="f-longbio">Detailed Bio (optional, up to 800 words)</label>
          <textarea id="f-longbio" name="Detailed Bio" rows="6"></textarea>
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Speaking Experience</legend>
      <div class="f-grid">
        <div class="f-field">
          <label for="f-exp">Years of Speaking Experience <span class="req" aria-hidden="true">*</span></label>
          <select id="f-exp" name="Speaking Experience" required>
            <option value="">Select experience</option>
            <option>Less than 1 year</option>
            <option>1–3 years</option>
            <option>3–5 years</option>
            <option>5–10 years</option>
            <option>10+ years</option>
          </select>
        </div>
        <div class="f-field">
          <label for="f-intl">Have you spoken at international events?</label>
          <select id="f-intl" name="International Events">
            <option value="">Select an option</option>
            <option>Yes</option>
            <option>No</option>
          </select>
        </div>
        <div class="f-field full">
          <label for="f-stages">Notable organizations or conferences you have spoken at</label>
          <textarea id="f-stages" name="Notable Stages" rows="3"></textarea>
        </div>
        <div class="f-field full">
          <label for="f-achieve">Biggest accomplishments as a speaker (publications, awards)</label>
          <textarea id="f-achieve" name="Accomplishments" rows="3"></textarea>
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Media &amp; Materials</legend>
      <div class="f-grid">
        <div class="f-field">
          <label for="f-headshot">Professional Headshot URL</label>
          <input id="f-headshot" name="Headshot URL" type="url" placeholder="Link to your headshot (Drive, Dropbox…)">
        </div>
        <div class="f-field">
          <label for="f-reel">Speaker Reel URL</label>
          <input id="f-reel" name="Speaker Reel URL" type="url" placeholder="https://">
        </div>
        <div class="f-field full">
          <label for="f-video">Sample Speech Video URL</label>
          <input id="f-video" name="Sample Speech Video URL" type="url" placeholder="YouTube or Vimeo link">
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Availability &amp; Fees</legend>
      <div class="f-grid">
        <div class="f-field">
          <label for="f-fee">Speaking Fee Range <span class="req" aria-hidden="true">*</span></label>
          <select id="f-fee" name="Fee Range" required>
            <option value="">Select fee range</option>
            <option>Negotiable</option>
            <option>$0 – $1,000</option>
            <option>$1,000 – $2,500</option>
            <option>$2,500 – $5,000</option>
            <option>$5,000 – $10,000</option>
            <option>$10,000+</option>
          </select>
        </div>
        <div class="f-field">
          <label for="f-travel">Open to traveling for engagements?</label>
          <select id="f-travel" name="Travel Availability">
            <option value="">Select an option</option>
            <option>Yes</option>
            <option>No</option>
            <option>Limited travel only</option>
          </select>
        </div>
        <div class="f-field">
          <label for="f-virtual">Available for virtual engagements?</label>
          <select id="f-virtual" name="Virtual Availability">
            <option value="">Select an option</option>
            <option>Yes</option>
            <option>No</option>
          </select>
        </div>
        <div class="f-field">
          <label for="f-heard">How did you hear about Tolkz?</label>
          <input id="f-heard" name="How Heard About Tolkz" type="text">
        </div>
        <div class="f-field full">
          <label for="f-notes">Additional Notes</label>
          <textarea id="f-notes" name="Additional Notes" rows="3"></textarea>
        </div>
      </div>
    </fieldset>

    <div class="check">
      <input id="f-terms" name="Terms Agreement" type="checkbox" value="Agreed" required>
      <label for="f-terms">I confirm that the information in this application is accurate, and I agree to Tolkz Speakers USA reviewing it for roster consideration. <span class="req" aria-hidden="true">*</span></label>
    </div>

    <p style="margin-top:24px;"><button class="btn" type="submit" id="submit-btn">Submit Application</button></p>
    <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
  </form>

  <div class="note" style="margin-top:26px;">
    <strong>Having trouble with the form?</strong> Email your application details — name, title, topics, bio, experience, fee range and links to your headshot and videos — directly to <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a> with the subject line &ldquo;Speaker Application&rdquo;. Every application is reviewed by the bureau; Tolkz replies to applicants whose profiles fit the roster.
  </div>
</div></section>

<script>
(function () {
  var form = document.getElementById('speaker-application');
  var status = document.getElementById('form-status');
  var btn = document.getElementById('submit-btn');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    btn.disabled = true; btn.textContent = 'Submitting…';
    status.className = 'form-status'; status.textContent = '';
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    data['_subject'] = 'New Speaker Application — Tolkz Speakers USA';
    data['_template'] = 'table';
    data['_captcha'] = 'false';
    fetch('https://formsubmit.co/ajax/ceo@tolkzspeakers.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) {
      if (!r.ok) { throw new Error('send failed'); }
      return r.json();
    }).then(function () {
      status.className = 'form-status ok';
      status.textContent = 'Application submitted — thank you. The Tolkz bureau has received your application and will review it. If your profile fits the roster, Tolkz will contact you at the email address you provided.';
      form.reset();
      btn.disabled = false; btn.textContent = 'Submit Application';
    }).catch(function () {
      status.className = 'form-status err';
      status.innerHTML = 'The form could not be sent just now. Please email your application directly to <a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a> with the subject line &ldquo;Speaker Application&rdquo;.';
      btn.disabled = false; btn.textContent = 'Submit Application';
    });
  });
})();
</script>
"""

# ---------------------------------------------------------------- academy.html
ACADEMY_BODY = """
<section class="hero"><div class="wrap">
  <p class="kicker">The TIPS Academy</p>
  <h1>Talent opens doors.<br><em>Certification</em> keeps them open.</h1>
  <p class="lede">Tolkz Speakers USA connects its speakers and clients to professional certification through the Texas Institute of Public Speaking (TIPS) — the TIPS Academy. Three certifications, earned in order, assessed at every step: no certificate on experience alone.</p>
  <div class="cta-row">
    <a class="btn" href="contact.html">Ask About Enrollment</a>
    <a class="btn ghost" href="https://tipscampus.com" target="_blank" rel="noopener">Visit the TIPS Campus</a>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head">
    <p class="kicker">The Certification Pathway</p>
    <h2>CES &rarr; CPS &rarr; CPTC</h2>
    <p>Each level is independently enrollable and progressive: the next level unlocks as you pass the one before it. Candidates must score at least 70% on both the knowledge examination and the practical assessment at their level. Founding cohorts begin <strong>January 11, 2027</strong> in the United States, Canada, Europe and Cameroon. United States tuition is shown below; tuition for other countries of residence is confirmed on application.</p>
  </div>
  <div class="price-grid">
    <div class="price-card">
      <p class="lvl">Beginner · Level 1</p>
      <h3>Certified Emerging Speaker (CES)</h3>
      <p class="price">$495 <small>USD · 4 weeks</small></p>
      <ul>
        <li>For new and emerging speakers building their foundation</li>
        <li>Speech craft, structure, delivery and stage confidence</li>
        <li>Assessed speech + knowledge examination (70% / 70%)</li>
      </ul>
      <a class="btn navy small" href="contact.html">Enquire About CES</a>
    </div>
    <div class="price-card featured">
      <p class="lvl">Professional · Level 2</p>
      <h3>Certified Professional Speaker (CPS)</h3>
      <p class="price">$1,495 <small>USD · 8–12 weeks</small></p>
      <ul>
        <li>For working speakers moving to professional, paid stages</li>
        <li>Keynote development, positioning and the business of speaking</li>
        <li>Entry: CES completion, or approved experience-based direct entry</li>
        <li>Assessed professional keynote + knowledge examination (70% / 70%)</li>
      </ul>
      <a class="btn small" href="contact.html">Enquire About CPS</a>
    </div>
    <div class="price-card">
      <p class="lvl">Advanced · Level 3</p>
      <h3>Certified Professional Trainer &amp; Coach (CPTC)</h3>
      <p class="price">$2,995 <small>USD · 12–16 weeks</small></p>
      <ul>
        <li>For experienced speakers who train and coach others</li>
        <li>Training design, facilitation and coaching methodology</li>
        <li>Entry: CPS completion, or approved advanced direct entry</li>
        <li>Assessed training / coaching demonstration + knowledge examination (70% / 70%)</li>
      </ul>
      <a class="btn navy small" href="contact.html">Enquire About CPTC</a>
    </div>
  </div>

  <div class="card" style="margin-top:26px;">
    <h3>The Complete Certification Pathway — $3,995 USD</h3>
    <p>One enrollment covering all three certifications, unlocked in order as each level is passed. Bought separately in the United States, the three programs total $4,985 — the Complete Pathway saves $990. Enrollment is selection-first: candidates apply, are placed at the right level, and receive their enrollment details directly. There is no public checkout — <a href="contact.html">contact the bureau</a> to begin.</p>
  </div>
</div></section>

<section class="block alt"><div class="wrap">
  <div class="grid2">
    <div class="card">
      <h3>About the Texas Institute of Public Speaking</h3>
      <p>The Texas Institute of Public Speaking (TIPS) owns and operates the Academy: it delivers the training, administers the examinations and assessments, keeps student records and issues every Academy certificate. Training is delivered through the TIPS Campus at <a href="https://tipscampus.com" target="_blank" rel="noopener">tipscampus.com</a>, with full program details at <a href="https://www.tipstexas.org/academy.html" target="_blank" rel="noopener">tipstexas.org</a>.</p>
    </div>
    <div class="card">
      <h3>Partnership Note</h3>
      <p>TIPS is in discussion with the Cameroon National Speakers Association (CANASA) regarding a proposed professional certification partnership. Any such arrangement will be announced if and when a formal agreement is concluded.</p>
    </div>
  </div>
  <div class="cta-band" style="margin-top:34px;">
    <div>
      <h2>Founding cohorts begin January 11, 2027</h2>
      <p>Tell the bureau where you live and the level you are aiming for — Tolkz will route your application to the Academy.</p>
    </div>
    <a class="btn" href="contact.html">Start Your Application</a>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- contact.html
CONTACT_BODY = """
<section class="hero"><div class="wrap">
  <p class="kicker">Contact</p>
  <h1>Talk to <em>Tolkz.</em></h1>
  <p class="lede">Booking a speaker, joining the roster, or asking about TIPS certification — the bureau replies to every serious inquiry.</p>
</div></section>

<section class="block"><div class="wrap">
  <div class="contact-grid">
    <div class="card">
      <h3>Bureau &amp; Corporate</h3>
      <p>Speaker bookings, roster representation, partnerships and all Tolkz Speakers USA corporate matters.</p>
      <p style="margin-top:12px;"><a href="mailto:ceo@tolkzspeakers.com">ceo@tolkzspeakers.com</a></p>
    </div>
    <div class="card">
      <h3>Speaking &amp; Coaching — Oliver Nshom</h3>
      <p>Keynote and coaching inquiries about Tolkz's founder, Oliver Nshom, go to his speaking office.</p>
      <p style="margin-top:12px;"><a href="mailto:speaking@olivernshom.com">speaking@olivernshom.com</a></p>
    </div>
    <div class="card">
      <h3>Phone &amp; Office</h3>
      <p><a href="tel:+15073195381">+1 (507) 319-5381</a></p>
      <p style="margin-top:8px;">Tolkz Speakers USA<br>3387 Brownlow Ave<br>St Louis Park, MN 55426, USA</p>
    </div>
  </div>

  <div class="grid2" style="margin-top:26px;">
    <div class="card">
      <h3>Booking a speaker?</h3>
      <p>Include your event date, city (or virtual), audience size and type, theme, and your budget range. The bureau will recommend the right voices from the <a href="speakers.html">roster</a> and confirm availability and terms in writing.</p>
    </div>
    <div class="card">
      <h3>Want to be represented?</h3>
      <p>Speakers apply through the <a href="become-a-speaker.html">Become a Speaker</a> page. For TIPS certification, see the <a href="academy.html">TIPS Academy</a> page — founding cohorts begin January 11, 2027.</p>
    </div>
  </div>

  <div class="cta-band" style="margin-top:34px;">
    <div>
      <h2>One email starts it.</h2>
      <p>Write to the bureau at ceo@tolkzspeakers.com — or to Oliver's speaking office at speaking@olivernshom.com.</p>
    </div>
    <a class="btn" href="mailto:ceo@tolkzspeakers.com">Email the Bureau</a>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- write pages
PAGES = {
    "index.html": page("index.html", "Home",
        "Tolkz Speakers USA is a U.S. speakers bureau representing African and African-American voices: book a speaker, join the roster, or certify through the TIPS Academy.",
        INDEX_BODY),
    "about.html": page("about.html", "About",
        "About Tolkz Speakers USA — a U.S. LLC formed March 31, 2026, founded by Oliver Nshom, and built to be the best speakers bureau for African and African-American speakers.",
        ABOUT_BODY),
    "speakers.html": page("speakers.html", "Speakers",
        "The Tolkz Speakers USA roster: approved speakers represented by the bureau across the United States, Cameroon, Africa and the diaspora.",
        SPEAKERS_BODY),
    "become-a-speaker.html": page("become-a-speaker.html", "Become a Speaker",
        "Apply to join the Tolkz Speakers USA roster. Approved speakers are profiled to event organizers and positioned for paid speaking engagements.",
        BECOME_BODY),
    "academy.html": page("academy.html", "TIPS Academy",
        "Professional speaker certification through the Texas Institute of Public Speaking: CES ($495), CPS ($1,495) and CPTC ($2,995) — founding cohorts begin January 11, 2027.",
        ACADEMY_BODY),
    "contact.html": page("contact.html", "Contact",
        "Contact Tolkz Speakers USA: ceo@tolkzspeakers.com for bureau and corporate matters, speaking@olivernshom.com for speaking and coaching inquiries, +1 (507) 319-5381.",
        CONTACT_BODY),
}

if __name__ == "__main__":
    for name, html in PAGES.items():
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", name, len(html), "bytes")
