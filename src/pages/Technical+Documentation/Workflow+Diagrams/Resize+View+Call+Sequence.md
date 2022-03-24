>/ ... / [VST 3 Workflow Diagrams](../Workflow+Diagrams/Index.md)
>
># Resize View Call Sequence

**On this page:**

[[_TOC_]]

---

## Initiated from Plug-In

```mermaid
sequenceDiagram

    participant P as PlugView
    participant H as Host resp. IPlugFrame

    autonumber

    Note left of P: Press e.g. "Large" button on plug-in GUI
    P->>+H:     resizeView(size)
    H->>+P:     getSize
    P-->>-H:    return
    Note right of H: Still returns the "old" size
    H->>H:      resize frame
    H->>+P:     onSize
    P->>P:      resize view
    P-->>-H:    return
    H->>+P:     getSize
    P-->>-H:    return
    Note right of H: Now returns the "new" size
    H-->>-P:    return
```

## Initiated from Host

**User drags window frame in order to resize**

```mermaid
sequenceDiagram

    participant P as PlugView
    participant H as Host resp. IPlugFrame

    autonumber

    Note right of H: User drags window frame
    Note right of H: in order to resize
    H->>+P:     checkSizeContraints(size)
    P-->>-H:    return
    H->>+H:     resize frame to [size]
    H->>+P:     onSize(size)
    P->>P:      resize view
    P-->>-H:    return
```

**Moving window to other screen**

```mermaid
sequenceDiagram

    participant P as IPlugViewContentScaleSupport
    participant H as Host resp. IPlugFrame

    autonumber
    
    Note right of H:    Move window to other screen
    H->>+P:             setContentScaleFactor(factor)
    P-->>-H:            return
    Note right of H:    From here, same sequence
    Note right of H:    than "Initiated from Plug-In"
    P->>+H:             resizeView(size)
    H-->>-P:            return
```