%define Name	WordNet

%define major		%{version}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		wordnet
Version:	3.0
Release:	%mkrel 13
Summary:	A lexical database for the English language
Group:		Sciences/Other
License:	MIT
URL:		http://wordnet.princeton.edu
Source0:	http://wordnet.princeton.edu/%{version}/%{Name}-%{version}.tar.bz2
Patch0:		%{name}-2.1.libtool.patch
Patch1:		%{name}-3.0.fhs.patch
Patch2:		%{name}-CVE-2008-2149_3908.patch
# Kludge (not a fix) for Tcl 8.6 (TIP #330, interp->result) - AdamW
# 2008/12
Patch3:		wordnet-3.0-tcl86.patch
Patch4:		wordnet_autoconf.patch
Patch5:		wordnet_wformat.patch
Requires:       %{libname} = %{version}
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
WordNet® is an online lexical reference system whose design is inspired by
current psycholinguistic theories of human lexical memory. English nouns,
verbs, adjectives and adverbs are organized into synonym sets, each
representing one underlying lexical concept. Different relations link the
synonym sets.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{develname}
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname wordnet 3.0 -d}

%description -n %{develname}
Libraries, include files and other resources you can use to develop.

%prep
%setup -q -n %{Name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .tcl86
%patch4 -p1
%patch5 -p1
autoreconf -fi

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall
chmod 644 %{buildroot}%{_libdir}/libWN.la

mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-wordnet.desktop << EOF
[Desktop Entry]
Type=Application
Name=WordNet
Comment=Graphical Interface for WordNet
Icon=accessories-dictionary
Exec=wnb
Categories=Office;X-MandrivaLinux-Office-Accessories;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README doc/{html,ps,pdf}
%{_bindir}/*
%{_datadir}/applications/mandriva-wordnet.desktop
%{_datadir}/%{Name}
%{_mandir}/*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libWN-%{version}.so

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libWN.so
%{_libdir}/libWN.a
%{_libdir}/libWN.la
%{_includedir}/*
