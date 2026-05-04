# 2026-04-09 Grouping Pattern Explained

- The student explained that grouping stores the actual values by status rather than only counting them.
- The student also explained that the first-seen empty-list setup prevents a missing-key failure before `append(...)`.
- The order explanation was beginner-level but correct in substance: left-to-right iteration plus `append(...)` keeps first-seen items first inside each status group.
- Updated the next task to a small compositional report function that combines grouping, joining, and alphabetical sorting.
