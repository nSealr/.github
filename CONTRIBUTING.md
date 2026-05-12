# Contributing

nSealr values careful, source-backed work over speed. All durable project
artifacts must be written in English.

## Workflow

1. Read the relevant repository README and docs.
2. Check `nSealr/lab` for current roadmap, threat model, and decisions.
3. Write or update tests before implementation where behavior changes.
4. Keep commits focused and reviewable.
5. Run the repository verification command before claiming completion.
6. Update docs when behavior, architecture, security posture, or build steps
   change.

## Quality Gate

A task is complete only after the audit loop passes:

```text
plan -> implement with tests -> verify -> audit -> fix -> re-verify -> docs -> commit
```

If the audit finds a fixable issue, fix it and run the relevant verification
again. Do not mark the task complete while known fixable issues remain in scope.

## Technical Standards

- Do not hand-roll cryptography.
- Prefer canonical protocol sources over commentary.
- Keep private keys out of host-side production software.
- Mark uncertainty as `Unknown`, `Unverified`, or `Needs source`.
- Do not make production-readiness or security claims before evidence exists.

