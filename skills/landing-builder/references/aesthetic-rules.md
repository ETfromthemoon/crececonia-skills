# Aesthetic Rules — Landing Builder

Reglas de dirección visual para landings de alta conversión. Combina los principios anti "AI slop" con la identidad Crececonia (refined, premium, editorial).

**Invocar también**: `anthropic-skills:premium-taste-frontend-global` para detalle adicional sobre arquitectura de componentes y CSS hardware acceleration.

---

## 1. Elegir UNA dirección estética (no neutral)

Antes de tocar código, comprometerse a una dirección. **Bold maximalismo y minimalismo refinado funcionan. Lo intermedio no.**

**Direcciones válidas**:

| Estilo | Cuándo usar | Ejemplos |
|---|---|---|
| **Editorial / Magazine** | B2B premium, consultoría, servicios profesionales | crececonia.cl, Stripe, Linear |
| **Brutalista / Raw** | Tech, SaaS edgy, audiencias jóvenes | Are.na, Vercel (versión 2020) |
| **Luxury / Refined** | High-ticket, coaching, exclusividad | Apple, Tesla |
| **Playful / Toy-like** | Productos para creativos, edu-tech | Notion, Loom |
| **Industrial / Utilitarian** | DevOps, infra, B2B técnico | Datadog, Render |
| **Organic / Natural** | Wellness, sostenibilidad, lifestyle | Allbirds, Patagonia |
| **Retro-futuristic** | Cripto, web3, gaming, niche tech | Linear (2024), Vercel |
| **Soft / Pastel** | Femenino, lifestyle, healthcare | Headspace, Calm |

**Default Crececonia**: Editorial + acentos luxury (champagne sobre obsidian).

**Nunca**:
- Estilo "ni fu ni fa" (purple SaaS gradient sobre white)
- Mezclar 3 estilos
- Copiar pixel-perfect a un competidor

---

## 2. Tipografía distintiva

**NUNCA usar**:
- Inter
- Roboto  
- Arial
- system-ui / -apple-system como font de display
- Open Sans
- Lato

**Fuentes recomendadas** (par display + body):

### Editorial / Premium
- Display: **Fraunces** (serif moderno, con variaciones) — *lo que usa crececonia.cl*
- Body: **Inter** OK para body si display es bold
- Mono: **JetBrains Mono** o **IBM Plex Mono**

### Brutalista / Raw
- Display: **Space Grotesk** o **Migra** o **PP Editorial New**
- Body: **Söhne** (paid) o **Inter Tight**
- Mono: **JetBrains Mono**

### Luxury
- Display: **Playfair Display** o **Cormorant Garamond**
- Body: **Lato** o **Crimson Text**
- Mono: ninguna o **Source Code Pro**

### Tech / Industrial
- Display: **IBM Plex Sans** o **Geist**
- Body: **Geist** o **GeneralSans**
- Mono: **JetBrains Mono** o **Fira Code**

### Playful
- Display: **DM Serif Display** + **Quincy CF**
- Body: **DM Sans** o **Nunito**

**Reglas**:
- 2 fuentes max (display + body, mono opcional)
- Display debe tener personalidad
- Body debe ser legible
- Cargar via next/font para optimizar

---

## 3. Paleta de color (dominante + acento)

**Estructura**:
- 1 color DOMINANTE de fondo (ocupa 60-70% del espacio)
- 1 color de TEXTO contrastante (>4.5:1 ratio)
- 1 color de ACENTO (max 10% del espacio, para CTAs y highlights)
- 1-2 tonos neutros (smoke, ash, graphite)

**Paletas validadas**:

### Crececonia (editorial dark)
```
--obsidian:    #0A0A0B  (fondo principal)
--graphite:    #1E1E1F  (cards)
--carbon:      #0F0F10  (cards alt)
--champagne:   #D9B36A  (acento)
--bone:        #F5F5F4  (texto primario)
--ash:         #A8A29E  (texto secundario)
--smoke:       #8C8C8C  (texto terciario)
```

### Tech minimalist (Linear-style)
```
--bg:          #08080F
--fg-primary:  #FFFFFF
--fg-muted:    #A0A0AB
--accent:      #5E6AD2  (indigo solo en CTAs)
--card:        #16161D
```

### Luxury warm
```
--bg:          #FAF7F2  (off-white)
--fg-primary:  #1A1A1A
--accent:      #C9A86A  (gold)
--card:        #FFFFFF
--muted:       #6B6354
```

### Brutalist contrast
```
--bg:          #FAFAFA
--fg:          #000000
--accent:      #FF4500  (orange-red bold)
--card:        #FFFFFF (con border negro thick)
```

**Anti-paletas (NO usar)**:
- Purple gradient on white (típico AI slop)
- Pastel everything
- 5+ colores compitiendo
- Neón sobre fondo claro

---

## 4. Motion intencional, no decorativo

**Sí**:
- Page load orquestado: hero stagger reveal (delay 0.08s, 0.16s, 0.24s, 0.34s)
- Hover sutil en CTAs: scale 1.03 + glow
- Scroll-triggered fade-up en sections (threshold 0.2)
- Backdrop blur en navbar al scroll
- Orb animations en background (slow, opacity baja)

**No**:
- Texto que se mueve en bucle infinito
- Marquees gigantes sin propósito
- Hover states que distraen del CTA
- Animaciones >800ms en interacciones
- Parallax pesado en mobile

**Implementación recomendada**:
- React: **framer-motion** (lo que usa crececonia.cl)
- CSS puro: keyframes con animation-fill-mode
- GSAP solo si necesitas timeline complejo

---

## 5. Layout: composición no genérica

**Sí**:
- Grid asimétrico cuando hace sentido (hero con texto offset)
- Generous negative space en sections de transición
- Densidad controlada en cards de info (no apilar todo al centro)
- Mix de full-width + max-w-Xxl según contenido

**No**:
- Todo centrado vertical y horizontal
- Padding uniforme en todas las sections
- Grids 3x3 simétricos por default
- "Bento boxes" para contenido que no lo necesita

---

## 6. Backgrounds con atmósfera

**Capas recomendadas** (combinar 2-3):
1. **Dot pattern** (overlay sutil, opacity 0.4-0.6)
2. **Orbe(s)** radial-gradient con blur 60-80px
3. **Noise texture** (opcional, sutiliza solid colors)
4. **Animated paths** (opcional, SVG paths con stroke-dashoffset)

**Anti-patrones**:
- Foto stock genérica de fondo
- Gradiente simple sin texture
- Solid color sin atmósfera (a menos que sea brutalist)

**Ejemplo Crececonia (Hero)**:
```jsx
<div className="absolute inset-0">
  <BackgroundPaths />                              {/* animated SVG */}
  <div className="absolute inset-0 dot-pattern opacity-60" />
  <div className="orb-animate" style={{ /* champagne orb */ }} />
  <div className="orb" style={{ /* secondary orb */ }} />
</div>
```

---

## 7. Detalles de polish (no skipear)

- **Sombras**: usar 2 capas (sharp + soft) en cards importantes
- **Bordes**: `1px solid rgba(brand, 0.15)` se ve más premium que `border-gray-200`
- **Border radius**: 2-4px en design editorial/premium, 12-16px en playful
- **Focus visible**: NO removerlo. Diseñarlo en color del acento
- **Transiciones**: 0.2-0.3s ease-out en hovers
- **Sticky bars**: backdrop-blur cuando se vean

---

## 8. Mobile-first sin compromiso

**Reglas**:
- Probar en iPhone SE (375px) ANTES de desktop
- Hero: que el headline + CTA quepan sin scroll en mobile
- Navbar: hamburger menu funcional, no "todo el menú apilado"
- Cards: 1 columna en <640px, 2 en md, 3 en lg
- Touch targets: ≥44×44px (Apple HIG)

---

## Output esperado de Fase 3

Crear `aesthetic.md` en raíz del proyecto:

```markdown
# Aesthetic — [Proyecto]

## Dirección elegida
Editorial premium con acentos luxury (champagne sobre obsidian).

## Fuentes
- Display: Fraunces (Google Fonts) — variable, style italic/normal
- Body: Inter (Google Fonts) — variable
- Mono: JetBrains Mono — variable

## Paleta
```css
--obsidian: #0A0A0B;
--champagne: #D9B36A;
[completar todas las variables]
```

## Motion
- Page load: stagger reveal con framer-motion
- Hover CTAs: scale + glow champagne
- Scroll: fade-up con IntersectionObserver (threshold 0.2)

## Backgrounds
- Dot pattern overlay opacity 0.6
- 3 orbes radial-gradient (top-center champagne, top-right champagne dim, bottom-left subtle green)
- BackgroundPaths animated SVG en Hero
```

Este archivo es la **fuente de verdad visual** del proyecto.
