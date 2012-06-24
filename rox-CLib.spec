%define _appsdir /usr/X11R6/share/ROX-apps
%define _name ROX-CLib
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	A library for ROX applications
Summary(pl.UTF-8):   Biblioteka dla aplikacji ROXa
Name:		rox-CLib
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-allow-configure-options.patch
Patch2:		%{name}-libxml-includes.patch
URL:		http://www.kerofin.demon.co.uk/rox/libs.html
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	libxml2-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A library for ROX applications.

%description -l pl.UTF-8
Biblioteka dla aplikacji ROXa.

%package devel
Summary:	ROX-CLib header files
Summary(pl.UTF-8):   Pliki nagłówkowe do ROX-CLib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.2.8

%description devel
Header files for the ROX-CLib libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe do bibliotek ROX-CLib.

%package static
Summary:	ROX-CLib static libraries
Summary(pl.UTF-8):   Biblioteki statyczne ROX-CLib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	gtk+-devel >= 1.2.8

%description static
Static libraries for the ROX-CLib libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla ROX-CLib.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{%{_platform}/bin,Help}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{_name},%{_libdir}}

rm -f ../install
install App* $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
cd %{_platform}
install bin/rox_run $RPM_BUILD_ROOT%{_bindir}
rm -f bin/{rox_run,test}
install bin/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}/bin
cp -d lib/* $RPM_BUILD_ROOT%{_libdir}
install include/* $RPM_BUILD_ROOT%{_includedir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Help/{Authors,Versions}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}/bin
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
%dir %{_appsdir}/%{_name}/%{_platform}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/%{_name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
