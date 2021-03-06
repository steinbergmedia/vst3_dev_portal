>/ [VST Home](../) / [Change History](./Index.md)
>
># Version 3.6.10 (2018/06/11)

## Version 3.6.10 (2018/06/11)

- New definition of plug-in format for Windows including icon support (VST 3 Bundle: [VST 3 Locations / Format](../Technical+Documentation/Locations+Format/Plugin+Locations.md))
- Support of Snapshots inside the VST 3 Bundle
- cmake:
  - adapt cmake files for better integration of users projects
  - fix support Universal Binary for AudioUnit
- Plug-in wrappers:
  - refactoring AAX/VST 2 Wrappers
  - AAX Wrapper (VST 3 - AAX Wrapper):
    - fix Bypass behaviour
    - fix initial signal latency
    - fix indexing of parameter, conflicting with VST 2
- Helpers classes:
  - fix activateBus issue in class SingleComponentEffect
  - fix Ring Buffer class issue
