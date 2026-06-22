---
name: trellis
description: Grow an Obsidian knowledge graph from YouTube. Bulk-download a channel or playlist's transcripts and weave them into linked Markdown notes (topic tags plus [[wikilinks]]) whose Obsidian graph view clusters by subject. Use when the user wants to turn YouTube content into an Obsidian vault, a knowledge graph, linked notes, or a "second brain."
---

# Trellis

A trellis gives a climbing plant something to grow on. This skill gives YouTube
transcripts a structure to grow into: an Obsidian vault whose graph view clusters
videos by topic. A downloader gets the words; Trellis turns them into a connected
garden of notes.

## Instructions

### Step 1: Bulk-download the transcripts

Use a transcript downloader to write one file per video into a folder. The
companion tool is TubeScribe:

```bash
tubescribe "https://www.youtube.com/@3blue1brown" -f txt -o transcripts/ -n 40
```

`-n` caps the count; drop it for the whole channel. Playlists work the same way.
If live fetching is blocked (datacenter IP), run on the user's own machine or use
TubeScribe's browser extension.

Optional, for human-readable note titles instead of video ids, build a
`titles.json` (`{ "<video_id>": "<title>" }`) with `yt-dlp`:

```bash
yt-dlp --flat-playlist --print "%(id)s\t%(title)s" "<url>"
```

### Step 2: Scaffold the vault

Turn each transcript into a Markdown note with frontmatter:

```bash
python scripts/build_vault.py --input transcripts/ --output vault/
# with titles:
python scripts/build_vault.py --input transcripts/ --output vault/ --titles titles.json
```

Each note gets `title`, `video_id`, `source`, `type: transcript`, an empty
`tags: []`, and a "Related:" line ready for links.

### Step 3: Weave the graph (the part that matters)

Edges in an Obsidian graph come from **tags** and **[[wikilinks]]**. This step is
what turns a folder into a knowledge graph. Read the notes and edit them:

1. **Tag each note by topic** - 1-3 tags from a small, consistent vocabulary, in
   frontmatter `tags:` and/or as `#inline-tags` near the top (e.g.
   `#linear-algebra`, `#calculus`, `#neural-networks`). A tight vocabulary makes
   videos cluster cleanly.
2. **Link related videos** - on the `Related:` line add `[[Note Title]]` wikilinks
   to notes that share concepts: a video that builds on another, a series in
   order, a topic referenced across series. These cross-links are what make the
   graph interesting instead of just star-shaped.
3. Leave the transcript body untouched.

Work in batches for large channels. Prefer a few accurate links per note over
many weak ones.

### Step 4: Open in Obsidian

Tell the user:
1. Obsidian, **Open folder as vault**, pick `vault/`.
2. Open **Graph View** (Cmd/Ctrl + G).
3. In graph settings, under **Groups**, color by tag (e.g. `tag:#calculus`) to
   get the clustered look in `examples/example-graph.html`.

## Notes

- Obsidian only graphs `.md` files, which the script already produces.
- Use `-f json` when downloading to keep timestamps for deep-linking into a note.
- `examples/example-graph.html` is a live preview of the end result.
