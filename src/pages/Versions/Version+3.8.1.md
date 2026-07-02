  >/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.8.1 (2026/08/03)

## Version 3.8.1 (2026/08/03)

- Interface changes:
  - New interface [ITransportControl](../Technical+Documentation/Change+History/3.8.1/ITransportControl.md) allowing a plug-in to request transport-related actions from the host.
  - Small change in the [Midi2Controller](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/structSteinberg_1_1Vst_1_1Midi2Controller.html) struct in *ivstmidimapping2.h* that guarantees full ABI compatibility across compilers. Developers using this struct need to make a small adaptation.
  - Publication of text-based XML definition: [Clipboard VST-XML](../Technical+Documentation/Clipboard+VST-XML/Index.md) for drag-and-drop and copy-paste exchange of audio and musical elements (for example, audio files, chords, scales, and clips) with contextual metadata such as project time and color between Plug-ins and/or Applications.

- [VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md) update [4.15.1](https://github.com/steinbergmedia/vstgui/releases/tag/vstgui4_15_1)
  
- Documentation
  - Fix doxy doc in *ivstprocesscontext.h*.
  - Add clarification to the doc about [MIDILearn2](../Technical+Documentation/Change+History/3.8.0/IMidiLearn2.md) (n to m mapping).

- CMake
  - Remove AUWrapper target from main *CMakeLists.txt*.
  - Better detection of Windows 32-bit build for non-Visual Studio generators ([PR#14](https://github.com/steinbergmedia/vst3_cmake/pull/14)).

- [Plug-in Wrappers](../What+is+the+VST+3+SDK/Wrappers/Index.md):
  - Audio Unit:
    - **AUv2Wrapper**:
      - Improve MIDI value conversion.
      - Fix auwrapper.mm:
        - building AUWrapper with the new AUSDK.
        - wrong arguments to CFStringGetCharacters ([PR#80](https://github.com/steinbergmedia/vst3_public_sdk/pull/80)).
        - AUWrapper::restartComponent kLatencyChanged handling ([PR#79](https://github.com/steinbergmedia/vst3_public_sdk/pull/79)).

- [Examples](../What+is+the+VST+3+SDK/Plug-in+Examples.md):
  - Fix: incorrect note expression info in the example [Note Expression Synth](../What+is+the+VST+3+SDK/Plug-in+Examples.md#note-expression-synth) Plug-in ([Issue#78](https://github.com/steinbergmedia/vst3_public_sdk/issues/78)).
  - Fix: missing call to *notifyProgramListChange* after changing exported programs count in the [Test Multiple Program Changes](../What+is+the+VST+3+SDK/Plug-in+Examples.md#test-multiple-program-changes) Plug-in.
  - Update **Hostchecker** plug-in:
    - Check support of [ITransportControl](../Technical+Documentation/Change+History/3.8.1/ITransportControl.md).
    - Add Randomize parameters (**Vst::FunctionNameType::kRandomize** and **Vst::FunctionNameType::kRandomizeAroundCurrent**).

- Helper Classes:
  - Fix: unused parameter in module_mac.mm ([Issue#83](https://github.com/steinbergmedia/vst3_public_sdk/issues/83)).
  - Update: linux VST3 system paths: add */usr/lib64/vst3* in *vst/source/hosting/module_linux.cpp* ([PR#82](https://github.com/steinbergmedia/vst3_public_sdk/pull/82)).
  - Fix: compilation with some compilers (e.g. Clang 17), missing include *exception.h* in *threadchecker* file ([Issue#84](https://github.com/steinbergmedia/vst3_public_sdk/issues/84)).
  - Fix set window title on macOS: *editorhost/source/platform/mac/window.mm* ([Issues#134](https://github.com/steinbergmedia/vst3sdk/issues/134)).
  - Fix VST Hosting / registerWindowClass() method: RegisterClassEx() Executed Repeatedly (Win Only) in *editorhost/source/platform/win/window.cpp* ([Issues#155](https://github.com/steinbergmedia/vst3sdk/issues/155)).
  - Fix issues and improve handling when switching between different scaling factors under [Wayland](../Technical+Documentation/Change+History/3.8.0/IWaylandHost.md).
  - Fix missing *return false* when controller initialization did not work in *vst/hosting/plugprovider.cpp*.
  
- [Validator](../What+is+the+VST+3+SDK/Index.md#validator-command-line):
  - Fix: Validator test which does not respect the Audio Processor Call Sequence ([Issue#148](https://github.com/steinbergmedia/vst3sdk/issues/148)).
  - Add a new test to verify that **getParamStringByValue** and **getParamValueByString** correctly round-trip values.

- [VST3PluginTestHost](../What+is+the+VST+3+SDK/Plug-in+Test+Host.md) v3.11.0:
  - Add host support of [ITransportControl](../Technical+Documentation/Change+History/3.8.1/ITransportControl.md).
  - Add support of Randomize parameters (**Vst::FunctionNameType::kRandomize** and **Vst::FunctionNameType::kRandomizeAroundCurrent**) using [Parameter Function Name](../Technical+Documentation/Change+History/3.7.0/IParameterFunctionName.md).
  