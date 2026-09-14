# Iliad study workspace

Follow the official Iliad course order in `iliad-intensive/schedule.yaml`.
The course clone is reference material; make personal notes in `worksheets/`
and symbolic checks in `derivations/`. Do not alter the course's teaching approach.

Ask for an attempt before a solution. Address the first error, one hint per turn;
flag pattern-matching without understanding. Course solution blocks (including
those embedded in `tex/` worksheets) are off-limits until the learner says
`reveal`. Read only the relevant problem statement when helping with an exercise.
Do not fill in proofs or solve exercises as part of setup or environment checking.

Write mathematics in Quarto Markdown with LaTeX notation. SymPy and mpmath are
for checking results the learner has first derived by hand. `just check` only
tests the math environment; run a particular derivation script when requested.
Use WSL Ubuntu-24.04. The uv environment lives at `/home/emlyn/.venvs/iliad`.
Use `just env`, `just render`, and `just check`. Keep `uv.lock` reproducible.

No Anki or additional learning-management layer. Preserve existing notes and
checkboxes when refreshing worksheet scaffolding. No paid API calls without an
explicit model, cost estimate, and approval. Do not add a Claude co-author trailer.
