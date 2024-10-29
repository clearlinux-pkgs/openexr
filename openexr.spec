#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : openexr
Version  : 3.1.8
Release  : 32
URL      : https://github.com/AcademySoftwareFoundation/openexr/archive/v3.1.8/openexr-3.1.8.tar.gz
Source0  : https://github.com/AcademySoftwareFoundation/openexr/archive/v3.1.8/openexr-3.1.8.tar.gz
Summary  : OpenEXR image library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: openexr-bin = %{version}-%{release}
Requires: openexr-lib = %{version}-%{release}
Requires: openexr-license = %{version}-%{release}
BuildRequires : Imath-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules
BuildRequires : fltk-dev
BuildRequires : glibc-dev
BuildRequires : python3
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The OpenEXRUtil Library
----------------------
The OpenEXRUtil library implements an in-memory image data structure, as
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


%prep
%setup -q -n openexr-3.1.8
cd %{_builddir}/openexr-3.1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686070708
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1686070708
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openexr
cp %{_builddir}/openexr-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/openexr/8bdba5713cb211c07a30241ee1d0a9c668f071cd || :
cp %{_builddir}/openexr-%{version}/docs/license.rst %{buildroot}/usr/share/package-licenses/openexr/abe6364c70643c16b35007073306461670b47181 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/libImath.so
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/exr2aces
/V3/usr/bin/exrenvmap
/V3/usr/bin/exrheader
/V3/usr/bin/exrinfo
/V3/usr/bin/exrmakepreview
/V3/usr/bin/exrmaketiled
/V3/usr/bin/exrmultipart
/V3/usr/bin/exrmultiview
/V3/usr/bin/exrstdattr
/usr/bin/exr2aces
/usr/bin/exrenvmap
/usr/bin/exrheader
/usr/bin/exrinfo
/usr/bin/exrmakepreview
/usr/bin/exrmaketiled
/usr/bin/exrmultipart
/usr/bin/exrmultiview
/usr/bin/exrstdattr

%files dev
%defattr(-,root,root,-)
/usr/include/OpenEXR/Iex.h
/usr/include/OpenEXR/IexBaseExc.h
/usr/include/OpenEXR/IexConfig.h
/usr/include/OpenEXR/IexErrnoExc.h
/usr/include/OpenEXR/IexExport.h
/usr/include/OpenEXR/IexForward.h
/usr/include/OpenEXR/IexMacros.h
/usr/include/OpenEXR/IexMathExc.h
/usr/include/OpenEXR/IexMathFloatExc.h
/usr/include/OpenEXR/IexMathIeeeExc.h
/usr/include/OpenEXR/IexNamespace.h
/usr/include/OpenEXR/IexThrowErrnoExc.h
/usr/include/OpenEXR/IlmThread.h
/usr/include/OpenEXR/IlmThreadConfig.h
/usr/include/OpenEXR/IlmThreadExport.h
/usr/include/OpenEXR/IlmThreadForward.h
/usr/include/OpenEXR/IlmThreadMutex.h
/usr/include/OpenEXR/IlmThreadNamespace.h
/usr/include/OpenEXR/IlmThreadPool.h
/usr/include/OpenEXR/IlmThreadSemaphore.h
/usr/include/OpenEXR/ImfAcesFile.h
/usr/include/OpenEXR/ImfArray.h
/usr/include/OpenEXR/ImfAttribute.h
/usr/include/OpenEXR/ImfBoxAttribute.h
/usr/include/OpenEXR/ImfCRgbaFile.h
/usr/include/OpenEXR/ImfChannelList.h
/usr/include/OpenEXR/ImfChannelListAttribute.h
/usr/include/OpenEXR/ImfCheckFile.h
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
/usr/include/OpenEXR/ImfIDManifest.h
/usr/include/OpenEXR/ImfIDManifestAttribute.h
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
/usr/include/OpenEXR/openexr.h
/usr/include/OpenEXR/openexr_attr.h
/usr/include/OpenEXR/openexr_base.h
/usr/include/OpenEXR/openexr_chunkio.h
/usr/include/OpenEXR/openexr_coding.h
/usr/include/OpenEXR/openexr_conf.h
/usr/include/OpenEXR/openexr_context.h
/usr/include/OpenEXR/openexr_debug.h
/usr/include/OpenEXR/openexr_decode.h
/usr/include/OpenEXR/openexr_encode.h
/usr/include/OpenEXR/openexr_errors.h
/usr/include/OpenEXR/openexr_part.h
/usr/include/OpenEXR/openexr_std_attr.h
/usr/lib64/cmake/OpenEXR/OpenEXRConfig.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRConfigVersion.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OpenEXR/OpenEXRTargets.cmake
/usr/lib64/libIex-3_1.so
/usr/lib64/libIex.so
/usr/lib64/libIlmThread-3_1.so
/usr/lib64/libIlmThread.so
/usr/lib64/libOpenEXR-3_1.so
/usr/lib64/libOpenEXR.so
/usr/lib64/libOpenEXRCore-3_1.so
/usr/lib64/libOpenEXRCore.so
/usr/lib64/libOpenEXRUtil-3_1.so
/usr/lib64/libOpenEXRUtil.so
/usr/lib64/pkgconfig/OpenEXR.pc

%files doc
%defattr(0644,root,root,0755)
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
/V3/usr/lib64/libIex-3_1.so.30.8.1
/V3/usr/lib64/libIlmThread-3_1.so.30.8.1
/V3/usr/lib64/libOpenEXR-3_1.so.30.8.1
/V3/usr/lib64/libOpenEXRCore-3_1.so.30.8.1
/V3/usr/lib64/libOpenEXRUtil-3_1.so.30.8.1
/usr/lib64/libIex-3_1.so.30
/usr/lib64/libIex-3_1.so.30.8.1
/usr/lib64/libIlmThread-3_1.so.30
/usr/lib64/libIlmThread-3_1.so.30.8.1
/usr/lib64/libOpenEXR-3_1.so.30
/usr/lib64/libOpenEXR-3_1.so.30.8.1
/usr/lib64/libOpenEXRCore-3_1.so.30
/usr/lib64/libOpenEXRCore-3_1.so.30.8.1
/usr/lib64/libOpenEXRUtil-3_1.so.30
/usr/lib64/libOpenEXRUtil-3_1.so.30.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openexr/8bdba5713cb211c07a30241ee1d0a9c668f071cd
/usr/share/package-licenses/openexr/abe6364c70643c16b35007073306461670b47181
