# Cualificación y scoring de prospectos

Objetivo: convertir una lista cruda en prospectos priorizados. Puntúa cada candidato y ordena de mayor a menor. Descarta los que no llegan al umbral.

## Las 3 dimensiones (0–3 cada una)

### 1. FIT — ¿encaja con el ICP?
- 3 = calce perfecto (industria, tamaño, zona, perfil exactos).
- 2 = encaja en lo esencial, falla un atributo menor.
- 1 = encaja a medias, dudoso.
- 0 = no es el ICP → descartar.

**Zona como filtro duro:** si el brief definió comunas/radio específicos, un candidato fuera de esa lista de comunas baja a FIT ≤1 (o descarte directo si la zona es crítica). Confirma la comuna real del candidato en su fuente primaria (dirección del sitio/ficha), no por el nombre de la ciudad en el resumen del buscador — en los tests esto descartó leads que parecían de Santiago pero estaban en Peñalolén, Puerto Varas o Concepción.

### 2. SEÑAL — ¿hay indicio de que necesita/compraría ahora?
- 3 = señal fuerte y reciente (contratando, ronda, lanzamiento, dolor visible).
- 2 = señal indirecta (crecimiento, web anticuada, queja pública).
- 1 = sin señal clara, solo fit.
- 0 = señal de que NO es momento (acaba de comprar a un rival, cerrando).

### 3. ACCESIBILIDAD — ¿puedo llegar al decisor?
- 3 = decisor identificado + canal de contacto real (email/LinkedIn/DM).
- 2 = empresa correcta pero falta el decisor o el contacto exacto.
- 1 = solo formulario genérico de contacto.
- 0 = sin vía realista de contacto.

## Score total = FIT + SEÑAL + ACCESIBILIDAD (0–9)

- **7–9 → Prioridad A** (contactar primero).
- **5–6 → Prioridad B** (segunda ola).
- **≤4 → Descartar** (o "a verificar" si falta info que se puede conseguir).

## Orden final: por VALOR ESPERADO, no solo por score

El score dice "qué tan bueno es el lead"; el valor esperado dice "dónde está la plata". Ordena la lista final por:

**Valor esperado ≈ Ticket × FIT × SEÑAL**

- **Ticket**: el del brief (precio/recurrencia del ICP). Si un nicho del ICP paga más, pondéralo.
- Un lead con score 7 y ticket alto vale más que uno con score 8 y ticket bajo.
- Usa FIT y SEÑAL (no ACCESIBILIDAD) en la fórmula: la accesibilidad afecta el esfuerzo de llegar, no cuánto vale el cliente.
- Entrega la lista ordenada por valor esperado y muestra una nota corta del cálculo (ej. "ticket alto + señal fuerte → tope de la lista").

## Reglas
- FIT = 0 descarta automáticamente, sin importar el resto.
- **Excluir clientes actuales / contactos previos** del brief (pregunta 9): si el candidato ya está en esa lista, descártalo antes de puntuar.
- Si descartas, escribe en una línea por qué (sirve para afinar el ICP).
- Meta de salida: ~8–12 prospectos de Prioridad A/B bien justificados, mejor que 50 dudosos.
- Cada prospecto que pasa lleva su **razón de fit** en una frase concreta (no "parece interesante").
