# Component Library — Decisión de librerías

Qué librería de componentes usar según el contexto del proyecto.

---

## Stack default Crececonia (recomendado para 90% de casos)

**Base**: Next.js 15+ App Router + Tailwind 4 + TypeScript

**Componentes**:
- **shadcn/ui** — base accesible (botones, forms, dialogs, accordions)
- **framer-motion** — animaciones declarativas
- **Lucide icons** — set de íconos consistente
- **next/font** — fuentes optimizadas

**Invocar para componentes complejos**: `claude-web-designer` (setup) o `ui-ux-pro-max:ui-ux-pro-max` (UI patterns)

---

## Cuándo agregar Magic UI

**Usar cuando** la landing necesita componentes animados específicos:
- **Marquee** (logos en loop)
- **Blur-fade** (text reveals)
- **Animated beam** (conexiones entre elementos)
- **Bento grid** (showcase de features visualmente)
- **Number ticker** (stats animadas)
- **Globe** (alcance geográfico)

**Setup**:
```bash
npx claude mcp add magicui --transport sse https://magicui.design/mcp
```

Después en código:
```bash
# Listar componentes disponibles
npx magicui list

# Agregar un componente
npx magicui add marquee
```

---

## Cuándo usar Aceternity UI

**Usar cuando** necesitas componentes "wow" más elaborados (background effects, 3D-feel):
- **Background gradient animation**
- **Spotlight effect**
- **Sparkles**
- **Aurora background**
- **Floating navbar**

**Trade-off**: pesa más, más JS. Bueno para landings con WOW factor pero mide el impact en Lighthouse.

---

## Cuándo usar Tremor

**Usar cuando** la landing tiene **dashboards o demos de producto** (SaaS landings con preview de UI):
- Charts (line, bar, donut, area)
- KPI cards
- Tables stylizadas

No usar para componentes generales (botones, forms).

---

## Cuándo usar custom desde cero

**Hacer custom cuando**:
- La aesthetic es muy específica (brutalist, editorial, luxury)
- El componente no existe en ninguna librería
- Necesitas full control de animaciones

**Componentes que casi siempre son custom en Crececonia**:
- Hero con orbes animados + dot pattern + BackgroundPaths
- Cards de Resultados con progress bars
- StickyBar mobile
- Botones del tipo "btn-evaluacion" (gradient gold + glow on hover)

---

## Lista de check antes de elegir

Antes de meter una nueva librería, preguntar:

1. **¿Lo necesitamos realmente?** Si shadcn + Tailwind alcanza, no agregar más.
2. **¿Cuánto pesa?** Lighthouse Performance objetivo: >85.
3. **¿Es accesible?** WCAG AA es no-negociable.
4. **¿Funciona en mobile?** Test en iPhone SE.
5. **¿Lo entiende el cliente para mantenerlo?** Si solo lo entiendo yo, problema.

---

## Setup commands rápidos

```bash
# Next.js + TypeScript + Tailwind
npx create-next-app@latest mi-landing --typescript --tailwind --app

# shadcn/ui base
npx shadcn@latest init
npx shadcn@latest add button input textarea card dialog accordion

# framer-motion
npm install framer-motion

# Lucide icons
npm install lucide-react

# Magic UI (si aplica)
npx claude mcp add magicui --transport sse https://magicui.design/mcp

# Resend (si hay forms con email)
npm install resend
```

---

## Componentes obligatorios para cualquier landing

Sin importar el stack:

| Componente | Por qué |
|---|---|
| **Navbar** | Sticky, transparent → blurred on scroll |
| **Footer** | Repetir nav + legal + copyright |
| **Hero** | Primer pantallazo |
| **CTAButton** | Botón estilizado del acento (no genérico) |
| **Section wrapper** | Padding consistente, max-width estandar |
| **ScrollReveal** | Wrapper para fade-up con IntersectionObserver |
| **Modal/Dialog** | Para formularios o CTAs sin salir de la página |
| **FAQ Accordion** | Colapsable, accesible (keyboard) |

---

## Decisión rápida según tipo de proyecto

| Tipo | Stack recomendado |
|---|---|
| **SaaS B2B** | Next.js + shadcn + Magic UI (Marquee + Bento) |
| **Coaching / Servicios** | Next.js + shadcn + framer-motion custom |
| **E-commerce mini** | Next.js + Stripe Checkout + Tailwind custom |
| **Pre-launch / Waitlist** | Astro + Tailwind + Resend (minimal, rápido) |
| **Curso / Infoproducto** | Next.js + shadcn + Aceternity (más visual) |
| **Portfolio / Personal** | Astro + custom CSS (creative freedom) |
| **Newsletter / Content** | Next.js + MDX + Resend |
