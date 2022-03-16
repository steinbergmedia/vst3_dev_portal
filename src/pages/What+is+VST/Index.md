/ [VST Home](../Index.md)

<font size="5">**What is VST?**</font>

### VST 3: New Standard for Virtual Studio Technology

With **VST** (Virtual Studio
Technology), [Steinberg](https://www.steinberg.net/) established the
world’s leading and most widely supported standard for plug-ins and
virtual instruments in 1996. With **VST 3**
[Steinberg](https://www.steinberg.net/) releases the next major revision
of [Steinberg](https://www.steinberg.net/)’s Virtual Studio Technology to
the audio industry. **VST 3** marks an important milestone in audio
technology with a completely rewritten code base providing not only many
new features but also the most stable and reliable VST platform ever.
This combination of latest technology and new features is the result
of [Steinberg](https://www.steinberg.net/)’s twelve years of development
experience as the leading plug-in interface provider.**VST 3** has been
designed to provide a technological and creative basis for many
innovative and exciting new products for the audio industry, offering a
new world of creative possibilities for instrument and effect plug-in
users. The **VST 3 SDK** is available as a free technology, open in use
for any developer.

### About the VST standard

The Virtual Studio Technology (**VST**) interface is nothing short of a
revolution in digital audio. Developed by Steinberg and first launched
in 1996, VST creates a full, professional studio environment on your
computer.**VST** allows the integration of virtual effect processors and
instruments into your digital audio environment. These can be software
recreations of hardware effect units and instruments or new creative
effect components in your **VST** system. All are integrated seamlessly
into **VST** compatible host applications like digital audio
workstations (DAW). **VST** also allows easy integration of external
equipment, allowing you to put together a system tailor-made to your
needs. Being an open standard, the possibilities offered by **VST** have
steadily been growing over the past decade. New virtual effect
processors and virtual instruments are constantly being developed by
Steinberg and of course dozens of other companies.

### From the technical point of view

A **VST** plug-in is an audio processing component that is utilized
within a host application. This host application provides the audio
or/and event streams that are processed by the plug-in's code. Generally
speaking, a **VST** plug-in can take a stream of audio data, apply a
process to the audio, and return the result to the host application. A
**VST** plug-in normally performs its process using the processor of the
computer. The audio stream is broken into a series of blocks. The host
supplies the blocks in sequence. The host and its current environment
control the block-size. The **VST** plug-in maintains the status of all
its own parameters relating to the running process: The host does not
maintain any information about what the plug-in did with the last block
of data it processed.

From the host application's point of view, a **VST** plug-in is a black
box with an arbitrary number of inputs, outputs (Event (MIDI) or Audio),
and associated parameters. The host needs no implicit knowledge of the
plug-in's process to be able to use it. The plug-in process can use
whatever parameters it wants, internally to the process, but depending
on the capabilities of the host, it can allow the changes to user
parameters to be automated by the host.

The source code of a **VST** plug-in is platform independent, but the
delivery system depends on the platform architecture:

* On **Windows**, a **VST** plug-in is a multi-threaded DLL (Dynamic Link Library), recently packaged into a folder structure.
* On **Mac OS X**, a **VST** plug-in is a Mach-O Bundle
* On **Linux**, a **VST** plug-in is a package

  
