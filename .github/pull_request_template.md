# Summary

Describe the change and the repository scope.

# Verification

- [ ] I ran the relevant repository `make ci`.
- [ ] I ran `lab make integration` for shared contracts, vectors, or cross-repo behavior.
- [ ] I checked GitHub Actions logs after push when this closes a milestone.

# Audit

- [ ] The change matches the five-signer-family taxonomy.
- [ ] The companion/browser/SDK path stays secretless for production use.
- [ ] QR vault behavior remains stateless, RAM-only, air-gapped, and manual.
- [ ] ESP32 production signing remains disabled unless every readiness gate is complete.
- [ ] Smartcard review remains display-less with explicit external review acknowledgement.
- [ ] TROPIC01 direct BIP-340/Schnorr support is not claimed unless source-backed.
- [ ] No stale, legacy, or duplicate implementation path was kept without a current reason.

# Notes

Add blockers, hardware evidence gaps, or follow-up links here.
