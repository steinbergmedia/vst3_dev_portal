>/ ... / [VST 3 Workflow Diagrams](../Workflow+Diagrams/Index.md)
>
># Bus Arrangement Setting Sequence

**On this page:**

[[_TOC_]]

---

## Plug-In does accepts what the host wants as Bus Arrangements

```mermaid
sequenceDiagram

    participant H as Host
    participant P as Plug-in: IAudioProcessor

    autonumber

    H->>+P:     setProcessing (false)
    P-->>-H:    return
    H->>+P:     setActive (false)
    P-->>-H:    return

    H->>+P:     setBusArrangements (req. Ins, req. Outs)
    P-->>P:     adapt its arrangements if needed

    P-->>-H:    return kResultTrue

    H->>+P:     setActive (true)
    P-->>-H:    return
    H->>+P:     setProcessing (true)
    P-->>-H:    return
```

## Plug-In does not accept what the host wants as Bus Arrangements

```mermaid
sequenceDiagram

    participant H as Host
    participant P as Plug-in: IAudioProcessor

    autonumber

    H->>+P:     setProcessing (false)
    P-->>-H:    return
    H->>+P:     setActive (false)
    P-->>-H:    return

    H->>+P:     setBusArrangements (req. Ins, req. Outs)
    P-->>P:     Adapt its buses according to the requested ones if possible
    P-->>P:     return kResultFalse if not match.

    P-->>-H:    return kResultFalse

    H->>+P:     for each Bus: getBusArrangement ()
    P-->>-H:    return kResultTrue

    H->>+P:     setActive (true)
    P-->>-H:    return
    H->>+P:     setProcessing (true)
    P-->>-H:    return
```

## [Check FAQ for some use case!](/pages/FAQ/Processing.md#q-how-are-speaker-arrangement-settings-handled-for-fx-plug-ins)