# Iliad learning

Open [the rendered worksheet index](_site/index.html) in your browser to start.
Begin with Foundations: Prerequisites, then A.1: AI Alignment Introduction.

To edit, run `./Open-Iliad.ps1` from PowerShell in this folder. It opens the
workspace in WSL Ubuntu-24.04. Write notes and proofs in `worksheets/*.qmd`,
using `$...$` for inline maths and `$$...$$` for display maths.

In a WSL terminal opened in this folder:

```bash
just render     # rebuild _site/index.html and all worksheet pages
just check      # test SymPy and mpmath
just env        # reinstall exactly uv.lock if needed
```

`just preview` prints a local preview URL. `just worksheets` adds missing blank
pages from the course schedule while preserving existing notes and checkboxes.
It leaves an existing index intact; add links there if the schedule changes.

The isolated Python 3.11 environment is `/home/emlyn/.venvs/iliad` on the Linux
filesystem, managed by uv. SymPy 1.14.0, mpmath 1.3.0 and PyYAML 6.0.3 are locked.
WSL Quarto 1.9.38 rendered all 29 pages successfully. Embedded assets and native
MathML let you read your rendered notes and equations offline in Edge/Chrome.
Official web worksheets and Google Docs links still require internet access.

The shallow `iliad-intensive/` clone is the
[official course repository](https://github.com/iliad-team/iliad-intensive),
at `c0317e71c634` on 2026-09-13, with its LFS figures downloaded.
Its current `schedule.yaml` supplies the order: Foundations, Alignment, Learning,
Abstractions/Representations/Interpretability, Agency, then Safety Guarantees.

There are 28 blank notes pages: 21 named worksheets and 7 days with no local
worksheet. Those days link to the course's documents and available sources.
The original course sources are reference material and may contain solutions;
your notes do not copy those solutions. No Next.js server or TeX distribution is
needed to render your personal notes.

Put symbolic checks of your own hand-derived results in `derivations/` and run,
for example, `UV_PROJECT_ENVIRONMENT=$HOME/.venvs/iliad uv run --locked python
derivations/my_check.py`. The included `just check` only tests the toolchain;
it does not grade proofs or automatically run your derivation files.

The current course also has coding modules and external repositories; their
module-specific environments are separate from this maths-notes setup. No Anki
integration or paid API setup was added.

## GitHub and course updates

Your learning workspace is stored in the private repository
`emlynsg/iliad-learning`, with `origin` pointing to your GitHub. Personal notes,
the schedule index, configuration and the Python lockfile are tracked. The
rendered `_site/`, caches and Python environment are generated locally.

`iliad-intensive/` is a Git submodule pinned to the official course revision.
Its URL in `.gitmodules` points to `iliad-team/iliad-intensive`, so the course
source is restored without copying its history or figures into your notes repo.
The current local course clone also has an `upstream` remote for that official URL.

To restore on another machine:

```bash
git clone --recurse-submodules https://github.com/emlynsg/iliad-learning.git
```

Git LFS is needed for the course figures. Then configure the local tools and run
`just env` and `just render`. The VS Code launch settings currently target this
laptop's WSL paths.

To save your notes from the learning workspace:

```bash
git add worksheets index.qmd derivations
git commit -m "Update learning notes"
git push
```

Course updates are deliberate: `git submodule update --remote iliad-intensive`,
then `just worksheets`. Review the schedule and add any new links to `index.qmd`,
which the scaffolder preserves. Commit the changed submodule pointer alongside
your notes when you want to adopt that course version.
