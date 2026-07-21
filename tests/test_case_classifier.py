#!/usr/bin/env python3
"""Synthetic scenario tests for the adaptive ITR route classifier."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "skills" / "india-itr-filing" / "scripts" / "classify_case.py"
SPEC = importlib.util.spec_from_file_location("classify_case", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def check(profile: dict, route: str, risk: str) -> None:
    result = MODULE.classify(profile)
    assert result["primary_route"] == route, result
    assert result["risk_tier"] == risk, result
    assert result["submission_allowed"] is False, result


def main() -> int:
    check({"salary": True, "residency": "ror"}, "salary-essential", "green")
    check(
        {"salary": True, "delivery_investments": True, "residency": "ror"},
        "salary-investor",
        "amber",
    )
    check(
        {"professional_income": True, "considering_44ada": True, "residency": "ror"},
        "professional-44ada-candidate",
        "amber",
    )
    check(
        {"professional_income": True, "audit_or_books_uncertain": True, "residency": "ror"},
        "professional-regular",
        "red",
    )
    check(
        {"delivery_investments": True, "intraday": True, "fno": True, "residency": "ror"},
        "trader",
        "amber",
    )
    check(
        {"vda": True, "unknown_transaction": True, "residency": "ror"},
        "complex-composite",
        "red",
    )
    check(
        {"foreign_asset_or_income": True, "unlisted_equity": True, "residency": "ror"},
        "foreign-cross-border",
        "red",
    )
    check({"property": True, "residency": "ror"}, "property", "amber")
    check(
        {"salary": True, "professional_income": True, "fno": True, "residency": "ror"},
        "complex-composite",
        "amber",
    )
    check(
        {"salary": True, "notice_or_late_return": True, "residency": "ror"},
        "complex-composite",
        "red",
    )
    check(
        {"brought_forward_loss": True, "records_incomplete": True, "residency": "ror"},
        "complex-composite",
        "red",
    )
    check({"salary": True, "residency": "unsure"}, "foreign-cross-border", "red")
    print("case classifier tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
