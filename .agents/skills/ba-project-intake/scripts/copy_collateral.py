#!/usr/bin/env python3
"""Copy user-supplied files or directories into an existing project's collateral folder."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for child in sorted(path.rglob("*"), key=lambda item: item.as_posix().lower()):
        if child.is_symlink():
            raise ValueError(f"symlinked collateral is not supported: {child}")
        if child.is_file():
            digest.update(child.relative_to(path).as_posix().encode("utf-8"))
            digest.update(file_digest(child).encode("ascii"))
    return digest.hexdigest()


def equivalent(source: Path, destination: Path) -> bool:
    if source.is_file() and destination.is_file():
        return file_digest(source) == file_digest(destination)
    if source.is_dir() and destination.is_dir():
        return tree_digest(source) == tree_digest(destination)
    return False


def collision_path(destination: Path, digest: str) -> Path:
    if destination.suffix:
        return destination.with_name(f"{destination.stem}-{digest[:8]}{destination.suffix}")
    return destination.with_name(f"{destination.name}-{digest[:8]}")


def validate_sources(supplied: list[str]) -> None:
    for value in supplied:
        source = Path(value).expanduser().resolve()
        if not source.exists():
            raise ValueError(f"collateral does not exist: {source}")
        if source.is_symlink():
            raise ValueError(f"symlinked collateral is not supported: {source}")
        if source.is_dir():
            symlink = next((child for child in source.rglob("*") if child.is_symlink()), None)
            if symlink:
                raise ValueError(f"symlinked collateral is not supported: {symlink}")


def copy_source(source: Path, collateral_dir: Path) -> list[str]:
    source = source.expanduser().resolve()
    collateral_dir = collateral_dir.resolve()
    if not source.exists():
        raise ValueError(f"collateral does not exist: {source}")
    if source.is_symlink():
        raise ValueError(f"symlinked collateral is not supported: {source}")

    try:
        relative_existing = source.relative_to(collateral_dir)
        if source.is_file():
            return [f"collateral/{relative_existing.as_posix()}"]
        return [
            f"collateral/{path.relative_to(collateral_dir).as_posix()}"
            for path in sorted(source.rglob("*"), key=lambda item: item.as_posix().lower())
            if path.is_file()
        ]
    except ValueError:
        pass

    digest = file_digest(source) if source.is_file() else tree_digest(source)
    destination = collateral_dir / source.name
    if destination.exists():
        if equivalent(source, destination):
            if destination.is_file():
                return [f"collateral/{destination.name}"]
            return [
                f"collateral/{path.relative_to(collateral_dir).as_posix()}"
                for path in sorted(destination.rglob("*"), key=lambda item: item.as_posix().lower())
                if path.is_file()
            ]
        destination = collision_path(destination, digest)
        if destination.exists():
            if not equivalent(source, destination):
                raise ValueError(f"deterministic collision destination already differs: {destination}")
            if destination.is_file():
                return [f"collateral/{destination.name}"]
            return [
                f"collateral/{path.relative_to(collateral_dir).as_posix()}"
                for path in sorted(destination.rglob("*"), key=lambda item: item.as_posix().lower())
                if path.is_file()
            ]

    if source.is_file():
        shutil.copy2(source, destination)
        return [f"collateral/{destination.name}"]

    shutil.copytree(source, destination)
    return [
        f"collateral/{path.relative_to(collateral_dir).as_posix()}"
        for path in sorted(destination.rglob("*"), key=lambda item: item.as_posix().lower())
        if path.is_file()
    ]


def copy_sources(project_dir: Path, supplied: list[str]) -> list[str]:
    validate_sources(supplied)
    collateral_dir = project_dir / "collateral"
    collateral_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for value in supplied:
        copied.extend(copy_source(Path(value), collateral_dir))
    return sorted(set(copied), key=str.lower)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    parser.add_argument("sources", nargs="+")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "projects" / args.project_id
    if not project_dir.is_dir():
        parser.error(f"project workspace does not exist: {project_dir}")
    try:
        copied = copy_sources(project_dir, args.sources)
    except ValueError as error:
        parser.error(str(error))
    for path in copied:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
