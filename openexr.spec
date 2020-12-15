#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x85B2B8104CCF35AF (cary@ilm.com)
#
Name     : openexr
Version  : 2.5.3
Release  : 14
URL      : https://github.com/AcademySoftwareFoundation/openexr/archive/v2.5.3/openexr-2.5.3.tar.gz
Source0  : https://github.com/AcademySoftwareFoundation/openexr/archive/v2.5.3/openexr-2.5.3.tar.gz
Source1  : https://github.com/AcademySoftwareFoundation/openexr/archive/v2.5.3/openexr-2.5.3.tar.gz.sig
Summary  : Python bindings for the IlmBase libraries
Group    : Development/Tools
License  : BSD-3-Clause
Requires: openexr-bin = %{version}-%{release}
Requires: openexr-lib = %{version}-%{release}
Requires: openexr-license = %{version}-%{release}
Requires: openexr-python = %{version}-%{release}
Requires: openexr-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : fltk-dev
BuildRequires : freeglut-dev
BuildRequires : glibc-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
The IlmImfUtil Library
----------------------
The IlmImfUtil library implements an in-memory image data structure, as
well as simple function calls for saving images in OpenEXR files, and for
constructing images from the contents of existing OpenEXR files.

%package bin
Summary: bin components for the openexr package.
Group: Binaries
Requires: openexr-license = %{version}-%{release}

%description bin
bin components for the openexr package.


%package dev
Summary: dev components for the openexr package.
Group: Development
Requires: openexr-lib = %{version}-%{release}
Requires: openexr-bin = %{version}-%{release}
Provides: openexr-devel = %{version}-%{release}
Requires: openexr = %{version}-%{release}

%description dev
dev components for the openexr package.


%package doc
Summary: doc components for the openexr package.
Group: Documentation

%description doc
doc components for the openexr package.


%package lib
Summary: lib components for the openexr package.
Group: Libraries
Requires: openexr-license = %{version}-%{release}

%description lib
lib components for the openexr package.


%package license
Summary: license components for the openexr package.
Group: Default

%description license
license components for the openexr package.


%package python
Summary: python components for the openexr package.
Group: Default
Requires: openexr-python3 = %{version}-%{release}

%description python
python components for the openexr package.


%package python3
Summary: python3 components for the openexr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openexr package.


%prep
%setup -q -n openexr-2.5.3
cd %{_builddir}/openexr-2.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604374496
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604374496
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openexr
cp %{_builddir}/openexr-2.5.3/LICENSE.md %{buildroot}/usr/share/package-licenses/openexr/ce40fed41edcb2473538bb84f85ff79e585760b5
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exr2aces
/usr/bin/exrenvmap
/usr/bin/exrheader
/usr/bin/exrmakepreview
/usr/bin/exrmaketiled
/usr/bin/exrmultipart
/usr/bin/exrmultiview
/usr/bin/exrstdattr

%files dev
%defattr(-,root,root,-)
/usr/include/OpenEXR/Iex.h
/usr/include/OpenEXR/IexBaseExc.h
/usr/include/OpenEXR/IexErrnoExc.h
/usr/include/OpenEXR/IexExport.h
/usr/include/OpenEXR/IexForward.h
/usr/include/OpenEXR/IexMacros.h
/usr/include/OpenEXR/IexMathExc.h
/usr/include/OpenEXR/IexMathFloatExc.h
/usr/include/OpenEXR/IexMathFpu.h
/usr/include/OpenEXR/IexMathIeeeExc.h
/usr/include/OpenEXR/IexNamespace.h
/usr/include/OpenEXR/IexThrowErrnoExc.h
/usr/include/OpenEXR/IlmBaseConfig.h
/usr/include/OpenEXR/IlmThread.h
/usr/include/OpenEXR/IlmThreadExport.h
/usr/include/OpenEXR/IlmThreadForward.h
/usr/include/OpenEXR/IlmThreadMutex.h
/usr/include/OpenEXR/IlmThreadNamespace.h
/usr/include/OpenEXR/IlmThreadPool.h
/usr/include/OpenEXR/IlmThreadSemaphore.h
/usr/include/OpenEXR/ImathBox.h
/usr/include/OpenEXR/ImathBoxAlgo.h
/usr/include/OpenEXR/ImathColor.h
/usr/include/OpenEXR/ImathColorAlgo.h
/usr/include/OpenEXR/ImathEuler.h
/usr/include/OpenEXR/ImathExc.h
/usr/include/OpenEXR/ImathExport.h
/usr/include/OpenEXR/ImathForward.h
/usr/include/OpenEXR/ImathFrame.h
/usr/include/OpenEXR/ImathFrustum.h
/usr/include/OpenEXR/ImathFrustumTest.h
/usr/include/OpenEXR/ImathFun.h
/usr/include/OpenEXR/ImathGL.h
/usr/include/OpenEXR/ImathGLU.h
/usr/include/OpenEXR/ImathHalfLimits.h
/usr/include/OpenEXR/ImathInt64.h
/usr/include/OpenEXR/ImathInterval.h
/usr/include/OpenEXR/ImathLimits.h
/usr/include/OpenEXR/ImathLine.h
/usr/include/OpenEXR/ImathLineAlgo.h
/usr/include/OpenEXR/ImathMath.h
/usr/include/OpenEXR/ImathMatrix.h
/usr/include/OpenEXR/ImathMatrixAlgo.h
/usr/include/OpenEXR/ImathNamespace.h
/usr/include/OpenEXR/ImathPlane.h
/usr/include/OpenEXR/ImathPlatform.h
/usr/include/OpenEXR/ImathQuat.h
/usr/include/OpenEXR/ImathRandom.h
/usr/include/OpenEXR/ImathRoots.h
/usr/include/OpenEXR/ImathShear.h
/usr/include/OpenEXR/ImathSphere.h
/usr/include/OpenEXR/ImathVec.h
/usr/include/OpenEXR/ImathVecAlgo.h
/usr/include/OpenEXR/ImfAcesFile.h
/usr/include/OpenEXR/ImfArray.h
/usr/include/OpenEXR/ImfAttribute.h
/usr/include/OpenEXR/ImfB44Compressor.h
/usr/include/OpenEXR/ImfBoxAttribute.h
/usr/include/OpenEXR/ImfCRgbaFile.h
/usr/include/OpenEXR/ImfChannelList.h
/usr/include/OpenEXR/ImfChannelListAttribute.h
/usr/include/OpenEXR/ImfChromaticities.h
/usr/include/OpenEXR/ImfChromaticitiesAttribute.h
/usr/include/OpenEXR/ImfCompositeDeepScanLine.h
/usr/include/OpenEXR/ImfCompression.h
/usr/include/OpenEXR/ImfCompressionAttribute.h
/usr/include/OpenEXR/ImfConvert.h
/usr/include/OpenEXR/ImfDeepCompositing.h
/usr/include/OpenEXR/ImfDeepFrameBuffer.h
/usr/include/OpenEXR/ImfDeepImage.h
/usr/include/OpenEXR/ImfDeepImageChannel.h
/usr/include/OpenEXR/ImfDeepImageIO.h
/usr/include/OpenEXR/ImfDeepImageLevel.h
/usr/include/OpenEXR/ImfDeepImageState.h
/usr/include/OpenEXR/ImfDeepImageStateAttribute.h
/usr/include/OpenEXR/ImfDeepScanLineInputFile.h
/usr/include/OpenEXR/ImfDeepScanLineInputPart.h
/usr/include/OpenEXR/ImfDeepScanLineOutputFile.h
/usr/include/OpenEXR/ImfDeepScanLineOutputPart.h
/usr/include/OpenEXR/ImfDeepTiledInputFile.h
/usr/include/OpenEXR/ImfDeepTiledInputPart.h
/usr/include/OpenEXR/ImfDeepTiledOutputFile.h
/usr/include/OpenEXR/ImfDeepTiledOutputPart.h
/usr/include/OpenEXR/ImfDoubleAttribute.h
/usr/include/OpenEXR/ImfEnvmap.h
/usr/include/OpenEXR/ImfEnvmapAttribute.h
/usr/include/OpenEXR/ImfExport.h
/usr/include/OpenEXR/ImfFlatImage.h
/usr/include/OpenEXR/ImfFlatImageChannel.h
/usr/include/OpenEXR/ImfFlatImageIO.h
/usr/include/OpenEXR/ImfFlatImageLevel.h
/usr/include/OpenEXR/ImfFloatAttribute.h
/usr/include/OpenEXR/ImfFloatVectorAttribute.h
/usr/include/OpenEXR/ImfForward.h
/usr/include/OpenEXR/ImfFrameBuffer.h
/usr/include/OpenEXR/ImfFramesPerSecond.h
/usr/include/OpenEXR/ImfGenericInputFile.h
/usr/include/OpenEXR/ImfGenericOutputFile.h
/usr/include/OpenEXR/ImfHeader.h
/usr/include/OpenEXR/ImfHuf.h
/usr/include/OpenEXR/ImfIO.h
/usr/include/OpenEXR/ImfImage.h
/usr/include/OpenEXR/ImfImageChannel.h
/usr/include/OpenEXR/ImfImageChannelRenaming.h
/usr/include/OpenEXR/ImfImageDataWindow.h
/usr/include/OpenEXR/ImfImageIO.h
/usr/include/OpenEXR/ImfImageLevel.h
/usr/include/OpenEXR/ImfInputFile.h
/usr/include/OpenEXR/ImfInputPart.h
/usr/include/OpenEXR/ImfInt64.h
/usr/include/OpenEXR/ImfIntAttribute.h
/usr/include/OpenEXR/ImfKeyCode.h
/usr/include/OpenEXR/ImfKeyCodeAttribute.h
/usr/include/OpenEXR/ImfLineOrder.h
/usr/include/OpenEXR/ImfLineOrderAttribute.h
/usr/include/OpenEXR/ImfLut.h
/usr/include/OpenEXR/ImfMatrixAttribute.h
/usr/include/OpenEXR/ImfMultiPartInputFile.h
/usr/include/OpenEXR/ImfMultiPartOutputFile.h
/usr/include/OpenEXR/ImfMultiView.h
/usr/include/OpenEXR/ImfName.h
/usr/include/OpenEXR/ImfNamespace.h
/usr/include/OpenEXR/ImfOpaqueAttribute.h
/usr/include/OpenEXR/ImfOutputFile.h
/usr/include/OpenEXR/ImfOutputPart.h
/usr/include/OpenEXR/ImfPartHelper.h
/usr/include/OpenEXR/ImfPartType.h
/usr/include/OpenEXR/ImfPixelType.h
/usr/include/OpenEXR/ImfPreviewImage.h
/usr/include/OpenEXR/ImfPreviewImageAttribute.h
/usr/include/OpenEXR/ImfRational.h
/usr/include/OpenEXR/ImfRationalAttribute.h
/usr/include/OpenEXR/ImfRgba.h
/usr/include/OpenEXR/ImfRgbaFile.h
/usr/include/OpenEXR/ImfRgbaYca.h
/usr/include/OpenEXR/ImfSampleCountChannel.h
/usr/include/OpenEXR/ImfStandardAttributes.h
/usr/include/OpenEXR/ImfStdIO.h
/usr/include/OpenEXR/ImfStringAttribute.h
/usr/include/OpenEXR/ImfStringVectorAttribute.h
/usr/include/OpenEXR/ImfTestFile.h
/usr/include/OpenEXR/ImfThreading.h
/usr/include/OpenEXR/ImfTileDescription.h
/usr/include/OpenEXR/ImfTileDescriptionAttribute.h
/usr/include/OpenEXR/ImfTiledInputFile.h
/usr/include/OpenEXR/ImfTiledInputPart.h
/usr/include/OpenEXR/ImfTiledOutputFile.h
/usr/include/OpenEXR/ImfTiledOutputPart.h
/usr/include/OpenEXR/ImfTiledRgbaFile.h
/usr/include/OpenEXR/ImfTimeCode.h
/usr/include/OpenEXR/ImfTimeCodeAttribute.h
/usr/include/OpenEXR/ImfUtilExport.h
/usr/include/OpenEXR/ImfVecAttribute.h
/usr/include/OpenEXR/ImfVersion.h
/usr/include/OpenEXR/ImfWav.h
/usr/include/OpenEXR/ImfXdr.h
/usr/include/OpenEXR/OpenEXRConfig.h
/usr/include/OpenEXR/PyIex.h
/usr/include/OpenEXR/PyIexExport.h
/usr/include/OpenEXR/PyIexTypeTranslator.h
/usr/include/OpenEXR/PyImath.h
/usr/include/OpenEXR/PyImathAutovectorize.h
/usr/include/OpenEXR/PyImathBasicTypes.h
/usr/include/OpenEXR/PyImathBox.h
/usr/include/OpenEXR/PyImathBoxArrayImpl.h
/usr/include/OpenEXR/PyImathColor.h
/usr/include/OpenEXR/PyImathColor3ArrayImpl.h
/usr/include/OpenEXR/PyImathColor4Array2DImpl.h
/usr/include/OpenEXR/PyImathColor4ArrayImpl.h
/usr/include/OpenEXR/PyImathDecorators.h
/usr/include/OpenEXR/PyImathEuler.h
/usr/include/OpenEXR/PyImathExport.h
/usr/include/OpenEXR/PyImathFixedArray.h
/usr/include/OpenEXR/PyImathFixedArray2D.h
/usr/include/OpenEXR/PyImathFixedMatrix.h
/usr/include/OpenEXR/PyImathFixedVArray.h
/usr/include/OpenEXR/PyImathFrustum.h
/usr/include/OpenEXR/PyImathFun.h
/usr/include/OpenEXR/PyImathLine.h
/usr/include/OpenEXR/PyImathM44Array.h
/usr/include/OpenEXR/PyImathMathExc.h
/usr/include/OpenEXR/PyImathMatrix.h
/usr/include/OpenEXR/PyImathOperators.h
/usr/include/OpenEXR/PyImathPlane.h
/usr/include/OpenEXR/PyImathQuat.h
/usr/include/OpenEXR/PyImathRandom.h
/usr/include/OpenEXR/PyImathShear.h
/usr/include/OpenEXR/PyImathStringArray.h
/usr/include/OpenEXR/PyImathStringArrayRegister.h
/usr/include/OpenEXR/PyImathStringTable.h
/usr/include/OpenEXR/PyImathTask.h
/usr/include/OpenEXR/PyImathUtil.h
/usr/include/OpenEXR/PyImathVec.h
/usr/include/OpenEXR/PyImathVec2Impl.h
/usr/include/OpenEXR/PyImathVec3ArrayImpl.h
/usr/include/OpenEXR/PyImathVec3Impl.h
/usr/include/OpenEXR/PyImathVec4ArrayImpl.h
/usr/include/OpenEXR/PyImathVec4Impl.h
/usr/include/OpenEXR/PyImathVecOperators.h
/usr/include/OpenEXR/half.h
/usr/include/OpenEXR/halfExport.h
/usr/include/OpenEXR/halfFunction.h
/usr/include/OpenEXR/halfLimits.h
/usr/lib64/cmake/IlmBase/IlmBaseConfig.cmake
/usr/lib64/cmake/IlmBase/IlmBaseConfigVersion.cmake
/usr/lib64/cmake/IlmBase/IlmBaseTargets-relwithdebinfo.cmake
/usr/lib64/cmake/IlmBase/IlmBaseTargets.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRConfig.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRConfigVersion.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRTargets.cmake
/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfig-relwithdebinfo.cmake
/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfig.cmake
/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfigVersion.cmake
/usr/lib64/libHalf-2_5.so
/usr/lib64/libHalf.so
/usr/lib64/libIex-2_5.so
/usr/lib64/libIex.so
/usr/lib64/libIexMath-2_5.so
/usr/lib64/libIexMath.so
/usr/lib64/libIlmImf-2_5.so
/usr/lib64/libIlmImf.so
/usr/lib64/libIlmImfUtil-2_5.so
/usr/lib64/libIlmImfUtil.so
/usr/lib64/libIlmThread-2_5.so
/usr/lib64/libIlmThread.so
/usr/lib64/libImath-2_5.so
/usr/lib64/libImath.so
/usr/lib64/libPyIex_Python3_8-2_5.so
/usr/lib64/libPyImath_Python3_8-2_5.so
/usr/lib64/pkgconfig/IlmBase.pc
/usr/lib64/pkgconfig/OpenEXR.pc
/usr/lib64/pkgconfig/PyIlmBase.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/OpenEXR/InterpretingDeepPixels.pdf
/usr/share/doc/OpenEXR/MultiViewOpenEXR.pdf
/usr/share/doc/OpenEXR/OpenEXRFileLayout.pdf
/usr/share/doc/OpenEXR/ReadingAndWritingImageFiles.pdf
/usr/share/doc/OpenEXR/TechnicalIntroduction.pdf
/usr/share/doc/OpenEXR/TheoryDeepPixels.pdf
/usr/share/doc/OpenEXR/examples/drawImage.cpp
/usr/share/doc/OpenEXR/examples/drawImage.h
/usr/share/doc/OpenEXR/examples/generalInterfaceExamples.cpp
/usr/share/doc/OpenEXR/examples/generalInterfaceExamples.h
/usr/share/doc/OpenEXR/examples/generalInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR/examples/generalInterfaceTiledExamples.h
/usr/share/doc/OpenEXR/examples/lowLevelIoExamples.cpp
/usr/share/doc/OpenEXR/examples/lowLevelIoExamples.h
/usr/share/doc/OpenEXR/examples/main.cpp
/usr/share/doc/OpenEXR/examples/namespaceAlias.h
/usr/share/doc/OpenEXR/examples/previewImageExamples.cpp
/usr/share/doc/OpenEXR/examples/previewImageExamples.h
/usr/share/doc/OpenEXR/examples/rgbaInterfaceExamples.cpp
/usr/share/doc/OpenEXR/examples/rgbaInterfaceExamples.h
/usr/share/doc/OpenEXR/examples/rgbaInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR/examples/rgbaInterfaceTiledExamples.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libHalf-2_5.so.25
/usr/lib64/libHalf-2_5.so.25.0.2
/usr/lib64/libIex-2_5.so.25
/usr/lib64/libIex-2_5.so.25.0.2
/usr/lib64/libIexMath-2_5.so.25
/usr/lib64/libIexMath-2_5.so.25.0.2
/usr/lib64/libIlmImf-2_5.so.25
/usr/lib64/libIlmImf-2_5.so.25.0.2
/usr/lib64/libIlmImfUtil-2_5.so.25
/usr/lib64/libIlmImfUtil-2_5.so.25.0.2
/usr/lib64/libIlmThread-2_5.so.25
/usr/lib64/libIlmThread-2_5.so.25.0.2
/usr/lib64/libImath-2_5.so.25
/usr/lib64/libImath-2_5.so.25.0.2
/usr/lib64/libPyIex_Python3_8-2_5.so.25
/usr/lib64/libPyIex_Python3_8-2_5.so.25.0.2
/usr/lib64/libPyImath_Python3_8-2_5.so.25
/usr/lib64/libPyImath_Python3_8-2_5.so.25.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openexr/ce40fed41edcb2473538bb84f85ff79e585760b5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
