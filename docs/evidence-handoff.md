# Evidence Handoff

This note defines how future taxonomy entries should reference research ledger
evidence.

It does not add taxonomy claims, citations, or paper-ready wording.

## Handoff Requirements

Future taxonomy entries should identify:

* the related ledger claim ID, when applicable;
* the related ledger source ID or source IDs;
* whether supporting evidence is primary or secondary;
* whether the entry is ready for paper use;
* any unresolved evidence gap.

## Readiness States

| State | Meaning |
|---|---|
| `planning` | Entry is a placeholder or structure note. |
| `evidence_needed` | Entry needs approved ledger evidence before use. |
| `candidate` | Entry has evidence direction but is not paper-ready. |
| `ready` | Entry can support paper work after review. |
| `blocked` | Entry should not be used until the blocker is resolved. |

## Ledger Integration Guidelines

To reference research ledger evidence, future entries must adhere to the following rules:

1. **Claim Association**: Each taxonomy term requiring empirical backing must link to a valid claim ID from the research ledger. This is formatted as `claim-` followed by the sequential claim number (e.g. `claim-012`).
2. **Source Association**: Every linked claim must be backed by one or more source IDs from the research ledger. This is formatted as `source-` followed by the unique source identifier (e.g. `source-smith-2024`).
3. **Verification Process**: 
   * A term in state `ready` must have at least one valid `Claim ID` and one valid `Source ID`.
   * A term in state `planning` or `evidence_needed` can have `N/A` or empty fields for claims and sources.
   * If a term is in state `blocked`, the `Evidence Gap` field must document the specific issue or contradiction in the ledger.

## Current Limits

Do not add final taxonomy wording from this handoff issue.
