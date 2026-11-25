# Run: python build.py  -> regenerates every page, sitemap, robots, ads.txt, CNAME
import json, datetime, html

# ===== FILL THESE =====
CNAME  = False   # True once the domain is bought and its DNS points to GitHub Pages
DOMAIN = "grandcheatcodes.com"   # e.g. "gta6cheatcodes.com" (no https, no slash)
PUB    = ""   # AdSense publisher id, e.g. "pub-1234567890123456"
EMAIL  = "gamecode.team@gmail.com"   # e.g. "contact@gta6cheatcodes.com"
GSC    = ""   # Google Search Console meta code (only the content="..." value)
# ======================

SITE = "GrandCheatCodes.com"
TODAY = datetime.date.today().isoformat()
BASE = f"https://{DOMAIN}/" if DOMAIN else ""
AR = {"U": "↑", "R": "→", "D": "↓", "L": "←"}
CATS = [("player", "Player"), ("weapons", "Weapons & Combat"), ("vehicles", "Vehicle Spawns"),
        ("police", "Wanted Level"), ("world", "Weather & Filters")]

C = []
for line in open("cheats.txt", encoding="utf-8"):
    if line.strip():
        n, c, s, u = line.rstrip("\n").split("|")
        C.append((n, c, " ".join(AR[x] for x in s), u or "To be announced"))
N = len(C)

def table(sel=lambda c: True, tid=""):
    rows = [c for c in C if sel(c)]
    idattr = f' id="{tid}"' if tid else ""
    return (f'<p class="count"{" id=count" if tid else ""}>{len(rows)} cheat codes</p><table{idattr}><thead><tr><th>Cheat</th>'
            f'<th>D-Pad code (PS5 &amp; Xbox)</th><th>How to unlock</th></tr></thead><tbody>'
            + "".join(f'<tr data-c="{c[1]}"><td>{html.escape(c[0])}</td><td class="code">{c[2]}</td><td>{html.escape(c[3])}</td></tr>' for c in rows)
            + "</tbody></table>")

def cat(k): return lambda c: c[1] == k
def unlock(w): return lambda c: w in c[3].lower()

NAV = [("index", "All Cheats"), ("ps5-cheats", "PS5"), ("xbox-cheats", "Xbox"), ("vehicle-cheats", "Vehicles"),
       ("weapon-cheats", "Weapons"), ("money-cheats", "Money"), ("screen-filter-cheats", "Filters & Weather"),
       ("unlock-challenges", "Unlocks"), ("best-cheats", "Best Cheats"), ("how-to-enter-cheats", "How to Enter"), ("faq", "FAQ")]
def href(k): return "./" if k == "index" else f"{k}.html"

HEADER = (f'<header><div class="nav"><a class="logo" href="./"><span>GrandCheatCodes<small>.com</small></span></a>'
          '<button class="mbtn" aria-label="Open menu" aria-expanded="false">☰</button></div><nav class="menu">'
          + "".join(f'<a href="{href(k)}">{v}</a>' for k, v in NAV) + "</nav></header>")
FOOTER = ('<footer><p>' + " · ".join(f'<a href="{href(k)}">{v}</a>' for k, v in
          [("about", "About"), ("contact", "Contact"), ("privacy", "Privacy Policy"), ("terms", "Terms"), ("sitemap", "Sitemap")])
          + f'</p><p>© 2026 {SITE} — independent fan guide, not affiliated with Rockstar Games or Take-Two Interactive.</p></footer>')

TOOL = ('<div class="tool"><label for="q">Search a cheat (e.g. ammo, armor, weather, spawn)</label>'
        '<input id="q" type="search" placeholder="Type a cheat name..." autocomplete="off"><select id="cat" aria-label="Category">'
        '<option value="all">All categories</option>' + "".join(f'<option value="{k}">{v}</option>' for k, v in CATS) + '</select></div>')

GUIDE = '<p>New to cheats? Read <a href="how-to-enter-cheats.html">how to enter GTA 6 cheats</a> or the <a href="faq.html">FAQ</a>.</p>'
HOW = ('<h2>How to enter GTA 6 cheats</h2><p>Cheats are entered on Jason or Lucia\'s in-game phone. Open the phone, hold <b>L1 + R1</b> on PS5 or <b>LB + RB</b> on Xbox Series X|S, '
       'then input the sequence on the D-Pad. A notification confirms the cheat. All codes only use the D-Pad, so the sequence is identical on PlayStation and Xbox.</p>'
       '<p>The Cheats list (Progress menu &gt; Cheats) appears only after you finish the story, and each cheat must then be unlocked by its own requirement (see the "How to unlock" column). '
       'Activating a cheat disables trophies, achievements and saving for that session — so save first. Full details in our <a href="how-to-enter-cheats.html">step-by-step guide</a>.</p>')
FAQ = [("Are there cheat codes in GTA 6?", "Yes. GTA 6 keeps the series tradition: cheats are entered through the in-game phone with a D-Pad sequence while holding L1+R1 (PS5) or LB+RB (Xbox)."),
       ("Is there a money cheat in GTA 6?", "A $250,000 money cheat is listed by several guides (↑ → ↓ ← ↑ ← ↓ →). Cheats disable saving for the session, so the money may not be kept permanently."),
       ("Do GTA 6 cheats disable trophies?", "Yes. Activating any cheat disables trophies and achievements as well as saving for the current session. Reload your save to play normally again."),
       ("Do cheats work in GTA Online?", "No. Cheats only work in story mode. Mods or hacks online break Rockstar's rules and can get your account banned."),
       ("Is GTA 6 on PC?", "GTA 6 launched on PS5 and Xbox Series X|S. No PC version has been dated yet; we will add PC cheats when it releases."),
       ("Why is a code not working?", "Make sure you are in free roam (not in a mission or cutscene), that you hold both shoulder buttons while typing, that you finished the story and that the cheat is unlocked.")]
FQ = "<h2>Frequently asked questions</h2>" + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
FAQLD = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
CONTACT = f'<a href="mailto:{EMAIL}">{EMAIL}</a>' if EMAIL else '<a href="contact.html">our contact page</a>'

# key: (title, h1, subtitle, description, search tool?, body, extra JSON-LD)
P = {
"index": (f"GTA 6 Cheat Codes – All {N} Cheats for PS5 & Xbox (2026)", "GTA 6 Cheat Codes", "simple, fast and up-to-date GTA 6 cheat finder",
  f"Find all {N} GTA 6 cheat codes in seconds: money, armor, ammo, vehicle spawns, wanted level, weather and screen filters for PS5 and Xbox Series X|S.", 1,
  '<h2>All GTA 6 cheat codes</h2>' + table(tid="list") + HOW +
  f'<h2>What is GTA 6 Cheat Codes?</h2><p>Grand Theft Auto VI brings back cheat codes, but searching through long articles and videos to find the one you need is frustrating. This website puts all {N} GTA 6 cheats in a single searchable table. Type a word like "ammo" or "spawn", choose a category, and the list filters instantly — no scrolling, no sign-up.</p>'
  '<p>Whether you want to cause chaos in Vice City with explosive weapons, escape the police by spawning a bulldozer, or change the weather for a better photo, you will find the right code here. We also have dedicated pages for <a href="ps5-cheats.html">PS5</a>, <a href="xbox-cheats.html">Xbox</a>, <a href="vehicle-cheats.html">vehicle spawns</a>, <a href="weapon-cheats.html">weapons</a> and the <a href="money-cheats.html">money cheat</a>.</p>'
  '<h2>GTA 6 cheat categories</h2><p><b>Player cheats</b> boost Jason and Lucia: body armor, unlimited focus, no fall damage, parachute and drunk mode. <b>Combat cheats</b> give max or infinite ammo, no reload, explosive and incendiary rounds. <b>Vehicle cheats</b> spawn vehicles such as the Maibatsu Boomazoom, MTL Pumper, HVY Bulldozer or an ambulance, and can repair your ride or give unlimited nitrous. <b>Environment cheats</b> cycle the weather and apply cinematic screen filters like Cataclysm, Dollhouse, Faded Glory and Golden Hour.</p>' + FQ, [FAQLD]),
"ps5-cheats": ("GTA 6 Cheats PS5 – All Codes & How to Use Them", "GTA 6 Cheats for PS5", "every PlayStation 5 cheat code in one table",
  "All GTA 6 cheat codes for PlayStation 5. Open the phone, hold L1 + R1 and enter the D-Pad sequence.", 0,
  '<h2>Using cheats on PS5</h2><p>On PlayStation 5, open the phone, hold <b>L1 + R1</b> and press the arrows on the D-Pad. Keep both buttons held for the whole sequence. If you make a mistake, release and start again. The DualSense gives a small vibration when the cheat is accepted.</p>'
  '<p>Trophies are disabled for the session as soon as a cheat is active. If you are hunting the Platinum, keep a clean save and load a separate one for cheating.</p>' + '<h2>All PS5 cheat codes</h2>' + table() + GUIDE, []),
"xbox-cheats": ("GTA 6 Cheats Xbox Series X|S – All Codes", "GTA 6 Cheats for Xbox", "every Xbox Series X|S cheat code in one table",
  "All GTA 6 cheat codes for Xbox Series X and Series S. Open the phone, hold LB + RB and enter the D-Pad sequence.", 0,
  '<h2>Using cheats on Xbox</h2><p>On Xbox Series X|S, open the phone, hold <b>LB + RB</b> (the bumpers) and input the arrows on the D-Pad. The sequences are exactly the same as on PS5, so you can share codes with friends on either console.</p>'
  '<p>Achievements are disabled for the session while a cheat is active. Quick Resume keeps that state, so fully reload your save to earn achievements again.</p>' + '<h2>All Xbox cheat codes</h2>' + table() + GUIDE, []),
"vehicle-cheats": ("GTA 6 Vehicle Cheats – Spawn Cars, Bikes & Tanks", "GTA 6 Vehicle Cheats", "spawn, repair and boost vehicles",
  "Spawn vehicles, repair your car and get unlimited nitrous in GTA 6 with these codes.", 0,
  '<h2>Vehicle cheat codes</h2>' + table(cat("vehicles")) + '<h2>Tips for vehicle cheats</h2><p>Spawn vehicles on an open road so they have space to appear. Spawned vehicles are not stored in your garage. The Repair Vehicle cheat is perfect after a long police chase, and Unlimited Nitrous turns any car into a rocket on the highways of Leonida.</p><p>Most spawns are unlocked through challenges — see <a href="unlock-challenges.html">which challenge unlocks which vehicle</a>.</p>' + GUIDE, []),
"weapon-cheats": ("GTA 6 Weapon Cheats – Ammo, Explosives & Combat", "GTA 6 Weapon & Combat Cheats", "ammo, explosive weapons and combat effects",
  "All GTA 6 weapon and combat cheats: max ammo, infinite ammo, no reload, explosive and incendiary rounds.", 0,
  '<h2>Weapon &amp; combat cheat codes</h2>' + table(cat("weapons")) + '<h2>Best combos</h2><p>Combine <b>Infinite Ammo</b> with <b>No Reload</b> for non-stop shooting, or <b>Body Armor</b> with <b>All Explosive Weapons</b> for maximum chaos. Raise your wanted level only if you are ready for the police response.</p>'
  '<h2>Wanted level cheats</h2>' + table(cat("police")) + GUIDE, []),
"money-cheats": ("GTA 6 Money Cheat – $250,000 Code", "GTA 6 Money Cheat", "the $250,000 cash cheat explained",
  "The GTA 6 money cheat gives $250,000 instantly. Here is the code and what you need to know before using it.", 0,
  '<h2>Money &amp; player cheats</h2>' + table(cat("player")) + '<h2>Does the money stay?</h2><p>Cheats disable saving for the session, so treat the cash as a way to have fun, not to progress your save. For permanent money, focus on heists, businesses and side activities.</p>'
  '<h2>Beware of scams</h2><p>Never trust "money generators", console mod menus or sites asking for your PSN, Xbox or Rockstar login. They are scams and can get your account stolen or banned.</p>' + GUIDE, []),
"how-to-enter-cheats": ("How to Enter Cheats in GTA 6 – Step by Step", "How to Enter GTA 6 Cheats", "a simple step-by-step guide",
  "Learn how to activate cheat codes in GTA 6 on PS5 and Xbox Series X|S using the in-game phone.", 0,
  '<h2>Step by step</h2><ol><li>Finish the story and load your story mode save.</li><li>Save your game first — saving is disabled while a cheat is active.</li><li>Open the in-game phone.</li><li>Hold L1 + R1 (PS5) or LB + RB (Xbox).</li><li>Enter the D-Pad sequence from <a href="./">our table</a>.</li><li>Wait for the on-screen confirmation.</li></ol>'
  '<h2>Reading the arrows</h2><p>↑ is D-Pad up, → right, ↓ down and ← left. Enter them in order from left to right without long pauses.</p>'
  '<h2>Troubleshooting</h2><p>Codes do not work during missions, cutscenes or menus. If nothing happens, check that the cheat is unlocked in Progress &gt; Cheats. If a code still fails, it may require a game update — <a href="contact.html">tell us</a> and we will re-test it.</p>' + FQ, [FAQLD]),
"unlock-challenges": ("GTA 6 Cheat Unlocks – Challenges Guide", "GTA 6 Challenges & Cheat Unlocks", "which challenges unlock which cheat",
  "In GTA 6, most vehicle spawn cheats are unlocked by completing challenges. This guide lists every challenge-based unlock.", 0,
  '<h2>How challenges unlock cheats</h2><p>After you finish the story, the Cheats list appears in the Progress menu. Most vehicle spawn cheats are tied to the challenge categories: Fitness, Combat, Shopping, Exploration, Vehicle, Sports, Survival and Criminal. Completing 5 challenges in a category unlocks one vehicle, and completing all challenges of that category unlocks a second, usually better, vehicle. Completing every challenge in the game unlocks the Hauners P-996 Lazer jet.</p>'
  '<h2>Cheats unlocked by challenges</h2>' + table(unlock("challenges")) + '<h2>Challenge categories at a glance</h2><table><thead><tr><th>Category</th><th>5 challenges</th><th>All challenges</th></tr></thead><tbody><tr><td>Fitness</td><td>Tuff BMX</td><td>&#39;65 Vapid Dominator</td></tr><tr><td>Combat</td><td>Speeder 700 GT</td><td>Bravado Banshee</td></tr><tr><td>Shopping</td><td>Maibatsu Boomazoom</td><td>Truffade Thrax</td></tr><tr><td>Exploration</td><td>Nagasaki Sea Sparrow</td><td>Nagasaki Carbon RS</td></tr><tr><td>Vehicle</td><td>Lapwing Mallard</td><td>Progen Emerus</td></tr><tr><td>Sports</td><td>Vapid Stanier G2 Taxi</td><td>Brimstone Golfer</td></tr><tr><td>Survival</td><td>Airboat 09</td><td>Hauners Rhino Tank</td></tr><tr><td>Criminal</td><td>Maibatsu Sanchez</td><td>Western Zombie Bobber</td></tr></tbody></table>'
  '<h2>Other unlock types</h2><p>Some cheats are unlocked by discovering a vehicle in the Progress menu (Interstate Ambulance, MTL Pumper, HVY Bulldozer), by collectibles (Watches, Vice City Flamingos cards), by activities with your partner, or by repeating an action many times, such as throwing 100 grenades or catching 100 fish.</p>' + GUIDE, []),
"screen-filter-cheats": ("GTA 6 Screen Filter Cheats – All Visual Filters", "GTA 6 Screen Filter Cheats", "change the look of Vice City",
  "GTA 6 includes screen filter cheats that change the visual style of the game, plus weather and time-of-day cheats.", 0,
  '<h2>Screen filter, weather &amp; time cheats</h2>' + table(cat("world")) + '<h2>What are screen filters?</h2><p>Screen filter cheats change the colours and look of the whole game, like a camera filter. They are perfect for screenshots, videos and photo mode. All filters start with the same sequence (↓ ↓ ↑ → → ↑ ← ←) followed by two final directions, which makes them easy to remember once you know the pattern.</p>'
  '<h2>Weather and time cheats</h2><p>Cycle Weather changes the current weather, Move Time Forward skips ahead in the day, and Pause Time of Day freezes the clock — useful to keep a sunset for your photos. The time cheats are unlocked by finding collectible Watches.</p>' + GUIDE, []),
"best-cheats": ("Best GTA 6 Cheats to Unlock First", "Best GTA 6 Cheats to Use First", "our top picks and the easiest unlocks",
  "Which GTA 6 cheats should you unlock first? Our selection of the most useful cheats and the easiest ones to get.", 0,
  '<h2>Unlocked just by finishing the story</h2><p>Four cheats are available as soon as the story is completed: <b>$250,000 Money</b>, <b>Unlimited Focus</b>, <b>Attack Force</b> and <b>Cycle Weather</b>. Start with these — no extra grinding needed.</p>' + table(unlock("finish the story")) +
  '<h2>Our top picks</h2><ol><li><b>Body Armor</b> — the most useful survival cheat (complete 100 workouts).</li><li><b>Infinite Ammo</b> and <b>No Reload</b> — unlocked through the Shooting Ranges; aim for gold medals to get both.</li><li><b>Repair Vehicle</b> — saves you after every police chase (win races at Gellhorn Raceway, Thrillbilly Mud Club and Boone Speedway).</li><li><b>Parachute</b> and <b>No Fall Damage</b> — great for exploring rooftops and cliffs.</li><li><b>Hauners Rhino Tank</b> — the ultimate fun vehicle (complete all Survival challenges).</li></ol>'
  '<h2>Easy unlocks</h2><p>Some cheats need fewer repetitions than others: <b>Exploding Balls</b> (hit 20 enemies with explosive damage), <b>Vehicle Force</b> (25 enemies with a vehicle) and <b>Drunk</b> (spend $2,500 on alcohol) can be unlocked quickly during free roam.</p>' + GUIDE, []),
"faq": ("GTA 6 Cheats FAQ – Common Questions Answered", "GTA 6 Cheats FAQ", "answers to common questions",
  "Answers to the most common questions about GTA 6 cheat codes: trophies, GTA Online, money, PC and codes that do not work.", 0, FQ + HOW, [FAQLD]),
"about": (f"About – {SITE}", "About Us", "who we are and how we check codes",
  f"{SITE} is an independent fan website built to make GTA 6 cheat codes easy to find.", 0,
  f"<h2>Our mission</h2><p>We are GTA players who were tired of cheat lists hidden in long articles and videos. {SITE} shows every GTA 6 code at a glance, in a table you can search and filter in one second, on phone or desktop.</p>"
  "<h2>How we check codes</h2><p>Each sequence is cross-checked against several published guides before it is added. When a reader reports a code that does not work, we re-test it and update the table. Pages show the date of their last update.</p>"
  f"<h2>Contact</h2><p>Found a new cheat or an error? Write to {CONTACT}.</p>"
  "<h2>Disclaimer</h2><p>Not affiliated with Rockstar Games or Take-Two Interactive. Grand Theft Auto is a trademark of Take-Two Interactive. All game names are used for identification only.</p>", []),
"contact": (f"Contact – {SITE}", "Contact", "report a code or ask a question",
  "Found a new cheat or a code that does not work? Contact the GTA6CheatCodes.hub team.", 0,
  f"<h2>Get in touch</h2><p>Email: {CONTACT}. We usually reply within 48 hours.</p>"
  "<h2>Reporting a code</h2><p>To help us fix a code quickly, tell us the cheat name, your console (PS5 or Xbox Series X|S), your game version and what happened. We never ask for your account login or password.</p>", []),
"privacy": (f"Privacy Policy – {SITE}", "Privacy Policy", "how we use data and cookies",
  f"This privacy policy explains how {SITE} handles data and cookies.", 0,
  "<h2>Data we collect</h2><p>We do not require accounts and do not collect personal data through forms. Our hosting provider may keep standard server logs (IP address, browser, pages visited) for security.</p>"
  "<h2>Cookies and advertising</h2><p>This site uses Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the Internet. "
  'You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads">Google Ads Settings</a> or <a href="https://www.aboutads.info">www.aboutads.info</a>. See also <a href="https://policies.google.com/technologies/partner-sites">how Google uses data from partner sites</a>.</p>'
  "<h2>Consent (EEA, UK, Switzerland)</h2><p>Visitors from these regions are asked for consent before personalised ads are shown, through a Google-certified consent message. You can change your choice at any time from the link in that message.</p>"
  f"<h2>Your rights</h2><p>You can request access to or deletion of your data by writing to {CONTACT}.</p><p>Last updated: {TODAY}.</p>", []),
"terms": (f"Terms of Use – {SITE}", "Terms of Use", "rules for using this site", f"Terms of use for {SITE}.", 0,
  "<h2>Use of content</h2><p>Content is for personal, informational use. Codes are provided as-is; always save before using cheats.</p><h2>No affiliation</h2><p>Not endorsed by Rockstar Games or Take-Two Interactive.</p><h2>Liability</h2><p>We are not responsible for lost progress, disabled trophies or any issue resulting from cheats.</p>"
  f"<h2>Changes</h2><p>We may update these terms; the date below shows the latest version.</p><p>Last updated: {TODAY}.</p>", []),
"sitemap": (f"Sitemap – {SITE}", "Sitemap", "all pages of this website", f"Every page of {SITE}.", 0, None, []),
}
P["sitemap"] = P["sitemap"][:5] + ('<h2>All pages</h2><ul>' + "".join(f'<li><a href="{href(k)}">{v[1]}</a></li>' for k, v in P.items() if k != "sitemap") + '</ul>', [])

HEAD_ADS = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-{PUB}" crossorigin="anonymous"></script>' if PUB else ""

def page(k, t, h, s, d, tl, b, ld):
    url = BASE + ("" if k == "index" else f"{k}.html")
    graph = ld[:]
    if k == "index":
        graph.insert(0, {"@type": "WebSite", "name": SITE, "url": BASE or None})
    else:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE or None},
            {"@type": "ListItem", "position": 2, "name": h}]})
    ldj = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace(', "url": null', "").replace(', "item": null', "")
    meta = [f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t)}</title>',
            f'<meta name="description" content="{html.escape(d)}">',
            '<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="apple-touch-icon.png">',
            '<meta name="theme-color" content="#2e6690">',
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="{SITE}"><meta property="og:title" content="{html.escape(t)}"><meta property="og:description" content="{html.escape(d)}">',
            '<meta name="twitter:card" content="summary_large_image">']
    if BASE:
        meta += [f'<link rel="canonical" href="{url}">', f'<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}og-image.png">']
    if GSC and k == "index":
        meta.append(f'<meta name="google-site-verification" content="{GSC}">')
    meta += ['<link rel="stylesheet" href="style.css">', HEAD_ADS, f'<script type="application/ld+json">{ldj}</script>']
    js = '<script src="app.js" defer></script>'
    return (f'<!doctype html><html lang="en"><head>{"".join(meta)}</head><body><div class="page">{HEADER}<main>'
            f'<h1>{h}</h1><p class="sub">{s}</p>{TOOL if tl else ""}<div class="intro">{d}</div>{b}'
            f'<p class="upd">Last updated: {TODAY}</p></main>{FOOTER}</div>{js}</body></html>')

for k, v in P.items():
    open(k + ".html", "w", encoding="utf-8").write(page(k, *v))

open("404.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found – {SITE}</title>'
    '<meta name="robots" content="noindex"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"></head>'
    '<body><div class="page"><main><h1>Page not found</h1><p class="sub">this page does not exist</p><p><a href="/">See all GTA 6 cheat codes</a></p></main></div></body></html>')

if BASE:
    open("sitemap.xml", "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{BASE}{'' if k == 'index' else k + '.html'}</loc><lastmod>{TODAY}</lastmod></url>" for k in P) + "</urlset>")
    if CNAME: open("CNAME", "w").write(DOMAIN)
open("robots.txt", "w").write("User-agent: *\nAllow: /\n" + (f"Sitemap: {BASE}sitemap.xml\n" if BASE else ""))
if PUB:
    open("ads.txt", "w").write(f"google.com, {PUB}, DIRECT, f08c47fec0942fa0\n")
missing = [n for n, v in [("DOMAIN", DOMAIN), ("PUB", PUB), ("EMAIL", EMAIL), ("GSC", GSC)] if not v]
print(f"ok: {len(P)} pages, {N} cheats" + (f" | missing: {', '.join(missing)}" if missing else ""))
