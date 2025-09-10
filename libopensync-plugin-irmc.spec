Summary:	OpenSync IRMC plugin
Summary(pl.UTF-8):	Wtyczka IRMC do OpenSync
Name:		libopensync-plugin-irmc
Version:	0.36
Release:	1
License:	GPL v2
Group:		Libraries
# originally http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2
# restored from http://ftp.iij.ad.jp/pub/linux/momonga/5/Everything/SOURCES/libopensync-plugin-irmc-0.36.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	21f9789fa41c2f06c547a17bc13c6081
Patch0:		%{name}-libopensync0.39.patch
Patch1:		%{name}-openobex.patch
# dead domain
#URL:		http://www.opensync.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= 1:0.39
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	linux-irda-devel
BuildRequires:	openobex-devel >= 1.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libopensync >= 1:0.39
Obsoletes:	multisync-irmc < 0.90
Obsoletes:	multisync-irmc-bluetooth < 0.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains IRMC plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę IRMC dla szkieletu OpenSync.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libopensync1/plugins/irmc-sync.so
%{_datadir}/libopensync1/defaults/irmc-sync
