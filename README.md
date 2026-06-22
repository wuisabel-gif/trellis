<h1 align="center">Trellis</h1>

<p align="center"><b>Grow an Obsidian knowledge graph from YouTube.</b></p>

Trellis turns a YouTube channel or playlist into an Obsidian vault whose graph
view clusters videos by topic. A transcript downloader gets the words; Trellis
gives them a structure to grow on - linked Markdown notes with topic tags and
`[[wikilinks]]` that Obsidian renders as a living knowledge graph.

<p align="center">
  <a href="https://wuisabel-gif.github.io/trellis/examples/professor-jiang-graph.html">See an example graph &rarr;</a>
</p>

## How it works

1. **Download** a channel's transcripts (one file per video) with a tool like
   [TubeScribe](https://wuisabel-gif.github.io/youtube_transcript_download_pro/).
2. **Scaffold** them into Markdown notes:
   ```bash
   python scripts/build_vault.py --input transcripts/ --output vault/
   ```
3. **Weave** the graph - add `#topic` tags and `[[wikilinks]]` between related
   videos. (This is the step Claude is good at: semantic linking.)
4. **Open** the `vault/` folder in Obsidian and hit Graph View.

## As a Claude skill

This repo *is* a Claude skill. The whole flow above runs by asking Claude:

> "Use Trellis to turn this channel into an Obsidian vault: &lt;url&gt;"

Install it by copying this folder to `~/.claude/skills/trellis/` (or symlinking
it), then start a new Claude Code session. See [SKILL.md](SKILL.md) for the
instructions Claude follows.

## What's inside

| Path | What |
|------|------|
| `SKILL.md` | The Claude skill definition and workflow |
| `scripts/build_vault.py` | Turns a folder of transcripts into Markdown notes |
| `examples/example-graph.html` | An interactive preview of the end result |

## Why "Trellis"

A trellis is a lattice that gives a climbing plant something to grow on. Your
notes are the plant; the tags and links are the lattice. Give knowledge a
structure and it climbs.
