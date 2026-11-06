# Deploy a Netlify — Checklist completo

Pasos para deployar la landing a Netlify de forma robusta.

---

## Pre-requisitos antes del deploy

- [ ] Build local pasa sin errores: `npm run build`
- [ ] Lighthouse en local >85 (Performance, Accessibility, Best Practices, SEO)
- [ ] Testeado en mobile (iPhone SE 375px) y desktop (1440px)
- [ ] Form principal probado en dev: el POST llega al destino
- [ ] No hay `console.log` ni `// TODO` en código de producción
- [ ] `.env.local` está en `.gitignore` (no subir secretos)

---

## Estructura mínima para deploy

```
mi-landing/
├── netlify.toml          ← config Netlify
├── package.json
├── next.config.ts        ← (si es Next.js)
├── .gitignore           ← incluye .next/, node_modules/, .env*
└── public/
    ├── favicon.ico
    ├── og-image.png      ← 1200×630 para social previews
    └── robots.txt
```

---

## netlify.toml — Plantilla Next.js

```toml
[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"

# Forzar HTTPS
[[redirects]]
  from = "http://*.netlify.app/*"
  to = "https://:splat"
  status = 301
  force = true
```

---

## netlify.toml — Plantilla Astro

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[plugins]]
  package = "@netlify/plugin-lighthouse"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
```

---

## netlify.toml — HTML estático

```toml
[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
```

---

## 3 maneras de hacer el deploy

### Opción A — Drag-and-drop (más simple)

1. Build local: `npm run build`
2. Abrir https://app.netlify.com
3. Arrastrar la carpeta de output (`.next/` para Next.js, `dist/` para Astro, `.` para HTML) al área de "Deploys"
4. Netlify asigna URL temporal tipo `<random>.netlify.app`
5. En Site settings → Domain management → conectar dominio custom

**Pro**: No requiere git ni CLI.
**Contra**: Manual cada vez.

### Opción B — Netlify CLI

```bash
npm install -g netlify-cli
netlify login
cd mi-landing
netlify init        # crea site y vincula
netlify deploy --prod
```

**Pro**: Comando único.
**Contra**: Setup inicial.

### Opción C — Conectar a GitHub (CI/CD)

1. Push del proyecto a un repo de GitHub
2. En Netlify: "Add new site" → "Import from GitHub"
3. Selecciona el repo
4. Netlify detecta el framework y propone config
5. Click "Deploy"

A partir de ahí, cada `git push main` deploya automáticamente.

**Pro**: Deploys automáticos en cada push.
**Contra**: Requiere repo de GitHub.

---

## Configurar dominio custom

1. En Netlify: Site settings → Domain management
2. Click "Add custom domain"
3. Ingresar `crececonia.cl` (o el dominio del cliente)
4. Netlify ofrece 2 opciones:
   - **Netlify DNS** (recomendado): cambiar nameservers en el registrador
   - **External DNS**: agregar CNAME `www → <site>.netlify.app` y A record para apex

5. Esperar propagación (15 min - 24 hrs)
6. Netlify provisiona SSL Let's Encrypt automático

---

## Variables de entorno

Si la landing usa secrets (API keys, etc.):

1. Site settings → Build & deploy → Environment
2. Add variable:
   - `RESEND_API_KEY` = `re_xxx`
   - `STRIPE_PUBLIC_KEY` = `pk_xxx`
   - etc.

**Para Next.js**:
- Variables con `NEXT_PUBLIC_*` → expuestas al browser
- Resto → solo server-side

---

## DNS records para email (si la landing envía emails)

**SPF** (apex domain):
```
Type: TXT
Name: @
Value: v=spf1 include:_spf.improvmx.com ~all
```

**MX** (recibir email):
```
Type: MX, Priority 10, Value: mx1.improvmx.com
Type: MX, Priority 20, Value: mx2.improvmx.com
```

**DMARC**:
```
Type: TXT
Name: _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:hola@dominio.cl
```

**DKIM** (si usas servicio propio o Resend):
```
Type: TXT
Name: default._domainkey  (o el selector que indique tu provider)
Value: v=DKIM1; k=rsa; p=<clave pública>
```

---

## Checklist post-deploy (verificación en producción)

- [ ] **HTTPS funciona**: `https://dominio.cl` carga con candado verde
- [ ] **Redirect HTTP→HTTPS**: `http://dominio.cl` redirige a HTTPS
- [ ] **www y apex**: ambos cargan el sitio (uno redirige al otro)
- [ ] **Mobile test real**: abrir en celular, todo se ve bien
- [ ] **CTA principal funciona**: submit del form llega al destino esperado
- [ ] **Email de confirmación llega**: si hay welcome email, verificar inbox
- [ ] **Analytics tracking**: eventos llegan a GA4/Plausible
- [ ] **Lighthouse producción**: corro PageSpeed Insights en URL real, >85
- [ ] **OG image renderiza**: usar https://www.opengraph.xyz/ con URL
- [ ] **Sitemap.xml accesible**: `dominio.cl/sitemap.xml` devuelve XML
- [ ] **robots.txt**: `dominio.cl/robots.txt` permite crawling de Google
- [ ] **404 page**: ir a URL inexistente, debe mostrar 404 custom
- [ ] **Google Search Console**: agregado el sitio, sitemap subido

---

## Si algo falla

### Build falla en Netlify pero pasa en local
- Verificar versiones: `node --version` en local vs `NODE_VERSION` en netlify.toml
- Variables de entorno: ¿faltan en Netlify?
- Logs: `Deploys → último deploy → Deploy log`

### Lighthouse Performance bajo (<85)
- Imágenes grandes: optimizar a WebP, lazy load
- Fuentes: usar `next/font` o `display=swap`
- JS bundle grande: revisar componentes que se cargan en SSR pero no se usan

### Forms no funcionan
- Si usás Netlify Forms: agregar `data-netlify="true"` al form
- Si usás endpoint externo (autodrive.cl): verificar CORS
- Test con `curl` directo al endpoint

### Email no llega
- Revisar SPF/DKIM/DMARC en https://mxtoolbox.com
- Verificar que el sender domain coincide con DKIM
- Test con mail-tester.com

---

## Cuándo NO usar Netlify

Considerar **Vercel** si:
- El proyecto usa muchas Server Components y Server Actions de Next.js
- Necesitas Edge Functions especiicas
- El cliente ya tiene workflow con Vercel

Considerar **AWS / Cloudflare Pages** si:
- Es proyecto enterprise con compliance
- Necesitas CDN global propio
- Tráfico muy alto donde Netlify cobra mucho

Considerar **VPS propio** si:
- El cliente quiere control total (compliance, datos sensibles)
- La landing es parte de una app más grande con backend
- Ya tiene infra que no quiere mover
