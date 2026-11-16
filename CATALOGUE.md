# Skill catalogue

Skill packs that belong in **some projects, not every session**. None of them live in this repo or in the global targets. When a project needs a pack, install it from the project root:

```sh
skillshare install -p <source> [-s skill1,skill2]
skillshare sync -p
```

Global (this repo, synced to `~/.claude/skills` and `~/.agents/skills`) keeps the skills you use in any repo: grilling, pr, code-review, tdd, research, herdr-viz, skillshare, treg, agent-browser, untangle, the engineering flow (setup-matt-pocock-skills, to-spec, to-tickets, implement-spec, implement, triage, wayfinder, to-questionnaire, ask-matt), paper-design, and so on.

Token figures are on-demand body plus description, measured before removal.

## Video / HyperFrames (~66.9K)

Install in repos that make or edit videos.

| Skills | Source |
|---|---|
| hyperframes, hyperframes-cli, hyperframes-registry, media-use, reverse-any-video, style-sampling (plus title and transition blocks) | `heygen-com/hyperframes` |
| hyperframes-core, hyperframes-animation, hyperframes-audio, hyperframes-creative, hyperframes-keyframes, hyperframes-studio, general-video, music-to-video, embedded-captions, talking-head-recut | HyperFrames CLI skill bundle |
| watch-video | `coreyhaines31/makerskills/skills/watch-video` |

```sh
npx hyperframes skills update          # full bundle, matched to the CLI version
# or a subset through skillshare:
skillshare install -p heygen-com/hyperframes -s hyperframes,hyperframes-cli,hyperframes-registry,media-use,reverse-any-video,style-sampling
skillshare install -p coreyhaines31/makerskills/skills/watch-video
```

## Reverse engineering (~10.9K)

Install when you're taking apart a binary, an Electron app or a web app.

```sh
skillshare install -p morluto/rea        # reverse-engineer-anything
```

## Obsidian (~9.6K)

Install in vaults and Obsidian plugin repos. The same repo also has `defuddle` (web page to clean Markdown) if a project needs it.

```sh
skillshare install -p obsidianmd/obsidian-skills -s obsidian-markdown,obsidian-bases,obsidian-cli,json-canvas
```

## Frontend app (~8.1K)

Install in React, Next.js and Tailwind apps.

```sh
skillshare install -p shadcn/ui -s shadcn
skillshare install -p pbakaus/impeccable
skillshare install -p vercel/turborepo/skills/turborepo     # monorepos only
```

## Marketing copy (~8.4K)

Install in marketing sites and landing-page repos. The same repo has about 50 more marketing skills (seo-audit, cro, pricing, emails and others).

```sh
skillshare install -p coreyhaines31/marketingskills -s copywriting,copy-editing
```

## claude.ai account skills (not in skillshare)

Claude Code syncs your claude.ai account skills itself, into `~/.claude/skills/synced/<account>/` (docx, pdf, pptx, xlsx, docs, google-workspace, morning, product-guide, raisefunding-linear and others). They are native to Claude and don't belong in this repo; `synced/` is in `.gitignore`. To remove one, delete it on claude.ai.

## Budget effect

Global skillshare skills: 41, **~62.1K on demand and ~2.6K always loaded** (was ~231.9K and ~9.5K, budget 100K). `skillshare analyze` also counts Claude's native `synced/` folder in the `claude` target, which shows ~109.8K there.
