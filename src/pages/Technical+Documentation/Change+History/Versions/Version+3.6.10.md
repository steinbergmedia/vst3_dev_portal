>/ ... / [Change History](../Index.md)
>
># Version 3.6.10 (2018/06/11)

## Version 3.6.10 (2018/06/11)

- New definition of plug-in format for Windows including icon support ([VST3]() **<- Link?** Bundle: [VST 3 Locations / Format](../Locations+Format/Plugin+Locations.md))
- Support of [Snapshots]() **<- Link?** inside the [VST3]() **<- Link?** Bundle
- cmake:
    - adapt cmake files for better integration of users projects
    - fix support Universal Binary for AudioUnit
- Plug-in wrappers:
    - refactoring AAX/VST2 Wrappers
    - AAX Wrapper (VST 3 - AAX Wrapper):
        - fix Bypass behaviour
        - fix initial signal latency
        - fix indexing of parameter, conflicting with VST2
- Helpers classes:
    - fix activateBus issue in class SingleComponentEffect
    - fix Ring Buffer class issue