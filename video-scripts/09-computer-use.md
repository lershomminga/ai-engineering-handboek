# 09 — Computer Use · richtduur 15-25 min

De demo verkoopt zichzelf — als je een werkende sandbox hebt, laat die zien.
Heb je 'm niet draaiend, leun dan zwaarder op de code-walkthrough + Anthropic's
eigen demo-opname.

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Dit is de feature waar mensen 'wacht, wát?' bij zeggen. Claude bestuurt
> een echte computer — muis, toetsenbord, screenshots. Ik laat zien hoe het werkt,
> hoe je het veilig insluit, en wanneer je het wél en niet moet gebruiken."
>
> *Toon:* de ComputerUse-module.

## 📋 LEERDOELEN
De drie tools, de harness-loop, sandbox-security, en de eerlijke afweging vs
klassieke automation.

## 🎬 BEATS

**Beat 1 — De drie tools (0:30-3:00)**
- *Zeg:* computer (muis/toetsenbord/screenshot), bash, text_editor.
- *Toon:* de drie-tools-sectie.

**Beat 2 — De harness-loop (3:00-10:00)**
- *Zeg:* "Anthropic bewaart geen state. Jij stuurt screenshots, jij regelt
  error-recovery."
- *Toon:* de `ComputerUseAgent`-class in de module (de ~90-regel harness). Loop
  door: action-timeout, screenshot-after-elke-action, trajectory-logging, de
  `max_actions`-cap.
- *Bonus (als je een sandbox draaiend hebt):* laat Claude live een browser openen
  en een simpele taak doen. Dit is je "wow"-moment — neem er de tijd voor.

**Beat 3 — Sandbox-security (10:00-15:00)**
- *Zeg:* "Dit draait in een container die JÍJ host. Hardening is geen optie."
- *Toon:* de Docker-compose met `--cap-drop=ALL`, read-only fs, squid-proxy
  egress-allowlist. De screenshot-diff voor "ging de actie door?".
- *⚠ Noem:* "Geen credentials in screenshots. Allowlist apps. Human-approval bij
  irreversibele acties. En DOM-content is untrusted — spotlighting toepassen."

**Beat 4 — Wanneer wel/niet (15:00-19:00)**
- *Zeg:* eerlijk. "Begin met Playwright. Computer Use pas als je script >20% faalt
  of je elke 2 weken selectoren moet updaten. Niet voor CAPTCHA's, niet voor
  high-frequency, niet voor pixel-perfect."
- *Toon:* de use-cases-die-werken vs -tegenvallen + de vuistregel-callout.

## 🔁 RECAP + CTA (19:00-20:00)
> *Zeg:* "Laatste video van de serie: we brengen alles samen in een capstone —
> een productie customer-support-agent."
