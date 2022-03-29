>/ ... / [VST 3 Workflow Diagrams](../Workflow+Diagrams/Index.md)
>
># Edit Controller Call Sequence

**Related pages:**

- [Audio Processor Call Sequence](../Workflow+Diagrams/Audio+Processor+Call+Sequence.md)

---

```mermaid
stateDiagram

State0: Factory
State1: Created
State2: Initialized
State3: Connected

State2: IEditController->setComponentHandler
State3: IConnectionPoint->notify
State3: ----------------------------------------------
State3: IEditController->setComponentState
State3: IEditController->getTailSamples
State3: IEditController->getParameterCount
State3: IEditController->getParameterInfo
State3: IEditController->getParamValueByString
State3: IEditController->normalizedParamToPlain
State3: IEditController->plainParamToNormalized
State3: IEditController->getParamNormalized
State3: IEditController->setParamNormalized
State3: IEditController->createView
State3: ----------------------------------------------
State3: IEditController2 ...
State3: ----------------------------------------------
State3: IMidiMapping ...
State3: ----------------------------------------------
State3: IEditControllerHostEditing ...
State3: ----------------------------------------------
State3: INoteExpressionController ...
State3: ----------------------------------------------
State3: IKeyswitchController ...
State3: ----------------------------------------------
State3: IXmlRepresentationController ...

State0 --> State1: createInstance
State1 --> State0: release
State1 --> State2: initialize
State2 --> State1: terminate
State2 --> State3: IConnectionPoint->connect
State3 --> State1: terminate
```
```admonish info
Note: All Edit Controller methods must be called from the UI Thread
```
