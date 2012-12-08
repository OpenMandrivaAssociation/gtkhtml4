%define major	0
%define oname gtkhtml
%define api_version 4.0
%define libname %mklibname %{oname} %{api_version} %{major}
%define develname %mklibname -d %{oname} %{api_version}

Summary: HTML rendering/editing library
Name: gtkhtml4
Version: 4.6.1
Release: 1
License: LGPLv2+
Group: Graphical desktop/GNOME
URL: http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
Source0: http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/4.6/%{oname}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(enchant) >= 1.1.7
BuildRequires:	pkgconfig(gail-3.0) >= 3.0.2
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.2
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(cairo) >= 1.10.0
BuildRequires:	pkgconfig(ORBit-2.0)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.22.0

Requires:	%{libname} >= %{version}-%{release}

%description 
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

GtkHTML was originally based on KDE's KHTMLW widget, but is now
developed independently of it.  The most important difference between
KHTMLW and GtkHTML, besides being GTK-based, is that GtkHTML is also
an editor.  Thanks to the Bonobo editor component that comes with the
library, it's extremely simple to add HTML editing to an existing
application.

%package -n %{libname}
Summary:	Libraries for GtkHTML
Group:		System/Libraries

%description -n %{libname}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains libraries used by GtkHTML.

%package -n %{develname}
Summary:	Development libraries, header files and utilities for GtkHTML
Group:		Development/GNOME and GTK+
#Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Provides:	%{oname}-%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static \
	--program-suffix=4

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -delete
%{find_lang} %{oname}-%{api_version}

%files -f %{oname}-%{api_version}.lang
%doc AUTHORS NEWS README TODO COPYING
%{_datadir}/gtkhtml-%{api_version}

%files -n %{libname}
%{_libdir}/libgtkhtml-%{api_version}.so.%{major}*
%{_libdir}/libgtkhtml-editor-%{api_version}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_bindir}/gtkhtml-editor-test4
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*



%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 4.6.1-1
- update to 4.6.1

* Mon Oct  1 2012 Arkady L. Shane <ashejn@rosalab.ru> 4.6.0-1
- update to 4.6.0

* Mon Aug 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 4.4.4-1
+ Revision: 814437
- update to new version 4.4.4

* Tue Jun 19 2012 Matthew Dawkins <mattydaw@mandriva.org> 4.4.3-1
+ Revision: 806164
- update to new version 4.4.3

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 4.4.2-1
+ Revision: 799173
- update to new version 4.4.2

* Mon Apr 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.4.1-1
+ Revision: 792841
- version update 4.4.1

* Mon Jan 09 2012 Götz Waschk <waschk@mandriva.org> 4.2.3-1
+ Revision: 758811
- new version

* Thu Dec 08 2011 Matthew Dawkins <mattydaw@mandriva.org> 4.2.2-1
+ Revision: 739035
- added patch0
- fixed configure
- added p0 for g_thread_init deprecation
- new version 4.2.2
- cleaned up spec
- removed .la files
- removed defattr, clean section, BuildRoot, mkrel
- converted BRs to pkgconfig

* Wed Aug 31 2011 Götz Waschk <waschk@mandriva.org> 4.0.2-1
+ Revision: 697582
- new version
- xz tarball

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 4.0.1-1
+ Revision: 659110
- update to new version 4.0.1

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 4.0.0-1
+ Revision: 650155
- import gtkhtml4

