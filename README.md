# India ITR Filing Skill

A privacy-safe Agent Skill for preparing, reconciling, reviewing, and troubleshooting Indian individual income-tax returns.

The skill focuses on difficult real-world combinations: salary plus professional income, section 44ADA, securities and mutual funds, intraday/F&O activity, VDA, foreign assets, unlisted shares, home-loan questions, tax credits, portal validations, and final preview reconciliation.

It is designed for Claude Code, OpenAI Codex, Hermes Agent, Pi, and other tools that support the `SKILL.md` Agent Skills format.

## Safety model

- Lawful optimization only; no fabricated deductions, dates, losses, or omissions.
- Current official sources must be checked for assessment-year-specific rules.
- PAN, Aadhaar, passwords, OTPs, complete bank details, and private addresses remain with the taxpayer.
- The agent stops before declaration, payment, submission, and e-verification.
- The generated preview must be reconciled before filing.

This is a workflow aid, not a substitute for a chartered accountant or legal opinion. Use professional review for audits, disputed residency, complex foreign holdings, valuation uncertainty, or material trading losses.

## Repository layout

```text
skills/india-itr-filing/
├── SKILL.md
├── references/
│   ├── form-and-regime.md
│   ├── income-schedules.md
│   ├── official-sources.md
│   ├── portal-troubleshooting.md
│   ├── preview-checklist.md
│   └── securities-and-trading.md
└── scripts/
    └── privacy_scan.py
```

## Install

Clone the repository, then copy or symlink `skills/india-itr-filing` into the skill directory used by your agent.

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/india-itr-filing ~/.claude/skills/india-itr-filing
```

### OpenAI Codex

```bash
mkdir -p ~/.codex/skills
cp -R skills/india-itr-filing ~/.codex/skills/india-itr-filing
```

### Pi

```bash
mkdir -p ~/.pi/agent/skills
cp -R skills/india-itr-filing ~/.pi/agent/skills/india-itr-filing
```

Pi also supports the shared `~/.agents/skills/` location.

### Hermes Agent

```bash
mkdir -p ~/.hermes/skills
cp -R skills/india-itr-filing ~/.hermes/skills/india-itr-filing
```

The repository also follows the Hermes tap layout, so it can be added as a custom skill tap.

Restart or reload the agent after installation. Invoke the skill explicitly as `india-itr-filing`, or ask for help preparing or reviewing an Indian ITR.

## Validate

```bash
python3 tests/validate_repository.py
python3 skills/india-itr-filing/scripts/privacy_scan.py .
```

The privacy scan accepts extra case-insensitive deny-list values without placing them in the repository:

```bash
python3 skills/india-itr-filing/scripts/privacy_scan.py . --deny "private value"
```

## Sources and maintenance

The bundled guidance points agents to the Income Tax Department, Income Tax India, and CBDT. Rules, utilities, schemas, thresholds, and due dates change, so the skill deliberately requires current official verification instead of freezing every number into the instructions.

## License

MIT
