%define Name WordNet

%define major 3.0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		wordnet
Version:	3.1
Release:	2
Summary:	A lexical database for the English language
Group:		Sciences/Other
License:	MIT
URL:		http://wordnet.princeton.edu
Source0:	http://wordnet.princeton.edu/3.0/%{Name}-3.0.tar.bz2
Source1:	http://wordnetcode.princeton.edu/wn%{version}.dict.tar.gz
Patch0:		%{name}-2.1.libtool.patch
Patch1:		%{name}-3.0.fhs.patch
Patch2:		%{name}-CVE-2008-2149_3908.patch
# Kludge (not a fix) for Tcl 8.6 (TIP #330, interp->result) - AdamW
# 2008/12
Patch3:		wordnet-3.0-tcl86.patch
Patch4:		wordnet_autoconf.patch
Patch5:		wordnet_wformat.patch
Requires:	%{libname} = %{version}
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

%description
WordNet® is an online lexical reference system whose design is inspired by
current psycholinguistic theories of human lexical memory. English nouns,
verbs, adjectives and adverbs are organized into synonym sets, each
representing one underlying lexical concept. Different relations link the
synonym sets.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{EVRD}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{develname}
Summary:	Development header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname wordnet 3.0 -d}

%description -n %{develname}
Libraries, include files and other resources you can use to develop.

%prep
%autosetup -p1 -n %{Name}-3.0
autoreconf -fi
rm -f dict/*3.0*
sed -i -e 's,3\.0,3.1,g' dict/Makefile.am
tar xf %{S:1}

%build
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/wordnet.desktop << EOF
[Desktop Entry]
Type=Application
Name=WordNet
Comment=Graphical Interface for WordNet
Icon=accessories-dictionary
Exec=wnb
Categories=Office;X-MandrivaLinux-Office-Accessories;
EOF


%files
%doc AUTHORS COPYING INSTALL ChangeLog README doc/{html,ps,pdf}
%{_bindir}/*
%{_datadir}/applications/wordnet.desktop
%{_datadir}/%{Name}
%{_mandir}/*/*

%files -n %{libname}
%{_libdir}/libWN-3.0.so

%files -n %{develname}
%{_libdir}/libWN.so
%{_includedir}/*
