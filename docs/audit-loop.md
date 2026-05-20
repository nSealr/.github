# Audit Loop

Every meaningful nSealr task must pass an audit loop before it is called
complete.

## Required Loop

```text
plan
-> implement with tests
-> verify locally
-> audit correctness
-> audit architecture
-> audit security
-> audit docs
-> fix all known issues
-> re-run verification
-> repeat until no known fixable defects remain
-> commit
-> push when the milestone is complete
-> record outcome when project state changed
```

## Completion Gate

Completion requires fresh evidence:

- tests or validation commands pass;
- docs match the implemented behavior;
- security implications are reviewed;
- dependency and license changes are understood;
- organization metadata still passes label, issue-template, pull-request gate,
  repository-list, and stale-term validation where applicable;
- `git status` is clean after commit;
- the result is pushed when a milestone closes.

If any item fails, the task remains open.
