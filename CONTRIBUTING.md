# Contributing to nSealr

nSealr is pre-release software and hardware for Nostr signing. Start with the
[current product README](https://github.com/nSealr/nsealr) and
[product requirements](https://github.com/nSealr/nsealr/tree/main/docs/product).
The public [task graph](https://github.com/nSealr/nsealr/blob/main/plan/work-items.json)
records accepted scope and evidence. No private lab checkout is required.

The first milestone covers a connected ESP32-S3 without a secure element or
persistent identity vault, and independent Raspberry Pi and ESP32-P4 offline
session signers, with the Bridge/client/CLI/service/browser/TypeScript SDK
needed to use them. Custom hardware and its Nostr-free embedded Board SDK
remain future work. A public-fixture signature or software test is not a
production custody, entropy, recovery or device-release qualification.

## Choose the current owner

- [nsealr](https://github.com/nSealr/nsealr): shared Rust engine, device apps,
  Bridge and host packages, contracts/vectors, requirements and task graph.
- [website](https://github.com/nSealr/website): public site and user/developer entry points.
- [.github](https://github.com/nSealr/.github): shared contribution and security guidance.
- [hardware](https://github.com/nSealr/hardware) and
  [board-sdk](https://github.com/nSealr/board-sdk): retained future board work;
  they are not prerequisites for the three initial device profiles.

The former companion, raspberry and specs repositories retain migration history;
open current software issues and pull requests in nsealr. Smartcard research
is retired. Do not copy historical installation instructions into a new guide.

## Get a reproducible development environment

For the product on Linux x86_64/glibc:

```sh
git clone https://github.com/nSealr/nsealr.git
cd nsealr
python3 tools/baseline/bootstrap.py /absolute/absent/runtime
python3 /absolute/absent/runtime/nsealr/tools/baseline/run.py /absolute/absent/runtime
```

Choose a new absolute runtime path; the installer rejects reuse. See the
[pinned bootstrap guide](https://github.com/nSealr/nsealr/tree/main/tools/baseline)
for host prerequisites, exact dependency pins and limitations. Do not use a
test-only software signer with a real identity. Board-specific toolchains and
physical tests have separate recipes and admission gates.

For website or organization metadata changes, follow that repository's README
and existing verification commands. Use focused checks while developing and
the required candidate/PR/main gates for delivery. Successful software checks
do not replace installed-browser, live-client or hardware evidence.

## Make a reviewable change

1. Find or open a non-sensitive issue describing the concrete problem and
   affected profile. Link its task/requirement when relevant.
2. Keep one useful branch and focused commits. Preserve original licenses,
   attribution, failures and still-applicable evidence.
3. For behavior changes, state the expected result and add meaningful
   regressions. Security-sensitive work needs distinct review that considers
   the requirement and at least one relevant adverse assumption.
4. Record exact commands, candidate/artifact identities, results and limits.
   Reuse sufficient unchanged checks; explain omissions and inherited failures.
5. Update the current public instructions when behavior or ownership changes.
   Open a pull request and satisfy the repository's protected delivery gates.
   Never rewrite merged history or bypass checks to obtain a green result.

Use maintained cryptographic libraries and the shared normative Rust engine.
Keep identity keys out of Bridge/client production paths; transport/client keys
have a separate bounded lifecycle. Host UI and local grants cannot approve a
device signature. State unknowns and unsupported capabilities explicitly.
Durable project documentation is written in English.

Report vulnerabilities through the [security policy](https://github.com/nSealr/.github/blob/main/SECURITY.md), with
sensitive details kept out of public issues, pull requests and logs.
