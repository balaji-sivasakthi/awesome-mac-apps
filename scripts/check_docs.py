"""Validate local Markdown links and catalog icon references without network access."""

from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ("README.md", "command-line-apps.md", "editor-plugin.md")
errors = []


def unfenced(text):
    return re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M | re.S)


def anchors(text):
    found = set()
    counts = {}
    for heading in re.findall(r"^#{1,6} (.+)$", unfenced(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        number = counts.get(slug, 0)
        found.add(f"{slug}-{number}" if number else slug)
        counts[slug] = number + 1
    return found


for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.relative_to(ROOT).parts:
        continue
    content = unfenced(path.read_text())
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
        target = target.strip().strip("<>")
        if urlsplit(target).scheme or target.startswith("//"):
            continue
        filename, _, fragment = target.partition("#")
        destination = path.parent / unquote(filename) if filename else path
        if not destination.is_file():
            errors.append(f"{path.relative_to(ROOT)}: missing file {target}")
        elif fragment and unquote(fragment) not in anchors(destination.read_text()):
            errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    definitions = set(re.findall(r"^\[([^\]]+ Icon)\]:", content, re.M))
    used = set(re.findall(r"\]\[([^\]]+ Icon)\]", content))
    for reference in sorted(used - definitions):
        errors.append(f"{path.relative_to(ROOT)}: undefined icon {reference}")

counts = {}
for name in CATALOGS:
    path = ROOT / name
    if not path.is_file():
        errors.append(f"Missing catalog: {name}")
        continue
    content = path.read_text()
    rows = re.findall(r"^\| \[[^\]]+\]\(https?://.*$", content, re.M)
    counts[name] = len(rows)
    for number, row in enumerate(rows, 1):
        columns = re.split(r"(?<!\\)\|", row)[1:-1]
        if len(columns) != 4:
            errors.append(f"{name}: app row {number} must have four columns")
        elif any(not column.strip() for column in columns):
            errors.append(f"{name}: app row {number} contains an empty cell")
        else:
            app_url = re.search(r"\]\((https?://[^)]+)\)", columns[0])
            website = re.search(r"\[Website\]\((https?://[^)]+)\)", columns[3])
            if not website or not app_url or website.group(1) != app_url.group(1):
                errors.append(f"{name}: app row {number} needs its official Website link in Resources")
    if re.search(r"^\s*[*-] \[[^\]]+\]\(https?://", content, re.M):
        errors.append(f"{name}: app entries must use directory table rows")
    if not counts[name]:
        errors.append(f"Empty catalog: {name}")

manifest_path = ROOT / "data/consolidation.json"
if manifest_path.is_file():
    manifest = json.loads(manifest_path.read_text())
    sources = {source["full_name"]: source for source in manifest["sources"]}
    if len(sources) != 5:
        errors.append("Consolidation must record five distinct source collections")
    additions = manifest["additions"]
    if len(additions) != manifest["new_entries"]:
        errors.append("Consolidation addition count does not match its manifest")
    if sum(source["added_entries"] for source in sources.values()) != len(additions):
        errors.append("Consolidation source totals do not match its additions")
    all_catalogs = "\n".join((ROOT / name).read_text() for name in CATALOGS)
    for addition in additions:
        escaped_name = addition["name"].replace("|", r"\|")
        marker = f'[{escaped_name}]({addition["url"]})'
        if marker not in all_catalogs:
            errors.append(f"Consolidated listing missing: {addition['name']}")
        source = sources.get(addition["origin"])
        if not source or addition["commit"] != source["snapshot_commit"]:
            errors.append(f"Consolidation source snapshot mismatch: {addition['name']}")

exclusions_path = ROOT / "data/exclusions.json"
if exclusions_path.is_file():
    exclusions = json.loads(exclusions_path.read_text())
    catalog_names = {
        name.casefold()
        for catalog in CATALOGS
        for name in re.findall(r"^\| \[(.*?)\]\(https?://", (ROOT / catalog).read_text(), re.M)
    }
    for name in exclusions["app_names"]:
        if name.casefold() in catalog_names:
            errors.append(f"Excluded notch competitor has been reintroduced: {name}")
    if "notchdude" not in catalog_names:
        errors.append("NotchDude must remain in the catalog")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
for name, count in counts.items():
    print(f"{name}: {count} listing entries")
print("Documentation checks passed. Review external links, duplicates, and ordering manually.")
