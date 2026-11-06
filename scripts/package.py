"""Empaqueta una skill pública con todas sus referencias."""

from argparse import ArgumentParser
from pathlib import Path
from re import fullmatch
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    if not fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("El slug debe usar minúsculas, números y guiones.")

    skill_dir = ROOT / "skills" / args.slug
    if not (skill_dir / "SKILL.md").is_file():
        parser.error(f"No existe {skill_dir / 'SKILL.md'}")

    files = sorted(path for path in skill_dir.rglob("*") if path.is_file())
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{args.slug}.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED) as bundle:
        for path in files:
            bundle.write(path, arcname=(Path(args.slug) / path.relative_to(skill_dir)).as_posix())
    print(f"{archive} ({len(files)} archivos)")


if __name__ == "__main__":
    main()
