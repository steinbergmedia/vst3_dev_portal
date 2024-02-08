//------------------------------------------------------------------------
// Copyright(c) 2024 Steinberg Media Technologies.
//------------------------------------------------------------------------

#include "processor.h"
#include "controller.h"
#include "cids.h"
#include "version.h"

#include "public.sdk/source/main/pluginfactory.h"

#define stringPluginName "dataexchange-tutorial"

using namespace Steinberg::Vst;
using namespace Steinberg::Tutorial;

//------------------------------------------------------------------------
//  VST Plug-in Entry
//------------------------------------------------------------------------
// Windows: do not forget to include a .def file in your project to export
// GetPluginFactory function!
//------------------------------------------------------------------------

BEGIN_FACTORY_DEF ("Steinberg Media Technologies", 
			       "https://steinberg.net", 
			       "mailto:info@steinberg.de")

	//---First Plug-in included in this factory-------
	// its kVstAudioEffectClass component
	DEF_CLASS2 (INLINE_UID_FROM_FUID(kDataExchangeProcessorUID),
				PClassInfo::kManyInstances,	// cardinality
				kVstAudioEffectClass,	// the component category (do not change this)
				stringPluginName,		// here the Plug-in name (to be changed)
				Vst::kDistributable,	// means that component and controller could be distributed on different computers
				DataExchangeVST3Category, // Subcategory for this plug-in (to be changed)
				FULL_VERSION_STR,		// Plug-in version (to be changed)
				kVstVersionString,		// the VST 3 SDK version (do not change this, always use this define)
				DataExchangeProcessor::createInstance)	// function pointer called when this component should be instantiated

	// its kVstComponentControllerClass component
	DEF_CLASS2 (INLINE_UID_FROM_FUID (kDataExchangeControllerUID),
				PClassInfo::kManyInstances, // cardinality
				kVstComponentControllerClass,// the Controller category (do not change this)
				stringPluginName "Controller",	// controller name (can be the same as the component name)
				0,						// not used here
				"",						// not used here
				FULL_VERSION_STR,		// Plug-in version (to be changed)
				kVstVersionString,		// the VST 3 SDK version (do not change this, always use this define)
				DataExchangeController::createInstance)// function pointer called when this component should be instantiated

	//----for others plug-ins contained in this factory, same as for the first Plug-in different DEF_CLASS2---

END_FACTORY