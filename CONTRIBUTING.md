# Developer submission guide

Thanks for helping grow Awesome Mac Apps. I’m Balaji, and I maintain this collection. If you’ve built something useful for Mac, you’re welcome to submit it — free, open source, or paid.

Send a pull request or use the [app suggestion form](https://github.com/balaji-sivasakthi/awesome-mac-apps/issues/new?template=app-suggestion.yml). There’s no fee to submit an app. I review suggestions for usefulness, accuracy, and fit with the list.

## Eligibility

- Offer an app that runs on macOS, a Mac-compatible command-line tool, or an editor plugin useful to Mac users.
- Provide an official website or maintainer repository with a working download or installation path.
- State macOS requirements and Apple silicon or Intel support in the submission, supported by official documentation.
- Identify whether the app is free, freemium, paid once, subscription-based, or a trial.
- Use a concise factual description and disclose if you develop, work for, or promote the app.
- Exclude pirated software, misleading claims, referral links, and entries with no usable Mac version.

Apps do not need to have launched in 2026. Existing imported entries may predate these guidelines; new submissions should meet them.

## Submit your app

### Option 1: Open an issue

Use the [Suggest an app form](https://github.com/balaji-sivasakthi/awesome-mac-apps/issues/new?template=app-suggestion.yml). Supply the app name, official URL, proposed category, one-sentence description, pricing model, macOS and processor requirements, an installation link, and your affiliation. Include a source-code URL if claiming the app is open source.

I’ll use these details to review your app and prepare an entry if it fits. Opening an issue starts the review; it doesn’t guarantee a listing.

### Option 2: Open a pull request

1. Search the catalog and [existing issues and PRs](https://github.com/balaji-sivasakthi/awesome-mac-apps/issues) for your app to avoid duplicates.
2. Fork [this repository](https://github.com/balaji-sivasakthi/awesome-mac-apps/fork) and create a branch such as `add-your-app`.
3. Edit the appropriate English list: `README.md` for apps, `command-line-apps.md` for CLI tools, or `editor-plugin.md` for editor extensions.
4. Choose the closest existing category and place your entry alphabetically among comparable entries. Keep the change focused on one app; avoid reordering unrelated imported entries.
5. Add a four-column table row with the app link, a short description, availability, and useful project links. Use official HTTPS URLs without tracking or referral parameters.
6. Run `python3 scripts/check_docs.py` and `git diff --check` from the repository root. Manually open the links you add.
7. Commit your change, push your branch to your fork, and open a pull request targeting this repository's `main` branch.
8. Complete the PR template, including compatibility, pricing, sources, and affiliation. Respond to any review feedback.

English is sufficient; translated entries are not required here. If adding a category, update that document's contents links too.

## Entry format

Add a row to the existing category table. Keep these four columns in order:

| App | Purpose | Availability | Resources |
| --- | --- | --- | --- |
| [App Name](https://example.com/) | A short sentence explaining what the app does. | Free + Pro | [Website](https://example.com/) · [Source](https://github.com/owner/project) |

Copy this row and replace the example details:

```markdown
| [App Name](https://example.com/) | A short description. | Free + Pro | [Website](https://example.com/) · [Source](https://github.com/owner/project) |
```

- **App:** link the product name to its official website or maintainer repository.
- **Purpose:** explain the main task in one factual sentence. Escape literal pipe characters as `\|` so they don't break the table.
- **Availability:** use `Free`, `Free + Pro`, `Paid once`, `Subscription`, `Trial`, or `See website` when details aren't verified. Existing `Free option` labels indicate a listed free version or free personal-use license.
- **Resources:** start with a `Website` link to the same official product page or maintainer repository used in the App column. Add links such as `Source` or `App Store`, separated by ` · `; add `Native` only with supporting evidence.

Keep paid-feature limits clear in your submission. A trial-only app should use `Trial` rather than `Free`. Source links should point to the app's public code repository; identify its license in the issue or PR. No icon badges are needed.

Avoid exact prices and version numbers unless necessary. Don't make unsupported claims about security, privacy, performance, or competing apps.

## Review criteria

I look for a working Mac download, a clear description, the right category, and honest details about pricing and affiliation. Explain what your app helps someone do and link to the official information. A screenshot is welcome if it makes the app easier to understand. Listings are editorial selections; inclusion doesn’t mean I’ve audited the app.

## Corrections and discontinued apps

Use the correction issue template or send a focused PR for broken links, inaccurate descriptions, or discontinued apps. Include an official source explaining the change. An app may be listed in more than one relevant category in the imported catalog; avoid adding unnecessary duplicates in new submissions.

## Licensing and conduct

Catalog additions to the three app lists are contributed under [CC BY 4.0](LICENSES/CATALOG.md). Original tooling, guidelines, and templates use the [MIT license](LICENSE). Imported content retains the notices documented in [ATTRIBUTION.md](ATTRIBUTION.md). Each app retains its own software license and trademarks.

Be respectful, disclose affiliations, and keep discussion focused on the submission. I may decline or remove entries that are misleading, broken, spammy, or outside the scope of this collection.
