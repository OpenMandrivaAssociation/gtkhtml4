%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	gtkhtml
%define api	4.0
%define major	0
%define libname %mklibname %{oname} %{api} %{major}
%define libeditor %mklibname %{oname}-editor %{api} %{major}
%define devname %mklibname -d %{oname} %{api}

Summary:	HTML rendering/editing library
Name:		gtkhtml4
Version:	4.6.3
Release:	7
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(cairo) >= 1.10.0
BuildRequires:	pkgconfig(enchant) >= 1.1.7
BuildRequires:	pkgconfig(gail-3.0) >= 3.0.2
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.22.0
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.2
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:	pkgconfig(ORBit-2.0)

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
Suggests:	 %{name} = %{version}-%{release}

%description -n %{libname}
This package contains a shared library used by GtkHTML.

%package -n %{libeditor}
Summary:	Libraries for GtkHTML
Group:		System/Libraries
Suggests:	 %{name} = %{version}-%{release}
Conflicts:	%{_lib}gtkhtml4.0_0 < 4.6.3-2

%description -n %{libeditor}
This package contains a shared library used by GtkHTML.

%package -n %{devname}
Summary:	Development libraries, header files and utilities for GtkHTML
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Requires:	%{libeditor} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static \
	--program-suffix=4

%make

%install
%makeinstall_std
%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README TODO COPYING
%{_datadir}/gtkhtml-%{api}

%files -n %{libname}
%{_libdir}/libgtkhtml-%{api}.so.%{major}*

%files -n %{libeditor}
%{_libdir}/libgtkhtml-editor-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_bindir}/gtkhtml-editor-test4
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

