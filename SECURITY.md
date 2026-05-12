# Security Policy

nSealr is experimental until a release explicitly says otherwise. Do not use
unreleased prototypes to protect production Nostr identities.

## Reporting Security Issues

Report suspected vulnerabilities privately before opening a public issue.

- Preferred contact: open a private security advisory on the affected GitHub
  repository when available.
- Fallback contact: contact the organization maintainers directly through
  GitHub.

Include:

- affected repository and commit;
- exact reproduction steps;
- expected and observed behavior;
- impact analysis;
- logs, traces, APDU captures, serial captures, or screenshots when relevant.

## Scope

Security-sensitive areas include:

- NIP-01 event canonicalization and event id computation;
- BIP-340/secp256k1 signing and verification;
- private key custody, provisioning, and wipe behavior;
- firmware update and debug-lock paths;
- QR, USB, serial, NFC, PC/SC, and NIP-46 transports;
- trusted review UI behavior;
- hardware attack surface and supply-chain assumptions.

## Handling Standard

No security claim is accepted without evidence. Fixes must include tests,
documentation updates, and an audit note in the relevant repository or in
`nSealr/lab`.

