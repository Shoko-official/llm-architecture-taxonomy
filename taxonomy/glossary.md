# Glossary

This file is a placeholder for future architecture terms.

It does not define terms, make taxonomy claims, or provide paper-ready wording.

## Future Entry Shape

Future entries should include:

* term;
* related layer stub;
* readiness state;
* linked ledger claim ID, when applicable;
* linked ledger source ID, when applicable;
* unresolved evidence gap, if any.

## Current Entries

| Term | Layer | State | Claim ID | Source ID | Definition / Notes |
|---|---|---|---|---|---|
| Attention | Model Layer | `ready` | claim-attention-transformer | source-attention-2017 | Self-attention correlates different positions of a sequence to compute a representation of the sequence. |
| Fine-tuning | Training Layer | `planning` | N/A | N/A | Adapting model parameters on task-specific datasets. |
| Batching | Inference Layer | `ready` | claim-kv-cache-paged-attention | source-kv-cache-2023 | Grouping multiple inference requests together to maximize parallel GPU execution. |
| Vector Search | Retrieval Layer | `planning` | N/A | N/A | Searching for high-dimensional embeddings using nearest-neighbor algorithms. |
| State Cache | Memory Layer | `planning` | N/A | N/A | Caching short-term conversational history or agent state variables. |
| Tool Call | Agent Layer | `planning` | N/A | N/A | System actions executing external APIs or python runtimes. |
| Accuracy Metric | Evaluation Layer | `planning` | N/A | N/A | Algorithmic metrics evaluating model predictions against references. |
| Safety Filter | Governance Layer | `ready` | claim-adversarial-prompt-injection | source-adversarial-2024 | Input scanner filtering out prompt injection attempts. |
| Telemetry | Observability Layer | `ready` | claim-dapper-distributed-tracing | source-dapper-2010 | Structured logging and distributed tracing spans tracking system executions. |
| Audit | Governance Layer | `planning` | N/A | N/A | Retaining compliance logs of user requests and model actions. |
| Policy | Governance Layer | `planning` | N/A | N/A | Defining operational boundaries, allowed tools, and execution action budgets. |

## Current Limits

Do not add definitions or claims here before evidence handoff rules and source
records support the term.
