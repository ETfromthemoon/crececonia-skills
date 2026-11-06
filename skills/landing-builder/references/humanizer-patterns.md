# Humanizer Patterns — Copy de Landing

Los 24 patrones del skill `humanizer` aplicados específicamente a copy de landing page. **Invocar `humanizer` directamente** sobre cada sección antes de inyectarla al código.

---

## Cómo se usa en Fase 4

Para cada una de las 9 secciones de la landing:

1. Generar copy inicial basado en el brief
2. Pasar el copy por el skill `humanizer` (los 24 patrones en 2 pasadas)
3. Inyectar el resultado en el código

```bash
# Conceptual: invocar humanizer sobre el texto
/humanizer "[texto de la sección]"
```

---

## Los 24 patrones (resumen aplicado a landings)

### Patrones de contenido (6)

1. **Importancia inflada**
   - ❌ "Revolucionamos la productividad"
   - ✅ "Reducimos 40% el tiempo de reportes"

2. **Frases vacías de triunfo**
   - ❌ "Estamos creciendo cada día"
   - ✅ "30 proyectos completados en 18 meses"

3. **Nombres de marcas sin contexto**
   - ❌ "Trabajamos con startups que usan stripe y openai"
   - ✅ "Integramos con Stripe (pagos), HubSpot (CRM) y tu sistema actual"

4. **Generalidades vacías**
   - ❌ "Ayudamos empresas a crecer"
   - ✅ "Auditamos 5 procesos y los automatizamos en 6 semanas"

5. **Hipérboles no respaldadas**
   - ❌ "El mejor consultor del rubro"
   - ✅ "5+ años, +30 proyectos, 7 industrias"

6. **Nota de prensa vacía**
   - ❌ "Crecemos junto a nuestros clientes"
   - ✅ "Si en la semana 3 nadie usa el sistema, iteramos sin costo"

### Patrones de lenguaje (6)

7. **Palabras IA-favoritas**: revoluciona, transforma, potencia, optimiza, maximiza, eleva, libera, desbloquea, empodera, redefine
   - Eliminar todas. Si necesitas decir "mejora", di **mejora**.

8. **Voz pasiva excesiva**
   - ❌ "Los reportes son generados automáticamente por el sistema"
   - ✅ "El sistema genera los reportes solo"

9. **Sustantivos abstractos**
   - ❌ "Implementación de soluciones de automatización"
   - ✅ "Automatizamos tu facturación"

10. **Verbo "es" overused**
    - ❌ "Esta es una herramienta que es útil para empresas que son grandes"
    - ✅ "Herramienta útil para empresas grandes"

11. **Conectores exagerados**: "asimismo", "además", "no obstante", "por consiguiente"
    - Usar punto y nueva oración.

12. **Clichés de apertura**: "En el mundo actual", "En la era digital", "Hoy en día más que nunca"
    - Empezar directo con el problema o promesa.

### Patrones de estilo (6)

13. **Guiones largos en exceso (—)**
    - Usar máximo 1-2 por página. Reemplazar con punto o coma.

14. **Negritas innecesarias**
    - Solo bold para 1-2 palabras clave en un párrafo. No 5+.

15. **Formato "Etiqueta: contenido"**
    - ❌ "Beneficio: ahorrás tiempo. Resultado: más productividad."
    - ✅ "Ahorrás tiempo. Eso es más productividad."

16. **Emojis decorativos en B2B**
    - 🚀 ✨ 💡 → Usar máximo 1-2 en toda la landing, solo si la voz es playful.

17. **Estructura demasiado ordenada**
    - 3 párrafos del mismo largo, 3 features por sección, simetría total → variar.

18. **Párrafos uniformes**
    - Mezclar párrafos de 1 línea con párrafos de 3-4 líneas. Crear ritmo.

### Patrones de comunicación (3)

19. **Cierre tipo chatbot**
    - ❌ "Espero que esta información haya sido útil"
    - ✅ Cerrar con dato concreto o CTA

20. **Disclaimer falso**
    - ❌ "Por supuesto, los resultados pueden variar"
    - ✅ Decir exactamente bajo qué condiciones (D1+D2 ≥ X)

21. **Tono de acuerdo total**
    - ❌ "Entendemos perfectamente tu situación"
    - ✅ "Si tu equipo pierde >3h/día en X, te aplica"

### Relleno y cobertura (3)

22. **Frases relleno**: "Vale la pena mencionar", "Cabe destacar", "Es importante notar"
    - Eliminar siempre. Si vale la pena, ponlo directamente.

23. **Conclusiones vagas**: "En resumen, todo esto es para ti", "Esperamos verte pronto"
    - Cerrar con la acción concreta.

24. **Cobertura excesiva**: enumerar 10 features cuando 4 son las importantes
    - Cortar a las 3-5 más impactantes.

---

## Reglas específicas de copy de landing

### Hero
- Headline ≤12 palabras, una promesa
- Subhead 1-2 líneas, el "cómo"
- 1 sola CTA texto en infinitivo: "Recibir evaluación", "Empezar diagnóstico"
- 3 señales: sin compromiso · respuesta < 2h · si no es para ti, te lo decimos

### Problema (con stats)
- "Por eso 7 de cada 10 empresas..." → conectar dato con cliente
- Año de la fuente visible
- 3-4 stats max

### Servicios
- Precio visible (no "consultar")
- "Te llevas:" línea concreta de qué se lleva
- CTAs específicos por tier

### FAQ
- Preguntas como objeciones reales, no marketing
- Respuestas directas, primera persona del consultor
- Máximo 3 oraciones por respuesta

### CTA Final
- 1 sola acción
- Urgencia REAL (cupos, fecha, cohorte)
- Repetir señales de confianza

---

## Validación final del copy

Antes de inyectar al código, leer cada sección haciéndose estas 3 preguntas:

1. **¿Suena a Sergio hablando o a un copywriter de IA?**
2. **¿Hay un dato concreto que el lector pueda verificar?**
3. **¿Lo entiende mi tía en 5 segundos?**

Si la respuesta es NO a cualquiera, pasarlo otra vez por `humanizer`.

---

## Anti-ejemplos vs ejemplos buenos

### Caso: Hero de SaaS B2B

❌ **AI slop**:
> "Revoluciona tu productividad con la plataforma líder en automatización inteligente. Potencia tu equipo y desbloquea nuevos niveles de eficiencia."

✅ **Humanizado**:
> "Mejoramos los 3 procesos que te cuestan más dinero cada mes. En 30 minutos te decimos cuáles son y cuánto se ahorra."

### Caso: Sección Servicios

❌ **AI slop**:
> "Nuestros servicios premium están diseñados para llevar tu empresa al siguiente nivel mediante metodologías de vanguardia."

✅ **Humanizado**:
> "Tres formas de empezar. Misma metodología. Pago contra entregables, sin contrato anual."

### Caso: Garantía

❌ **AI slop**:
> "Estamos comprometidos con tu éxito y trabajaremos incansablemente para garantizar los mejores resultados."

✅ **Humanizado**:
> "Si en la semana 3 nadie en tu equipo está usando el sistema, lo iteramos sin costo hasta que lo hagan."

### Caso: CTA Final

❌ **AI slop**:
> "¡Empieza tu viaje hoy! Únete a cientos de empresas que ya están transformando su negocio."

✅ **Humanizado**:
> "Dinos qué proceso te quita el sueño. Respondemos en menos de 2 horas hábiles."
