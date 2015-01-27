Name:       agl-plugins
Summary:    A collection of IVI software
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    ASL 2.0
URL:        http://www.tizen.org2
Source0:    %{name}-%{version}.tar.bz2

# External deps requirements
BuildRequires:  python
BuildRequires:  desktop-file-utils
BuildRequires:  rpmbuild
BuildRequires:  cmake
BuildRequires:  pkgconfig(libusb)
BuildRequires:  libusb-devel

# Actual app/service requirements
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(eet)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eldbus)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)

Requires:       ibus
Requires:       ibus-hangul
Requires:       ibus-libpinyin
Requires:       systemd
Requires:       gstreamer-1.0
Requires:       gstreamer-base-1.0
Requires:       gstreamer-audio-1.0
Requires:       dbus-glib-1
Requires:       dbus-1
Requires:       glib-2.0
Requires:       libusb

%global folder_list extension_common BoilerPlateExtension wkb_client_ext FMRadioExtension FMRadioService

%description
A collection of IVI software

%package service
Summary: FMRadioService dbus service
Group: Applications/System
%description service
FMRadioService dbus-daemon

%prep
%setup -q -n %{name}-%{version}
cd FMRadioService/deps/rtl-sdr
mkdir build && cd  build
cmake ..
make install
#rpmbuild --rebuild FMRadioService/deps/shadow-utils-4.1.5.1-17.fc21.src.rpm
#rpmbuild --rebuild FMRadioService/deps/rtl-sdr-0.5.3-3.src.rpm
#rpm -ivh ${HOME}/rpmbuild/RPMS/i586/rtl-sdr-0.5.3-3.*.rpm

# Support for GNU autotools-style build systems
for folder in %{folder_list}; do
	cd ${folder}
	if [ -f autogen.sh ]; then
		./autogen.sh
	fi
	cd ..
done

%build
# Support for GNU autotools-style build systems
for folder in %{folder_list}; do
	cd ${folder}
	if [ -f configure ]; then
	 # We have to install inside gbs buildroot jail! 
	 ./configure --prefix=%{_prefix}
	fi
	cd ..
make -C ${folder}
done

%install
# manually add those paths that we are going to install
mkdir -p %{buildroot}/usr/lib/systemd/user
mkdir -p %{buildroot}/usr/share/dbus-1/services
for folder in %{folder_list}; do
    make -C ${folder} install DESTDIR=%{buildroot} PREFIX=%{_prefix}
done

%files
%{_prefix}/lib/tizen-extensions-crosswalk/libbp.so
%{_prefix}/lib/tizen-extensions-crosswalk/libwkb_client.so
%{_prefix}/lib/tizen-extensions-crosswalk/lib_fmradio.so
%{_prefix}/share/X11/xkb/symbols/wkb
%{_prefix}/local/sbin/kb_inst
%{_prefix}/share/weekeyboard/blue_1080.edj
%{_prefix}/share/weekeyboard/blue_720.edj
%{_prefix}/share/weekeyboard/blue_600.edj
%{_prefix}/share/weekeyboard/green_1080.edj
%{_prefix}/share/weekeyboard/green_720.edj
%{_prefix}/share/weekeyboard/green_600.edj
%{_prefix}/share/weekeyboard/amber_1080.edj
%{_prefix}/share/weekeyboard/amber_720.edj
%{_prefix}/share/weekeyboard/amber_600.edj

%files service
%{_prefix}/lib/systemd/user/fmradioservice.service
%{_prefix}/share/dbus-1/services/com.jlr.fmradioservice.service
%{_prefix}/bin/fmradioservice

