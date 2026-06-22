<p align="center">
  <img src="assets/logo.svg" alt="Trellis logo" width="120" height="120" />
</p>

<h1 align="center">Trellis</h1>

<p align="center"><b>Grow an Obsidian knowledge graph from YouTube.</b></p>

<p align="center">
  <a href="https://wuisabel-gif.github.io/trellis/"><img src="https://img.shields.io/badge/demo-live-43d17f?style=flat-square" alt="Live demo" /></a>
  <img src="https://img.shields.io/badge/Claude-skill-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude skill" />
  <img src="https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/Obsidian-vault-7C3AED?style=flat-square&logo=obsidian&logoColor=white" alt="Obsidian" />
  <img src="https://img.shields.io/badge/deps-none-555?style=flat-square" alt="No dependencies" />
</p>

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

## Why Obsidian

[Obsidian](https://obsidian.md) is one of the most popular note-taking apps for
building a "second brain," with millions of users and a famously devoted
community. It's free for personal use, and it stores everything as plain Markdown
files on your own disk - no account, no cloud lock-in, no proprietary format. The
notes Trellis writes are just text files you fully own.

What makes it the right home for transcripts is the way it connects things:

- **`[[Wikilinks]]` and backlinks.** Link one note to another and Obsidian builds
  the reverse link automatically. A web forms as you write.
- **Graph View.** Obsidian draws every note and link as an interactive graph (the
  look the examples here imitate). Clusters appear on their own, and you can
  literally see how ideas across dozens of videos relate.
- **Tags and search.** Group notes by `#topic`, then filter the graph by tag to
  watch a subject light up.
- **Plugins.** A large community ecosystem adds everything from spaced repetition
  to canvas boards on top of your notes.

A channel's worth of transcripts is a pile of disconnected text. Inside Obsidian,
with a few tags and links, it becomes something you can explore - which is exactly
the gap Trellis fills.

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
