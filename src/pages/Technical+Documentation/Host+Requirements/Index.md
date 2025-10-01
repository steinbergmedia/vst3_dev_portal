>/ [VST Home](../../) / [Technical Documentation](../Index.md)
>
># Minimum Host requirements for VST 3 support

---

**VST 3** Interfaces to be implemented by a **VST 3** host:

- [\[3.0.0\] Interfaces supported by the host](../Change+History/3.0.0/Host+Interfaces.md).
- If MIDI is supported:
    - [\[3.6.12\] MIDI Learn (MIDI 1.0 support)](../Change+History/3.6.12/IMidiLearn.md).
    - in addition to previous MIDI Learn: [\[3.8.0\] MIDI Learn 2 (MIDI 2.0 support)](../Change+History/3.8.0/IMidiLearn2.md).
- [\[3.6.12\] Host Query Interface support](../Change+History/3.6.12/IPlugInterfaceSupport.md).
- If a plug-in implements *IPluginViewContentScaleSupport*, the host should follow the [\[3.6.6\] PlugView Content Scaling](../Change+History/3.6.6/IPlugViewContentScaleSupport.md) requirements.
