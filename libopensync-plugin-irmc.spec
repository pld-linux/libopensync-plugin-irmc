Summary:	OpenSync IRMC plugin
Summary(pl.UTF-8):	Wtyczka IRMC do OpenSync
Name:		libopensync-plugin-irmc
Version:	0.22
Release:	6
License:	GPL v2
Group:		Libraries
# Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	ecec872b2bccd824b1c5cbb2ec1d5399
URL:		http://www.opensync.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync02-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	openobex-devel >= 1.0.0
BuildRequires:	pkgconfig
Obsoletes:	multisync-irmc
Obsoletes:	multisync-irmc-bluetooth
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/irmc_sync.so
%{_datadir}/opensync/defaults/irmc-sync

# devel
#%{_includedir}/opensync-1.0/opensync/irmc_sync.h
