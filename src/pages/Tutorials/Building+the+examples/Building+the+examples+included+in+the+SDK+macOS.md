>/ [VST Home](../../)  / [Tutorials](../Index.md) / [Building the examples](Index.md)
>
># Building the examples included in the SDK on macOS

**On this page:**

[[_TOC_]]

---

## Goal

This tutorial explains how to set up your computer and create an environment for compiling the **VST 3** audio plug-in examples provided with the **VST 3 SDK**. These include plug-ins like simple DSP effects (Gain, compressor, delay, ...), synths instruments and some plug-ins showing how to handle some specific **VST 3** features (Note Expression, Program Change, channel info context, ...).

They can be loaded into **VST 3** hosts like Cubase, WaveLab, ...

---

## Part 1: Getting and installing the VST 3 SDK

For downloading the SDK, see this section "[How to set up my system for VST 3](../../Getting+Started/How+to+setup+my+system.md)".

Download cmake from: <https://cmake.org/download/> or use a package manager for your OS.

---

## Part 2: Building the examples on macOS

- Create a folder for the build and move to this folder (using cd):

``` c++
mkdir build
cd build
```

- Generate the solution/projects: specify the path to the project where CMakeLists.txt is located:

For XCode:

``` c++
cmake -GXcode ../vst3sdk
```

Without XCode (here debug variant):

``` c++
cmake -DCMAKE_BUILD_TYPE=Debug ../
```

- Build the plug-in (you can use XCode too):

``` c++
xcodebuild
(or alternatively for example for release)

cmake --build . --config Release
```
