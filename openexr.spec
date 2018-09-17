#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openexr
Version  : 2.2.1
Release  : 9
URL      : http://download.savannah.nongnu.org/releases/openexr/openexr-2.2.1.tar.gz
Source0  : http://download.savannah.nongnu.org/releases/openexr/openexr-2.2.1.tar.gz
Summary  : OpenEXR image library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: openexr-bin
Requires: openexr-lib
Requires: openexr-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : fltk-dev
BuildRequires : ilmbase-dev
BuildRequires : zlib-dev
Patch1: build.patch

%description
ABOUT THE OPENEXR LIBRARIES
----------------------------
IlmImf is our "EXR" file format for storing 16-bit FP images.  Libraries in
this package depend on the IlmBase library.

%package bin
Summary: bin components for the openexr package.
Group: Binaries
Requires: openexr-license

%description bin
bin components for the openexr package.


%package dev
Summary: dev components for the openexr package.
Group: Development
Requires: openexr-lib
Requires: openexr-bin
Provides: openexr-devel

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
Requires: openexr-license

%description lib
lib components for the openexr package.


%package license
Summary: license components for the openexr package.
Group: Default

%description license
license components for the openexr package.


%prep
%setup -q -n openexr-2.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537215201
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -std=gnu++98"
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1537215201
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openexr
cp COPYING %{buildroot}/usr/share/doc/openexr/COPYING
cp LICENSE %{buildroot}/usr/share/doc/openexr/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exrenvmap
/usr/bin/exrheader
/usr/bin/exrmakepreview
/usr/bin/exrmaketiled
/usr/bin/exrmultipart
/usr/bin/exrmultiview
/usr/bin/exrstdattr

%files dev
%defattr(-,root,root,-)
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
/usr/include/OpenEXR/ImfFloatAttribute.h
/usr/include/OpenEXR/ImfForward.h
/usr/include/OpenEXR/ImfFrameBuffer.h
/usr/include/OpenEXR/ImfFramesPerSecond.h
/usr/include/OpenEXR/ImfGenericInputFile.h
/usr/include/OpenEXR/ImfGenericOutputFile.h
/usr/include/OpenEXR/ImfHeader.h
/usr/include/OpenEXR/ImfHuf.h
/usr/include/OpenEXR/ImfIO.h
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
/usr/include/OpenEXR/ImfMisc.h
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
/usr/include/OpenEXR/ImfStandardAttributes.h
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
/usr/include/OpenEXR/ImfVecAttribute.h
/usr/include/OpenEXR/ImfVersion.h
/usr/include/OpenEXR/ImfWav.h
/usr/include/OpenEXR/ImfXdr.h
/usr/include/OpenEXR/OpenEXRConfig.h
/usr/lib64/libIlmImf.so
/usr/lib64/libIlmImfUtil.so
/usr/lib64/pkgconfig/OpenEXR.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/OpenEXR-2.2.1/InterpretingDeepPixels.pdf
/usr/share/doc/OpenEXR-2.2.1/MultiViewOpenEXR.pdf
/usr/share/doc/OpenEXR-2.2.1/OpenEXRFileLayout.pdf
/usr/share/doc/OpenEXR-2.2.1/ReadingAndWritingImageFiles.pdf
/usr/share/doc/OpenEXR-2.2.1/TechnicalIntroduction.pdf
/usr/share/doc/OpenEXR-2.2.1/TheoryDeepPixels.pdf
/usr/share/doc/OpenEXR-2.2.1/examples/drawImage.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/drawImage.h
/usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceExamples.h
/usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceTiledExamples.h
/usr/share/doc/OpenEXR-2.2.1/examples/lowLevelIoExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/lowLevelIoExamples.h
/usr/share/doc/OpenEXR-2.2.1/examples/main.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/namespaceAlias.h
/usr/share/doc/OpenEXR-2.2.1/examples/previewImageExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/previewImageExamples.h
/usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceExamples.h
/usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceTiledExamples.cpp
/usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceTiledExamples.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libIlmImf-2_2.so.23
/usr/lib64/libIlmImf-2_2.so.23.0.0
/usr/lib64/libIlmImfUtil-2_2.so.23
/usr/lib64/libIlmImfUtil-2_2.so.23.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/openexr/COPYING
/usr/share/doc/openexr/LICENSE
