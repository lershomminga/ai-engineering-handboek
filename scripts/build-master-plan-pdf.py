"""
Genereer Master-Expansion-Plan.pdf — geconsolideerd 8-cluster deep-audit rapport.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable, ListFlowable, ListItem,
)

# Brand colors
ORANGE = HexColor("#EA580C")
ORANGE_SOFT = HexColor("#FED7AA")
INK = HexColor("#1C1917")
MUTED = HexColor("#57534E")
SUBTLE = HexColor("#A8A29E")
RULE = HexColor("#D6D3D1")
RED = HexColor("#DC2626")
AMBER = HexColor("#D97706")
GREEN = HexColor("#16A34A")

OUT = "C:/Users/lars/ai-engineering/Master-Expansion-Plan.pdf"


def make_styles():
    s = getSampleStyleSheet()
    return {
        "cover_eyebrow": ParagraphStyle("ce", parent=s["Normal"], fontName="Helvetica-Bold",
                                         fontSize=9, textColor=ORANGE, leading=12, spaceAfter=10),
        "cover_title": ParagraphStyle("ct", parent=s["Title"], fontName="Helvetica-Bold",
                                       fontSize=38, textColor=INK, leading=42, spaceAfter=14, alignment=TA_LEFT),
        "cover_sub": ParagraphStyle("cs", parent=s["Normal"], fontName="Helvetica",
                                     fontSize=13, textColor=MUTED, leading=19, spaceAfter=24),
        "cover_meta": ParagraphStyle("cm", parent=s["Normal"], fontName="Helvetica",
                                      fontSize=9, textColor=SUBTLE, leading=14),
        "h1": ParagraphStyle("h1", parent=s["Heading1"], fontName="Helvetica-Bold",
                              fontSize=20, textColor=INK, spaceBefore=14, spaceAfter=8, leading=24),
        "h2": ParagraphStyle("h2", parent=s["Heading2"], fontName="Helvetica-Bold",
                              fontSize=14, textColor=INK, spaceBefore=12, spaceAfter=6, leading=18),
        "h3": ParagraphStyle("h3", parent=s["Heading3"], fontName="Helvetica-Bold",
                              fontSize=11, textColor=ORANGE, spaceBefore=10, spaceAfter=3, leading=14),
        "eyebrow": ParagraphStyle("ey", parent=s["Normal"], fontName="Helvetica-Bold",
                                   fontSize=8, textColor=ORANGE, spaceAfter=4, leading=10),
        "body": ParagraphStyle("body", parent=s["Normal"], fontName="Helvetica",
                                fontSize=9.5, textColor=INK, leading=14, spaceAfter=7, alignment=TA_JUSTIFY),
        "bullet": ParagraphStyle("bu", parent=s["Normal"], fontName="Helvetica",
                                  fontSize=9.5, textColor=INK, leading=13, spaceAfter=2, leftIndent=10),
        "callout": ParagraphStyle("co", parent=s["Normal"], fontName="Helvetica",
                                   fontSize=9.5, textColor=INK, backColor=ORANGE_SOFT, borderPadding=10,
                                   leading=13, spaceBefore=8, spaceAfter=10),
        "table_head": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5,
                                      textColor=white, leading=11),
        "table_cell": ParagraphStyle("tc", fontName="Helvetica", fontSize=8.5,
                                      textColor=INK, leading=11),
        "table_cell_b": ParagraphStyle("tcb", fontName="Helvetica-Bold", fontSize=8.5,
                                        textColor=INK, leading=11),
    }


def header_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(SUBTLE)
    canvas_obj.drawString(2 * cm, 1.2 * cm,
                          "Claude Engineering Handboek — Master Expansion Plan")
    canvas_obj.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"{doc.page}")
    if doc.page > 1:
        canvas_obj.setStrokeColor(ORANGE)
        canvas_obj.setLineWidth(2)
        canvas_obj.line(2 * cm, A4[1] - 1.2 * cm, 2 * cm + 1.5 * cm, A4[1] - 1.2 * cm)
    canvas_obj.restoreState()


def H1(text, styles):
    return [Paragraph(text, styles["h1"]),
            HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=8)]


def H2(text, styles):
    return [Paragraph(text, styles["h2"])]


def P(text, styles):
    return Paragraph(text, styles["body"])


def Bullets(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(it, styles["bullet"]), leftIndent=12, value="•") for it in items],
        bulletType="bullet", leftIndent=12,
    )


def Callout(text, styles):
    return Paragraph(f"<b>→</b> &nbsp; {text}", styles["callout"])


def DataTable(header, rows, styles, col_widths=None, header_color=ORANGE):
    data = [[Paragraph(h, styles["table_head"]) for h in header]]
    for row in rows:
        cells = []
        for c in row:
            cells.append(Paragraph(str(c), styles["table_cell"]))
        data.append(cells)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), header_color),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, RULE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#FAF6F0")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def cover(styles):
    elems = []
    elems.append(Spacer(1, 3 * cm))
    elems.append(Paragraph("DEEP-AUDIT RAPPORT · MEI 2026", styles["cover_eyebrow"]))
    elems.append(Paragraph("Master<br/>Expansion Plan", styles["cover_title"]))
    elems.append(HRFlowable(width="20%", thickness=3, color=ORANGE, spaceBefore=4, spaceAfter=20))
    elems.append(Paragraph(
        "Line-by-line audit van alle 45 modules door 8 parallelle deep-research agents. "
        "Top-50 geprioriteerde uitbreidingen, 3 fases, ~443 uur totaal werk verdeeld over "
        "Sprint A (bug-fixes), B (dun-modules), C (companion-repo), D (schemas+glossary), "
        "E (premium content).",
        styles["cover_sub"]
    ))
    elems.append(Spacer(1, 0.5 * cm))
    elems.append(Paragraph(
        "<b>Inhoud</b><br/>"
        "1. TL;DR<br/>"
        "2. Cluster-overzicht — diepte per module<br/>"
        "3. Top-15 (fase 1 · ~148u)<br/>"
        "4. Top-15 (fase 2 · ~142u)<br/>"
        "5. Top-20 (fase 3 · ~153u)<br/>"
        "6. Tien diepste gaps — geconsolideerd<br/>"
        "7. Aanbevolen uitvoeringsvolgorde<br/>"
        "8. Verwachte impact op prijs-positie<br/>"
        "9. Slotadvies",
        styles["body"]
    ))
    elems.append(Spacer(1, 3 * cm))
    elems.append(Paragraph(
        "Datum: 2026-05-10 &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; "
        "8 agents · 100+ bronnen · 150+ uitbreidings-items",
        styles["cover_meta"]))
    elems.append(PageBreak())
    return elems


def build_story(styles):
    story = []
    story.extend(cover(styles))

    # ===================== TL;DR =====================
    story.extend(H1("TL;DR", styles))
    story.append(P(
        "Het handboek is in mei 2026 ~15.246 regels over 45 modules. De deep-audit "
        "identificeert drie soorten gaps:", styles))
    story.append(Bullets([
        "<b>Verouderde claims & API-versies</b> — bv. structured outputs gebruikt nog "
        "beta-header <font name='Courier' size='9'>2025-11-13</font> terwijl het GA is, "
        "Anthropic Memory Tool toont oude beta-naam, MCP-cijfers zijn outdated "
        "(770 → echte 9.652-22.775).",
        "<b>Dun-vs-belofte modules</b> — AIUX (91), HostingFree (158), PromptOps (93), "
        "FineTuning (88), Voice (71), Memory (105), Guardrails (104), Observability (105), "
        "Multi-agent (88), ComputerUse (113), AgentSDK (109): elf modules onder 200 regels "
        "die elk een productie-pijler representeren.",
        "<b>Hands-on infrastructure ontbreekt</b> — geen companion-repo, geen runnable Python "
        "end-to-end voorbeelden voor 60% van de modules, geen capstone met scaffold, geen "
        "CI-gating-templates.",
    ], styles))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Callout(
        "<b>Top-50 master-uitbreidingen volgen.</b> Geschat totaal-effort: 300-450 uur "
        "verdeeld over 5 sprints. Sprint A (bug-fixes, 30u) levert direct kwaliteits-lift.",
        styles))

    # ===================== Cluster-overzicht =====================
    story.append(PageBreak())
    story.extend(H1("Cluster-overzicht — diepte per module", styles))
    story.append(P("De kolom 'Diepte' is een 1-liner. Voor exacte H2/H3/code-blok-tellingen: zie "
                   "individuele cluster-rapporten via de agent-IDs achterin.", styles))
    story.append(Spacer(1, 0.2 * cm))

    cluster_data = [
        ["Fundamenten", "", "", ""],
        ["fundamentals", "384", "18", "Diep"],
        ["claude-models", "434", "17", "Diep"],
        ["tokens-context", "359", "16", "Zeer diep"],
        ["api-keys", "222", "9", "Gemiddeld"],
        ["Prompting", "", "", ""],
        ["prompting-basics", "223", "7", "Gemiddeld"],
        ["prompting-advanced", "546", "22", "Zeer diep"],
        ["prompt-patterns", "144", "2", "Dun"],
        ["structured-outputs", "130", "7", "Dun"],
        ["evals", "374", "14", "Diep"],
        ["Agent stack", "", "", ""],
        ["skills", "424", "17", "Diep"],
        ["tools-mcp", "407", "16", "Diep"],
        ["computer-use", "113", "6", "Zeer dun"],
        ["agents", "404", "14", "Diep"],
        ["multi-agent", "88", "5", "Zeer dun"],
        ["agent-sdk", "109", "7", "Dun"],
        ["Retrieval & Voice", "", "", ""],
        ["rag", "613*", "22 (incl. dupes)", "Zeer diep, dupes"],
        ["memory", "105", "8", "Dun"],
        ["voice", "71", "9", "Zeer dun"],
        ["Claude Mastery", "", "", ""],
        ["claude-deep", "155", "7", "Dun"],
        ["claude-code-deep", "619", "12 + 9 H3", "Zeer diep"],
        ["claude-cloud", "363", "13 + 3 H3", "Diep"],
        ["Bouwen", "", "", ""],
        ["workflows", "523", "14", "Sterk"],
        ["automation", "519", "14", "Sterk"],
        ["second-brain", "563", "17", "Zeer sterk"],
        ["frontend", "468", "17", "Sterk"],
        ["ai-ux", "91", "10", "SCHOKKEND dun"],
        ["backend", "615", "19", "Zeer sterk"],
        ["deployment", "476", "22", "Sterk, weinig code"],
        ["hosting-free", "158", "7", "Dun"],
        ["Productie", "", "", ""],
        ["security", "429", "12", "Diep"],
        ["guardrails", "104", "7", "Dun"],
        ["observability", "105", "9", "Dun"],
        ["prompt-ops", "93", "8", "Dun"],
        ["cost-opt", "500", "16", "Diep"],
        ["fine-tuning", "88", "7", "Dun"],
        ["Praktijk & Ref", "", "", ""],
        ["welcome", "116", "—", "Gemiddeld"],
        ["roadmap", "489", "18", "Diep"],
        ["ecosystem", "401", "16", "Diep"],
        ["cases", "416", "9", "Diep"],
        ["workflow-checklist", "526", "6", "Diep"],
        ["exercises", "251", "—", "Gemiddeld"],
        ["schemas", "164", "6", "Gemiddeld"],
        ["glossary", "136 (93 termen)", "1", "Gemiddeld"],
        ["resources", "185", "1", "Gemiddeld"],
    ]
    story.append(DataTable(
        ["Module", "Regels", "H2's", "Diepte"],
        cluster_data, styles,
        col_widths=[5 * cm, 2 * cm, 3 * cm, 6 * cm]
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(P(
        "<b>Patroon:</b> de 'Bouwen'- en 'Productie'-categorieën hebben de scherpste asymmetrie — "
        "sommige modules zijn 500+ regels productie-grade, andere onder de 100. "
        "Eerste werk: gelijktrekken.", styles))

    # ===================== Top-15 fase 1 =====================
    story.append(PageBreak())
    story.extend(H1("Top-15 (fase 1) — Bug-fixes & verouderde claims", styles))
    story.append(Paragraph("Geschat 100-130 uur · doe deze eerst",
                           styles["eyebrow"]))
    story.append(P("Subtotaal fase 1: ~148u (≈4 weken full-time of 6-8 weken parttime). "
                   "Lever direct kwaliteits-lift zonder content-debat.", styles))
    story.append(Spacer(1, 0.2 * cm))

    fase1 = [
        ["1", "structured-outputs", "Update Pattern 2 naar GA-API (output_config.format). Beta-header werkt binnenkort niet meer", "XS · 2u"],
        ["2", "memory", "Update Anthropic Memory Tool (header context-management-2025-06-27, type memory_20250818) + BetaAbstractMemoryTool", "S · 4u"],
        ["3", "ai-ux", "Volledige expansie 2-3× (alle 10 sub-secties uitbreiden met code + screenshots)", "L · 24u"],
        ["4", "computer-use", "End-to-end Python harness (80-100r) + Anthropic Docker reference + sandbox-hardening", "L · 16u"],
        ["5", "rag", "Merge duplicaten (Contextual, GraphRAG, hybrid, RAGAS staan elk 2×) + H3-niveau", "M · 6u"],
        ["6", "claude-code-deep", "Complete Hooks Reference (~27 events tabel + env-vars + matcher-syntax)", "M · 8u"],
        ["7", "claude-code-deep", "Plugin format + marketplace H2 (.claude-plugin/plugin.json, marketplace.json)", "M · 6u"],
        ["8", "glossary", "Uitbreiden naar 200+ termen + niveau-tag + categorie-tag + filter", "M · 10u"],
        ["9", "observability", "Volledige OTEL GenAI span-attributes (30+ attrs) + Langfuse self-host docker-compose v3", "M · 8u"],
        ["10", "agent-sdk", "Fix incorrecte imports + complete API klasse-tabel + TypeScript-naast-Python", "L · 16u"],
        ["11", "schemas", "Mermaid-migratie 6 bestaande + 12 nieuwe schemas (prompt-cache, MCP, memory, multi-agent, RAG, eval CI, cost, security, OTel, error-recovery, compaction, voice)", "L · 20u"],
        ["12", "welcome", "Competentie-matrix klikbaar + persona-decision-tree + leerduur per categorie", "S · 6u"],
        ["13", "multi-agent", "LangGraph state-machine voorbeeld + Framework feature-matrix (CrewAI 31k, AutoGen 42k, LangGraph 12.8k stars)", "M · 10u"],
        ["14", "api-keys", "Admin API key management + Exponential backoff (429 vs 529, equal jitter) + 2026 rate-limits", "M · 6u"],
        ["15", "claude-deep", "Pricing-matrix per product + Decision tree welke laag pak ik", "S · 6u"],
    ]
    story.append(DataTable(
        ["#", "Module", "Uitbreiding", "Effort"],
        fase1, styles,
        col_widths=[1 * cm, 3.5 * cm, 9 * cm, 2.5 * cm], header_color=RED
    ))

    # ===================== Top-15 fase 2 =====================
    story.append(PageBreak())
    story.extend(H1("Top-15 (fase 2) — Diepe content-uitbreiding", styles))
    story.append(Paragraph("Geschat 90-120 uur · na fase 1",
                           styles["eyebrow"]))
    story.append(Spacer(1, 0.2 * cm))

    fase2 = [
        ["16", "agents", "Werkende ReAct-agent (30r, 3 tools) + Reflexion-loop + Debug-toolkit (logs/traces/replay)", "M · 10u"],
        ["17", "rag", "Embedding-selectie-matrix (voyage-3-large, Cohere v4, etc) + Query transformation (HyDE, multi-query, decomposition)", "M · 8u"],
        ["18", "security", "Penetration-testing playbook (Garak + Promptfoo Red Team + PyRIT) + Incident-response", "M · 10u"],
        ["19", "guardrails", "NeMo Guardrails Colang 2.0 policy + Llama Guard 3 8B+1B + Prompt Guard 2 (Python role-split)", "M · 10u"],
        ["20", "prompting-advanced", "CoT vs Adaptive Thinking cost/quality matrix + Self-correction loops code + Few-shot benchmark", "S · 8u"],
        ["21", "structured-outputs", "Streaming partial JSON + oneOf/anyOf workarounds + Refusal-as-field deep-dive", "M · 8u"],
        ["22", "prompt-patterns", "Decision-matrix wanneer-welk + per-pattern anti-example + Pattern-combinaties (4 stacks)", "S · 6u"],
        ["23", "evals", "CI/CD GitHub Actions YAML + Bias-mitigation code + Bootstrap-CI + McNemar Python", "M · 8u"],
        ["24", "tools-mcp", "Tool Search Tool deep dive + SSE-deprecation/Streamable HTTP migratie + OWASP MCP Top 10 + CVE-2025-6514", "M · 10u"],
        ["25", "frontend", "Volledig Next.js 15 + AI SDK 5 example (~80r) + Testing-strategie + CopilotKit/assistant-ui matrix", "M · 10u"],
        ["26", "backend", "FastAPI streaming+auth+rate-limit (~80r) + Multi-tenant key-vault + Temporal + Batch API", "M · 10u"],
        ["27", "cost-opt", "Cost-calculator widget + RouteLLM concrete setup + ICLR-2025 benchmarks + Stacking-strategies", "M · 10u"],
        ["28", "fine-tuning", "QLoRA Unsloth tutorial (Llama 3.1 8B) + Distillation pipeline + Synthetic-data comparison + Golden-ratio", "L · 14u"],
        ["29", "claude-cloud", "Routine cookbook 8 → 15 recepten + Managed Agents intro + Audit-log/Compliance API patterns", "M · 10u"],
        ["30", "roadmap", "Claude Certified Architect-sectie + Quick-start paden + Interview-prep + Portfolio 4 → 10", "M · 10u"],
    ]
    story.append(DataTable(
        ["#", "Module", "Uitbreiding", "Effort"],
        fase2, styles,
        col_widths=[1 * cm, 3.5 * cm, 9 * cm, 2.5 * cm], header_color=AMBER
    ))

    # ===================== Top-20 fase 3 =====================
    story.append(PageBreak())
    story.extend(H1("Top-20 (fase 3) — Premium polish", styles))
    story.append(Paragraph("Geschat 80-110 uur · maakt het echte premium-product",
                           styles["eyebrow"]))
    story.append(Spacer(1, 0.2 * cm))

    fase3 = [
        ["31", "memory", "Concrete code per Tulving-type + Zep/Graphiti H2 + Conflict-resolution + GDPR forget", "M · 10u"],
        ["32", "voice", "Python Vapi codevoorbeeld (40r) + OpenAI Realtime API + actuele prijzen + NL/GDPR compliance", "M · 10u"],
        ["33", "rag", "LazyGraphRAG (jun 2025) + RAG production-ops + RAG CI-pipeline", "M · 8u"],
        ["34", "workflow-checklist", "Interactive checkboxes 72 items + decision-tree + anti-pattern lijst + printable card", "S · 6u"],
        ["35", "cases", "Bouw dit vandaag tutorial per industrie + Compliance-checklist + Failure modes + Mermaid-architecturen", "L · 14u"],
        ["36", "exercises", "5 oefeningen per nieuwe module + Difficulty in uren + Solutions-repo + Capstone 5 varianten", "M · 10u"],
        ["37", "resources", "Anthropic Certificeringen + DeepLearning.AI 2026 updates + NL-bronnen-sectie + Events-kalender", "S · 6u"],
        ["38", "ecosystem", "MCP-cijfers mei 2026 + Per-laag stack-diagram + Vendor-lock-in-matrix + Emerging tools", "S · 6u"],
        ["39", "prompt-ops", "Langfuse Prompt API end-to-end + Braintrust workflow + A/B-test pattern + Rollback strategy", "M · 8u"],
        ["40", "observability", "Trace-link parent/child multi-step + Production sampling impl + Cost-attribution code + Drift-detection", "M · 8u"],
        ["41", "skills", "Schrijf je eerste skill in 15 min + Bad-skill gallery + evals.json schema + grader-prompt", "M · 8u"],
        ["42", "claude-code-deep", "Headless mode + CI patterns + Subagent YAML alle 15 velden + IDE feature-parity + Output styles", "M · 10u"],
        ["43", "deployment", "Per-platform deploy guides (6) + Bedrock vs Vertex vs Foundry matrix + Canary rollout + Migration runbook", "M · 10u"],
        ["44", "automation", "Complete n8n workflow JSON dumps (3 templates) + State-machine + Test-strategieën + Zapier→n8n", "M · 8u"],
        ["45", "second-brain", "n8n workflow JSON downloads + E2EE pattern + Voice-pipeline OpenAI Realtime Whisper", "M · 8u"],
        ["46", "hosting-free", "Stap-voor-stap echte AI-app deploy op free tiers + Limits matrix + Gratis-tot-betaald thresholds", "M · 8u"],
        ["47", "fundamentals", "Sampling onder motorkap (temp/top-p/top-k/min-p) + Hallucinaties + Knowledge cutoff per model", "S · 6u"],
        ["48", "tokens-context", "Automatic caching toggle (feb 2026) + Cache breakpoint 20-block lookback gotcha", "XS · 3u"],
        ["49", "claude-models", "Bedrock vs Vertex vs direct + Model routing code + Adaptive thinking effort-levels", "M · 8u"],
        ["50", "prompting-basics", "Prompt-evolutie v0→v4 + Anti-patterns fix-zij-aan-zij + Per-domein templates", "S · 6u"],
    ]
    story.append(DataTable(
        ["#", "Module", "Uitbreiding", "Effort"],
        fase3, styles,
        col_widths=[1 * cm, 3.5 * cm, 9 * cm, 2.5 * cm], header_color=GREEN
    ))

    # ===================== Tien diepste gaps =====================
    story.append(PageBreak())
    story.extend(H1("Tien diepste gaps — geconsolideerd", styles))
    story.append(P("Over alle 8 cluster-rapporten heen herhalen deze gaps zich:", styles))
    story.append(Bullets([
        "<b>Verouderde API-versies</b> in code-voorbeelden (Structured Outputs, Memory, MCP-cijfers, "
        "Helicone maintenance-mode, prompt cache TTL).",
        "<b>Ontbrekende end-to-end runnable code</b> — meeste modules tonen snippets, geen complete werkende voorbeelden.",
        "<b>Schokkend dunne UI-laag</b> — AIUX is 91 regels voor wat het zichtbare deel van AI-apps is.",
        "<b>Geen companion-repo</b> — alle modules met code zouden naar één GitHub-repo moeten linken voor paste-and-run.",
        "<b>Duplicatie binnen modules</b> — vooral RAG (Contextual Retrieval, GraphRAG, hybrid search elk 2×).",
        "<b>Geen capstone-scaffold</b> — Exercises noemen 'bouw dit', geen rubric, geen voorbeeld, geen review.",
        "<b>Compliance dun voor regulated industries</b> — Healthcare/Finance/Legal-cases zonder NEN 7510, "
        "PCI-DSS, MDR, EU AI Act details (laatste deadline aug 2026!).",
        "<b>Geen production case studies met cijfers</b> — handboek noemt patterns, niet 'bij klant X gingen we van Y naar Z'.",
        "<b>Auteur-identiteit ontbreekt</b> — nergens 'Over de auteur' met production-scars.",
        "<b>Cross-references zijn één-richting</b> — Glossary, Resources, Schemas verwijzen niet terug naar de hoofdmodule.",
    ], styles))

    # ===================== Uitvoeringsvolgorde =====================
    story.append(PageBreak())
    story.extend(H1("Aanbevolen uitvoeringsvolgorde", styles))

    story.extend(H2("Sprint A — Bug-fixes & verouderde claims (1 week, ~30u)", styles))
    story.append(Bullets([
        "#1 structured-outputs GA-API update",
        "#2 memory Anthropic Memory Tool update",
        "#5 rag duplicaten merge",
        "#48 tokens-context automatic caching toggle",
        "#14 api-keys rate-limits 2026 + admin API",
        "#9 observability OTEL reference + Langfuse v3",
        "#38 ecosystem MCP-cijfers + Helicone maintenance-mode",
    ], styles))
    story.append(P("<i>Output: geen verouderde info meer. Onmiddellijke quality-lift "
                   "zonder grote uitbreiding.</i>", styles))

    story.extend(H2("Sprint B — Dun-modules optillen (3-4 weken, ~80-100u)", styles))
    story.append(P("Doel: alle modules ≥ 200 regels brengen.", styles))
    story.append(Bullets([
        "#3 ai-ux (91 → 250) · #4 computer-use (113 → 250)",
        "#10 agent-sdk (109 → 230) · #13 multi-agent (88 → 220)",
        "#19 guardrails (104 → 220) · #28 fine-tuning (88 → 220)",
        "#31 memory (105 → 230) · #32 voice (71 → 230)",
        "#39 prompt-ops (93 → 220) · #46 hosting-free (158 → 230)",
    ], styles))
    story.append(P("<i>Output: geen 'schokkend dunne' modules meer. Productie-pijlers "
                   "krijgen elk hun fair share.</i>", styles))

    story.extend(H2("Sprint C — Companion-repo opzetten (2-3 weken, ~80-100u)", styles))
    story.append(P("Niet in de Top-50 maar essentieel — verandert lezen → doen:", styles))
    story.append(Bullets([
        "Eén GitHub-repo claude-handbook-code met folder per priority-module",
        "Werkende code voor: Fundamentals, Prompting Advanced, Tools&MCP, Agents, RAG, "
        "Evals, Backend, Computer Use, Multi-agent, Voice, Memory",
        "Nightly CI tegen Anthropic API",
        "'Open in repo →' knop in elk Pre-blok in het handboek",
    ], styles))

    story.extend(H2("Sprint D — Schemas & glossary (2 weken, ~30u)", styles))
    story.append(Bullets([
        "#11 schemas Mermaid + 12 nieuwe",
        "#8 glossary 93 → 200+ termen",
        "#12 welcome competentie-matrix + persona-tree",
    ], styles))

    story.extend(H2("Sprint E — Schrijf-intensieve content (4-6 weken, ~100-120u)", styles))
    story.append(P("Resterende top-50 items in dependency-volgorde. Brengt naar volwaardig "
                   "premium-handboek dat €169-199 verdedigt.", styles))

    # ===================== Impact tabel =====================
    story.append(PageBreak())
    story.extend(H1("Verwachte impact op product-positie", styles))

    impact_data = [
        ["A (bug-fixes)", "30", "€79", "Niet verouderd voelen"],
        ["B (dun-optillen)", "130", "€99", "Geen schokkend thin modules"],
        ["C (companion-repo)", "230", "€129", "Runnable code = ik doe, niet ik lees"],
        ["D (schemas + glossary)", "260", "€139", "Referentiewerk-status"],
        ["E (volledige content)", "380", "€169", "Echt premium-niveau"],
        ["Plus: video, community, capstone-review (eerdere roadmap)", "600+", "€299+", "Cohort + live element"],
    ]
    story.append(DataTable(
        ["Sprint", "Cumulatieve uren", "Prijs-ceiling", "Reden"],
        impact_data, styles,
        col_widths=[5.5 * cm, 3 * cm, 3 * cm, 5 * cm]
    ))

    # ===================== Slot =====================
    story.append(PageBreak())
    story.extend(H1("Wat ik aanraad", styles))
    story.append(P(
        "<b>Doe Sprint A meteen</b> — 30 uur werk, geen content-debat, alles \"moet\" gefixt worden. "
        "Levert direct kwaliteits-lift en haalt de pijnlijkste verouderde claims weg.", styles))
    story.append(P(
        "<b>Doe daarna Sprint B + C parallel</b> — als jij content schrijft, kan iemand anders "
        "(of een toekomstige jou-met-tijd) de repo bouwen. Twee weken werk, fundamenteel anders product.",
        styles))
    story.append(P(
        "<b>Sprint D + E</b> kan in 6-12 maanden, naast launch. Zelfs zonder D+E is het product al "
        "verkoopbaar op €119 na Sprint C.", styles))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Callout(
        "<b>Wat ik NIET zou doen:</b> alle 50 items in één keer aanpakken. Het is verleidelijk maar "
        "fragmenteert je aandacht. Sprint A is in de tijd dat je dit rapport leest al uitvoerbaar.",
        styles))

    story.append(Spacer(1, 1 * cm))
    story.append(HRFlowable(width="30%", thickness=2, color=ORANGE))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Master Expansion Plan v1.0 &nbsp;·&nbsp; mei 2026 &nbsp;·&nbsp; "
        "8 deep-research agents · 150+ uitbreidings-items · ~443u Top-50",
        styles["cover_meta"]))

    return story


def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Claude Engineering Handboek — Master Expansion Plan",
        author="Deep-audit · 8 parallelle agents",
        subject="Geconsolideerd uitbreidings-plan v1.0",
    )
    styles = make_styles()
    story = build_story(styles)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF written to {OUT}")


if __name__ == "__main__":
    main()
