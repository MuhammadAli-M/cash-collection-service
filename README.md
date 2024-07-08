# Cash Collection

## Overview

This repo is a solution implementation to the cash collector problem.

### Contents

- [High-level Design](#High-level-Design)
- [Approaches](#Approaches)
- [Installation](#Installation)

## High-level Design

![high_level_design.png](docs/high_level_design.png)

## Approaches

We have a challenge here which is the future automatic freeze in addition to be
able to show the freeze status at different time points.

So. I thought of two solutions:

1. When the collection passes the amount, add event to denote future freeze. And
   when paying, update the event or add new event to inactivate the future
   freezing or declare the unfreezing.
2. When the collection passes the amount, schedule a job to validate freezing
   after 2 days (the tolerance before actual freeze)

### Persisting Array of Events (freeze and unfreeze)

Assume collector has `status_events: List[StatusEvent]`.
`StatusEvent (due_at, is_frozen, active, created_at, updated_at)`

After each `collect`, we check:

1. If we didn't pass the amount, we do nothing
2. If we passed the amount && the latest event is a freeze but not active or an
   unfreeze event but active, we add a freeze event

Before the `collect`, we check the latest active freeze event:

1. If it's not due yet, we do nothing.
2. If it's already due, we reject the collection.

With each `pay`, we check the latest active StatusEvent:

1. If it is not due yet, we make it inactive.
2. If it is already due, we add an unfreeze event.

![time_followup_approach1.png](docs/time_followup_approach1.png)

### Job scheduling (Using Celery Tasks)

Assume collector has `status_events: List[StatusEvent]`.
`StatusEvent (is_frozen, created_at, updated_at)`

With each `collect`, we schedule a celery task to validate freezing after 2
days.
If there is already a scheduled task, we do nothing.

With each `pay`, we cancel the scheduled task or add unfreeze event.

With each freeze validation, we add freeze event, or do nothing if it's paid.

## Installation

### Prerequisites

- sqlite3 database, just for simplicity.
- virtualenv, mentioned in the Makefile targets

### Getting Started

Create virtual environment and install requirements

```shell
make build
```

### Tools

- Install [Trunk](https://docs.trunk.io/check/usage#install-the-cli) for linting

### Project Structure

The project structure is influenced by **clean architecture**.

#### Clean Architecture Influence:

- Mainly, each Django app should have the following structure:

  - entities
  - usecases
  - contracts
  - infra
  - controllers
  - models
  - repositories
  - migrations

- Most requests would sequentially pass through multiple layers.
  - infra/controllers/{endpoint_name}\_api.py
  - usecases/{usecase_name}.py
  - entities/{entity_name}.py
  - infra/repos/{repo_name}\_repo.py
  - infra/repos/{dao_name}\_dao.py
  - infra/models/{model}.py

Also, there is the `/tests` directory that contains the test files with
mirroring the structure for the `/src` that contains the code.
