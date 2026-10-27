# nSealr

Open-source Nostr signing devices and the software needed to use them.

**Pre-release development. No production-ready device or real-key custody
qualification is claimed.**

The first milestone has three independent device paths: a connected ESP32-S3
with display and physical confirmation, without a secure element or persistent
identity vault; and Raspberry Pi and ESP32-P4 offline signers with session
custody. The shared Rust engine owns signing semantics. Bridge, CLI, service,
browser/client integration and the TypeScript SDK belong to the same usable
workflow; the host cannot grant device approval.

Public-fixture round trips are development evidence. Installation, recovery,
entropy, interface lifecycle and each profile's security gates remain explicit.
Connected/offline describe interaction modes, not a security ranking.

## Current destinations

- [nsealr](https://github.com/nSealr/nsealr): device apps, shared core,
  Bridge/host packages, contracts, requirements and the sole task graph.
  Renamed from firmware, preserving its history.
- [website](https://github.com/nSealr/website): public site and documentation.
- [.github](https://github.com/nSealr/.github): shared contribution and security guidance.
- [hardware](https://github.com/nSealr/hardware): future programmable board design.
- [board-sdk](https://github.com/nSealr/board-sdk): future embedded board platform,
  independent of Nostr and distinct from the product's TypeScript SDK.

Custom hardware and its embedded SDK are preserved future work, outside the
critical path for the initial devices. Smartcard research is retired.

Selected companion, raspberry and specs components were consolidated through
[the reviewed A02 migration](https://github.com/nSealr/nsealr/tree/main/docs/restart/implementation/A02).
Their original repositories retain source history and licenses; current
development and issues belong in nsealr, not in those migration sources.

Read [Contributing](https://github.com/nSealr/.github/blob/main/CONTRIBUTING.md),
[Security](https://github.com/nSealr/.github/blob/main/SECURITY.md) and the
[current product requirements](https://github.com/nSealr/nsealr/tree/main/docs/product).
