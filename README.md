# Port Scanner 👋

Lightweight Python port scanner for quickly checking common ports or a custom port range, with optional banner grabbing for basic service identification.
Built for simple, practical network troubleshooting and visibility.

<img src="https://raw.githubusercontent.com/SimplyGregory/SimplyGregory/main/images/matrix.gif" alt="Matrix animation" align="right" width="220" />

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%2F%20Linux%20%2F%20macOS-555?style=flat-square)](#)

---

## About This Project
- 🎯 Goal: a fast, no-frills port scanner you can run anywhere Python runs.
- 🔎 Scans either a curated list of common ports or a user-provided range.
- 🏷️ Attempts basic service labeling + banner read for some ports.

## Features
<hr />

- Common-port scan (FTP/SSH/HTTP/HTTPS/RDP/etc.).
- Custom port range scan (`start,end`).
- “Open” reporting with simple service names.
- Optional banner grabbing (skips ports that typically don’t respond well).

## Usage
<hr />

Run:
- `python PortScanner.py`

Then follow the prompts:
- Enter the IP
- Choose `c`/`common` or `custom`
- If `custom`, enter `start,end`

## Notes
<hr />

- Default socket timeout is 1 second per port.
- Banner grabbing is best-effort and may return nothing depending on the service.

## Contact
<hr />

- YouTube: https://www.youtube.com/@ModSpidr
- Portfolio: https://gregorybridges.dev
- Email: contact@gregorybridges.dev
