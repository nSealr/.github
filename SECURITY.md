# Security policy

nSealr is pre-release. No production-ready device or safe custody of real
identities is claimed by the current development snapshots. Use public test
identities until the relevant profile's release gates have passed.

## Report privately

Use the central [private vulnerability report form](https://github.com/nSealr/nsealr/security/advisories/new)
in **nSealr/nsealr**. This also accepts reports concerning the organization's
other repositories or migrated/retired code: identify the affected repository
and original commit in the report. The report is handled by nSealr repository
maintainers in the private GitHub advisory thread.

You need a GitHub account. Do not include sensitive details in a public issue,
pull request, discussion, CI log or social message. If the private form is
unavailable, do not post an exploit or key material; a public issue may request
restoration of the private reporting channel without revealing the vulnerability.
No private GitHub direct-message feature or unverified email address is assumed.

Include the affected repository/commit or artifact hash, reproduction steps,
expected and observed behavior, potential impact and sanitized supporting
captures. Never send a real identity key, seed or unrelated user data. State
which device, interface or client version is involved without publishing private
device identifiers.

## Scope and handling

Security-sensitive areas include canonical event encoding and BIP340,
identity/request binding, key lifetime and recovery, physical review/approval,
QR/USB/NIP-46 input bounds and lifecycle, entropy, update/reset/debug behavior,
and hardware or supply-chain assumptions.

Maintainers triage reports, discuss scope and reproduction privately, and
coordinate fixes and disclosure with the reporter. A fix needs appropriate
regressions, distinct review, documentation and exact candidate/evidence
bindings. Physical properties require evidence on the identified profile;
a software test or AI review alone is not certification. There is no promised
response deadline or currently supported stable device-release series.

Current requirements and evidence are public in
[nsealr/docs/product](https://github.com/nSealr/nsealr/tree/main/docs/product) and
[the task graph](https://github.com/nSealr/nsealr/blob/main/plan/work-items.json).
Private research repositories are not required to understand this policy.
