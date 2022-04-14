>/ ... / [VST 3 Workflow Diagrams](Index.md)
>
># Get Latency Call Sequence

**On this page:**

[[_TOC_]]

---

## Initiated from AudioProcessor

```mermaid
sequenceDiagram

participant AP as AudioProcessor
participant H as Host
participant EC as EditController

autonumber

AP->>+H:    sendMessage/latency changed
H-->>-AP:   return
H->>+EC:    notify
    EC->>+H:    restatComponent
    H-->>-EC:   return
EC-->>-H:   return

H->>+AP:    setProcessing (false)
    AP-->>-H: return
H->>+AP:    setActive (false)
AP-->>-H:   return
H->>+AP:    setActive (true)
    AP->>AP:    Change/adapt internal processing Algo
AP-->>-H:   return

H->>+AP:    getLatency
AP-->>-H:   return
H->>+AP:    setProcessing (true)
AP-->>-H:   return
```

## Initiated from EditController/UI

```mermaid
sequenceDiagram

participant AP as AudioProcessor
participant H as Host
participant EC as EditController

autonumber

EC->>+H:     sendMessage/latency changed
    H->>+AP:     notify
    AP-->>-H:    return
H-->>-EC:    return

EC->>+H:     restatComponent
H-->>-EC:    return
H->>+AP:     setProcessing (false)
AP-->>-H:    return
H->>+AP:     setActive (false)
AP-->>-H:    return
H->>+AP:     setActive (true)
    AP->>AP:        Change/adapt internal processing Algo
AP-->>-H:    return

H->>+AP:     getLatency
AP-->>-H:    return
H->>+AP:     setProcessing (true)
AP-->>-H:    return
```

## without EditController

```mermaid
sequenceDiagram

participant AP as AudioProcessor
participant H as Host

autonumber

H->>+AP:     setupProcessing
AP-->>-H:    return

H->>+AP:     setState
AP-->>-H:    return
H->>+AP:     setActive (true)
    AP->>AP:        Change/adapt internal processing Algo
AP-->>-H:    return

H->>+AP:     getLatency
AP-->>-H:    return
H->>+AP:     setProcessing (true)
AP-->>-H:    return
```