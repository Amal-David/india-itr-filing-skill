#!/usr/bin/env python3
"""Route a PII-free Indian ITR case profile to workflow modes.

This is a deterministic intake aid. It does not determine legal eligibility.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


BOOLEAN_FIELDS = {
    "salary",
    "multiple_employers",
    "professional_income",
    "other_business",
    "delivery_investments",
    "intraday",
    "fno",
    "vda",
    "property",
    "foreign_asset_or_income",
    "unlisted_equity",
    "director_or_partner",
    "brought_forward_loss",
    "tax_credit",
    "notice_or_late_return",
    "unknown_transaction",
    "audit_or_books_uncertain",
    "treaty_or_foreign_tax_credit",
    "fema_or_ad_bank_issue",
    "records_incomplete",
    "considering_44ada",
}


def truth(profile: dict[str, Any], key: str) -> bool:
    value = profile.get(key, False)
    if not isinstance(value, bool):
        raise ValueError(f"{key} must be true or false")
    return value


def classify(profile: dict[str, Any]) -> dict[str, Any]:
    unknown = sorted(set(profile) - BOOLEAN_FIELDS - {"residency"})
    if unknown:
        raise ValueError(f"unknown profile fields: {', '.join(unknown)}")

    flags = {key: truth(profile, key) for key in BOOLEAN_FIELDS}
    residency = profile.get("residency", "unsure")
    if residency not in {"ror", "rnor", "nonresident", "unsure"}:
        raise ValueError("residency must be ror, rnor, nonresident, or unsure")

    modifiers = [key.replace("_", "-") for key, enabled in flags.items() if enabled]
    if residency != "ror":
        modifiers.append(f"residency-{residency}")

    trading = flags["intraday"] or flags["fno"]
    cross_border = (
        flags["foreign_asset_or_income"]
        or flags["treaty_or_foreign_tax_credit"]
        or flags["fema_or_ad_bank_issue"]
        or residency != "ror"
    )
    complexity_count = sum(
        [
            flags["salary"],
            flags["professional_income"] or flags["other_business"],
            flags["delivery_investments"],
            trading,
            flags["vda"],
            flags["property"],
            cross_border,
        ]
    )

    if complexity_count >= 3 or flags["notice_or_late_return"]:
        primary = "complex-composite"
    elif cross_border:
        primary = "foreign-cross-border"
    elif trading:
        primary = "trader"
    elif flags["professional_income"] or flags["other_business"]:
        primary = (
            "professional-44ada-candidate"
            if flags["professional_income"] and flags["considering_44ada"]
            else "professional-regular"
        )
    elif flags["property"] and not flags["salary"]:
        primary = "property"
    elif flags["salary"] and flags["delivery_investments"]:
        primary = "salary-investor"
    elif flags["salary"]:
        primary = "salary-essential"
    elif flags["delivery_investments"]:
        primary = "investor"
    elif flags["property"]:
        primary = "property"
    else:
        primary = "complex-composite"

    red_reasons: list[str] = []
    if residency in {"rnor", "nonresident", "unsure"}:
        red_reasons.append("residency requires review")
    for key, message in {
        "notice_or_late_return": "notice or non-routine filing status",
        "audit_or_books_uncertain": "audit or books position is uncertain",
        "treaty_or_foreign_tax_credit": "treaty or foreign-tax-credit issue",
        "fema_or_ad_bank_issue": "FEMA, RBI, or AD-bank issue",
        "unknown_transaction": "transaction identity is unresolved",
    }.items():
        if flags[key]:
            red_reasons.append(message)

    if flags["foreign_asset_or_income"] or flags["unlisted_equity"]:
        red_reasons.append("foreign or unlisted asset review")
    if flags["brought_forward_loss"] and flags["records_incomplete"]:
        red_reasons.append("prior-loss provenance is incomplete")

    if red_reasons:
        risk = "red"
    elif (
        complexity_count >= 2
        or trading
        or flags["vda"]
        or flags["property"]
        or flags["professional_income"]
        or flags["other_business"]
    ):
        risk = "amber"
    else:
        risk = "green"

    form_hypothesis = "derive-after-eligibility-trace"
    if flags["professional_income"] or flags["other_business"] or trading:
        form_hypothesis = "itr-3-default; test limited itr-4 eligibility"
    elif flags["foreign_asset_or_income"] or flags["unlisted_equity"] or flags["director_or_partner"]:
        form_hypothesis = "itr-2 unless business/profession facts require itr-3"
    elif flags["delivery_investments"]:
        form_hypothesis = "itr-2 unless business/profession facts require itr-3"
    elif flags["salary"]:
        form_hypothesis = "test all itr-1 restrictions; otherwise itr-2"

    return {
        "primary_route": primary,
        "modifiers": sorted(set(modifiers)),
        "risk_tier": risk,
        "specialist_review_reasons": red_reasons,
        "form_hypothesis": form_hypothesis,
        "submission_allowed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", nargs="?", help="JSON profile file; omit for stdin")
    args = parser.parse_args()

    try:
        if args.profile:
            payload = Path(args.profile).read_text(encoding="utf-8")
        else:
            payload = sys.stdin.read()
        profile = json.loads(payload)
        if not isinstance(profile, dict):
            raise ValueError("profile must be a JSON object")
        print(json.dumps(classify(profile), indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"classification failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
