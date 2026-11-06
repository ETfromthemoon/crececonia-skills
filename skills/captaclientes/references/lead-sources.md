# Fuentes de leads — Recetario de búsqueda

Reglas: cada candidato sale de una **fuente verificable** (URL). Adapta las queries al ICP (industria, cargo, zona). Reemplaza `[INDUSTRIA]`, `[CIUDAD]`, `[CARGO]`, `[PAÍS]` por los valores del brief.

---

## A. Web abierta (ejecutable con WebSearch / WebFetch)

Usa estos operadores de Google en `WebSearch`. Tras encontrar una página candidata, usa `WebFetch` para confirmar datos reales (nombre, contacto, fit).

**Empresas por nicho:**
- `[INDUSTRIA] en [CIUDAD]` — listado base.
- `"[INDUSTRIA]" [CIUDAD] -directorio -wikipedia` — limpiar ruido.
- `[INDUSTRIA] [CIUDAD] site:.[PAÍS]` — acotar país (ej. site:.cl, site:.mx).

**Señales de compra:**
- `[INDUSTRIA] [CIUDAD] "contratando" OR "buscamos" OR "vacante"` — están creciendo.
- `[INDUSTRIA] "ronda" OR "levantó" OR "inversión" 2025..2026` — tienen presupuesto.
- `[INDUSTRIA] "lanzamos" OR "nuevo producto" [CIUDAD]` — momento activo.

**Contacto / decisor (solo para DESCUBRIR, no para el dato final):**
- `"[NOMBRE EMPRESA]" [CARGO] (linkedin OR email OR contacto)`
- `"[NOMBRE EMPRESA]" "@" email` — pista de que existe un correo. **Es solo pista**: el email que entra a la lista debe confirmarse después en la fuente primaria (sitio propio), nunca tomarse del resumen del buscador.

---

## B. LinkedIn / redes (NO automático — generar queries pegables)

No hay scraping libre de LinkedIn. Entrega al usuario filtros listos y pide que pegue los resultados; tú los estructuras.

**Búsqueda en LinkedIn (pegar en la barra de LinkedIn):**
- Personas: `[CARGO] [INDUSTRIA] [CIUDAD]` → filtrar por ubicación y sector.
- Sales Navigator (si lo tiene): filtros sugeridos → Geografía, Sector, Tamaño de empresa, Cargo, Antigüedad en el puesto, "Cambió de trabajo recientemente".

**Google sobre LinkedIn (ejecutable con WebSearch):**
- `site:linkedin.com/in [CARGO] [INDUSTRIA] [CIUDAD]`
- `site:linkedin.com/company [INDUSTRIA] [CIUDAD]`

**Instagram / redes (B2C o negocios visuales):**
- `site:instagram.com [INDUSTRIA] [CIUDAD]`
- Hashtags y geolocalización: pedir al usuario que pegue cuentas relevantes.

---

## C. Negocio local / B2C (Google Maps + directorios)

- Google Maps: el usuario busca `[INDUSTRIA] [CIUDAD/COMUNA]` en Maps y **pega** los resultados (web, teléfono, reseñas); `WebFetch` no puede abrir Maps directo. Priorizar los que tengan web propia y reseñas (señal de negocio activo).
- Directorios sectoriales, cámaras de comercio, asociaciones gremiales de `[INDUSTRIA]`.
- `WebSearch`: `directorio [INDUSTRIA] [CIUDAD]` / `asociación [INDUSTRIA] [PAÍS] miembros`.

---

## C-bis. B2B / startups (cuando los candidatos vienen de noticias o rondas)

Para ICPs de empresas/startups, WebSearch devuelve sobre todo **noticias y listicles**, no una lista limpia con sitios. Pasos:

- Señales de compra fuertes: `startups [PAÍS] levantaron ronda [AÑO]`, `[INDUSTRIA] contratando [CIUDAD]`, cohortes de aceleradoras (Start-Up Chile, Platanus, etc.).
- **Extraer el roster real**: abre el artículo-roundup con `WebFetch` y pídele la lista de empresas + el **dominio/URL de cada una**. No te quedes con el resumen de WebSearch.
- **Nunca adivines el dominio.** Si el artículo no lo trae, busca `"[NOMBRE EMPRESA]" sitio oficial` o `"[NOMBRE EMPRESA]" linkedin company` para confirmar la URL antes de cualificar o confirmar contacto.
- Filtra por tamaño/etapa: descarta los que ya están en Serie A+ o son demasiado grandes si tu ICP es PYME/early-stage (probablemente ya tienen el área internalizada).

## D. Bolsas de oportunidad transversales

- Competidores: ¿quién comenta/sigue/reseña a tus competidores? (clientes potenciales).
- Eventos y ferias del nicho: lista de expositores/asistentes.
- Marketplaces y reviews (G2, Capterra, Trustpilot) para B2B SaaS: quién dejó reseñas de un rival.

---

## Verificación de contacto — jerarquía de fuentes primarias

El resumen de `WebSearch` y los directorios (carta.menu, infoisinfo, tallermecanicorys, páginas amarillas, etc.) **sirven solo para descubrir candidatos y URLs**. NUNCA tomes de ahí el email/teléfono final: esos resúmenes inventan y mezclan datos de varios negocios.

**Qué puede y qué no puede abrir `WebFetch`:**
- ✅ **Sitio web propio del negocio** → `WebFetch` lo lee bien. Es la fuente primaria por defecto.
- ❌ **Google Maps / Google Business** → `WebFetch` NO funciona (la ficha carga por JavaScript). No la abras con `WebFetch`.
- ❌ **LinkedIn / Instagram** → `WebFetch` NO funciona (requieren login). No los abras con `WebFetch`.

**Cadena de confirmación (en orden):**

1. **Sitio web propio** → ábrelo con `WebFetch`, lee la página "Contacto" o el footer. Si lo tiene, este es el dato bueno.
2. **Sin sitio propio, pero hay ficha de Maps o perfil de LinkedIn/IG** → como `WebFetch` no puede abrirlos, **pídele al usuario que pegue** la ficha/perfil (o el teléfono/email que ahí aparece) y tómalo de ahí. Es dato del propio negocio, así que es válido.
3. **Nada de lo anterior disponible** → el contacto queda **"a verificar"**.

Regla: el dato debe **aparecer textualmente en la fuente primaria** (sitio propio que abriste, o ficha/perfil que el usuario pegó). Si no, "a verificar". Anota *de qué fuente primaria* salió cada dato (ej. "tel: footer del sitio", "email: ficha pegada por el usuario").

## Higiene de datos
- Una fuente primaria por dato de contacto, con su URL.
- Datos de contacto: solo si los **leíste en la fuente primaria**. Si no, "a verificar". Nunca inventar.
- Descartar duplicados y empresas que claramente son el anti-cliente.
