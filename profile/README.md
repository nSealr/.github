# nSealr

Open-source Nostr signing tools and a programmable security-board platform.

**Restart and engineering validation are in progress. No production-ready device release is claimed.**

The retained paths are an accessible ESP32 signer without a secure element, offline Raspberry Pi and ESP32-P4 kits, and a custom board. Shared Nostr behavior belongs to nSealr Signer; nSealr Bridge connects clients. Every physical implementation has its own security and release gates.

## Active destinations

- [nsealr](https://github.com/nSealr/nsealr): main software, Signer/Bridge architecture, restart plan and tests. Renamed from `firmware`, preserving its history.
- [hardware](https://github.com/nSealr/hardware): general-purpose programmable security board, component review, KiCad, mechanics and manufacturing validation.
- [board-sdk](https://github.com/nSealr/board-sdk): generic firmware-development foundation, independent of Nostr; under development.
- [website](https://github.com/nSealr/website): public documentation, being aligned with the restart.
- [.github](https://github.com/nSealr/.github): organization and contribution metadata.

## Migration sources

`companion`, `raspberry` and `specs` remain available until selected code, vectors and ownership have migrated and passed verification. Smartcard research is retired. Historical documents may describe the previous scope; use the [restart plan](https://github.com/nSealr/nsealr/tree/main/docs/restart) for current decisions.

## Principles

Private keys stay out of ordinary clients. Device approval binds the exact operation. Documentation follows source, specifications and measurements. Hardware support is demonstrated on identified assemblies. The Board platform can host independent firmware, but does not promise every application or algorithm merely by exposing a secure element.
