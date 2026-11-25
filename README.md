# Brandon Smith — game design portfolio

A static, multipage game design portfolio migrated from [Brandon's Wix portfolio](https://bsmith5701.wixsite.com/brandonsmithdesign). The site uses a blue theme, project rows, and case-study layouts. No framework or runtime build is required to view the site.

## Run and edit

Open `index.html`, or serve this folder with a local static server. Edit page content directly in the HTML files. Shared behavior lives in `index.js`; styles live in `sass/`, compiled to `css/style.css`.

- `npm install` installs development tools.
- `npm run compile:scss` watches Sass changes.
- `npm run build` compiles, prefixes, and compresses CSS.

Dart Sass replaces the old Node Sass dependency, which does not support the installed Node 24 runtime. The existing Sass partial structure is unchanged. Legacy Sass import deprecation notices are non-blocking.

## Project pages

1. `charons-corner.html`: Charon's Corner — game design leadership, level flow, and navigation support.
2. `project-dreamscape.html`: Project Dreamscape — enemy roles, combat balancing, and iteration.
3. `in-the-flesh.html`: In the Flesh — harvesting, destructible terrain, traversal, and designer tools, followed by a technical deep dive.
4. `birds-of-impalitism.html`: Birds of Impalitism — player progression and save/load systems.
5. `psycorp.html`: Psycorp — narrative tools and runtime systems for a project in development.

## Migration notes (September 19, 2026)

- Project images and original animated GIFs are local in `assets/png`, `assets/jpeg`, and `assets/gif`. Identical downloads are shared between pages. The media archive contains 50 unique files (about 131 MB), so galleries and project previews use lazy loading. GIFs retain their original animation; video conversion is a possible later optimization.
- The two design documents are local PDFs in `assets/documents`. No résumé PDF is currently present; the homepage CTA area includes a TODO for adding one. Embedded PDFs include direct open links for browsers without PDF viewing support.
- All eight distinct YouTube videos on the four complete Wix case studies are embedded with responsive players, descriptive titles, lazy loading, and direct YouTube fallback links. Playback still depends on YouTube and the source video's availability.
- `assets/media-manifest.json` records original download URLs, local paths, byte sizes, and SHA-256 hashes. `assets/embed-manifest.json` records project sources and external video embeds.
- Psycorp's Wix detail page duplicates Dreamscape's overview, contributions, metadata, images, and Steam link. Its migrated page uses only the distinct description, role, engine, team size, and artwork from the Wix project index. Add Psycorp-specific contributions and media when available.
- The source uses both "Birds of Impalitism" and "Birds of Impalatism". Navigation retains the portfolio's title, while the verified itch.io URL keeps its published spelling.
- The homepage positions Brandon as a Game Designer specializing in systems, gameplay, and technical design, supported by Unity/C# implementation. Personal details come from the public home/about pages. No degree completion date, email address, or additional social profiles have been invented.
- The template's inactive form is replaced with LinkedIn, itch.io, and GitHub profile links. A contact form will need a real submission service if added later.
- Only relevant portfolio media are shown; Wix chrome and social-icon duplicates are omitted. Source project descriptions and process explanations are preserved, with heading levels normalized for the case-study layout.

## License and attribution

This portfolio is adapted from Dopefolio by Ram Maheshwari and is licensed under GPL-3.0. See [LICENSE](LICENSE).
