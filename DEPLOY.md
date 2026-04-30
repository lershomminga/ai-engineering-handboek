# Hosting opzetten — gratis URL voor jezelf en je vriend

Dit handboek is een statische single-page app, dus hosten kost niks.
Hieronder de drie snelste opties.

## Snelste route (60 seconden, geen account)

```bash
npm run build
```

Dat maakt een `dist/` map. Sleep die map naar:
**https://app.netlify.com/drop**

Je krijgt direct een publieke URL als
`https://tender-bunny-x9k2.netlify.app`. Klaar. Stuur die naar je vriend.

Nadeel: bij elke wijziging moet je opnieuw slepen.

## Beste route voor doorgaan: Vercel + GitHub (5 minuten setup, daarna auto)

### 1. Maak een GitHub repo

```bash
cd C:\Users\lars\ai-engineering
git init
git add .
git commit -m "Initial commit: Claude Engineering Handboek"

# Maak online een lege repo op github.com/new
# Daarna:
git remote add origin https://github.com/JOUW-NAAM/ai-engineering.git
git branch -M main
git push -u origin main
```

### 2. Verbind Vercel met GitHub

1. Ga naar https://vercel.com/new
2. Login met GitHub
3. Selecteer de repo `ai-engineering`
4. Vercel detecteert Vite automatisch — laat de defaults staan
5. Klik **Deploy**

Binnen ~1 minuut staat het op `https://jouw-app.vercel.app`. Daarna:

- Elke `git push` deployt automatisch een nieuwe versie
- Pull requests krijgen elk een eigen preview-URL

### 3. (Optioneel) Eigen domein

Vercel dashboard → Project → Settings → Domains → Add. Volg de DNS-instructies.

## Alternatief: Cloudflare Pages

Net als Vercel maar met onbeperkte bandbreedte gratis.

1. https://dash.cloudflare.com/?to=/:account/pages
2. Connect GitHub → kies repo
3. Build command: `npm run build`
4. Output directory: `dist`
5. Deploy

## Lokaal testen voor je deployt

```bash
npm run build
npm run preview
# Open http://localhost:4173
```

## Wat zit er al voor je klaar?

- `vercel.json` — SPA-rewrites zodat directe URL's werken
- `netlify.toml` — zelfde voor Netlify
- Vite config — production-ready

## Privacy-check

- Het handboek bevat **geen** API keys
- Het roept geen externe API's aan
- Voortgang wordt in de browser opgeslagen (localStorage)
- Je vriend en jij hebben aparte voortgang
- Volledig veilig om publiek te delen
