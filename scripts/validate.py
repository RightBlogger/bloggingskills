#!/usr/bin/env python3
"""Structural validator for the bloggingskills collection. No dependencies.

Run: python3 scripts/validate.py

Checks every skill's frontmatter, line budget, body hygiene (no em dashes or
unicode arrows in reader-facing prose), that cross-references resolve to real
skills, that the bundled ai-tells.md copies stay in sync, and that the manifests
and VERSIONS table are consistent. Exits non-zero if anything fails.
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

errors = []
warnings = []

EM_DASH = "—"
ARROWS = ["→", "⇒"]
# Skills referenced before they were built. Flag any "see <name>" that points here.
RETIRED = ["content-plan", "copy-edit", "repurpose"]

skill_names = sorted(
    d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))
)


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


for name in skill_names:
    path = os.path.join(SKILLS, name, "SKILL.md")
    if not os.path.isfile(path):
        errors.append(f"{name}: missing SKILL.md")
        continue
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()

    if len(lines) >= 500:
        errors.append(f"{name}: SKILL.md is {len(lines)} lines (must be < 500)")

    fm, _ = split_frontmatter(text)
    if fm is None:
        errors.append(f"{name}: no YAML frontmatter")
        continue

    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not m:
        errors.append(f"{name}: frontmatter missing 'name'")
    elif m.group(1).strip() != name:
        errors.append(f"{name}: name '{m.group(1).strip()}' != folder '{name}'")

    dm = re.search(r'description:\s*"(.*?)"', fm, re.S)
    if not dm:
        errors.append(f"{name}: missing or unquoted 'description'")
    else:
        dl = len(dm.group(1))
        if dl > 1024:
            errors.append(f"{name}: description {dl} chars (max 1024)")
        elif dl < 40:
            warnings.append(f"{name}: description only {dl} chars (thin trigger)")

    if not re.search(r"version:\s*\S+", fm):
        errors.append(f"{name}: metadata.version missing")

    # Body hygiene: no em dashes or unicode arrows after the frontmatter.
    seen_delims = 0
    for i, line in enumerate(lines, 1):
        if line.strip() == "---":
            seen_delims += 1
            continue
        if seen_delims < 2:
            continue
        if EM_DASH in line:
            errors.append(f"{name}: em dash in body line {i}: {line.strip()[:60]}")
        for a in ARROWS:
            if a in line:
                errors.append(f"{name}: unicode arrow in body line {i}: {line.strip()[:60]}")

    # Related skills must resolve to real skills.
    rel = None
    for i, line in enumerate(lines):
        if line.strip().lower() == "## related skills":
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    rel = lines[j].strip()
                    break
            break
    if rel:
        for tok in (t.strip() for t in rel.split("·")):
            if tok and tok not in skill_names:
                errors.append(f"{name}: Related skills points to unknown skill '{tok}'")
    else:
        warnings.append(f"{name}: no 'Related skills' line found")

    for r in RETIRED:
        if re.search(r"\bsee " + re.escape(r) + r"\b", text):
            errors.append(f"{name}: references unbuilt skill '{r}'")

# Bundled ai-tells.md copies must match the canonical house-style copy byte for byte.
canonical = os.path.join(SKILLS, "house-style", "references", "ai-tells.md")
bundled = [
    os.path.join(SKILLS, "humanize", "references", "ai-tells.md"),
    os.path.join(SKILLS, "article", "references", "ai-tells.md"),
]
if os.path.isfile(canonical):
    digest = hashlib.sha256(open(canonical, "rb").read()).hexdigest()
    for c in bundled:
        if not os.path.isfile(c):
            errors.append(f"ai-tells.md copy missing: {os.path.relpath(c, ROOT)}")
        elif hashlib.sha256(open(c, "rb").read()).hexdigest() != digest:
            errors.append(f"ai-tells.md out of sync: {os.path.relpath(c, ROOT)} (run: cp {os.path.relpath(canonical, ROOT)} {os.path.relpath(c, ROOT)})")
else:
    errors.append("canonical ai-tells.md missing in house-style/references/")

# Manifests must be valid JSON.
for rel in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
    try:
        json.load(open(os.path.join(ROOT, rel), encoding="utf-8"))
    except Exception as e:
        errors.append(f"{rel}: invalid JSON ({e})")

# VERSIONS.md must list every skill.
vpath = os.path.join(ROOT, "VERSIONS.md")
if os.path.isfile(vpath):
    vtext = open(vpath, encoding="utf-8").read()
    for name in skill_names:
        if f"| {name} " not in vtext:
            errors.append(f"VERSIONS.md missing a row for '{name}'")
else:
    errors.append("VERSIONS.md missing")

# Routing test cases must reference real skills.
rpath = os.path.join(ROOT, "tests", "routing-cases.json")
if os.path.isfile(rpath):
    try:
        cases = json.load(open(rpath, encoding="utf-8"))
        if not isinstance(cases, list) or not cases:
            errors.append("tests/routing-cases.json: expected a non-empty list")
        else:
            for k, case in enumerate(cases):
                if "prompt" not in case or "expect" not in case:
                    errors.append(f"routing-cases[{k}]: missing 'prompt' or 'expect'")
                elif case["expect"] not in skill_names:
                    errors.append(f"routing-cases[{k}]: expects unknown skill '{case['expect']}'")
    except Exception as e:
        errors.append(f"tests/routing-cases.json: invalid JSON ({e})")

print(f"skills checked: {len(skill_names)}")
for w in warnings:
    print("WARN:", w)
if errors:
    for e in errors:
        print("FAIL:", e)
    print(f"\n{len(errors)} error(s)")
    sys.exit(1)
print("All checks passed.")
