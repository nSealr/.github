# NostrSeal

NostrSeal is a non-profit open-source hardware and software project for Nostr
signing devices.

The goal is to make Nostr key custody and signing reproducible, inspectable, and
composable by anyone: firmware, companion software, protocols, hardware
blueprints, smartcard support, and test vectors are all developed in the open.

## Repositories

- `lab`: knowledge base, roadmap, audits, sources, threat models, and decisions.
- `specs`: shared protocols, schemas, and NIP-01/BIP-340 test vectors.
- `companion`: host-side CLI, browser bridge, NIP-46, QR, USB, serial, and smartcard adapters.
- `esp32`: ESP32-S3 and classic ESP32 firmware targets.
- `vault`: Pi Zero / SeedSigner-style QR vault.
- `card`: JavaCard/NFC/contact smartcard signer work.
- `hardware`: open PCB, BOM, enclosures, wiring, and assembly references.

## Principles

- Private keys must not be exposed to ordinary Nostr clients.
- Sensitive signatures require explicit user review and approval.
- The host companion is not trusted with key custody.
- Protocols and test vectors should be reusable by other Nostr projects.
- Hardware should be buildable from documented parts and open design files.

