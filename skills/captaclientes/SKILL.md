---
name: captaclientes
description: >
  Buscador de nuevos clientes para cualquier negocio. Úsalo cuando el usuario quiera conseguir clientes, encontrar leads, hacer prospección o escribir mensajes de contacto en frío. La skill define el cliente ideal (ICP), encuentra prospectos reales con búsqueda web y queries pegables para LinkedIn/Google Maps, los cualifica y prioriza, y redacta un mensaje de outreach personalizado por cada uno (pasado por humanizer para que no suene a IA). Entrega una lista de prospectos lista para trabajar en tabla/CSV. Invocar con /captaclientes o cuando el usuario diga "ayúdame a conseguir clientes", "necesito leads", "buscar clientes", "captar clientes", "prospección", "outreach en frío", "mensajes de contacto", "find clients", "lead gen", "cold outreach", "necesito vender más", "no tengo clientes", o "cómo consigo más clientes".
---

# Captaclientes — Buscador de nuevos clientes

Tu trabajo es ayudar a la persona a **conseguir clientes reales** para su negocio, sea cual sea. No vendes humo ni listas genéricas: defines a quién buscar, encuentras prospectos verificables, los priorizas y entregas un mensaje de contacto listo para cada uno.

No es un generador genérico de "tips de ventas". Es un proceso operativo que termina con un entregable concreto: **una lista de prospectos con su outreach**.

---

## Cuándo usar esta skill

Actívala cuando el usuario quiera **encontrar y contactar nuevos clientes**. Disparadores típicos (en cualquier idioma):

- "Ayúdame a conseguir clientes" / "necesito clientes" / "no tengo clientes"
- "Necesito leads" / "buscar / captar clientes" / "prospección"
- "Escríbeme mensajes de contacto en frío" / "cold outreach" / "lead gen"
- "Cómo consigo más clientes para [negocio]"

**No la uses para**:
- Auditar campañas de ads ya activas → usa las skills `ads-*`.
- Construir una landing de captación → usa `landing-builder`.
- Solo humanizar un texto suelto → usa `humanizer` directo.

---

## Principios (no negociables)

1. **ICP antes de buscar.** Nunca busques prospectos sin definir primero el cliente ideal. Una lista sin foco es ruido.
2. **Contacto desde la fuente primaria, siempre.** Un teléfono, email o perfil **solo vale si lo leíste en una fuente primaria del propio negocio**. La única fuente primaria que `WebFetch` puede leer de forma fiable es el **sitio web propio** del negocio (página de contacto / footer). Las fichas de Google Maps y los perfiles de LinkedIn/Instagram **NO se pueden abrir con `WebFetch`** (JavaScript pesado o login) — para esos casos el dato debe venir de que el **usuario pegue** la ficha/perfil. **Nunca** aceptes datos de contacto del resumen de un buscador ni de un directorio de terceros (carta.menu, infoisinfo, etc.) — esos resúmenes inventan y mezclan datos. Si no lo confirmaste en fuente primaria, va como "a verificar". **Nunca inventes** nada. Ver la cadena completa en `references/lead-sources.md`.
3. **Razón de fit explícita.** Cada prospecto debe tener una frase de por qué encaja. Si no puedes justificar el fit, no entra en la lista.
4. **Outreach personalizado, no spam.** Mensajes 1-a-1 basados en la razón de fit. Respeta GDPR y las políticas de cada plataforma. Nada de envíos masivos idénticos.
5. **Por fases.** El usuario puede corregir el ICP antes de que gastes búsquedas. No saltes a redactar mensajes con un target equivocado.

---

## El proceso de 5 fases

El usuario no salta fases. Cada fase es un punto de avance.

```
1. BRIEF ICP   → definir a quién buscamos (no avanza sin esto)
2. ENCONTRAR   → generar queries + ejecutar búsqueda web + estructurar resultados
3. CUALIFICAR  → puntuar, descartar flojos, y confirmar contacto de finalistas
4. OUTREACH    → redactar mensaje por prospecto; pasar por humanizer
5. ENTREGAR    → tabla/CSV final priorizada con mensaje + fuente + próximo paso
```

### Fase 1 — BRIEF ICP
Haz las preguntas de `references/brief-icp.md`. Objetivo: saber **qué vende**, **a quién** (cargo/tipo de empresa o tipo de persona), **ticket aprox.**, **zona geográfica**, **canal de contacto preferido**, **ejemplos de clientes ideales** y **anti-cliente** (a quién NO quiere).

No avances hasta tener, como mínimo: qué vende + a quién + zona + canal. Si el usuario es vago, propón un ICP tentativo y pide confirmación antes de buscar.

### Fase 2 — ENCONTRAR
Usa `references/lead-sources.md` para construir las búsquedas:
- **Web abierta**: ejecuta `WebSearch` con los dorks/operadores adecuados; usa `WebFetch` para confirmar datos de una página concreta.
- **LinkedIn / redes**: NO hay scraping automático. Genera los **filtros y queries listos para pegar** y pide al usuario que pegue los resultados; tú los estructuras.
- **Negocio local / B2C**: orienta a Google Maps / directorios locales (queries pegables).
- **B2B / startups (candidatos vienen de noticias o listas)**: si los prospectos salen de un artículo-roundup ("las 62 startups de…", "empresas que levantaron ronda"), **abre ese artículo con `WebFetch`** para extraer el roster completo y el **dominio real de cada empresa**. Nunca asumas ni adivines el dominio (ej. `empresa.ai`) — un dominio inventado falla. Si el artículo no trae el sitio, busca `"[NOMBRE EMPRESA]" sitio oficial` para hallar el dominio antes de seguir.

Reúne 10–20 candidatos crudos antes de cualificar. Cada uno con su URL/fuente.

El resumen que devuelve `WebSearch` y los directorios de terceros sirven **solo para descubrir candidatos y URLs**, jamás como fuente del dato de contacto.

**Orden importante (para no malgastar llamadas):** la confirmación de contacto se hace en la Fase 3, **solo sobre los prospectos que sobreviven la cualificación** — no confirmes los 10–20 crudos. Tope sugerido: ~1 `WebFetch` de confirmación por prospecto finalista (8–12 en total).

### Fase 3 — CUALIFICAR Y CONFIRMAR CONTACTO
Primero **cualifica** con el scoring de `references/qualification.md` (fit + señal + accesibilidad), usando el contacto *tentativo* del descubrimiento. Ordena de mayor a menor y descarta los flojos diciendo por qué. Quédate con los mejores (~8–12).

Luego, **solo sobre los finalistas**, haz tres cosas:

**a) Identifica al decisor (persona, no inbox).** Busca el nombre y cargo de quien decide (fundador/CEO/gerente del área) y su LinkedIn. En B2B el mensaje va a una persona, no a `contacto@`. Si el decisor está en LinkedIn (que `WebFetch` no abre), **pide al usuario que pegue** el perfil. Si no se logra, usa el contacto general pero anótalo como tal.

**b) Confirma el contacto** siguiendo la cadena de fuentes primarias de `references/lead-sources.md`:
1. Abre el **sitio web propio** con `WebFetch` y lee email/teléfono del footer o página de contacto.
2. Si no tiene sitio (o solo tiene ficha de Maps / perfil de LinkedIn/IG, que `WebFetch` no puede abrir), **pide al usuario que pegue** la ficha o el perfil, y de ahí extrae el dato.
3. Si aun así no aparece, el contacto queda **"a verificar"**. Nunca inventes. Anota de qué fuente primaria salió cada dato.

**c) Define el mejor canal por prospecto.** Recomienda el canal que **realmente existe** para ese prospecto (email confirmado > LinkedIn del decisor > WhatsApp de la ficha), respetando la preferencia del brief cuando haya opción. El mensaje de la Fase 4 se redacta para ese canal.

Finalmente, **prioriza por valor esperado** (no solo por score): ver el ranking ticket × fit × señal en `references/qualification.md`. La lista se ordena por ahí.

### Fase 4 — OUTREACH
Para cada prospecto cualificado, redacta el mensaje según el **canal definido en la Fase 3** (email frío, DM, solicitud de conexión LinkedIn, WhatsApp) usando las estructuras de `references/outreach-playbook.md`. El mensaje debe ir dirigido al **decisor por su nombre** y apoyarse en la **razón de fit** específica.

Genera además la **secuencia de seguimiento**: no solo el primer toque, sino 2-3 mensajes con ángulos distintos y tiempos sugeridos (ver `references/outreach-playbook.md`). Así el usuario no se queda en el primer "no respondió".

**Obligatorio**: pasa todo el copy (primer mensaje + follow-ups) por la skill `humanizer` (sus 24 patrones) para que no suene a IA. Invoca `humanizer` antes de entregarlos.

### Fase 5 — ENTREGAR
Arma la lista final con el formato de `references/prospect-list-template.md`: tabla en pantalla **ordenada por valor esperado** y, si el usuario quiere, un archivo CSV guardado en el **directorio de trabajo actual** (ej. `prospectos-[nicho]-[fecha].csv`). Las columnas y cabeceras exactas están en el template (decisor, rol, LinkedIn, empresa, razón de fit, señal+fecha, score, valor esperado, canal recomendado, contacto, mensaje+secuencia, fuente/URL, estado, próximo paso).

Cierra con un **plan de acción**: a quién contactar primero (los de mayor valor esperado), en qué orden y cuándo disparar los toques 2 y 3.

---

## Salida esperada

Al terminar, el usuario tiene en la mano una lista priorizada de prospectos reales y verificables, cada uno con un mensaje de contacto personalizado y humanizado, listo para enviar.
