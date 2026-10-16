"""Control lookup table: CIS item to NIST 800-53 family, effort and fix.

Deterministic. No model is involved, and an unknown control id is an error.
The CIS titles come from CIS AWS Foundations Benchmark v7.1.0. The NIST
families are our own mapping (the benchmark does not include them), so a
human must review them.
"""

from __future__ import annotations

from dataclasses import dataclass

BENCHMARK_VERSION = "CIS AWS Foundations Benchmark v7.1.0"
ASSESSMENTS = ("automated", "manual")
EFFORTS = ("low", "medium", "high")


class UnknownControlError(ValueError):
    """A finding names a control id that is not in the lookup table."""


@dataclass(frozen=True)
class Control:
    control_id: str
    benchmark_version: str
    title: str
    assessment: str  # "automated" or "manual"
    nist_primary: str  # one NIST 800-53 family, for example "AC"
    nist_secondary: tuple[str, ...]  # other families that apply, may be empty
    effort: str  # "low", "medium" or "high"
    fix: str  # plain English, one or two sentences


# The table itself. Each row is written out in full so it is easy to read
# and easy to review one control at a time.
CONTROLS = {
    "CIS-AWS-3.1.4": Control(
        control_id="CIS-AWS-3.1.4",
        benchmark_version=BENCHMARK_VERSION,
        title="Ensure that S3 is configured with 'Block Public Access' enabled",
        assessment="automated",
        nist_primary="AC",
        nist_secondary=("SC",),
        effort="low",
        fix="Turn on Block Public Access for the bucket and remove any policy that "
        "lets everyone read it.",
    ),
    "CIS-AWS-2.5": Control(
        control_id="CIS-AWS-2.5",
        benchmark_version=BENCHMARK_VERSION,
        title="Ensure MFA is enabled for the 'root' user account",
        assessment="automated",
        nist_primary="IA",
        nist_secondary=("AC",),
        effort="low",
        fix="Sign in as the root user and add a hardware or app based second step "
        "to the sign in.",
    ),
    "CIS-AWS-6.3": Control(
        control_id="CIS-AWS-6.3",
        benchmark_version=BENCHMARK_VERSION,
        title="Ensure no security groups allow ingress from 0.0.0.0/0 to remote "
        "server administration ports",
        assessment="automated",
        nist_primary="SC",
        nist_secondary=("AC",),
        effort="medium",
        fix="Remove the rule that opens the admin port to the whole internet and "
        "allow only the addresses that need it.",
    ),
    "CIS-AWS-4.1": Control(
        control_id="CIS-AWS-4.1",
        benchmark_version=BENCHMARK_VERSION,
        title="Ensure CloudTrail is enabled in all regions",
        assessment="manual",
        nist_primary="AU",
        nist_secondary=(),
        effort="low",
        fix="Change the trail so it records activity in every region, not just one.",
    ),
    "CIS-AWS-2.12": Control(
        control_id="CIS-AWS-2.12",
        benchmark_version=BENCHMARK_VERSION,
        title="Ensure access keys are rotated every 90 days or less",
        assessment="automated",
        nist_primary="IA",
        nist_secondary=(),
        effort="medium",
        fix="Create a new access key, switch the application to it, then delete the "
        "old key.",
    ),
}


def lookup_control(control_id: str) -> Control:
    """Return the table row for a control id, or raise UnknownControlError."""
    # Exact match only. We never guess or fix up an id that is not in the table.
    if control_id not in CONTROLS:
        known = ", ".join(sorted(CONTROLS))
        raise UnknownControlError(
            f"unknown control id {control_id!r}. Known ids: {known}"
        )
    return CONTROLS[control_id]
