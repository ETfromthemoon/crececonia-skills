# Formato de la lista de prospectos (entregable)

El entregable final. Muestra siempre la tabla en pantalla. Ofrece exportar a CSV si el usuario quiere.

## Columnas

| Campo | Descripción |
|---|---|
| Decisor | Nombre de la persona que decide (o "—" si solo empresa) |
| Rol | Cargo del decisor (fundador/CEO/gerente del área) |
| LinkedIn decisor | Perfil del decisor si se obtuvo (para LinkedIn/contexto) |
| Empresa | Nombre de la empresa / negocio |
| Razón de fit | 1 frase: por qué encaja con el ICP |
| Señal + fecha | Evento reciente que la hace oportuna (ronda, vacante, lanzamiento) + cuándo |
| Score | 0–9 (de qualification.md) + Prioridad A/B |
| Valor esperado | Orden por Ticket × FIT × SEÑAL (ver qualification.md). La lista se ordena por aquí |
| Canal recomendado | El que realmente existe para este prospecto (email confirmado > LinkedIn decisor > WhatsApp) |
| Contacto | Dato **leído en fuente primaria** (sitio propio, ficha Maps/perfil pegado), indicando de cuál salió. Si no se confirmó: "a verificar" |
| Mensaje + secuencia | Toque 1 + follow-ups (días +3-5 y +7-10), ya pasados por humanizer |
| Fuente/URL | De dónde salió cada dato (verificable) |
| Estado | Nuevo / Contactado / Respondió / Descartado |
| Próximo paso | Acción + fecha del siguiente toque |

## Tabla en pantalla (ejemplo, ordenada por valor esperado)

| Decisor | Rol | Empresa | Razón de fit | Señal + fecha | Score | Valor esp. | Canal | Contacto |
|---|---|---|---|---|---|---|---|---|
| Ana Pérez | Directora | Estudio Norte | Agencia 8 pers., sin contabilidad externa | Publicó vacante de marketing (mayo 2026) | 8 (A) | Alto | LinkedIn | a verificar — solo LinkedIn |

(Los mensajes + secuencia van aparte, bajo cada prospecto, por su longitud.)

## CSV

Si el usuario pide exportar, genera un `.csv` en el directorio actual con cabeceras:
```
decisor,rol,linkedin_decisor,empresa,razon_fit,senal_fecha,score,prioridad,valor_esperado,canal_recomendado,contacto,fuente_url,mensaje,follow_up_2,follow_up_3,estado,proximo_paso
```
Escapa comas y saltos de línea dentro de los campos de mensaje con comillas dobles.

## Cierre: plan de acción
Tras la tabla, añade 3–5 líneas:
- A quién contactar **hoy** (los de mayor valor esperado).
- Orden sugerido y por qué (valor esperado, no solo score).
- Cuándo disparar el toque 2 y 3 a quienes no respondan.
