# Taxonomy

This directory is reserved for future architecture taxonomy files.

Milestone 1 defines the skeleton only. It does not add architecture claims,
rankings, diagrams, or paper-ready taxonomy content.

## Taxonomy Skeleton

Initial planning areas:

| Area | Purpose | Status |
|---|---|---|
| Model Layer | Model weight configurations, architecture variants, and parameters. | Boundaries defined |
| Training Layer | Optimization algorithms, fine-tuning configurations, and objectives. | Boundaries defined |
| Inference Layer | Servicing configurations, decoding strategies, and runtime executions. | Boundaries defined |
| Retrieval Layer | Vector databases, embeddings, chunking, and grounding contexts. | Boundaries defined |
| Memory Layer | Read/write structures, history retention, and state schemas. | Boundaries defined |
| Agent Layer | Planning loops, tool routing, and orchestration strategies. | Boundaries defined |
| Evaluation Layer | Benchmarks, metrics, validation scripts, and scores. | Boundaries defined |
| Governance Layer | Guardrails, moderation policies, and operational controls. | Boundaries defined |

## Layer Boundaries

The boundaries of each architecture layer are defined as follows:

* **Model Layer**: Focuses on core neural network weight configurations, architectures (e.g. dense, MoE), parameter counts, and model topology.
* **Training Layer**: Focuses on mechanisms of optimization, pre-training, supervised fine-tuning, RLHF/DPO, objective functions, and training hyperparameters.
* **Inference Layer**: Focuses on runtime execution, hardware serving configurations, token decoding (greedy, sampling), KV-caching, and batching.
* **Retrieval Layer**: Focuses on vector database search, embeddings, document chunking, indexing schemas, and context injection templates.
* **Memory Layer**: Focuses on conversational history storage, semantic caches, read/write protocols, and state persistence patterns.
* **Agent Layer**: Focuses on planning loops (ReAct, plan-and-solve), tool-use schemas, routing protocols, and execution orchestrations.
* **Evaluation Layer**: Focuses on automated and human benchmark runs, metrics (accuracy, BLEU, custom), and evaluation validation frameworks.
* **Governance Layer**: Focuses on runtime moderations, content filtering rules, alignment safety guardrails, and risk control mechanisms.

This table and definitions form a planning scaffold. Future entries must stay neutral until
supported by approved research ledger evidence.

## Layer Stubs

Current neutral stubs:

* `model-layer.md`
* `training-layer.md`
* `inference-layer.md`
* `retrieval-layer.md`
* `memory-layer.md`
* `agent-layer.md`
* `evaluation-layer.md`
* `governance-layer.md`

## Glossary

Current placeholder:

* `glossary.md`

## Current Limits

Do not add taxonomy claims, layer definitions, diagrams, or paper-ready wording
from this skeleton issue.
