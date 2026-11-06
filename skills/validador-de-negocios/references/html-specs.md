# Especificaciones HTML para los documentos generados

## Template base para ambos HTMLs

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TÍTULO</title>
  <style>
    /* === RESET Y BASE === */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
      background: #0d1117;
      color: #e6edf3;
      line-height: 1.6;
    }
    .container { max-width: 960px; margin: 0 auto; padding: 0 20px; }

    /* === SCROLLBAR === */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0d1117; }
    ::-webkit-scrollbar-thumb { background: #30363d; border-radius: 4px; }

    /* === TIPOGRAFÍA === */
    h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
    h2 { font-size: 1.5rem; font-weight: 600; margin: 2rem 0 1rem; color: #f0f6fc; }
    h3 { font-size: 1.15rem; font-weight: 600; margin: 1.5rem 0 0.75rem; }
    p { margin-bottom: 1rem; color: #8b949e; }
    a { color: #58a6ff; text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* === CARDS === */
    .card {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }
    .card-title {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #8b949e;
      margin-bottom: 0.5rem;
      font-weight: 600;
    }

    /* === SCORE BADGE === */
    .score-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 1.2rem;
    }
    .score-badge.green { background: rgba(63,185,80,0.15); color: #3fb950; border: 1px solid rgba(63,185,80,0.3); }
    .score-badge.amber { background: rgba(210,153,34,0.15); color: #d29922; border: 1px solid rgba(210,153,34,0.3); }
    .score-badge.red   { background: rgba(248,81,73,0.15); color: #f85149; border: 1px solid rgba(248,81,73,0.3); }

    /* === BARRAS DE PROGRESO === */
    .progress-bar {
      height: 8px;
      background: #21262d;
      border-radius: 4px;
      overflow: hidden;
      margin: 8px 0;
    }
    .progress-fill {
      height: 100%;
      border-radius: 4px;
      transition: width 0.8s ease;
    }
    .progress-fill.green { background: #3fb950; }
    .progress-fill.amber { background: #d29922; }
    .progress-fill.red   { background: #f85149; }

    /* === LEAN CANVAS GRID === */
    .canvas-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      margin: 1.5rem 0;
    }
    .canvas-cell {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 1rem;
    }
    .canvas-cell.empty { opacity: 0.5; }
    .canvas-cell h4 {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #8b949e;
      margin-bottom: 0.5rem;
    }
    .canvas-cell.wide { grid-column: span 2; }
    .canvas-cell.full { grid-column: 1 / -1; }

    /* === ALERTAS === */
    .alert {
      padding: 1rem 1.25rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      border-left: 4px solid;
    }
    .alert.critical { background: rgba(248,81,73,0.1); border-color: #f85149; }
    .alert.warning { background: rgba(210,153,34,0.1); border-color: #d29922; }
    .alert.info    { background: rgba(88,166,255,0.1); border-color: #58a6ff; }
    .alert.good    { background: rgba(63,185,80,0.1);  border-color: #3fb950; }
    .alert-label { font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 0.25rem; }
    .alert.critical .alert-label { color: #f85149; }
    .alert.warning .alert-label  { color: #d29922; }
    .alert.info .alert-label     { color: #58a6ff; }
    .alert.good .alert-label     { color: #3fb950; }

    /* === TABLAS === */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }
    th {
      text-align: left;
      padding: 0.75rem 0.5rem;
      border-bottom: 2px solid #30363d;
      color: #8b949e;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    td {
      padding: 0.75rem 0.5rem;
      border-bottom: 1px solid #21262d;
      font-size: 0.9rem;
    }
    tr:last-child td { border-bottom: none; }

    /* === SCORE SECTION (dimension cards) === */
    .dimension-row {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }
    .dimension-label { flex: 0 0 140px; font-weight: 500; }
    .dimension-bar   { flex: 1; }
    .dimension-score { flex: 0 0 40px; text-align: right; font-weight: 700; font-size: 1.1rem; }
    .dimension-desc  { font-size: 0.85rem; color: #8b949e; margin-top: -0.75rem; margin-bottom: 1.5rem; margin-left: 180px; }

    /* === TIMELINE (roadmap) === */
    .timeline { position: relative; padding-left: 2rem; margin: 1.5rem 0; }
    .timeline::before {
      content: '';
      position: absolute; left: 8px; top: 0; bottom: 0;
      width: 2px; background: #30363d;
    }
    .timeline-item { position: relative; margin-bottom: 2rem; }
    .timeline-item::before {
      content: '';
      position: absolute; left: -1.65rem; top: 4px;
      width: 12px; height: 12px;
      border-radius: 50%; background: #58a6ff;
      border: 2px solid #0d1117;
    }
    .timeline-item.phase-complete::before { background: #3fb950; }
    .timeline-item.phase-danger::before  { background: #f85149; }
    .timeline-phase {
      font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;
      color: #8b949e; margin-bottom: 0.25rem;
    }
    .timeline-title { font-weight: 600; font-size: 1.05rem; margin-bottom: 0.25rem; }
    .timeline-desc  { font-size: 0.9rem; color: #8b949e; }
    .timeline-meta  { font-size: 0.8rem; color: #8b949e; margin-top: 0.5rem; display: flex; gap: 1rem; }
    .timeline-meta span { display: inline-flex; align-items: center; gap: 4px; }

    /* === CHECKLIST === */
    .checklist { list-style: none; padding: 0; }
    .checklist li {
      padding: 0.6rem 0;
      border-bottom: 1px solid #21262d;
      display: flex; align-items: flex-start; gap: 10px;
    }
    .checklist input[type="checkbox"] {
      margin-top: 3px; width: 18px; height: 18px;
      accent-color: #3fb950; cursor: pointer;
    }
    .checklist label { cursor: pointer; flex: 1; font-size: 0.92rem; }
    .checklist input[type="checkbox"]:checked + label {
      text-decoration: line-through; color: #484f58;
    }

    /* === HERO === */
    .hero {
      text-align: center; padding: 3rem 0 2rem;
      border-bottom: 1px solid #21262d; margin-bottom: 2rem;
    }
    .hero h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
    .hero p  { font-size: 1.15rem; color: #8b949e; max-width: 600px; margin: 0 auto 1.5rem; }

    /* === STICKY NAV === */
    .sticky-nav {
      position: sticky; top: 0; z-index: 100;
      background: rgba(13,17,23,0.95); backdrop-filter: blur(8px);
      border-bottom: 1px solid #21262d;
      display: flex; gap: 0; overflow-x: auto; padding: 0;
    }
    .sticky-nav a {
      padding: 0.75rem 1.25rem; color: #8b949e; font-size: 0.85rem;
      white-space: nowrap; border-bottom: 2px solid transparent;
      transition: all 0.2s;
    }
    .sticky-nav a:hover, .sticky-nav a.active {
      color: #f0f6fc; text-decoration: none; border-bottom-color: #f0f6fc;
    }

    /* === SECTION === */
    .section { padding: 2rem 0; }

    /* === TAG/BADGE === */
    .tag {
      display: inline-block;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 0.78rem;
      font-weight: 500;
    }
    .tag.red    { background: rgba(248,81,73,0.15); color: #f85149; }
    .tag.amber  { background: rgba(210,153,34,0.15); color: #d29922; }
    .tag.green  { background: rgba(63,185,80,0.15); color: #3fb950; }
    .tag.blue   { background: rgba(88,166,255,0.15); color: #58a6ff; }
    .tag.gray   { background: rgba(139,148,158,0.15); color: #8b949e; }

    /* === DIVIDER === */
    hr { border: none; border-top: 1px solid #21262d; margin: 2rem 0; }

    /* === VERDAD SECTION === */
    .truth-box {
      background: linear-gradient(135deg, rgba(248,81,73,0.08), rgba(210,153,34,0.08));
      border: 1px solid rgba(248,81,73,0.2);
      border-radius: 12px;
      padding: 2rem;
      margin: 2rem 0;
    }
    .truth-box h3 { color: #f85149; }
    .truth-box p  { color: #e6edf3; }

    /* === COST TABLE === */
    .cost-table td:last-child { text-align: right; font-weight: 600; }
    .cost-table tr.total td {
      border-top: 2px solid #30363d;
      font-weight: 700; font-size: 1.05rem;
    }

    /* === RESPONSIVE === */
    @media (max-width: 768px) {
      .canvas-grid { grid-template-columns: 1fr; }
      .canvas-cell.wide { grid-column: span 1; }
      .dimension-row { flex-direction: column; align-items: stretch; gap: 4px; }
      .dimension-label { flex: none; }
      .dimension-desc { margin-left: 0; }
      .hero h1 { font-size: 1.8rem; }
      .sticky-nav a { padding: 0.6rem 0.9rem; font-size: 0.8rem; }
    }

    /* === PRINT === */
    @media print {
      body { background: white; color: black; }
      .card, .canvas-cell, .alert { background: #f6f8fa; border-color: #d0d7de; }
      .sticky-nav { display: none; }
      .progress-bar { border: 1px solid #d0d7de; }
      .score-badge { border: 1px solid; }
      .hero { border-bottom-color: #d0d7de; }
    }
  </style>
</head>
<body>

  <!-- STICKY NAV -->
  <nav class="sticky-nav" id="main-nav">
    <!-- Generar según secciones -->
  </nav>

  <div class="container">

    <!-- HERO -->
    <section class="hero">
      <h1>Validación de Idea</h1>
      <p>Resumen de una línea</p>
      <div class="score-badge green/amber/red">SCORE</div>
    </section>

    <!-- SECCIONES -->
    <!-- Cada sección sigue el mismo patrón -->
    <section class="section" id="section-id">
      <h2>Título de Sección</h2>
      <!-- Contenido -->
    </section>

  </div>

  <script>
    // === NAV HIGHLIGHT ===
    document.querySelectorAll('.sticky-nav a').forEach(link => {
      link.addEventListener('click', function() {
        document.querySelectorAll('.sticky-nav a').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
      });
    });

    // === SCROLL SPY ===
    // (opcional)
  </script>
</body>
</html>
```

## Patrones de chart (Canvas API)

Para los gráficos de score (radiales o donas), usar Canvas API con este patrón:

```javascript
function drawDonut(canvasId, percentage, color) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width, h = canvas.height;
  const cx = w/2, cy = h/2, r = Math.min(w,h)/2 - 10;

  ctx.clearRect(0, 0, w, h);

  // Background arc
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.strokeStyle = '#21262d';
  ctx.lineWidth = 8;
  ctx.stroke();

  // Value arc
  const endAngle = (percentage / 100) * Math.PI * 2 - Math.PI / 2;
  ctx.beginPath();
  ctx.arc(cx, cy, r, -Math.PI/2, endAngle);
  ctx.strokeStyle = color;
  ctx.lineWidth = 8;
  ctx.lineCap = 'round';
  ctx.stroke();

  // Percentage text
  ctx.fillStyle = '#e6edf3';
  ctx.font = 'bold 20px system-ui';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(Math.round(percentage) + '%', cx, cy);
}
```

Usar 3 canvas (o el que corresponda) para los scores principales.
