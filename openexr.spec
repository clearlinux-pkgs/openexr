#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE8515FFDCE2F7868 (dhess@bothan.net)
#
Name     : openexr
Version  : 1.4.0
Release  : 5
URL      : http://download.savannah.nongnu.org/releases/openexr/openexr-1.4.0a.tar.gz
Source0  : http://download.savannah.nongnu.org/releases/openexr/openexr-1.4.0a.tar.gz
Source99 : http://download.savannah.nongnu.org/releases/openexr/openexr-1.4.0a.tar.gz.sig
Summary  : OpenEXR image library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: openexr-bin
Requires: openexr-lib
Requires: openexr-data
BuildRequires : fltk-dev
BuildRequires : ilmbase-dev
BuildRequires : zlib-dev
Patch1: build.patch

%description
ABOUT THE OPENEXR LIBRARIES
----------------------------
Half is a class that encapsulates our 16-bit floating-point format.

%package bin
Summary: bin components for the openexr package.
Group: Binaries
Requires: openexr-data

%description bin
bin components for the openexr package.


%package data
Summary: data components for the openexr package.
Group: Data

%description data
data components for the openexr package.


%package dev
Summary: dev components for the openexr package.
Group: Development
Requires: openexr-lib
Requires: openexr-bin
Requires: openexr-data
Provides: openexr-devel

%description dev
dev components for the openexr package.


%package lib
Summary: lib components for the openexr package.
Group: Libraries
Requires: openexr-data

%description lib
lib components for the openexr package.


%prep
%setup -q -n openexr-1.4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502485772
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition -std=gnu++98"
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1502485772
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exrenvmap
/usr/bin/exrheader
/usr/bin/exrmakepreview
/usr/bin/exrmaketiled
/usr/bin/exrstdattr

%files data
%defattr(-,root,root,-)
/usr/share/doc/OpenEXR-1.4.0/examples/drawImage.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/drawImage.h
/usr/share/doc/OpenEXR-1.4.0/examples/generalInterfaceExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/generalInterfaceExamples.h
/usr/share/doc/OpenEXR-1.4.0/examples/generalInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/generalInterfaceTiledExamples.h
/usr/share/doc/OpenEXR-1.4.0/examples/lowLevelIoExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/lowLevelIoExamples.h
/usr/share/doc/OpenEXR-1.4.0/examples/main.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/previewImageExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/previewImageExamples.h
/usr/share/doc/OpenEXR-1.4.0/examples/rgbaInterfaceExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/rgbaInterfaceExamples.h
/usr/share/doc/OpenEXR-1.4.0/examples/rgbaInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR-1.4.0/examples/rgbaInterfaceTiledExamples.h

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/OpenEXR/Iex.h
%exclude /usr/include/OpenEXR/IexBaseExc.h
%exclude /usr/include/OpenEXR/IexErrnoExc.h
%exclude /usr/include/OpenEXR/IexMacros.h
%exclude /usr/include/OpenEXR/IexMathExc.h
%exclude /usr/include/OpenEXR/IexThrowErrnoExc.h
%exclude /usr/include/OpenEXR/IlmThread.h
%exclude /usr/include/OpenEXR/IlmThreadMutex.h
%exclude /usr/include/OpenEXR/IlmThreadPool.h
%exclude /usr/include/OpenEXR/IlmThreadSemaphore.h
%exclude /usr/include/OpenEXR/ImathBox.h
%exclude /usr/include/OpenEXR/ImathBoxAlgo.h
%exclude /usr/include/OpenEXR/ImathColor.h
%exclude /usr/include/OpenEXR/ImathColorAlgo.h
%exclude /usr/include/OpenEXR/ImathEuler.h
%exclude /usr/include/OpenEXR/ImathExc.h
%exclude /usr/include/OpenEXR/ImathFrame.h
%exclude /usr/include/OpenEXR/ImathFrustum.h
%exclude /usr/include/OpenEXR/ImathFun.h
%exclude /usr/include/OpenEXR/ImathGL.h
%exclude /usr/include/OpenEXR/ImathGLU.h
%exclude /usr/include/OpenEXR/ImathHalfLimits.h
%exclude /usr/include/OpenEXR/ImathInterval.h
%exclude /usr/include/OpenEXR/ImathLimits.h
%exclude /usr/include/OpenEXR/ImathLine.h
%exclude /usr/include/OpenEXR/ImathLineAlgo.h
%exclude /usr/include/OpenEXR/ImathMath.h
%exclude /usr/include/OpenEXR/ImathMatrix.h
%exclude /usr/include/OpenEXR/ImathMatrixAlgo.h
%exclude /usr/include/OpenEXR/ImathPlane.h
%exclude /usr/include/OpenEXR/ImathPlatform.h
%exclude /usr/include/OpenEXR/ImathQuat.h
%exclude /usr/include/OpenEXR/ImathRandom.h
%exclude /usr/include/OpenEXR/ImathRoots.h
%exclude /usr/include/OpenEXR/ImathShear.h
%exclude /usr/include/OpenEXR/ImathSphere.h
%exclude /usr/include/OpenEXR/ImathVec.h
%exclude /usr/include/OpenEXR/ImathVecAlgo.h
%exclude /usr/include/OpenEXR/half.h
%exclude /usr/include/OpenEXR/halfFunction.h
%exclude /usr/include/OpenEXR/halfLimits.h
%exclude /usr/lib64/libHalf.so
%exclude /usr/lib64/libIex.so
%exclude /usr/lib64/libIlmThread.so
%exclude /usr/lib64/libImath.so
/usr/include/OpenEXR/ImfArray.h
/usr/include/OpenEXR/ImfAttribute.h
/usr/include/OpenEXR/ImfBoxAttribute.h
/usr/include/OpenEXR/ImfCRgbaFile.h
/usr/include/OpenEXR/ImfChannelList.h
/usr/include/OpenEXR/ImfChannelListAttribute.h
/usr/include/OpenEXR/ImfChromaticities.h
/usr/include/OpenEXR/ImfChromaticitiesAttribute.h
/usr/include/OpenEXR/ImfCompression.h
/usr/include/OpenEXR/ImfCompressionAttribute.h
/usr/include/OpenEXR/ImfConvert.h
/usr/include/OpenEXR/ImfDoubleAttribute.h
/usr/include/OpenEXR/ImfEnvmap.h
/usr/include/OpenEXR/ImfEnvmapAttribute.h
/usr/include/OpenEXR/ImfFloatAttribute.h
/usr/include/OpenEXR/ImfFrameBuffer.h
/usr/include/OpenEXR/ImfHeader.h
/usr/include/OpenEXR/ImfHuf.h
/usr/include/OpenEXR/ImfIO.h
/usr/include/OpenEXR/ImfInputFile.h
/usr/include/OpenEXR/ImfInt64.h
/usr/include/OpenEXR/ImfIntAttribute.h
/usr/include/OpenEXR/ImfKeyCode.h
/usr/include/OpenEXR/ImfKeyCodeAttribute.h
/usr/include/OpenEXR/ImfLineOrder.h
/usr/include/OpenEXR/ImfLineOrderAttribute.h
/usr/include/OpenEXR/ImfLut.h
/usr/include/OpenEXR/ImfMatrixAttribute.h
/usr/include/OpenEXR/ImfName.h
/usr/include/OpenEXR/ImfOpaqueAttribute.h
/usr/include/OpenEXR/ImfOutputFile.h
/usr/include/OpenEXR/ImfPixelType.h
/usr/include/OpenEXR/ImfPreviewImage.h
/usr/include/OpenEXR/ImfPreviewImageAttribute.h
/usr/include/OpenEXR/ImfRgba.h
/usr/include/OpenEXR/ImfRgbaFile.h
/usr/include/OpenEXR/ImfRgbaYca.h
/usr/include/OpenEXR/ImfStandardAttributes.h
/usr/include/OpenEXR/ImfStringAttribute.h
/usr/include/OpenEXR/ImfTestFile.h
/usr/include/OpenEXR/ImfThreading.h
/usr/include/OpenEXR/ImfTileDescription.h
/usr/include/OpenEXR/ImfTileDescriptionAttribute.h
/usr/include/OpenEXR/ImfTiledInputFile.h
/usr/include/OpenEXR/ImfTiledOutputFile.h
/usr/include/OpenEXR/ImfTiledRgbaFile.h
/usr/include/OpenEXR/ImfTimeCode.h
/usr/include/OpenEXR/ImfTimeCodeAttribute.h
/usr/include/OpenEXR/ImfVecAttribute.h
/usr/include/OpenEXR/ImfVersion.h
/usr/include/OpenEXR/ImfWav.h
/usr/include/OpenEXR/ImfXdr.h
/usr/include/OpenEXR/OpenEXRConfig.h
/usr/lib64/libIlmImf.so
/usr/lib64/pkgconfig/OpenEXR.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libHalf.so.4
/usr/lib64/libHalf.so.4.0.0
/usr/lib64/libIex.so.4
/usr/lib64/libIex.so.4.0.0
/usr/lib64/libIlmImf.so.4
/usr/lib64/libIlmImf.so.4.0.0
/usr/lib64/libIlmThread.so.4
/usr/lib64/libIlmThread.so.4.0.0
/usr/lib64/libImath.so.4
/usr/lib64/libImath.so.4.0.0
