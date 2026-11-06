# Skills públicas de CrececonIA

Este repositorio guarda la fuente versionada de las skills descargables que
CrececonIA publica en [su Centro de Conocimiento](https://www.crececonia.cl/centro/skills).
Cada skill vive en `skills/<slug>/` con un `SKILL.md` y sus referencias.

| Skill | Carpeta |
| --- | --- |
| Captaclientes | `skills/captaclientes/` |
| Generador de guiones virales | `skills/generador-de-guiones-virales/` |
| Landing Builder | `skills/landing-builder/` |
| Validador de negocios | `skills/validador-de-negocios/` |

La ficha «Piensa con IA» del sitio es una lectura y no tiene paquete de skill.

## Publicar una actualización

1. Revisar `SKILL.md` y todas sus referencias en esta fuente.
2. Generar el ZIP con `python scripts/package.py <slug>`.
3. Copiar el ZIP a `public/downloads/skills/` del repositorio
   `crececonia-website`, actualizar su ficha en
   `content/public-catalog.json` y abrir un PR con Preview.

Los ZIP publicados se generan desde estas carpetas; el catálogo del sitio
decide qué versión está disponible al público. No se incorporan
automáticamente skills locales o en borrador.

Este repositorio no añade una licencia general sobre las skills. Revisar las
condiciones de cada recurso antes de reutilizarlo.
