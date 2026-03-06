# Security Policy

## Supported Versions

This project follows trunk-based releases from `main`. Security fixes are backported only when explicitly tagged.

## Reporting a Vulnerability

- Email: security@danielreis.dev
- Include: impact, reproduction steps, proof-of-concept
- SLA: first response within 48h, fix plan within 5 business days

## Security Controls

- Dependency pinning in `requirements.txt` and `package.json`
- CI tests on every PR
- Containerized runtime with minimal base images
