%define major	0
%define package_name gtkhtml
%define api_version 4.0
%define libname %mklibname %{package_name} %{api_version} %{major}
%define libnamedev %mklibname -d %{package_name} %{api_version}

Summary: HTML rendering/editing library
Name: gtkhtml4
Version: 4.0.2
Release: %mkrel 1
License: LGPLv2+
Group: Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{package_name}-%{version}.tar.xz
URL:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libgail-3.0-devel >= 3.0.2
BuildRequires:	gtk+3-devel >= 3.0.2
BuildRequires:	iso-codes
BuildRequires:	enchant-devel >= 1.1.7
BuildRequires:	libGConf2-devel
BuildRequires:	gnome-icon-theme >= 2.22.0
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	glade3-devel
BuildRequires:	intltool
Requires:	%{libname} >= %{version}

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
Summary:        Libraries for GtkHTML
Group:          System/Libraries

%description -n %{libname}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains libraries used by GtkHTML.

%package -n %{libnamedev}
Summary:        Development libraries, header files and utilities for GtkHTML
Group:          Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires:       %{libname} = %{version}
Provides:	%{package_name}-%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -qn %{package_name}-%{version}

%build
%configure2_5x --disable-static --program-suffix=4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{package_name}-%{api_version}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{package_name}-%{api_version}.lang
%defattr(-, root, root)
%doc AUTHORS NEWS README TODO
%{_datadir}/gtkhtml-%{api_version}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING 
%{_libdir}/libgtkhtml-%{api_version}.so.%{major}*
%{_libdir}/libgtkhtml-editor-%{api_version}.so.%{major}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc ChangeLog 
%{_bindir}/gtkhtml-editor-test4
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
