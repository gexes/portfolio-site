# Portfolio Case Study Refactor Brief

Use this file as the working brief for refactoring my GitHub Pages portfolio.

The goal is not to redesign the entire site from scratch or force every page into a rigid template. The goal is to make each project page read like a stronger Technical Designer case study by improving depth, evidence, visual rhythm, and readability.

## Core Goal

Refactor the five main project pages so they communicate:

- what the project is
- what my role was
- what I personally owned
- what technical or design problem I was solving
- what went wrong during development
- what I changed
- what the result was
- why the work matters for a Technical Designer role

This should be done using natural developer language, not corporate case-study language.

The pages should feel like I am explaining my process to another developer, designer, recruiter, or hiring manager who wants to understand how I think.

## Important Direction

Do not turn the pages into long diaries.

Do not try to showcase every single feature I worked on.

Each project should focus on 2-3 representative systems or design problems that best prove what kind of Technical Designer I am. The rest of my work should be summarized in a supporting contributions section and linked to documentation where available.

The portfolio should work at three depths:

1. 10 seconds: the viewer understands the game, my role, and what I owned.
2. 2-4 minutes: the viewer sees strong visual case studies that prove my thinking and implementation ability.
3. Deep dive: the viewer can open documentation, videos, GitHub links, or additional development material.

## Global Page Structure

Each project page should roughly follow this reading flow. This is a structure guide, not a strict visual template.

```text
PROJECT HERO
- Large GIF, video, or gameplay image
- Project title
- My role
- One natural sentence explaining the game and my main responsibility
- Buttons for playable build, Steam/itch, GitHub, documentation, or trailer when available

PROJECT AT A GLANCE
- Role
- Team size
- Engine/tools
- Duration
- My focus areas
- Short "What I Owned" paragraph

FEATURED WORK
- 2-3 selected case-study sections
- Each section should show one important system, design problem, or technical challenge
- These should be the main proof of my Technical Designer skill

SUPPORTING CONTRIBUTIONS
- Short list of other meaningful systems or responsibilities
- Keep this compact
- Link to documentation when available

PROJECT TAKEAWAY
- 1-2 short paragraphs about what the project changed in my thinking
- Must be specific to the project
- Avoid generic teamwork/reflection language

GALLERY / DEVELOPMENT MATERIAL
- Images, GIFs, diagrams, tools, blockouts, editor screenshots, gameplay clips
- Every asset should have a short caption explaining why it matters

PREVIOUS / NEXT PROJECT
- Keep navigation consistent
```

## Writing Style

Use plain, natural language. Avoid inflated words like "robust", "seamless", "leveraged", "utilized", "cutting-edge", or "innovative" unless they are already part of the page and truly needed.

Prefer this tone:

```text
The first version technically worked, but it did not scale once more actors and dialogue moments were added. The problem was not just saving data. It was deciding which system owned that state and making sure the scene could rebuild itself in a predictable way.
```

Avoid this tone:

```text
Implemented a robust scalable framework for seamless narrative gameplay integration.
```

The writing should explain:

- what I was trying to build
- what became difficult
- what I tried first
- why that was not enough
- what I changed
- what the result allowed designers or players to do

Use short paragraphs. Aim for 2-4 sentences per paragraph.

## Visual Rhythm

Avoid long walls of text. The page should alternate between seeing and understanding.

Preferred rhythm:

```text
Large GIF or gameplay image
Short explanation
Editor screenshot or diagram
Short explanation
Runtime result
Small takeaway
```

Avoid:

```text
Text
Text
Text
Text
Text
Image
Text
Text
Text
```

Every major case-study section should include at least one visual placeholder if the final image/GIF does not exist yet.

Use placeholder labels that tell me exactly what to capture later, for example:

```text
[GIF PLACEHOLDER: Glikit actor setup workflow from empty actor definition to runtime spawn]
[SCREENSHOT PLACEHOLDER: Chunk Grid Baker editor view showing authored voxel layout]
[GIF PLACEHOLDER: Follower enemy before/after tuning comparison]
```

## Technical Designer Positioning

The portfolio should make me look like:

```text
A systems-focused Technical Designer who can design gameplay, implement it, build tools for other designers, diagnose technical problems, iterate from testing, document pipelines, and work inside team production.
```

Each project should prove a different part of that identity.

## Project-Level Focus

### Psycorp

Primary argument:

```text
I can build designer-facing tools and gameplay pipelines that connect narrative, actors, cameras, objectives, flags, saves, and runtime systems.
```

Suggested featured work:

1. Glikit / designer authoring pipeline
2. Narrative, actor, and camera integration through Yarn and runtime coordinators
3. Persistent game state and scene restoration

What this page should leave the viewer thinking:

```text
Brandon can build infrastructure that other designers use, not just isolated gameplay features.
```

Evidence to prioritize:

- editor GIFs
- Yarn command examples
- actor/camera/objective pipeline diagrams
- save/load restoration GIF
- screenshots of tools designers interact with
- before/after examples of fragile scene setup becoming a reusable workflow

Suggested writing angle:

```text
As Psycorp grew, the hard part became less about making one scene work and more about creating a workflow that would keep working as more writers, actors, cameras, objectives, and state changes depended on it.
```

### In the Flesh

Primary argument:

```text
I can make unusual gameplay ideas technically viable through systems design, performance problem-solving, and editor tooling.
```

Suggested featured work:

1. Destructible voxel environment prototype
2. CPU/GPU performance architecture for rendering and physics
3. Chunk Grid Baker / level authoring workflow

What this page should leave the viewer thinking:

```text
Brandon understands enough engineering to make complex gameplay systems playable and authorable.
```

Evidence to prioritize:

- drilling/destruction gameplay GIFs
- before/after performance explanation
- compute shader / indirect instancing diagram
- dirty chunk / deferred collider rebuild diagram
- Chunk Grid Baker editor screenshots
- authored environment layout examples

Suggested writing angle:

```text
The design goal was simple: let the player carve through a dense destructible environment. The technical problem was that the environment could contain thousands of blocks, and treating each one like a normal object quickly became too expensive.
```

### Project Dreamscape

Primary argument:

```text
I can design and tune gameplay systems, enemy roles, combat pressure, and player-facing iteration.
```

Suggested featured work:

1. Defining enemy combat roles
2. Follower / Charger / Golem iteration
3. Testing, tuning, and balancing decisions

What this page should leave the viewer thinking:

```text
Brandon does not just program systems. He understands gameplay feel, pressure, counterplay, and iteration.
```

Evidence to prioritize:

- enemy behavior GIFs
- before/after tuning comparisons
- small stat tables showing changed values
- short clips showing combat readability
- notes from testing or team feedback
- diagrams explaining enemy roles in an encounter

Suggested writing angle:

```text
The enemies were functioning, but not all of them were doing their job in combat. I focused on whether each enemy created the kind of pressure it was supposed to create, then tuned their stats and behavior around that role.
```

### Charon's Corner

Primary argument:

```text
I can build level systems and team-facing workflows around high-speed gameplay.
```

Suggested featured work:

1. Designing around high-speed movement
2. Spline track / level framework
3. Guiding, checkpoint, and wrong-way support systems

What this page should leave the viewer thinking:

```text
Brandon can turn design direction into repeatable systems that help a team build levels more consistently.
```

Evidence to prioritize:

- gameplay clips of high-speed traversal
- spline/path editor screenshots
- diagrams of checkpoint and wrong-way logic
- before/after level readability examples
- designer workflow screenshots
- examples of how the system helped build or maintain levels

Suggested writing angle:

```text
The challenge was not only making one fast level feel good. The challenge was creating rules and tools that helped the team build readable high-speed spaces without every section becoming a custom one-off.
```

### Birds of Impalitism

Primary argument:

```text
I can build the invisible game-state systems that keep a project reliable across scenes, saves, and progression.
```

Suggested featured work:

1. Save architecture
2. Multi-scene persistence
3. World restoration / validation

What this page should leave the viewer thinking:

```text
Brandon understands state, dependencies, and the less flashy systems that make games stable.
```

Evidence to prioritize:

- save/load diagrams
- persistence flow screenshots
- gameplay GIFs showing progression being retained
- state restoration examples
- any debugging or validation tools
- short explanation of what would break without the system

Suggested writing angle:

```text
The important work here was mostly invisible to the player. The system needed to remember progression, restore the right world state, and avoid letting scenes disagree with the player's save data.
```

## Supporting Contributions Section

Each page should include a compact section for meaningful work that does not get a full case-study section.

Example:

```text
Other Contributions

- Event sequencing
- Objective tracking
- Input gating
- UI architecture
- Checkpoint handling
- Encounter tooling
- Dialogue commands
- Designer documentation

[View Technical Documentation]
```

This section should not become the main event. It exists to show that the featured case studies are selected examples, not the full extent of the work.

## Documentation Links

Keep documentation links, PDFs, design docs, and technical writeups where they exist.

The page should treat documentation as the deep-dive layer.

Use language like:

```text
For a deeper breakdown of the system architecture and designer-facing workflow, view the technical documentation.
```

Avoid making the page itself carry every detail from the docs.

## Asset Placeholder Rules

If the final images or GIFs are not available yet, add clear placeholders with capture instructions.

Good placeholder:

```text
[GIF PLACEHOLDER: Show the designer opening Glikit, creating an Actor Definition, assigning a prefab, then triggering the actor through Yarn in-game.]
```

Bad placeholder:

```text
[GIF placeholder]
```

Every placeholder should tell me exactly what I need to record later.

## What To Change In Existing Pages

When refactoring the current pages:

- preserve the existing site style unless a layout issue makes it hard to read
- improve case-study structure and content depth
- avoid rewriting everything into generic marketing copy
- reduce huge contribution lists near the top
- replace them with a short "What I Owned" section
- add or improve visual placeholders
- make each featured section tell a small development story
- use diagrams where they clarify system relationships
- make captions explain why an image matters
- keep mobile readability clean
- keep navigation between projects consistent

## What Not To Do

Do not:

- remove important existing project information without preserving it somewhere
- make every project use identical wording
- turn the site into a giant blog
- bury the actual game under too much explanation
- over-explain basic implementation details
- use buzzwords to sound more senior
- invent features, metrics, tools, or outcomes that are not already supported by the project
- rewrite the whole website identity unless required
- break GitHub Pages paths, asset links, or navigation

## Suggested Implementation Strategy For Codex

Use this brief to refactor the portfolio in one pass, but keep the changes controlled.

Recommended steps:

1. Inspect the current project page structure, shared CSS, and asset folders.
2. Identify the five main project pages and their current sections.
3. Update the shared layout/CSS only if needed to support better case-study rhythm.
4. Refactor each page around:
   - hero
   - project at a glance
   - what I owned
   - featured work
   - supporting contributions
   - takeaway
   - gallery/development material
   - documentation links
5. Add specific image/GIF placeholders where final assets are missing.
6. Preserve existing links, media, project titles, and page routes.
7. Run or preview the site locally if possible.
8. Check desktop and mobile layout for readability.

## Single-Prompt Version

Use this prompt with Codex/Sol Medium from the root of the GitHub Pages repository:

```text
I want you to refactor my portfolio project pages using PORTFOLIO_CASE_STUDY_REFACTOR_BRIEF.md as the source of truth.

Do not redesign the entire site from scratch. Preserve the existing visual identity, routes, project titles, links, and overall style unless something needs to change for readability.

The goal is to improve the depth and readability of the five main project pages so they feel like cohesive Technical Designer case studies. Each page should be understandable at three depths: 10 seconds, 2-4 minutes, and deep documentation.

Please inspect the current HTML/CSS/assets first, then update the five main project pages around:

- project hero
- project at a glance
- short "What I Owned" section
- 2-3 featured work sections
- supporting contributions
- project takeaway
- gallery/development material
- documentation links
- previous/next navigation

Do not try to showcase every feature. Choose representative systems for each project based on the brief:

- Psycorp: designer tools, narrative/actor/camera integration, persistent state
- In the Flesh: destructible voxels, performance architecture, Chunk Grid Baker/editor tooling
- Project Dreamscape: enemy roles, combat tuning, iteration
- Charon's Corner: high-speed level design, spline framework, checkpoint/wrong-way systems
- Birds of Impalitism: save architecture, persistence, world restoration

Use natural developer language. Explain what I was trying to build, what became difficult, what changed, and what the result allowed. Avoid generic marketing wording and avoid overusing "Problem / Solution / Outcome" as visible headings.

Where final media is missing, add specific placeholders that describe exactly what GIF/image I need to capture later. Do not use vague labels like "GIF placeholder."

Keep paragraphs short, improve visual rhythm, and make sure each visual has a caption explaining why it matters.

After editing, summarize what files changed, what structure each page now follows, and what assets I still need to capture.
```

## Success Criteria

The refactor is successful if:

- each project page feels like part of the same Technical Designer portfolio
- each project still has its own argument and identity
- the pages are easier to skim
- the pages show more evidence without becoming bloated
- the writing sounds like me explaining development decisions clearly
- missing assets are marked with useful capture instructions
- the project pages make my existing work feel more concrete, visual, and credible

