# Teacher State

`teacher_state/` is the current synthesized student model.

Update these files in place when better evidence appears.

Do not use this directory as a dated journal.

## How It Differs From Session Notes

- `teacher_state/` is current truth.
- `teacher_observations/sessions/` is historical evidence.
- Session notes preserve what happened.
- `teacher_state/` preserves what is currently believed and what should happen next.

## Ingest Workflow

1. Read the new evidence.
2. Update the relevant state pages in place.
3. Add or update a dated note in `../teacher_observations/sessions/` when the event matters historically.
4. Append a short entry to `log.md`.
5. Re-check `next_task.md`.

## Query Workflow

1. Start with `index.md`.
2. Read the relevant canonical pages.
3. Consult recent session notes only if provenance or ambiguity matters.
4. If the answer creates durable insight, file it back here and log it.

## Lint Workflow

Use `lint_checklist.md` for periodic checks.

The main goal is to keep this directory coherent, current, and free of stale contradictions.
