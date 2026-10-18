# Awesome Mac marketplace

A local app-discovery site built from this repository's catalog, with search, categories, filters, saved favorites, app details, and developer submissions through GitHub.

## Run locally

From the repository root:

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory marketplace/dist
```

Open [http://127.0.0.1:4173](http://127.0.0.1:4173). Stop the server with Ctrl+C.

The site uses plain HTML, CSS, and JavaScript. No package installation or build step is required to run it. Saved apps stay in the current browser; app downloads and purchases take place on developers' websites.

## Refresh the app catalog

After editing the Markdown app lists, run:

```sh
python3 marketplace/scripts/build-catalog.py
python3 marketplace/scripts/check-site.py
node --check marketplace/dist/app.js
```

Commit the updated `marketplace/dist/catalog.json` with the list changes. Deployment metadata is local and excluded from this GitHub repository.

## Source and licensing

Catalog content uses the terms documented in [catalog license](../LICENSES/CATALOG.md) and [source notices](../ATTRIBUTION.md). Original marketplace code uses the repository's [MIT license](../LICENSE).
