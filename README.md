# Lushin Training Library

Every Lushin training session in one place: 472 sessions across 11 categories, each with its key problem, light bulb, scenario, key rules, slide outline, and links to the materials.

## What's in the repo

- `index.html`: the searchable library page. Search by title or need, browse by category, open any session for its links and slides.
- `data/index.json`: the full index, used by the page and by the training-library skill.
- `data/slides.json`: every slide of every deck (slide number, slide type, slide text).
- `data/sessions.csv`: one row per session with every field and link, for opening in Excel or Sheets.
- `data/sprint_programs.csv`: the Sprint programs with their program, overview, role play, reinforcement and QR code folders.
- `thumbs/`: the original title-slide thumbnail for each session (`thumbs/M-017.jpg`).
- `thumbs v2/`: the same set, with title slides re-rendered after every "Presented by" line was changed to Dan Faber. Each session's `thumbnail` field in `data/index.json` says which folder to use; sessions with no thumbnail show a colored title card.
- `scripts/search.py`: command-line search (`python3 scripts/search.py search "cold call" --family=sales`).

## Home buttons

- Sales: Mastery, Sprint (Sales), Sales (Private), Negotiations
- Leadership: Leadership, Sprint (Leadership), Leadership (Private)
- Essentials, Bootcamp & Special Sessions: Essentials, Bootcamp, Special Sessions
- Sort: Unknown

To move a category or rename a button, edit `SECTIONS` at the top of the script in `index.html`.

## Filters on each page

- Sales: Mastery, Sprint, Private, Negotiations
- Leadership: Leadership, Sprint, Private
- Essentials, Bootcamp & Special Sessions: Essentials, Special, Bootcamps
- Sort: Sales topics, Leadership topics
- Every page also has a type filter (Behavior, Attitude, Technique) and a search box.
- The filter chips come from `subs` on each entry in `SECTIONS`.

## Light and dark mode

- The page opens in dark mode.
- The button at the top right switches to light mode, and the browser remembers the choice.

## Password

- The page opens to a password screen. The password is `Training`.
- It's remembered in that browser after the first time.
- To change it, replace `PASS_HASH` in `index.html` with the SHA-256 hash of the new password.
- The password protects the page only. The files in `data/` can still be opened directly by anyone who has their URL, so keep the repo private if that matters.

## Links each session can have

- Beautiful.ai
- Google Slides
- SharePoint folder
- SharePoint deck
- Leader guide
- Drive folder
- The downloaded deck on Dan's Mac (a file path; the page shows it with a copy button)

## Turning on the page

1. Upload everything in this folder to a repo, keeping the folder structure.
2. In the repo, go to Settings, then Pages, and deploy from the `main` branch, root folder.
3. The page loads `data/index.json` and `data/slides.json` from the same repo, so nothing else needs hosting.

## Updating

1. Rebuild `data/index.json` from the Session Master workbook and the slide inventory, keeping the same fields.
2. Regenerate `data/sessions.csv` and `data/sprint_programs.csv` from it.
3. Replace `data/slides.json` if any decks changed.
4. Upload the changed files. `index.html` doesn't change when the data does.

## Index fields

- Session fields:
  - `id`, `title`, `category`, `program`, `type` (Behavior, Attitude or Technique), `created_by`, `family` (sales or leadership)
  - `key_problem`, `light_bulb`, `scenario`, `key_rules`, `slide_count`
- `links` fields:
  - `beautiful_ai`, `google_slides`, `drive_folder`, `sharepoint_folder`, `sharepoint_deck`, `leader_guide`
  - `mac_deck`, `mac_folder`, `other_versions`
- Top-level lists: `sprint_programs`, `other_sharepoint_folders`, `drive_folders_not_in_sharepoint`
