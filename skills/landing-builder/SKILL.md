---
name: landing-builder
description: >
  Crea landing pages completas listas para deploy en Netlify siguiendo la metodología Crececonia. Orquesta brief estructurado, estrategia de conversión, aesthetic premium (anti AI-slop), copy humanizado en voz Crececonia, build con stack adaptado al proyecto, validación visual con Playwright y handoff con docs. Úsala cuando el usuario pida construir, lanzar o crear una landing page, sitio de captación, pre-launch, página de servicio, página de producto, lead-gen, o página de venta. También cuando diga "armemos una landing", "necesito una página para X", "hagamos un site", "diseña una landing", "lanzar un nuevo producto", "captar leads", o cuando suba un brief de cliente.
---

# Landing Builder — Crece con IA

Skill propia de Crece con IA para crear landing pages **conversion-oriented** de principio a fin: desde el brief con el cliente hasta el deploy en Netlify, pasando por estrategia, aesthetic premium, copy humanizado y validación visual.

No es un generador genérico. Aplica la metodología probada de crececonia.cl (alta conversión B2B LATAM) y **orquesta skills oficiales** en los pasos correctos:

- **Brief estructurado de 8 preguntas** (Fase 1) — el sistema no avanza sin esto
- **Estructura conversion-tested de 9 secciones** (Fase 2) — la fórmula Crececonia
- **Aesthetic premium** (Fase 3) — invoca `anthropic-skills:premium-taste-frontend-global` para anti AI-slop
- **Copy humanizado** (Fase 4) — invoca `humanizer` (los 24 patrones) sobre cada sección
- **Build con UI/UX expert** (Fase 5) — invoca `ui-ux-pro-max:ui-ux-pro-max` cuando hace falta UI compleja
- **Validación visual** (Fase 6) — invoca `gstack` para QA en browser
- **Deploy a Netlify** preconfigurado (Fase 8), salvo que el cliente pida otro server

---

## Cuándo usar esta skill

Activala cuando el usuario quiera **crear desde cero** una landing page. No la uses para:
- Editar componentes sueltos de un sitio existente → usa `frontend-design` directo
- Hacer audit de una landing ya construida → usa `ads-landing`
- Generar copy aislado sin código → usa `humanizer` directo

Activala cuando el usuario diga (en cualquier idioma):
- "Construyamos / armemos / lancemos una landing para X"
- "Necesito un sitio de captación para mi producto / servicio / evento"
- "Pre-launch / coming soon / waitlist"
- "Página de venta / página de servicio / lead-gen"
- "Voy a lanzar [producto/servicio]"
- "Diseña y código una landing"
- "Migrar landing actual a una nueva versión"

---

## El proceso de 8 fases

El usuario no salta fases. Cada fase es un commit lógico de avance.

```
1. BRIEF       → 8 preguntas obligatorias (no se construye sin esto)
2. ESTRATEGIA  → mapa de conversión + headline angle + CTA principal
3. AESTHETIC   → dirección visual bold + paleta + tipografía + motion
4. COPY        → texto de cada sección, pasado por humanizer
5. BUILD       → código con stack adecuado al proyecto
6. REVIEW      → Playwright self-review + ajustes visuales
7. POLISH      → micro-detalles + accesibilidad + SEO + analytics
8. ENTREGA     → README + checklist deploy Netlify
```

Cada fase está documentada en `references/`. Lee cada archivo según la fase activa, no todos de una.

---

## Fase 1 — Brief (obligatorio)

Antes de tocar código, exige las **8 preguntas del brief**.

Lee `references/brief-template.md` para el formulario completo.

**No avanzar a Fase 2 sin tener respuestas concretas a las 8.** Si el usuario es vago en alguna, repregunta con ejemplos.

**Output de Fase 1**: archivo `brief.md` en la raíz del proyecto con las 8 respuestas.

---

## Fase 2 — Estrategia de conversión

Con el brief en mano, define:

1. **Angle del headline** (3 variantes con framework: dolor / promesa / objeción)
2. **CTA principal** (1 sola acción primaria — lead form, demo, compra)
3. **Prueba social que va arriba del fold** (logos / número / testimonial corto)
4. **Hook de cada sección** (qué pregunta del lector responde cada bloque)

Lee `references/structure-crececonia.md` para entender cómo se conectan las 9 secciones en el flujo de conversión.

**Output de Fase 2**: sección "Estrategia" en `brief.md` (no archivo nuevo).

---

## Fase 3 — Aesthetic direction

Aplica los principios de `references/aesthetic-rules.md` (versión Crececonia del taste rules):

- **Elegir 1 dirección estética bold** (no neutral): brutalista / editorial / luxury / playful / etc.
- **Fuentes distintivas** (NO Inter, NO Roboto, NO system-ui)
- **Paleta con dominante + acento** (no paletas equilibradas tipo AI)
- **Motion con propósito** (page load orquestado, no micro-interacciones random)
- **Layout con asimetría o densidad controlada** (no grids genéricos)

**Output de Fase 3**: archivo `aesthetic.md` con: dirección + paleta hex + fuentes (con link) + sample CSS variables.

---

## Fase 4 — Copy

Genera el copy de cada una de las 9 secciones (ver Fase 5 estructura), aplicando los **24 patrones del humanizer** en `references/humanizer-patterns.md`.

**Reglas no negociables del copy Crece con IA:**

1. Tono directo, sin "revoluciona", "potencia", "transforma", "game-changer"
2. Datos concretos (números, %, USD, plazos), no generalidades
3. Voz activa, primera persona del consultor cuando aplique
4. Ejemplos LATAM (Chile/México/Argentina/Colombia/Perú) cuando se den
5. Honestidad sobre limitaciones (si no es para todos, decirlo)
6. CTAs en infinitivo o imperativo: "Recibir evaluación", "Empezar auditoría" (no "Postular a", no "Enviar")

**Output de Fase 4**: archivo `copy.md` con el texto de cada sección listo para inyectar.

---

## Fase 5 — Build

Stack:
- **Default**: Next.js 15+ App Router + Tailwind 4 + shadcn/ui (lo que usa crececonia.cl)
- **Si cliente prefiere otro**: Astro / Vue / Svelte / HTML estático → adaptar
- **Components library**: `references/component-library.md` para decidir Magic UI vs shadcn vs custom

**Estructura del proyecto**:
```
mi-landing/
├── app/
│   ├── layout.tsx          ← metadata + fonts + analytics
│   ├── page.tsx            ← compone las 9 sections en orden
│   └── globals.css         ← tailwind + CSS vars de aesthetic
├── components/
│   ├── Hero.tsx
│   ├── Problema.tsx
│   ├── CasoDeUso.tsx
│   ├── ComoFunciona.tsx
│   ├── Resultados.tsx
│   ├── Servicios.tsx
│   ├── Garantia.tsx
│   ├── FAQ.tsx
│   ├── CTAFinal.tsx
│   ├── Navbar.tsx
│   └── Footer.tsx
├── public/
├── netlify.toml            ← preconfigurado
├── package.json
├── tailwind.config.ts
├── next.config.ts
├── README.md               ← docs para handoff
├── brief.md                ← el de Fase 1
├── aesthetic.md            ← el de Fase 3
└── copy.md                 ← el de Fase 4
```

**Reglas obligatorias del build**:

1. Cada sección es 1 componente React (server component salvo que necesite state)
2. `globals.css` con CSS variables definidas en aesthetic.md
3. `metadata` en layout.tsx con title, description, OG image, canonical
4. Form de captación: POST a endpoint del CRM del cliente (o autodrive.cl/api/aplicar para Crece con IA)
5. Modal de captación opcional (estilo `EvaluacionModal` de crececonia.cl si aplica AI evaluator)
6. Mobile-first responsive
7. Accesibilidad WCAG AA: contraste, aria-labels, focus visible

---

## Fase 6 — Review visual con Playwright

Después del primer build funcional:

```bash
npm run dev
playwright open http://localhost:3000
```

Captura screenshot de cada sección en desktop + mobile. Identificar:
- Espaciado inconsistente
- Tipografía no escala bien
- Contraste insuficiente
- Layout roto en mobile
- Animaciones que distraen

**Output de Fase 6**: screenshots en `_review/` + lista de tweaks a aplicar.

Iterar hasta que se vea pulida.

---

## Fase 7 — Polish final

Antes del handoff, validar:

- [ ] **SEO**: title, description, OG image, canonical, sitemap.xml, robots.txt
- [ ] **Analytics**: Google Analytics 4 o Plausible configurado
- [ ] **Forms**: CTA principal envía a destino correcto (CRM / Resend / Netlify Forms)
- [ ] **Performance**: Lighthouse score >85 (Performance, Accessibility, Best Practices, SEO)
- [ ] **Mobile**: testeado en iPhone SE (375px) y Galaxy S20 (360px)
- [ ] **Open Graph**: imagen 1200×630 con título legible
- [ ] **Favicon**: 32×32 + apple-touch-icon
- [ ] **404**: página de error custom

---

## Fase 8 — Handoff y deploy

Lee `references/deploy-netlify.md` para el checklist completo.

**El proyecto entregado incluye**:

1. **README.md** con:
   - Stack usado
   - Cómo correr local (`npm install && npm run dev`)
   - Cómo deployar (con o sin CLI Netlify)
   - DNS records necesarios
   - Variables de entorno

2. **netlify.toml** preconfigurado con:
   - Build command
   - Publish directory
   - Plugin `@netlify/plugin-nextjs` (si es Next.js)
   - Redirects necesarios
   - Headers de seguridad

3. **Checklist post-deploy**:
   - [ ] Dominio conectado
   - [ ] HTTPS forzado
   - [ ] DNS records (SPF/DKIM/DMARC si hay email)
   - [ ] Analytics verificado (eventos llegan)
   - [ ] Form testeado en producción
   - [ ] Lighthouse >85 en producción
   - [ ] OG image se renderiza bien en debugger.facebook.com

---

## Outputs finales

Al terminar las 8 fases, el usuario tiene:

1. **Proyecto Next.js (o el stack elegido)** listo para `git init && git push` o `netlify deploy`
2. **brief.md** con la estrategia documentada
3. **aesthetic.md** con la dirección visual
4. **copy.md** con todos los textos
5. **README.md** con docs de operación
6. **netlify.toml** preconfigurado
7. **Screenshots Playwright** de validación visual

---

## Ejemplo de invocación

```
Usuario: "Necesito una landing para mi nuevo programa de coaching empresarial. 6 meses, 8 sesiones, USD 4.500."

Skill landing-builder:
  Fase 1 — Brief
  Te hago 8 preguntas antes de empezar. ¿Listo?

  1. ¿Cuál es el nombre del programa y a qué se dedica tu empresa?
  2. ¿Quién es el cliente ideal? (sector, tamaño empresa, rol)
  3. ¿Cuál es el dolor principal que resuelves?
  ...
```

Sin las 8 respuestas, no avanza.

---

## Anti-patrones que NUNCA debes hacer

1. **NO** empezar a codear sin el brief completo
2. **NO** usar paleta morada/azul tipo SaaS genérico (purple-on-white gradient)
3. **NO** usar Inter, Roboto, system-ui como font de display
4. **NO** poner CTAs vagos ("Empieza ahora", "Aprende más")
5. **NO** poner stats inventados — solo lo que el cliente confirme
6. **NO** prometer ROI sin que el cliente lo respalde
7. **NO** olvidar mobile (test obligatorio antes de handoff)
8. **NO** deployar sin checklist completo
