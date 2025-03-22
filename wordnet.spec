%define Name WordNet

%define major 3.0
%define oldlibname %mklibname %{name} 3.0
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

Name:		wordnet
Version:	3.1
Release:	5
Summary:	A lexical database for the English language
Group:		Sciences/Other
License:	MIT
URL:		https://wordnet.princeton.edu
Source0:	http://wordnet.princeton.edu/3.0/%{Name}-3.0.tar.bz2
Source1:	http://wordnetcode.princeton.edu/wn%{version}.dict.tar.gz
Requires:	%{libname} = %{version}
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

%patchlist
%{name}-3.0.fhs.patch
%{name}-CVE-2008-2149_3908.patch
# Kludge (not a fix) for Tcl 8.6 (TIP #330, interp->result) - AdamW
# 2008/12
wordnet-3.0-tcl86.patch
wordnet-3.0-tcl90.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-fix_man.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-wishwn_manpage.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-use_system_tk_headers.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-libtool.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-error_message.patch
https://src.fedoraproject.org/rpms/wordnet/raw/rawhide/f/wordnet-3.0-Pass-compilation-with-Werror-format-security.patch

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
%rename %{oldlibname}

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

%package gui
Summary:	Graphical UI for accessing WordNet
Group:		Sciences/Other
Requires:	%{libname} = %{EVRD}

%description gui
Graphical UI for accessing WordNet

%prep
%autosetup -p1 -n %{Name}-3.0
autoreconf -fi
rm -rf dict/*3.0* include/tk dict/dbfiles
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
%{_bindir}/wn
%{_datadir}/applications/wordnet.desktop
%{_datadir}/%{Name}
%{_mandir}/man1/grind.1*
%{_mandir}/man1/wn.1*
%{_mandir}/man1/wnintro.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*

%files gui
%{_bindir}/wishwn
%{_bindir}/wnb
%{_mandir}/man1/wnb.1*

%files -n %{libname}
%{_libdir}/libWN.so.*

%files -n %{develname}
%{_libdir}/libWN.so
%{_includedir}/*
%{_mandir}/man3/*.3*
