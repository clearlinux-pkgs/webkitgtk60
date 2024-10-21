#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x6C1009B693975393 (cgarcia@igalia.com)
#
Name     : webkitgtk60
Version  : 2.46.2
Release  : 130
URL      : https://webkitgtk.org/releases/webkitgtk-2.46.2.tar.xz
Source0  : https://webkitgtk.org/releases/webkitgtk-2.46.2.tar.xz
Source1  : https://webkitgtk.org/releases/webkitgtk-2.46.2.tar.xz.asc
Source2  : 6C1009B693975393.pkey
Summary  : GTK+ version of the JavaScriptCore engine
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-2-Clause-Patent BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT NCSA OFL-1.1
Requires: webkitgtk60-bin = %{version}-%{release}
Requires: webkitgtk60-data = %{version}-%{release}
Requires: webkitgtk60-lib = %{version}-%{release}
Requires: webkitgtk60-libexec = %{version}-%{release}
Requires: webkitgtk60-license = %{version}-%{release}
Requires: webkitgtk60-locales = %{version}-%{release}
Requires: bubblewrap
Requires: xdg-dbus-proxy
BuildRequires : WPEBackend-fdo-dev
BuildRequires : bison
BuildRequires : bubblewrap
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : compat-libsoup-soname-24-dev
BuildRequires : expat-dev
BuildRequires : extra-cmake-modules gperf
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : flex
BuildRequires : fontconfig-dev
BuildRequires : freetype-dev
BuildRequires : gjs-dev
BuildRequires : glibc-dev
BuildRequires : gnupg
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk4-dev
BuildRequires : harfbuzz-dev
BuildRequires : icu4c-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libXcomposite-dev
BuildRequires : libc-bin
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libnotify-dev
BuildRequires : libpng-dev
BuildRequires : libsoup-dev
BuildRequires : libwebp-dev
BuildRequires : libwpe-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : mesa-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(atk-bridge-2.0)
BuildRequires : pkgconfig(atspi-2)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gpg-error)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(harfbuzz-icu)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libavif)
BuildRequires : pkgconfig(libbrotlicommon)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpsl)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtasn1)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwoff2common)
BuildRequires : pkgconfig(libwoff2dec)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(sysprof-capture-4)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xt)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : unifdef
BuildRequires : xdg-dbus-proxy
BuildRequires : zlib-dev

%description
The headers in this directory are for compiling on macOS 12.5 (Monterey) and newer.
macOS releases include the ICU binary, but not ICU headers.

%package bin
Summary: bin components for the webkitgtk60 package.
Group: Binaries
Requires: webkitgtk60-data = %{version}-%{release}
Requires: webkitgtk60-libexec = %{version}-%{release}
Requires: webkitgtk60-license = %{version}-%{release}

%description bin
bin components for the webkitgtk60 package.


%package data
Summary: data components for the webkitgtk60 package.
Group: Data

%description data
data components for the webkitgtk60 package.


%package dev
Summary: dev components for the webkitgtk60 package.
Group: Development
Requires: webkitgtk60-lib = %{version}-%{release}
Requires: webkitgtk60-bin = %{version}-%{release}
Requires: webkitgtk60-data = %{version}-%{release}
Provides: webkitgtk60-devel = %{version}-%{release}
Requires: webkitgtk60 = %{version}-%{release}

%description dev
dev components for the webkitgtk60 package.


%package lib
Summary: lib components for the webkitgtk60 package.
Group: Libraries
Requires: webkitgtk60-data = %{version}-%{release}
Requires: webkitgtk60-libexec = %{version}-%{release}
Requires: webkitgtk60-license = %{version}-%{release}

%description lib
lib components for the webkitgtk60 package.


%package libexec
Summary: libexec components for the webkitgtk60 package.
Group: Default
Requires: webkitgtk60-license = %{version}-%{release}

%description libexec
libexec components for the webkitgtk60 package.


%package license
Summary: license components for the webkitgtk60 package.
Group: Default

%description license
license components for the webkitgtk60 package.


%package locales
Summary: locales components for the webkitgtk60 package.
Group: Default

%description locales
locales components for the webkitgtk60 package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 6C1009B693975393' gpg.status
%setup -q -n webkitgtk-2.46.2
cd %{_builddir}/webkitgtk-2.46.2
pushd ..
cp -a webkitgtk-2.46.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729528221
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DPORT=GTK \
-DENABLE_GEOLOCATION=off \
-DENABLE_SPELLCHECK=off \
-DUSE_LIBHYPHEN=off \
-DUSE_LD_GOLD=off \
-DUSE_SYSTEM_MALLOC=on \
-DENABLE_MINIBROWSER=ON \
-DCMAKE_BUILD_TYPE=Release \
-DUSE_GSTREAMER_GL=OFF \
-DUSE_OPENJPEG=off \
-DUSE_WPE_RENDERER=off \
-DENABLE_GAMEPAD=off \
-DENABLE_BUBBLEWRAP_SANDBOX=off \
-DUSE_GTK4=ON \
-DUSE_GSTREAMER_TRANSCODER=OFF \
-DUSE_JPEGXL=OFF \
-DUSE_LIBBACKTRACE=OFF \
-DUSE_SYSPROF_CAPTURE=OFF \
-DENABLE_DOCUMENTATION=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DPORT=GTK \
-DENABLE_GEOLOCATION=off \
-DENABLE_SPELLCHECK=off \
-DUSE_LIBHYPHEN=off \
-DUSE_LD_GOLD=off \
-DUSE_SYSTEM_MALLOC=on \
-DENABLE_MINIBROWSER=ON \
-DCMAKE_BUILD_TYPE=Release \
-DUSE_GSTREAMER_GL=OFF \
-DUSE_OPENJPEG=off \
-DUSE_WPE_RENDERER=off \
-DENABLE_GAMEPAD=off \
-DENABLE_BUBBLEWRAP_SANDBOX=off \
-DUSE_GTK4=ON \
-DUSE_GSTREAMER_TRANSCODER=OFF \
-DUSE_JPEGXL=OFF \
-DUSE_LIBBACKTRACE=OFF \
-DUSE_SYSPROF_CAPTURE=OFF \
-DENABLE_DOCUMENTATION=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1729528221
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/webkitgtk60
cp %{_builddir}/webkitgtk-%{version}/Source/JavaScriptCore/COPYING.LIB %{buildroot}/usr/share/package-licenses/webkitgtk60/130f5281a2ef2a49822787e013323bde2ff119dd || :
cp %{_builddir}/webkitgtk-%{version}/Source/JavaScriptCore/disassembler/zydis/LICENSE-zycore.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/8f9353c9865daac85a9586cfa0ae144d5adda700 || :
cp %{_builddir}/webkitgtk-%{version}/Source/JavaScriptCore/disassembler/zydis/LICENSE-zydis.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/7c317af0eb0da75f9f9b8fb8cb4b575a9f90bada || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/37126a0eda0b30f44070f59e6833187e99a7eb83 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/common/third_party/xxhash/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/390f8904578d05817ab7cafe1f470cd283bcfe93 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/libANGLE/overlay/LICENSE.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/libANGLE/renderer/vulkan/shaders/src/third_party/etc_decoder/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/7cbf6ce25dc89292771052f36ace84542d57a71a || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/libANGLE/renderer/vulkan/shaders/src/third_party/ffx_spd/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/18f2c8a1b68673441f7ae71085ce98b7cad01734 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/tests/test_utils/third_party/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/5ebf8574fea54a1c549c090652f327376b1376aa || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/third_party/ceval/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/5e1c32bca955c2f9b85e883fb084d8b06944133e || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/665f7371da2b70dc3908c7c1e8b43bbbada8e4c3 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/src/third_party/volk/LICENSE.md %{buildroot}/usr/share/package-licenses/webkitgtk60/f12c9d338be92bacfa1e21c513e3517ad3190931 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/android_system_sdk/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/01e162357df5b2522a974605b3467d7da33c31ca || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/bazel/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/colorama/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/1c1163ff2c64a68a4665bdfc69c26cf046a51768 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/flatbuffers/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/89e4939e88f1e7ff29e52604a9d65a762c062d1d || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/glslang/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/e9f8452ddfdc10be2669932ce3e0fe4d70794099 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/proguard/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/1cc0d86d7201f06df64d3c332bc031e0a6560ef7 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/r8/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/a42298d6678062ac6399611c2d5d2edde767cb47 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/spirv-headers/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/spirv-tools/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/turbine/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/third_party/vulkan-headers/LICENSE.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/tools/flex-bison/third_party/m4sugar/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/tools/flex-bison/third_party/skeletons/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/ANGLE/util/windows/third_party/StackWalker/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/33fe6f9feb6fc711ff8b5dc59283453f84fcbfe3 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/gtest/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/5a2314153eadadc69258a9429104cd11804ea304 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/libsysprof-capture/COPYING %{buildroot}/usr/share/package-licenses/webkitgtk60/f0464855038f72585350235098599184ac3b3810 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/pdfjs/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/pdfjs/web/cmaps/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/1afb5991fce0d60110b5092b68bf9ff76b0c73f6 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/pdfjs/web/standard_fonts/LICENSE_FOXIT %{buildroot}/usr/share/package-licenses/webkitgtk60/689c532308da601d10beba61b6672b0c16dc3b48 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/pdfjs/web/standard_fonts/LICENSE_LIBERATION %{buildroot}/usr/share/package-licenses/webkitgtk60/0898cb73de9283d38e6f4cef45ce79efbfafb0b2 || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/skia/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/7baa2025015038e928121c9a2813b7ff20e8577b || :
cp %{_builddir}/webkitgtk-%{version}/Source/ThirdParty/skia/include/third_party/vulkan/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/b483568509cf6b97a697ccefcd5d9df29cdf4f1f || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/LICENSE-LLVM.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/483d1c97dc79ef8741eae507897ca39cfe19da36 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/LICENSE-dragonbox.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/90cf69a91a795547d5ce551111634305d2752710 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/LICENSE-libc++.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/5aca84acb14d922c44453c8e781f98fcb1c6f58d || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/LICENSE-simde.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/cad3503af1964a216bc15457310afab46373715f || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/icu/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/dbcb5c4a57f45a48c971c06928a7c99fb5656f06 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/wtf/dtoa/COPYING %{buildroot}/usr/share/package-licenses/webkitgtk60/8d434c9c1704b544a8b0652efbc323380b67f9bc || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/wtf/dtoa/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/8d434c9c1704b544a8b0652efbc323380b67f9bc || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/wtf/fast_float/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/17d9f7912c62b7feadce3c1054e64ab70ade5111 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WTF/wtf/simdutf/LICENSE-simdutf.txt %{buildroot}/usr/share/package-licenses/webkitgtk60/2e183a18db08cb0c43db26dc1478e36a6ff97587 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebCore/LICENSE-APPLE %{buildroot}/usr/share/package-licenses/webkitgtk60/7ea0ac726dfef36527dfe261d1f2ae28c8f96d4d || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebCore/LICENSE-LGPL-2 %{buildroot}/usr/share/package-licenses/webkitgtk60/31c49697af1092e3e9e230f93c0e0f7dd9694abb || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebCore/LICENSE-LGPL-2.1 %{buildroot}/usr/share/package-licenses/webkitgtk60/1a180647a31404e0cf993fa333cdb7f7e75eaba5 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebInspectorUI/UserInterface/External/CSSDocumentation/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/feba7df50f49bf05a47cbf1875f259b1b8a3b484 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/e7ada8ae78ebdb41cc7c8e9dbad43c5870412bd7 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/26dd70b52c7c7111ca8913fc0bc240dc28ca15c0 || :
cp %{_builddir}/webkitgtk-%{version}/Source/WebInspectorUI/UserInterface/External/three.js/LICENSE %{buildroot}/usr/share/package-licenses/webkitgtk60/eb5e50200f181f35271557d301ffd7784df64f79 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang WebKitGTK-6.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/WebKitWebDriver
/usr/bin/WebKitWebDriver

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/JavaScriptCore-6.0.typelib
/usr/lib64/girepository-1.0/WebKit-6.0.typelib
/usr/lib64/girepository-1.0/WebKitWebProcessExtension-6.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/webkitgtk-6.0/jsc/JSCClass.h
/usr/include/webkitgtk-6.0/jsc/JSCContext.h
/usr/include/webkitgtk-6.0/jsc/JSCDefines.h
/usr/include/webkitgtk-6.0/jsc/JSCException.h
/usr/include/webkitgtk-6.0/jsc/JSCOptions.h
/usr/include/webkitgtk-6.0/jsc/JSCValue.h
/usr/include/webkitgtk-6.0/jsc/JSCVersion.h
/usr/include/webkitgtk-6.0/jsc/JSCVirtualMachine.h
/usr/include/webkitgtk-6.0/jsc/JSCWeakValue.h
/usr/include/webkitgtk-6.0/jsc/jsc.h
/usr/include/webkitgtk-6.0/webkit/WebKitApplicationInfo.h
/usr/include/webkitgtk-6.0/webkit/WebKitAuthenticationRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitAutocleanups.h
/usr/include/webkitgtk-6.0/webkit/WebKitAutomationSession.h
/usr/include/webkitgtk-6.0/webkit/WebKitBackForwardList.h
/usr/include/webkitgtk-6.0/webkit/WebKitBackForwardListItem.h
/usr/include/webkitgtk-6.0/webkit/WebKitClipboardPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitColorChooserRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitConsoleMessage.h
/usr/include/webkitgtk-6.0/webkit/WebKitContextMenu.h
/usr/include/webkitgtk-6.0/webkit/WebKitContextMenuActions.h
/usr/include/webkitgtk-6.0/webkit/WebKitContextMenuItem.h
/usr/include/webkitgtk-6.0/webkit/WebKitCookieManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitCredential.h
/usr/include/webkitgtk-6.0/webkit/WebKitDefines.h
/usr/include/webkitgtk-6.0/webkit/WebKitDeviceInfoPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitDownload.h
/usr/include/webkitgtk-6.0/webkit/WebKitEditingCommands.h
/usr/include/webkitgtk-6.0/webkit/WebKitEditorState.h
/usr/include/webkitgtk-6.0/webkit/WebKitEnumTypes.h
/usr/include/webkitgtk-6.0/webkit/WebKitError.h
/usr/include/webkitgtk-6.0/webkit/WebKitFaviconDatabase.h
/usr/include/webkitgtk-6.0/webkit/WebKitFeature.h
/usr/include/webkitgtk-6.0/webkit/WebKitFileChooserRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitFindController.h
/usr/include/webkitgtk-6.0/webkit/WebKitFormSubmissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitFrame.h
/usr/include/webkitgtk-6.0/webkit/WebKitGeolocationManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitGeolocationPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitHitTestResult.h
/usr/include/webkitgtk-6.0/webkit/WebKitInputMethodContext.h
/usr/include/webkitgtk-6.0/webkit/WebKitInstallMissingMediaPluginsPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitMediaKeySystemPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitMemoryPressureSettings.h
/usr/include/webkitgtk-6.0/webkit/WebKitNavigationAction.h
/usr/include/webkitgtk-6.0/webkit/WebKitNavigationPolicyDecision.h
/usr/include/webkitgtk-6.0/webkit/WebKitNetworkProxySettings.h
/usr/include/webkitgtk-6.0/webkit/WebKitNetworkSession.h
/usr/include/webkitgtk-6.0/webkit/WebKitNotification.h
/usr/include/webkitgtk-6.0/webkit/WebKitNotificationPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitOptionMenu.h
/usr/include/webkitgtk-6.0/webkit/WebKitOptionMenuItem.h
/usr/include/webkitgtk-6.0/webkit/WebKitPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitPermissionStateQuery.h
/usr/include/webkitgtk-6.0/webkit/WebKitPointerLockPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitPolicyDecision.h
/usr/include/webkitgtk-6.0/webkit/WebKitPrintOperation.h
/usr/include/webkitgtk-6.0/webkit/WebKitResponsePolicyDecision.h
/usr/include/webkitgtk-6.0/webkit/WebKitScriptDialog.h
/usr/include/webkitgtk-6.0/webkit/WebKitScriptWorld.h
/usr/include/webkitgtk-6.0/webkit/WebKitSecurityManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitSecurityOrigin.h
/usr/include/webkitgtk-6.0/webkit/WebKitSettings.h
/usr/include/webkitgtk-6.0/webkit/WebKitURIRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitURIResponse.h
/usr/include/webkitgtk-6.0/webkit/WebKitURISchemeRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitURISchemeResponse.h
/usr/include/webkitgtk-6.0/webkit/WebKitURIUtilities.h
/usr/include/webkitgtk-6.0/webkit/WebKitUserContent.h
/usr/include/webkitgtk-6.0/webkit/WebKitUserContentFilterStore.h
/usr/include/webkitgtk-6.0/webkit/WebKitUserContentManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitUserMediaPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitUserMessage.h
/usr/include/webkitgtk-6.0/webkit/WebKitVersion.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebContext.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebEditor.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebFormManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebHitTestResult.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebInspector.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebPage.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebProcessEnumTypes.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebProcessExtension.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebResource.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebView.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebViewBase.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebViewSessionState.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebsiteData.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebsiteDataAccessPermissionRequest.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebsiteDataManager.h
/usr/include/webkitgtk-6.0/webkit/WebKitWebsitePolicies.h
/usr/include/webkitgtk-6.0/webkit/WebKitWindowProperties.h
/usr/include/webkitgtk-6.0/webkit/webkit-web-process-extension.h
/usr/include/webkitgtk-6.0/webkit/webkit.h
/usr/lib64/libjavascriptcoregtk-6.0.so
/usr/lib64/libwebkitgtk-6.0.so
/usr/lib64/pkgconfig/javascriptcoregtk-6.0.pc
/usr/lib64/pkgconfig/webkitgtk-6.0.pc
/usr/lib64/pkgconfig/webkitgtk-web-process-extension-6.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libjavascriptcoregtk-6.0.so.1.3.11
/V3/usr/lib64/libwebkitgtk-6.0.so.4.10.4
/V3/usr/lib64/webkitgtk-6.0/injected-bundle/libwebkitgtkinjectedbundle.so
/usr/lib64/libjavascriptcoregtk-6.0.so.1
/usr/lib64/libjavascriptcoregtk-6.0.so.1.3.11
/usr/lib64/libwebkitgtk-6.0.so.4
/usr/lib64/libwebkitgtk-6.0.so.4.10.4
/usr/lib64/webkitgtk-6.0/injected-bundle/libwebkitgtkinjectedbundle.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/webkitgtk-6.0/MiniBrowser
/V3/usr/libexec/webkitgtk-6.0/WebKitNetworkProcess
/V3/usr/libexec/webkitgtk-6.0/WebKitWebProcess
/V3/usr/libexec/webkitgtk-6.0/jsc
/usr/libexec/webkitgtk-6.0/MiniBrowser
/usr/libexec/webkitgtk-6.0/WebKitNetworkProcess
/usr/libexec/webkitgtk-6.0/WebKitWebProcess
/usr/libexec/webkitgtk-6.0/jsc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/webkitgtk60/01e162357df5b2522a974605b3467d7da33c31ca
/usr/share/package-licenses/webkitgtk60/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/webkitgtk60/0898cb73de9283d38e6f4cef45ce79efbfafb0b2
/usr/share/package-licenses/webkitgtk60/130f5281a2ef2a49822787e013323bde2ff119dd
/usr/share/package-licenses/webkitgtk60/17d9f7912c62b7feadce3c1054e64ab70ade5111
/usr/share/package-licenses/webkitgtk60/18f2c8a1b68673441f7ae71085ce98b7cad01734
/usr/share/package-licenses/webkitgtk60/1a180647a31404e0cf993fa333cdb7f7e75eaba5
/usr/share/package-licenses/webkitgtk60/1afb5991fce0d60110b5092b68bf9ff76b0c73f6
/usr/share/package-licenses/webkitgtk60/1c1163ff2c64a68a4665bdfc69c26cf046a51768
/usr/share/package-licenses/webkitgtk60/1cc0d86d7201f06df64d3c332bc031e0a6560ef7
/usr/share/package-licenses/webkitgtk60/26dd70b52c7c7111ca8913fc0bc240dc28ca15c0
/usr/share/package-licenses/webkitgtk60/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/webkitgtk60/2e183a18db08cb0c43db26dc1478e36a6ff97587
/usr/share/package-licenses/webkitgtk60/31c49697af1092e3e9e230f93c0e0f7dd9694abb
/usr/share/package-licenses/webkitgtk60/33fe6f9feb6fc711ff8b5dc59283453f84fcbfe3
/usr/share/package-licenses/webkitgtk60/37126a0eda0b30f44070f59e6833187e99a7eb83
/usr/share/package-licenses/webkitgtk60/390f8904578d05817ab7cafe1f470cd283bcfe93
/usr/share/package-licenses/webkitgtk60/483d1c97dc79ef8741eae507897ca39cfe19da36
/usr/share/package-licenses/webkitgtk60/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/webkitgtk60/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/webkitgtk60/5aca84acb14d922c44453c8e781f98fcb1c6f58d
/usr/share/package-licenses/webkitgtk60/5e1c32bca955c2f9b85e883fb084d8b06944133e
/usr/share/package-licenses/webkitgtk60/5ebf8574fea54a1c549c090652f327376b1376aa
/usr/share/package-licenses/webkitgtk60/665f7371da2b70dc3908c7c1e8b43bbbada8e4c3
/usr/share/package-licenses/webkitgtk60/689c532308da601d10beba61b6672b0c16dc3b48
/usr/share/package-licenses/webkitgtk60/7baa2025015038e928121c9a2813b7ff20e8577b
/usr/share/package-licenses/webkitgtk60/7c317af0eb0da75f9f9b8fb8cb4b575a9f90bada
/usr/share/package-licenses/webkitgtk60/7cbf6ce25dc89292771052f36ace84542d57a71a
/usr/share/package-licenses/webkitgtk60/7ea0ac726dfef36527dfe261d1f2ae28c8f96d4d
/usr/share/package-licenses/webkitgtk60/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/webkitgtk60/89e4939e88f1e7ff29e52604a9d65a762c062d1d
/usr/share/package-licenses/webkitgtk60/8d434c9c1704b544a8b0652efbc323380b67f9bc
/usr/share/package-licenses/webkitgtk60/8f9353c9865daac85a9586cfa0ae144d5adda700
/usr/share/package-licenses/webkitgtk60/90cf69a91a795547d5ce551111634305d2752710
/usr/share/package-licenses/webkitgtk60/a42298d6678062ac6399611c2d5d2edde767cb47
/usr/share/package-licenses/webkitgtk60/b483568509cf6b97a697ccefcd5d9df29cdf4f1f
/usr/share/package-licenses/webkitgtk60/cad3503af1964a216bc15457310afab46373715f
/usr/share/package-licenses/webkitgtk60/dbcb5c4a57f45a48c971c06928a7c99fb5656f06
/usr/share/package-licenses/webkitgtk60/e7ada8ae78ebdb41cc7c8e9dbad43c5870412bd7
/usr/share/package-licenses/webkitgtk60/e9f8452ddfdc10be2669932ce3e0fe4d70794099
/usr/share/package-licenses/webkitgtk60/eb5e50200f181f35271557d301ffd7784df64f79
/usr/share/package-licenses/webkitgtk60/f0464855038f72585350235098599184ac3b3810
/usr/share/package-licenses/webkitgtk60/f12c9d338be92bacfa1e21c513e3517ad3190931
/usr/share/package-licenses/webkitgtk60/feba7df50f49bf05a47cbf1875f259b1b8a3b484

%files locales -f WebKitGTK-6.0.lang
%defattr(-,root,root,-)

