# Contributing to Trellis

Thanks for wanting to help Trellis grow. It's a small project: a Claude skill, a
Python script, and a static landing page. Contributions of any size are welcome,
from a typo fix to a new vault-building feature.

## What's in the repo

| Path | What it is |
|------|------------|
| `SKILL.md` | The Claude skill: the workflow Claude follows to build a vault |
| `scripts/build_vault.py` | Turns a folder of transcripts into Markdown notes |
| `index.html` | The landing page (self-contained, no build step) |
| `examples/` | Interactive example knowledge graphs |
| `assets/` | The logo (SVG) |

## Setup

You only need Python 3.9+ for the script. There are no dependencies.

```bash
git clone https://github.com/wuisabel-gif/trellis.git
cd trellis
```

To preview the landing page or an example graph, serve the folder and open it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Trying the vault builder

`build_vault.py` takes a folder of transcript text files and writes Markdown
notes. To test it without downloading anything, make a couple of fake transcripts:

```bash
mkdir -p /tmp/t/in && echo "A test transcript about eigenvectors." > /tmp/t/in/abc123.txt
python3 scripts/build_vault.py --input /tmp/t/in --output /tmp/t/vault
cat /tmp/t/vault/*.md
```

Each note should have YAML frontmatter (`title`, `video_id`, `source`, `tags: []`)
and the transcript as the body.

## How to contribute

1. Open an issue first for anything bigger than a small fix, so we can agree on
   the shape before you build it.
2. Fork, branch off `main`, make your change.
3. Keep pull requests focused: one idea per PR.
4. Match the surrounding style. No new dependencies in the script without a
   reason.
5. If you touch `index.html` or an example graph, open it in a browser and
   confirm it still renders in both light surroundings and dark.

## Good first contributions

- Add a new example graph in `examples/` for a channel you know well.
- Improve `build_vault.py`: a flag to write tags from a CSV, better filename
  handling, a `--dry-run` mode.
- Tighten the SKILL.md instructions where they were unclear in practice.
- Fix copy, typos, or broken links.

## Style

- Python: standard library only, type hints where they help, short functions.
- HTML/CSS: keep pages self-contained (no build step, no framework).
- Commits: a short imperative subject line ("Add CSV tag import"), present tense.

## License

By contributing, you agree your work is released under the same license as the
project.
