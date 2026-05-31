"""
Genereer Upgrade-Roadmap.pdf — het volledige plan om het Claude Engineering
Handboek naar volgend niveau te tillen.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, ListFlowable, ListItem, HRFlowable
)
from reportlab.pdfgen import canvas

# Brand colors — afgestemd op handboek
ORANGE = HexColor("#EA580C")
ORANGE_SOFT = HexColor("#FED7AA")
INK = HexColor("#1C1917")
MUTED = HexColor("#57534E")
SUBTLE = HexColor("#A8A29E")
PAPER = HexColor("#FAF6F0")
RULE = HexColor("#D6D3D1")

OUT = "C:/Users/lars/ai-engineering/Upgrade-Roadmap.pdf"


def make_styles():
    s = getSampleStyleSheet()
    styles = {
        "cover_eyebrow": ParagraphStyle(
            "cover_eyebrow", parent=s["Normal"],
            fontName="Helvetica-Bold", fontSize=9, textColor=ORANGE,
            spaceAfter=10, leading=12, letterSpacing=2
        ),
        "cover_title": ParagraphStyle(
            "cover_title", parent=s["Title"],
            fontName="Helvetica-Bold", fontSize=42, textColor=INK,
            leading=46, spaceAfter=14, alignment=TA_LEFT,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", parent=s["Normal"],
            fontName="Helvetica", fontSize=14, textColor=MUTED,
            leading=20, spaceAfter=24,
        ),
        "cover_meta": ParagraphStyle(
            "cover_meta", parent=s["Normal"],
            fontName="Helvetica", fontSize=9, textColor=SUBTLE,
            leading=14,
        ),
        "h1": ParagraphStyle(
            "h1", parent=s["Heading1"],
            fontName="Helvetica-Bold", fontSize=22, textColor=INK,
            spaceBefore=18, spaceAfter=10, leading=26,
        ),
        "h2": ParagraphStyle(
            "h2", parent=s["Heading2"],
            fontName="Helvetica-Bold", fontSize=15, textColor=INK,
            spaceBefore=14, spaceAfter=6, leading=19,
        ),
        "h3": ParagraphStyle(
            "h3", parent=s["Heading3"],
            fontName="Helvetica-Bold", fontSize=11, textColor=ORANGE,
            spaceBefore=10, spaceAfter=3, leading=14,
        ),
        "eyebrow": ParagraphStyle(
            "eyebrow", parent=s["Normal"],
            fontName="Helvetica-Bold", fontSize=8, textColor=ORANGE,
            spaceAfter=4, leading=10,
        ),
        "body": ParagraphStyle(
            "body", parent=s["Normal"],
            fontName="Helvetica", fontSize=10, textColor=INK,
            leading=15, spaceAfter=8, alignment=TA_JUSTIFY,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=s["Normal"],
            fontName="Helvetica", fontSize=10, textColor=INK,
            leading=14, spaceAfter=3, leftIndent=10,
        ),
        "code": ParagraphStyle(
            "code", parent=s["Code"],
            fontName="Courier", fontSize=8.5, textColor=INK,
            backColor=HexColor("#F5EFE5"), borderPadding=8,
            leading=12, spaceBefore=6, spaceAfter=10,
        ),
        "callout": ParagraphStyle(
            "callout", parent=s["Normal"],
            fontName="Helvetica", fontSize=10, textColor=INK,
            backColor=ORANGE_SOFT, borderColor=ORANGE,
            borderWidth=0, borderPadding=10, leading=14,
            spaceBefore=8, spaceAfter=10,
        ),
        "muted": ParagraphStyle(
            "muted", parent=s["Normal"],
            fontName="Helvetica-Oblique", fontSize=9, textColor=MUTED,
            leading=13, spaceAfter=6,
        ),
        "table_head": ParagraphStyle(
            "table_head", fontName="Helvetica-Bold", fontSize=9,
            textColor=white, leading=12,
        ),
        "table_cell": ParagraphStyle(
            "table_cell", fontName="Helvetica", fontSize=9,
            textColor=INK, leading=12,
        ),
        "table_cell_b": ParagraphStyle(
            "table_cell_b", fontName="Helvetica-Bold", fontSize=9,
            textColor=INK, leading=12,
        ),
    }
    return styles


def header_footer(canvas_obj, doc):
    """Page header + footer met branding."""
    canvas_obj.saveState()
    # Footer
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(SUBTLE)
    canvas_obj.drawString(
        2 * cm, 1.2 * cm,
        "Claude Engineering Handboek — Upgrade Roadmap"
    )
    canvas_obj.drawRightString(
        A4[0] - 2 * cm, 1.2 * cm, f"{doc.page}"
    )
    # Subtle accent line at top
    if doc.page > 1:
        canvas_obj.setStrokeColor(ORANGE)
        canvas_obj.setLineWidth(2)
        canvas_obj.line(2 * cm, A4[1] - 1.2 * cm,
                        2 * cm + 1.5 * cm, A4[1] - 1.2 * cm)
    canvas_obj.restoreState()


def cover_page(styles):
    elems = []
    elems.append(Spacer(1, 3 * cm))
    elems.append(Paragraph("STRATEGISCH PLAN · MEI 2026", styles["cover_eyebrow"]))
    elems.append(Paragraph(
        "Upgrade-Roadmap<br/>Claude Engineering<br/>Handboek",
        styles["cover_title"]
    ))
    elems.append(HRFlowable(width="20%", thickness=3, color=ORANGE,
                            spaceBefore=4, spaceAfter=20))
    elems.append(Paragraph(
        "Van interactief studieboek (€69 lifetime) naar volwaardig "
        "premium-product met repo, capstone, video, community en "
        "industry-verticals — gestapeld in 8 niveau's.",
        styles["cover_sub"]
    ))
    elems.append(Spacer(1, 0.8 * cm))
    elems.append(Paragraph(
        "<b>Inhoud</b><br/>"
        "1. Huidige status &amp; uitgangspunt<br/>"
        "2. Niveau 1 — Editorial polish (60u)<br/>"
        "3. Niveau 2 — Werkende code-repo (130u)<br/>"
        "4. Niveau 3 — Capstone met scaffold &amp; rubric (80u)<br/>"
        "5. Niveau 4 — Authority en originaliteit (140u)<br/>"
        "6. Niveau 5 — Video-walkthroughs (120u)<br/>"
        "7. Niveau 6 — Community + cohort<br/>"
        "8. Niveau 7 — Industry verticals<br/>"
        "9. Niveau 8 — Premium services<br/>"
        "10. App-engineering upgrades<br/>"
        "11. Roadmap-samenvatting (tabel)<br/>"
        "12. Aanbevolen volgorde van impact-per-uur<br/>"
        "13. Strategische slotvraag",
        styles["body"]
    ))
    elems.append(Spacer(1, 2.5 * cm))
    elems.append(Paragraph(
        "Datum: 2026-05-10 &nbsp;·&nbsp; Versie: 1.0 &nbsp;·&nbsp; "
        "~600-800u werk · 6-12 maanden",
        styles["cover_meta"]
    ))
    elems.append(PageBreak())
    return elems


def H1(text, styles):
    return [Paragraph(text, styles["h1"]),
            HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=8)]


def H2(text, styles):
    return [Paragraph(text, styles["h2"])]


def H3(text, styles):
    return [Paragraph(text, styles["h3"])]


def P(text, styles):
    return Paragraph(text, styles["body"])


def Bullets(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(it, styles["bullet"]), leftIndent=12, value="•")
         for it in items],
        bulletType="bullet", leftIndent=12,
    )


def Code(text, styles):
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    safe = safe.replace("\n", "<br/>")
    return Paragraph(f"<font name='Courier' size='8.5'>{safe}</font>",
                     styles["code"])


def Callout(text, styles):
    return Paragraph(f"<b>→</b> &nbsp; {text}", styles["callout"])


def TWO_COL_TABLE(rows, styles, col_widths=None):
    data = []
    for left, right in rows:
        data.append([
            Paragraph(left, styles["table_cell_b"]),
            Paragraph(right, styles["table_cell"]),
        ])
    t = Table(data, colWidths=col_widths or [4.5 * cm, 12 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.5, RULE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.5, RULE),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def DATA_TABLE(header, rows, styles, col_widths=None):
    data = [[Paragraph(h, styles["table_head"]) for h in header]]
    for row in rows:
        data.append([Paragraph(c, styles["table_cell"]) for c in row])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ORANGE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("LINEBELOW", (0, 0), (-1, 0), 0, ORANGE),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, RULE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F8F5F0")]),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


# =====================================================
#  CONTENT
# =====================================================

def build_story(styles):
    story = []
    story.extend(cover_page(styles))

    # ---- NIVEAU 0 ----
    story.extend(H1("Niveau 0 — Waar je nu staat", styles))
    story.append(P(
        "Het Claude Engineering Handboek is sinds mei 2026 een interactieve "
        "single-page React-app met 45 modules in 9 categorieën, "
        "ongeveer 15.000 regels gestructureerde Nederlandstalige content. "
        "Zes sprints aan upgrades zijn uitgevoerd: hash-routing, copy-knoppen, "
        "Cmd+K-palette, prev/next-navigatie, oefen-checkboxes, JSON-sync van "
        "voortgang, sepia-thema, streaks, in-page TOC, glossary-tooltip-helper, "
        "een quiz-modus met 96 vragen, een BYOK prompt-sandbox en AI-Tutor met "
        "module-context, en twaalf nieuwe modules (Computer Use, Structured "
        "Outputs, Multi-agent, Observability, Voice, Agent SDK, AI UX Patterns, "
        "Guardrails, Prompt Ops, Fine-tuning, Memory + verdrievoudiging van "
        "Cowork/Dispatch/Routines).", styles))
    story.append(P(
        "Wat ontbreekt: auteur-identiteit, werkende companion-repo, capstone-"
        "project met rubric, échte production case studies, video-walkthroughs, "
        "live element (cohort/community), en industry-specifieke diepte.",
        styles))
    story.append(Callout(
        "<b>Huidige prijs-ceiling: €69-89 lifetime.</b> Sterke breedte + "
        "interactiviteit, maar zonder auteur-merk en werkende repo blijft het "
        "een 'professional ebook+app'.", styles))

    story.append(PageBreak())

    # ---- NIVEAU 1 ----
    story.extend(H1("Niveau 1 — Editorial polish", styles))
    story.append(Paragraph("2 weken &nbsp;·&nbsp; 50-70 uur &nbsp;·&nbsp; "
                           "<b>ontgrendelt €69 → €99</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: van indie-handboek naar professional ebook+app. "
        "Grootste hefbomen: vertrouwen + auteur-zichtbaarheid.", styles))

    story.extend(H3("1.1 Citaties op elke numerieke claim — 15u", styles))
    story.append(P(
        "Bouw een Cite-component die voetnoten genereert. Achterin elk module "
        "een Bronnen-sectie. Pak alle '85% kostbesparing', '67% retrieval "
        "errors', '3.6× sneller' en koppel een paper of blogpost.", styles))

    story.extend(H3("1.2 Auteur-pagina — 4u", styles))
    story.append(P(
        "Eén nieuwe module: /auteur. Foto, 1-zin elevator pitch, vijf "
        "production-momenten ('Ik bouwde X bij Y, leerde Z'), LinkedIn + "
        "GitHub + website, 'Waarom dit handboek bestaat' (twee alinea's). "
        "Single grootste hefboom voor vertrouwen.", styles))

    story.extend(H3("1.3 Per-module changelog — 8u", styles))
    story.append(P(
        "Vervang uniform lastUpdated door werkelijke datums + wat er "
        "veranderde. Toon als hover-popover bij datum. Bewijst dat het "
        "levend werk is.", styles))

    story.extend(H3("1.4 Stylistische consistentie audit — 15u", styles))
    story.append(P(
        "De twaalf nieuwste modules zijn herkenbaar anders dan de originele. "
        "Pak elke module door en zorg voor consistente sectie-templates "
        "(Wat / Hoe / Patronen / Anti-patterns / Vuistregel), zelfde toon, "
        "zelfde dichtheid van code-voorbeelden.", styles))

    story.extend(H3("1.5 Real testimonials — 10u", styles))
    story.append(P(
        "DM 30 mensen uit netwerk die fragmenten kunnen gebruiken. "
        "Doel: vijf quotes met naam, foto en functie. Plaats op landingspagina "
        "én op auteur-pagina.", styles))

    story.append(PageBreak())

    # ---- NIVEAU 2 ----
    story.extend(H1("Niveau 2 — Werkende code-repo", styles))
    story.append(Paragraph("4 weken &nbsp;·&nbsp; 100-140 uur &nbsp;·&nbsp; "
                           "<b>ontgrendelt €99 → €129</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: lezers kunnen alles wat in het boek staat <b>runnen</b> "
        "binnen vijf minuten. Dit is het grootste gat tussen 'lezen' en "
        "'doen'.", styles))

    story.extend(H3("2.1 Companion repo: claude-handbook-code — 60-80u", styles))
    story.append(P(
        "Eén GitHub-repo, één folder per priority-module. Elke folder heeft "
        "README, requirements.txt, .env.example, seed-data, werkende code. "
        "Regels: paste-and-run binnen vijf minuten, werkt op Mac/Linux/Windows, "
        "geen externe download nodig.", styles))
    story.append(Code(
        "claude-handbook-code/\n"
        "├── 01-fundamentals/\n"
        "│   ├── README.md\n"
        "│   ├── requirements.txt\n"
        "│   ├── .env.example\n"
        "│   ├── 01_first_call.py\n"
        "│   └── 02_streaming.py\n"
        "├── 04-rag/\n"
        "│   ├── docker-compose.yml      # postgres + pgvector\n"
        "│   ├── seed_data/              # 100 sample docs\n"
        "│   ├── 01_naive_rag.py\n"
        "│   ├── 02_hybrid_search.py\n"
        "│   ├── 03_contextual_retrieval.py\n"
        "│   ├── 04_with_reranker.py\n"
        "│   └── 05_ragas_eval.py\n"
        "└── 09-agents/ ...", styles))

    story.extend(H3("2.2 Branch per hoofdstuk — 10u", styles))
    story.append(P(
        "Voor de RAG-folder: branches step-1-naive, step-2-hybrid, "
        "step-3-contextual. Lezer kan tussenstand checkouten.", styles))

    story.extend(H3("2.3 Nightly CI tegen Anthropic API — 15u", styles))
    story.append(P(
        "GitHub Actions runt elke 24 uur alle voorbeelden tegen echte API. "
        "Detecteert breakages binnen één etmaal (bv. model-deprecatie). "
        "Slack-alert.", styles))

    story.extend(H3("2.4 In-handboek 'Open in repo'-knop — 10u", styles))
    story.append(P(
        "Naast elke Pre met substantiële code: knopje 'Open in repo →' "
        "linkt naar specifiek bestand op specifieke regel. Lezer kan kiezen: "
        "kopiëren of doorklikken naar runnable versie.", styles))

    story.extend(H3("2.5 In-browser code execution (optioneel) — 30u", styles))
    story.append(P(
        "Embed StackBlitz of CodeSandbox iframes voor de simpelere "
        "voorbeelden. Werkt voor JS/TS modules. Voor Python: Pyodide voor "
        "simpel, anders Replit-iframe.", styles))

    story.append(PageBreak())

    # ---- NIVEAU 3 ----
    story.extend(H1("Niveau 3 — Capstone met scaffold en rubric", styles))
    story.append(Paragraph("2 weken &nbsp;·&nbsp; 60-80 uur &nbsp;·&nbsp; "
                           "<b>ontgrendelt €129 → €169</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: één concreet eindproject dat lezers daadwerkelijk afmaken "
        "en kunnen pronken. Deelbaar op LinkedIn = gratis marketing.", styles))

    story.extend(H3("3.1 Het project — 40u", styles))
    story.append(P(
        "Voorstel: <b>Production-Ready Customer Support Agent</b> — "
        "een agent die ticket-inkomend (e-mail webhook → Inngest) "
        "classificeert, bij FAQ direct via RAG antwoordt, bij escalatie "
        "context optrekt en een draft schrijft, met logging naar Langfuse, "
        "kosten per ticket, en een eval-suite van dertig test-tickets. "
        "Raakt: prompting, structured outputs, RAG, agents, observability, "
        "evals, cost-tracking — bijna alle modules.", styles))

    story.extend(H3("3.2 Scaffold-repo — 15u", styles))
    story.append(P(
        "Werkende skeleton in support-agent-starter repo. Twaalf mijlpalen "
        "met TODO-comments. Test-suite die per mijlpaal groen kleurt. "
        "Lezer hoeft alleen TODO's invullen.", styles))

    story.extend(H3("3.3 Rubric — 10u", styles))
    story.append(P(
        "Tien criteria, elk gewicht 1-3 (prompt-design, tool reliability, "
        "RAG-quality, cost-tracking, observability, security, ...). "
        "Lezer scoort zichzelf en kan zo gat identificeren.", styles))

    story.extend(H3("3.4 Drie voorbeeld-oplossingen — 15u", styles))
    story.append(Bullets([
        "Eén minimale oplossing (slaagt rubric net)",
        "Eén productie-niveau oplossing (alle bells and whistles)",
        "Eén 'fout maar leerzaam' (bewust gebrekkig, met annotaties)",
    ], styles))
    story.append(P(
        "Dit is hoe Frontend Masters het doet. Lezer leert door vergelijken.",
        styles))

    story.append(PageBreak())

    # ---- NIVEAU 4 ----
    story.extend(H1("Niveau 4 — Authority en originaliteit", styles))
    story.append(Paragraph("6-8 weken &nbsp;·&nbsp; 120-160 uur &nbsp;·&nbsp; "
                           "<b>ontgrendelt €169 → €229</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: van 'samenvatting van canon' naar 'doorleefde stem in het "
        "veld'. Dit is het verschil tussen een €150 handboek en een €299 "
        "cursus.", styles))

    story.extend(H3("4.1 Vijf échte case studies — 30-80u", styles))
    story.append(Bullets([
        "<b>Optie A — interview-based (snel, ~30u):</b> interview vijf NL "
        "AI-engineers (LinkedIn-DM, koffie, opname). Schrijf elk uit als "
        "1.500-woorden case-study met hun bedrijfsnaam, hun cijfers, hun "
        "fouten.",
        "<b>Optie B — eigen implementaties (langzamer, ~80u):</b> bouw zelf "
        "vijf systemen voor vijf sectoren. Documenteer proces incl. fouten.",
    ], styles))
    story.append(P(
        "Optie A is snel + bouwt netwerk. Optie B is dieper. "
        "Doe beide gespreid.", styles))

    story.extend(H3("4.2 Auteur-opinie per module — 30u", styles))
    story.append(P(
        "Elk module krijgt onderaan een sectie 'Mijn aanpak' of 'Wat ik "
        "anders zou doen'. Voorbeelden: 'Ik vind GraphRAG nog niet productie-"
        "klaar voor &lt;100k docs — hier is waarom' of 'Voor RAG begin ik "
        "altijd met BM25 alleen — pas hybrid bij &gt;5% miss-rate'. "
        "Transformeert handboek-stem van 'neutraal samenvatten' naar "
        "'actieve gids met meningen'. Mensen citeren handboeken alleen als "
        "ze meningen hebben.", styles))

    story.extend(H3("4.3 Manifest / thesis-essay — 10u", styles))
    story.append(P(
        "Eén nieuw hoofdstuk vooraan: 'Hoe ik denk over AI engineering'. "
        "Niet didactisch — manifest. Wat is je thesis? Wat geloof je dat "
        "anderen niet geloven? Eén goede thesis is een carrière waard.",
        styles))

    story.extend(H3("4.4 Auteur-introductie video — 10u", styles))
    story.append(P(
        "Eén 5-10min video. Camera op gezicht, goede mic. Vertel waarom je "
        "dit handboek schreef, welke pijn je oploste, wat lezers moeten "
        "verwachten, en eerlijk over wat dit handboek NIET is. "
        "Embed op landingspagina. Conversiestijging meestal 30-50%.", styles))

    story.extend(H3("4.5 War stories / failure-mode atlas — 20u", styles))
    story.append(P(
        "Aparte module: 'Wat ging er mis bij ons (en bij onze klanten)'. "
        "Twintig incidents met cijfers, namen waar mogelijk, en geleerde "
        "lessen. Dit is goud.", styles))

    story.extend(H3("4.6 Doorleeft je vakblik bewijzen (lopend werk)", styles))
    story.append(Bullets([
        "Wekelijkse LinkedIn-posts met één production-inzicht",
        "Maandelijkse blog: 'Wat ik geleerd heb in [maand]'",
        "Conferentie-talk inzenden (PyCon NL, AI Stage NL, AppDevCon)",
        "Gast op podcast (Code Voor Twee, NL Tech Talks)",
    ], styles))

    story.append(PageBreak())

    # ---- NIVEAU 5 ----
    story.extend(H1("Niveau 5 — Video-walkthroughs", styles))
    story.append(Paragraph("6 weken &nbsp;·&nbsp; 100-140 uur &nbsp;·&nbsp; "
                           "<b>ontgrendelt €229 → €299</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: verschillende leerstijlen bedienen + premium-perceptie.",
        styles))

    story.extend(H3("5.1 Welke modules video krijgen — 5u keuze", styles))
    story.append(P(
        "Niet alles. Top tien modules waar video meerwaarde heeft: "
        "Welcome (verkoopt het hele product), Roadmap, Prompting Basics "
        "(live prompt-iteraties tonen), Prompting Advanced, Tools &amp; MCP "
        "(server bouwen + connecten), Agents (loop debuggen live), RAG "
        "(build-along), Evals (LLM-as-judge instellen), Computer Use "
        "(live demo), Capstone-walkthrough.", styles))

    story.extend(H3("5.2 Productie-setup — 10u eenmalig", styles))
    story.append(Bullets([
        "Lavalier mic (€80, Rode Wireless GO)",
        "Camerahoek (telefoon op statief is prima)",
        "Screen-recording (Camtasia of OBS)",
        "Captions (Descript of Whisper auto)",
        "Aspect: gezicht in hoek (15% van scherm), screen primair",
    ], styles))

    story.extend(H3("5.3 Video-productie — ~10u per module", styles))
    story.append(P(
        "30-60 min per video. Tien modules × 10u = ~100u totaal. "
        "Plan in batches: twee modules per week × vijf weken.", styles))

    story.extend(H3("5.4 Embedding — 5u", styles))
    story.append(P(
        "Niet op YouTube (gratis SEO maar gratuit gevoel). "
        "Op Cloudflare Stream (~€1/1000 minuten weergegeven). "
        "Embedded in module-pagina, niet weglinken.", styles))

    story.append(PageBreak())

    # ---- NIVEAU 6 ----
    story.extend(H1("Niveau 6 — Community + cohort (live element)", styles))
    story.append(Paragraph("6 weken setup + lopend onderhoud &nbsp;·&nbsp; "
                           "<b>ontgrendelt €299 → €499</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: van eenmalig product naar levend ecosysteem.", styles))

    story.extend(H3("6.1 Discord/Slack community — 10u setup", styles))
    story.append(P(
        "Hoofdkanalen: announcements, general, hulp-per-module, capstone-"
        "pronken, jobs. Bot voor onboarding + module-progress milestones. "
        "Ingebouwd in upgrade-tier (€149) of als losse SKU.", styles))

    story.extend(H3("6.2 Maandelijkse office hours — 4u/maand lopend", styles))
    story.append(P(
        "Eerste donderdag van de maand, 90 min Q&amp;A op vragen die in "
        "Discord verzameld zijn. Opname beschikbaar. Inclusief in tier "
        "€149+.", styles))

    story.extend(H3("6.3 Cohort-format — 8 weken × 4u/week", styles))
    story.append(Bullets([
        "Wekelijkse 90-min Q&amp;A live",
        "Dagelijkse Discord-aanwezigheid (15 min/dag)",
        "Capstone-review op week 7",
        "Certificate of completion",
        "Prijs €299-499, 2-3 cohorts/jaar",
        "30-50 lezers per cohort",
    ], styles))
    story.append(Callout(
        "Praktisch: start met <b>één</b> cohort als pilot. Verkoop dertig "
        "plekken op €299. Loop door, leer wat brak, pas aan voor cohort 2.",
        styles))

    story.append(PageBreak())

    # ---- NIVEAU 7 ----
    story.extend(H1("Niveau 7 — Industry verticals", styles))
    story.append(Paragraph("3-6 maanden per vertical &nbsp;·&nbsp; "
                           "<b>add-on €99-199 bovenop base €69</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: ontspannen je breedte-flûte en diep gaan in vakgebieden "
        "waar mensen 5-10× meer betalen.", styles))

    story.extend(H3("7.1 Voorgestelde verticals (volgorde NL-marktomvang)",
                    styles))
    story.append(DATA_TABLE(
        ["Vertical", "Markt-grootte NL", "Bereidheid te betalen",
         "Diepte vereist"],
        [
            ["Legal-tech", "Klein, hoog tarief", "€299-499/persoon", "Middel"],
            ["Fintech / Banking", "Groot, hoog tarief",
             "€299-599/persoon", "Hoog (compliance)"],
            ["Healthcare", "Middelgroot, hoog", "€399-699/persoon",
             "Hoog (NEN 7510, MDR)"],
            ["E-commerce / Retail", "Groot, lager tarief",
             "€149-249/persoon", "Laag-middel"],
            ["Government / Overheid", "Niche, hoog",
             "€499-999/persoon", "Hoog (DSA, GDPR)"],
        ], styles,
        col_widths=[3.5 * cm, 4 * cm, 4.5 * cm, 4.5 * cm]
    ))

    story.extend(H3("7.2 Format per vertical", styles))
    story.append(P(
        "Niet een nieuw boek schrijven. Een <b>module-pack</b> van 8-12 "
        "modules ÓP het hoofdhandboek: compliance-laag voor de vertical, "
        "sector-specifieke prompts en evals, drie échte case studies met "
        "named klant, reference-implementaties, failure modes + "
        "audit-checklist. Verkocht als €99-199 add-on bovenop de €69 base. "
        "Bundle: base + één vertical = €199; alle verticals = €499.", styles))

    story.extend(H3("7.3 Co-creatie met sector-expert", styles))
    story.append(P(
        "Voor elke vertical: vind één expert in dat vakgebied "
        "(LinkedIn-DM, koffie). Co-author het pack. 50/50 revenue split. "
        "Hun naam + jouw infrastructuur = legitimiteit + bereik.", styles))

    story.append(PageBreak())

    # ---- NIVEAU 8 ----
    story.extend(H1("Niveau 8 — Premium services", styles))
    story.append(Paragraph("Lopend &nbsp;·&nbsp; voor select kopers "
                           "&nbsp;·&nbsp; <b>ARPU €2-15k per project</b>",
                           styles["eyebrow"]))
    story.append(P(
        "Doel: monetiseer de top 1% lezers die echt willen leren of laten "
        "bouwen. Hier komt het echte inkomen vandaan na jaar 1.", styles))

    story.extend(H3("8.1 1:1 office hours — €199/uur", styles))
    story.append(P(
        "60 min videocall over één concrete vraag van de koper. "
        "'Help me mijn agent debuggen' of 'review onze RAG-architectuur'. "
        "Schaal: max vijf/week → max €1.000/maand bovenop product-revenue.",
        styles))

    story.extend(H3("8.2 Implementation services — €2-15k/project", styles))
    story.append(P(
        "'Ik heb het handboek gelezen, kan jij dit systeem voor ons "
        "bouwen?' Vraag: 6-12 willen dit per jaar. Schaal: max 4-6 "
        "projecten/jaar simultaan.", styles))

    story.extend(H3("8.3 Custom training voor bedrijven — €5-15k/dag", styles))
    story.append(P(
        "Inhouse-workshop bij hun engineering-team. Aangepaste content voor "
        "hun stack. 1-2 dagen on-site of remote. Schaal: 6-10/jaar.", styles))

    story.extend(H3("8.4 Speaking / consultancy — €2-5k/talk", styles))
    story.append(Bullets([
        "Conferentie-talks",
        "Lunch-and-learns bij bedrijven",
        "'Ik kan over X spreken voor jullie team'",
    ], styles))
    story.append(Callout(
        "Het handboek wordt het lead-gen-instrument voor €50-150k aan "
        "diensten/jaar. Dit is waar de échte hefboom zit.", styles))

    story.append(PageBreak())

    # ---- APP-ENGINEERING ----
    story.extend(H1("App-engineering upgrades (parallel)", styles))
    story.append(Paragraph("80-120u &nbsp;·&nbsp; los van content-werk",
                           styles["eyebrow"]))
    story.append(P(
        "Tech-upgrades die dit van 'een React app' naar 'een leerplatform' "
        "tillen.", styles))

    story.extend(H3("A1. Migreer naar MDX-driven content — 30u", styles))
    story.append(P(
        "Vervang App.jsx (15.000 regels code+content) door content/01-"
        "fundamentals.mdx (puur content + JSX-componenten); App.jsx doet "
        "alleen routing + auth + interactiviteit. Content-editing wordt 5× "
        "sneller, anderen kunnen contributen.", styles))

    story.extend(H3("A2. Per-module routing met SEO — 15u", styles))
    story.append(P(
        "Elk module krijgt eigen URL: /m/rag i.p.v. hash. Aparte meta-tags. "
        "Sitemap. SEO-traffic potentieel: 1.000-5.000 NL-bezoekers/maand "
        "op long-tail queries binnen 12 maanden.", styles))

    story.extend(H3("A3. Algolia of Meilisearch full-text search — 10u",
                    styles))
    story.append(P(
        "Niet alleen titels — door ALLE body-content. Algolia €50/maand of "
        "Meilisearch self-host gratis.", styles))

    story.extend(H3("A4. Echte database backend (Supabase) — 20u", styles))
    story.append(Bullets([
        "User accounts (optioneel naast lifetime-key)",
        "Cross-device sync van progress",
        "Anonymous analytics: welke modules worden gelezen, waar haken "
        "mensen af",
        "Foundation voor community-features",
    ], styles))

    story.extend(H3("A5. Mermaid + Excalidraw embeds — 15u", styles))
    story.append(P(
        "Vervang ASCII-art schema's door echte interactieve diagrammen. "
        "Mermaid voor flowcharts, Excalidraw voor concept-tekeningen.",
        styles))

    story.extend(H3("A6. Spaced repetition voor quizzen — 15u", styles))
    story.append(P(
        "Anki-stijl algoritme: vragen die je fout had → vaker terug. "
        "Vragen die je 3× goed had → nog 1× over 30 dagen. Echt leereffect "
        "i.p.v. one-shot quiz.", styles))

    story.extend(H3("A7. Skill-radar / progress-dashboard — 10u", styles))
    story.append(P(
        "Visualiseer per-categorie progress: 'Je bent sterk in Prompting "
        "(87%), zwak in Productie (23%)'. Aanbevelingen.", styles))

    story.extend(H3("A8. Eigen analytics dashboard — 10u", styles))
    story.append(P(
        "Wat lezen mensen het meest? Waar verlaten ze? Wat zijn de FAQ's? "
        "Plausible Analytics is gratis-tier voldoende.", styles))

    story.append(PageBreak())

    # ---- ROADMAP-SAMENVATTING ----
    story.extend(H1("Roadmap-samenvatting", styles))
    story.append(P(
        "Tijdsinvestering en prijs-impact per niveau, cumulatief.", styles))
    story.append(Spacer(1, 0.2 * cm))

    story.append(DATA_TABLE(
        ["Niveau", "Tijd", "Uren", "Prijs-ceiling", "Sterkte-as"],
        [
            ["0 (huidig)", "—", "—", "€69-89", "Breedte + interactiviteit"],
            ["1 — Editorial polish", "2 wk", "60u", "€99", "Vertrouwen"],
            ["2 — Werkende repo", "4 wk", "130u", "€129", "Doe-vermogen"],
            ["3 — Capstone", "2 wk", "80u", "€169", "Tastbaar resultaat"],
            ["4 — Authority", "8 wk", "140u", "€229", "Doorleefdheid"],
            ["5 — Video", "6 wk", "120u", "€299", "Premium-perceptie"],
            ["6 — Community/cohort", "6 wk + lopend", "80u + lopend",
             "€299-499", "Live element"],
            ["7 — Verticals", "3-6 mnd/stuk", "200u/stuk",
             "€169-499 add-on", "Domein-diepte"],
            ["8 — Services", "Lopend", "Variabel", "€2-15k/project", "ARPU"],
        ], styles,
        col_widths=[3.8 * cm, 2.2 * cm, 2.5 * cm, 3.2 * cm, 4.3 * cm]
    ))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Callout(
        "<b>Cumulatief:</b> ~600-800 uur werk verdeeld over 6-12 maanden "
        "voor 'volwaardig premium-product met community + verticals + "
        "services'. Solo doable, ambitieus.", styles))

    story.append(PageBreak())

    # ---- AANBEVOLEN VOLGORDE ----
    story.extend(H1("Aanbevolen volgorde van impact-per-uur", styles))
    story.append(P(
        "Als je niet alles tegelijk doet, hier de optimale ROI-volgorde:",
        styles))
    story.append(Spacer(1, 0.1 * cm))

    story.append(DATA_TABLE(
        ["#", "Stap", "Uren", "Effect"],
        [
            ["1", "Auteur-pagina + 5 testimonials", "14u",
             "Biggest psychological lift"],
            ["2", "Capstone-project + scaffold + rubric + voorbeelden",
             "80u", "Tastbaarste meerwaarde"],
            ["3", "Werkende GitHub-repo voor 8 priority modules", "80u",
             "Verandert lezen → doen"],
            ["4", "5 case studies via interviews", "30u",
             "Bouwt netwerk + content"],
            ["5", "Auteur-opinie + thesis per module", "30u",
             "Verandert toon"],
            ["6", "Citaties op alle claims + per-module changelog", "20u",
             "Verhoogt geloofwaardigheid"],
            ["7", "Studio-video voor top-5 modules", "50u",
             "Premium-perceptie"],
            ["8", "Discord + maandelijkse office hours", "10u + lopend",
             "Community"],
            ["9", "Eerste cohort als pilot", "30u + 30u live",
             "Test of het werkt"],
            ["10", "Eerste vertical-pack", "200u",
             "Eerste echte ARPU-opwaartse beweging"],
        ], styles,
        col_widths=[1 * cm, 6.5 * cm, 2.8 * cm, 5.7 * cm]
    ))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Callout(
        "<b>De eerste 200 uur tilt het van €69 naar €169.</b> Daarna nemen "
        "marginale uren af in ROI tot je community + verticals erbij doet.",
        styles))

    story.append(PageBreak())

    # ---- SLOTVRAAG ----
    story.extend(H1("Strategische slotvraag", styles))
    story.append(P(
        "<b>Voordat je investeert: wil je dit echt?</b>", styles))
    story.append(P(
        "Een €69 handboek launchen en goedkoop houden levert ~€20-35k "
        "revenue + lijst van 500 mensen. Dat is een 1-2 maand investering "
        "met 12-maand opbrengst.", styles))
    story.append(P(
        "Een premium-product op €299 met community + verticals + services "
        "tilt naar €100-300k in jaar 2-3 maar vraagt 6-12 maanden volledige "
        "toewijding en je gezicht eraan te koppelen.", styles))
    story.append(P(
        "<b>De middenweg werkt zelden.</b> Half-investeren betekent dat je "
        "de prijs niet rechtvaardigt en de schaal niet bereikt.", styles))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Callout(
        "<b>Mijn advies:</b> doe niveau 1-3 in 6-8 weken (260 uur), launch "
        "op €119, valideer of er publiek is, en ga pas naar niveau 4-7 als "
        "de eerste 100 sales bewijzen dat de markt jouw versie wil. Als de "
        "eerste 100 sales nooit komen, weet je dat door op €119 te crashen "
        "— niet door op €299 te lanceren.", styles))

    story.append(Spacer(1, 1.5 * cm))
    story.append(HRFlowable(width="30%", thickness=2, color=ORANGE))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Claude Engineering Handboek &nbsp;·&nbsp; Upgrade-Roadmap "
        "v1.0 &nbsp;·&nbsp; mei 2026",
        styles["cover_meta"]))

    return story


def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Claude Engineering Handboek — Upgrade Roadmap",
        author="Claude Engineering Handboek",
        subject="Strategisch upgrade-plan",
    )
    styles = make_styles()
    story = build_story(styles)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF written to {OUT}")


if __name__ == "__main__":
    main()
