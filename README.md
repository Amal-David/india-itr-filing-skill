# India ITR Filing Skill

A privacy-safe Agent Skill that assists with preparing, reconciling, reviewing, and troubleshooting Indian individual income-tax returns.

It offers three clear ways to start and composes only the workflows that apply. It supports simple salary returns as well as salary plus investments, freelance or professional income, section 44ADA candidates, investors, intraday/F&O traders, property, VDA, foreign assets, unlisted shares, tax credits, portal validations, and complex mixed cases.

It is designed for Claude Code, OpenAI Codex, Hermes Agent, Pi, and other tools that support the `SKILL.md` Agent Skills format.

**Agent-ready origin:** [india-itr-filing-skill.pages.dev](https://india-itr-filing-skill.pages.dev/) publishes Markdown content negotiation, an agent-readable site map, and a digest-verifiable [Agent Skills discovery index](https://india-itr-filing-skill.pages.dev/.well-known/agent-skills/index.json).

## Start here

Choose any entry path. You do not need to know your ITR form or schedule names.

1. **Guided questions** — say: `Guide me through filing my Indian ITR.`
2. **Known modes** — say: `I have salary, freelance income, and mutual-fund sales.`
3. **Free-select from documents** — say: `Review these redacted tax documents, find what applies, and show supported optimization opportunities.`

With the document path, the skill inventories the files, infers provisional routes, finds evidence gaps, and builds the form/regime/schedule navigation plan. It does not assume the file set is complete or optimize for a refund at the expense of accuracy.

## What it does

- Classifies a taxpayer into a primary route plus applicable modifiers rather than forcing one persona.
- Discovers likely routes from redacted source documents when the taxpayer does not know the categories.
- Requests a tailored minimum evidence pack.
- Reviews lawful, evidence-supported elections, claims, credits, and loss treatment without fabricating a refund.
- Derives an ITR form, regime, and schedule hypothesis with an eligibility trace.
- Reconciles source documents, prefill, tax credits, portal schedules, and the final preview.
- Stops and recommends CA, tax-law, or RBI/FEMA review when the facts require it.

Typical users include salaried employees, developers and consultants with side income, independent professionals, mutual-fund and equity investors, intraday/F&O traders, VDA users, startup employees or founders with unlisted/foreign holdings, property owners or buyers, and taxpayers fixing portal validation errors.

## Documents it needs

This skill works from the taxpayer's own source records. Depending on the profile, that may include:

- Form 16 from every employer, AIS/TIS, Form 26AS, and bank-interest records;
- invoices, receipt ledgers, bank/remittance evidence, and GST/FIRC records where applicable;
- broker tax P&L, capital-gains reports, contract notes, and prior filed loss schedules;
- mutual-fund CAS or AMC/CAMS/KFintech/MF Central capital-gains reports;
- property ownership, possession, rent, lender, and property-TDS records;
- VDA exchange ledgers and section 194S evidence;
- foreign-account, foreign-income, share, valuation, conversion, ODI/LRS, and AD-bank records where applicable;
- TDS/TCS certificates and advance/self-assessment-tax challans.

Screenshots and portal prefill can identify what to investigate, but they do not replace source records.

## Safety and scope

- Filing assistance only; not a CA, lawyer, authorized representative, RBI/FEMA adviser, legal opinion, certification, or refund guarantee.
- Lawful claims supported by records; no fabricated deductions, dates, losses, turnover, or omissions.
- Current official sources must be checked for AY-specific rules and portal schema.
- Never provide passwords, OTPs, Aadhaar, full PAN, complete bank/card details, signatures, biometrics, or unredacted identity documents.
- The taxpayer personally controls declaration, payment, submission, upload, and e-verification.
- Professional review is mandatory for audit exposure, notices, disputed residency, treaty/foreign-tax-credit issues, foreign gifts or ODI/LRS/FEMA matters, valuation uncertainty, missing VDA basis, unsupported prior losses, and other blocked classifications.

## Repository layout

```text
skills/india-itr-filing/
├── agents/
│   └── openai.yaml
├── SKILL.md
├── references/
│   ├── document-intake-and-privacy.md
│   ├── document-led-discovery.md
│   ├── form-and-regime.md
│   ├── income-schedules.md
│   ├── intake-and-routing.md
│   ├── official-sources.md
│   ├── portal-troubleshooting.md
│   ├── preview-checklist.md
│   ├── risk-and-escalation.md
│   ├── scenario-matrix.md
│   ├── securities-and-trading.md
│   └── tax-and-fema.md
└── scripts/
    ├── classify_case.py
    └── privacy_scan.py
```

## Install

Clone the repository, then copy or symlink `skills/india-itr-filing` into your agent's skill directory.

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

Restart or reload the agent after installation. Invoke `india-itr-filing`, or ask for help preparing or reviewing an Indian ITR.

## Validate

```bash
python3 tests/validate_repository.py
python3 tests/test_case_classifier.py
python3 tests/test_agent_site.py
python3 skills/india-itr-filing/scripts/privacy_scan.py .
```

Build the deployable discovery site with:

```bash
python3 scripts/build_agent_site.py
```

The privacy scan accepts runtime deny-list values without placing them in the repository:

```bash
python3 skills/india-itr-filing/scripts/privacy_scan.py . --deny "private value"
```

## Sources and maintenance

The skill routes agents to current Income Tax Department, CBDT, Income Tax India, and RBI sources. Rules, utilities, schemas, thresholds, and due dates change, so assessment-year-specific official verification is mandatory.

## License

MIT
