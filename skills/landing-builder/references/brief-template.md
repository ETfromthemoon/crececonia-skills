# Brief Template — 8 preguntas obligatorias

Las 8 preguntas que la skill `landing-builder` exige antes de tocar código. Si el usuario es vago en alguna, repreguntar con ejemplos hasta tener respuesta concreta.

---

## 1. ¿Cuál es el nombre del producto/servicio y a qué se dedica la empresa?

**Por qué:** define identidad y contexto.

**Ejemplos de respuesta válida:**
- "Crece con IA, consultora de inteligencia artificial para PyMEs LATAM"
- "Strimo SaaS, software de gestión de inventario para retail con 10-50 sucursales"
- "Sergio Astudillo Coaching, programa de coaching empresarial para fundadores B2B"

**Si responde vago** ("una app de productividad"): repreguntar pidiendo el sector exacto + tamaño cliente.

---

## 2. ¿Quién es el cliente ideal? (sector, tamaño empresa, rol decisor)

**Por qué:** define el lenguaje, ejemplos y prueba social del copy.

**Estructura de respuesta**:
- Sector: tecnología, salud, retail, manufactura, servicios profesionales, etc.
- Tamaño: número de empleados o facturación
- Geografía: país/región
- Rol decisor: CEO / CMO / CTO / Operaciones / Gerente comercial

**Ejemplo válido:** "CEOs y directores de operaciones de empresas de logística con 30-150 empleados en Chile, México y Colombia"

---

## 3. ¿Cuál es el dolor o problema principal que tu cliente vive HOY?

**Por qué:** es la base del headline y del bloque "Problema". Sin dolor no hay conversión.

**Estructura de respuesta**:
- Síntoma observable (qué ve el cliente)
- Costo del síntoma (tiempo, dinero, oportunidad perdida)
- Por qué no lo ha resuelto solo

**Ejemplo válido:** "Sus equipos pierden 4-5 horas diarias en facturación manual de 200+ documentos. Eso son 3 personas full-time. Han intentado con Excel macros pero los errores generan retrabajo del 15%."

---

## 4. ¿Cuál es tu oferta y precio?

**Por qué:** define la sección Servicios + Pricing y la honestidad de la página.

**Estructura de respuesta**:
- Qué reciben (entregables concretos)
- Plazo (semanas, meses)
- Precio (USD o moneda local, rango o exacto)
- Forma de pago (one-shot, mensual, hitos)

**Ejemplo válido:** "Auditoría Express: mapa de 3-5 procesos + ROI + roadmap. 2 semanas. USD 500 al firmar (no se inicia sin pago). Si NPS final <7, refund 50%."

---

## 5. ¿Qué te diferencia de las alternativas?

**Por qué:** define la USP que va en Hero y en Garantía.

**Reglas:**
- NO usar "somos los mejores", "líderes en X", "expertos"
- SÍ usar contraste con lo que el cliente conocería como alternativa
- SÍ usar números o garantías concretas

**Ejemplo válido:** "Una agencia te vende horas de implementación. Un consultor genérico te entrega un PDF. Nosotros instalamos el sistema y nos quedamos hasta que tu equipo lo use. Si en la semana 3 no se usa, no facturamos la fase de adopción."

---

## 6. ¿Qué prueba social tienes y puedes mostrar?

**Por qué:** la sección Resultados y Caso de Uso necesitan datos reales.

**Tipos válidos**:
- Logos de empresas (con permiso)
- Stats: "+30 proyectos en producción", "70% reducción tiempo X"
- Testimonios con nombre + empresa + rol
- Casos de estudio breves: industria + métrica + resultado
- Certificaciones / partnerships

**Si no tiene prueba social todavía**: definir qué se puede mostrar legítimamente. NO inventar.

**Ejemplo válido:**
- "+30 proyectos en producción en 7 industrias en LATAM y España"
- "Reducción 62% tiempo de cotización en constructora de 120 empleados (3 semanas post go-live)"
- "Quote: 'Recuperamos 15 horas semanales en reportes' — María González, COO Logística RapidShip"

---

## 7. ¿Cuál es la urgencia o limitación de la oferta?

**Por qué:** la sección CTA Final necesita un motivo para actuar ahora, no después.

**Tipos válidos**:
- Cupos limitados (con número real, no inventado)
- Precio especial hasta fecha X
- Disponibilidad de calendario ("cupos para junio 2026")
- Cohorte que arranca tal fecha
- Promoción temporal

**Si no hay urgencia real**: usar el costo de oportunidad ("cada mes que pasa son X horas perdidas").

**Ejemplo válido:** "Cupos para junio 2026 (2 lugares disponibles). Cada mes que no se automatice este proceso son ~USD 6.600 en horas-equipo perdidas."

---

## 8. ¿Cuál es tu voz de marca? (tono y estilo)

**Por qué:** todo el copy se adapta a esto. Sin esto, suena genérico/IA.

**Estructura**:
- 3 adjetivos que describan el tono
- 3 adjetivos que NUNCA debería usarse
- Ejemplo de 2-3 frases que el cliente diría de manera natural
- Referencias (otras marcas con voz similar)

**Ejemplo válido:**
- Tono: directo, honesto, técnico-comercial (no jergoso, no formal)
- Nunca: pretencioso, vendedor, mágico
- Frases naturales del cliente: "Si no es para ti, te lo decimos." / "Pagas contra entregables, no horas." / "Si no se usa, no se factura."
- Referencias: Basecamp, Stripe (claridad), Linear (precisión)

---

## Output esperado de Fase 1

Después de las 8 preguntas, crear `brief.md` en la raíz del proyecto:

```markdown
# Brief — [Nombre proyecto]

**Fecha:** YYYY-MM-DD
**Cliente:** [empresa]
**Contacto:** [nombre, email]

## 1. Empresa y producto
...

## 2. Cliente ideal
...

[continuar con las 8 secciones]

---

## Notas adicionales del consultor
- Insights del brief
- Decisiones tomadas
- Riesgos identificados
```

Este archivo queda como **fuente de verdad** del proyecto. Toda decisión de copy y estrategia se justifica contra este brief.
