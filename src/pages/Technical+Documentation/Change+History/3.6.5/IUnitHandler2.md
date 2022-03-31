>/ [VST Home](../../../index.md) / [Technical Documentation](../../Index.md)
>
># [3.6.5] Unit-Bus Assignment Change

**On this page:**

[[_TOC_]]

---

## Introduction

Host callback for extended unit support: [Vst::IUnitHandler2](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler2.html)

[host imp]
[extends [IUnitHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler.html)]
[released: 3.6.5]
[optional]

Host callback interface, used with [IUnitInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitInfo.html). Retrieve via queryInterface from [IComponentHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IComponentHandler.html). The plug-in has the possibility to inform the host with [notifyUnitByBusChange](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler2.html#ad1f48213839cc5b28a612a2baaba6584) that something has changed in the bus - unit assignment,the host then has to recall [IUnitInfo::getUnitByBus](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitInfo.html#a718fa905d04d7d559bc89c7ca761413b) in order to get the new relations between busses and unit.

See also [VST 3 Units](../../VST+3+Units/Index.md), [IUnitHandler](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitHandler.html), [IUnitInfo](https://steinbergmedia.github.io/vst3_doc/vstinterfaces/classSteinberg_1_1Vst_1_1IUnitInfo.html)