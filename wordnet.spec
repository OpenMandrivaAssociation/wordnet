%define name	wordnet
%define Name	WordNet
%define version	3.0
%define major	%{version}
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%mkrel 8
Summary:	A lexical database for the english language
Group:		Sciences/Other
License:	GPL
URL:		http://wordnet.princeton.edu
Source0:	http://wordnet.princeton.edu/%{version}/%{Name}-%{version}.tar.bz2
Patch0:		%{name}-2.1.libtool.patch
Patch1:		%{name}-3.0.fhs.patch
Patch2:		%{name}-CVE-2008-2149.patch
Requires:       %{libname} = %{version}
BuildRequires:	automake1.8
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	X11-devel
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

%package -n %{libname}-devel
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Libraries, include files and other resources you can use to develop.

%prep
%setup -q -n %{Name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize
autoreconf
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall
chmod 644 %{buildroot}%{_libdir}/libWN.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README doc/{html,ps,pdf}
%{_bindir}/*
%{_datadir}/%{Name}
%{_mandir}/*/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libWN-%{version}.so

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/libWN.so
%{_libdir}/libWN.a
%{_libdir}/libWN.la
%{_includedir}/*

