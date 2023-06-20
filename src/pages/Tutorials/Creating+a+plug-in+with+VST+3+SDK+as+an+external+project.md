>/ [VST Home](../) / [Tutorials](Index.md)
>
># Creating a plug-in with VST 3 SDK as an external project

**On this page:**

[[_TOC_]]

**Related pages:**

- [Generate a new plug-in with Project Generator](Generate+new+plug-in+with+Project+Generator.md)

---

## Goal

This is a simple Hello World VST 3 FX plug-in to demonstrate how to use the VST 3 SDK as an external project.

This plug-in was generated with the VST 3 Project Generator and it is available here [https://github.com/steinbergmedia/vst3_example_plugin_hello_world](https://github.com/steinbergmedia/vst3_example_plugin_hello_world)

---

## Part 1: How to clone and build
Open a command prompt and do the following:

 ``` 
git clone https://github.com/steinbergmedia/vst3_example_plugin_hello_world.git
mkdir build
cd build
cmake ../vst3_example_plugin_hello_world
cmake --build .
 ```

---

## Part 2: Adapting the **helloworld** example

- This example is there mainly to demonstrate how to use **VST 3 SDK** as an external project, we highly recommand to use the [Project Generator](Generate+new+plug-in+with+Project+Generator.md) to start from scratch.

- In the following explaination we try to show you how to modify the source code to build your plug-in on the helloworld example.

- Now you have to adapt some ***uids*** and naming to make your plug-in unique (and not a duplicate of helloworld!)
  1. Rename all strings for your plug-in from ***HelloWorld*** to ***MyDelay*** (for example):
     - ***HelloWorldProcessor::HelloWorldProcessor*** to ***MyDelayProcessor::MyDelayProcessor***

  2. Open the file vst3_example_plugin_hello_world/include/helloworldcids.h and create new uids for processor and for controller: you can use GUID creator tools like <https://www.guidgenerator.com>:
  ``` c++
  static const FUID kHelloWorldProcessorUID (0x2A0CC26C, 0xBF88964C, 0xB0BFFCB0, 0x554AF523);
  static const FUID kHelloWorldControllerUID (0xB9DBBD64, 0xF7C40A4C, 0x9C8BFB33, 0x8761E244);
  ```

  3. Open the file ***version.h*** and adapt the strings like this:

  ``` c++
  #define stringOriginalFilename "MyDelay.vst3"
  
  #define stringFileDescription	"MyDelay VST3"
  ```

  4. Open the file ***helloworldentry.cpp*** and adapt string:
    
  ``` c++
  #define stringPluginName "My First Delay"
  ```

- Now you can start to code for your effect/instrument (see [Code your first plug-in](Code+your+first+plug-in.md) for a step-by-step explanation)
  1. Add parameters in helloworldcontroller.cpp
  2. Adapt your process algorithm in helloworldprocessor.cpp
  3. Add persistence in helloworldprocessor.cpp
  4. Add UI (check SDK examples using **[VSTGUI](../What+is+the+VST+3+SDK/VSTGUI.md))**
- Happy coding!
