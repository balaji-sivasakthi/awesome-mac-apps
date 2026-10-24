## App or correction

Describe the change and why it belongs. Submit one app per PR.

## Submission details

- Official website:
- List and category:
- macOS requirements and Apple silicon / Intel support:
- Download or installation link:
- Pricing model and material paid features:
- Source repository and license (if open source):
- Your affiliation (or None):

## Evidence and validation

Link official sources supporting the description, compatibility, pricing, and any icons used.

- [ ] Read CONTRIBUTING.md and searched existing entries, issues, and PRs.
- [ ] Used a four-column directory row with a factual description, availability, and resources in the appropriate category.
- [ ] Placed the new entry alphabetically without reordering unrelated entries.
- [ ] Used official links without tracking or referrals and checked them manually.
- [ ] Rebuilt the marketplace catalog with `python3 marketplace/scripts/build-catalog.py` and committed `marketplace/dist/catalog.json`.
- [ ] Ran `python3 marketplace/scripts/check-site.py`, `python3 scripts/check_docs.py`, and `git diff --check`.
- [ ] Understand catalog additions are licensed under CC BY 4.0.
