"""AI drafting helpers (disabled – no external API).

Previously used Claude / Grok API. The app now runs fully offline.
Faculty can draft relevance, assignments, end-term papers and solutions
manually in the UI, or paste content generated elsewhere (e.g. by chatting
with Grok) into the editors in tab 5.
"""
from __future__ import annotations


def _disabled(*_args, **_kwargs):
    raise RuntimeError(
        "AI drafting via API has been removed from this build. "
        "Edit Relevance, Assignments and End-term paper manually in the app, "
        "or generate text with Grok chat and paste it into the editors."
    )


draft_relevance = _disabled
draft_assignments = _disabled
draft_end_term = _disabled
draft_solutions = _disabled
extract_course_from_syllabus = _disabled
