%define Name	WordNet

%define major		%{version}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		wordnet
Version:	3.0
Release:	22
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
%{_includedir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0-13mdv2011.0
+ Revision: 670813
- mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - tighten BR

* Thu Oct 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.0-12mdv2011.0
+ Revision: 589712
- provide a .desktop file for wnb to make show up in the menu
- remove rpm macros for releases older than 2009.0

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 3.0-11mdv2010.0
+ Revision: 450406
- fix format error (from Arnaud Patard)
- fix configure.ac (from Arnaud Patard)
- rediff libtool patch (from Arnaud Patard)

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 3.0-10mdv2009.1
+ Revision: 311068
- rebuild for new tcl
- kludge build for Tcl 8.6 (tcl86.patch)
- new devel policy
- correct license
- spec clean

* Mon Sep 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.0-9mdv2009.0
+ Revision: 285058
- update patch for CVE-2008-2149 and CVE-2008-3908 (bug #43433)

* Thu Sep 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.0-8mdv2009.0
+ Revision: 280562
- security fix for CVE-2008-2149 (bug #43433)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.0-7mdv2009.0
+ Revision: 225929
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0-6mdv2008.1
+ Revision: 179683
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 3.0-5mdv2008.0
+ Revision: 82071
- use autoreconf
- rebuild for new soname of tcl

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 3.0-4mdv2008.0
+ Revision: 36547
- rebuild with correct optflags

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version, rediff FHS patch
    - new version
    - import wordnet


* Fri Aug 11 2006 Laurent MONTEL <lmontel@mandriva.com> 2.1-5
- Rebuild

* Fri Mar 17 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.1-4mdk
- fix non sense

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.1-3mdk
- patch 2: fix build on x86_64

* Thu Jan 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-2mdk
- fix dictionary files location (#20720)

* Wed Jan 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-1mdk
- new version
- new libtool and fhs patches
- new URL

* Mon Jan 02 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0-7mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-6mdk
- %%mkrel

* Thu Jun 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-5mdk 
- spec cleanup
- drop release on requires
- fix libtool file perms

* Tue May 24 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.0-4mdk
- add BuildRequires: automake1.8 tcl tk XFree86-devel

* Fri May 20 2005 Olivier Thauvin <nanardon@mandriva.org> 2.0-3mdk
- fix build on amd64 (aka libtoolize --force + fix -L X11 path)

* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0-2mdk 
- fixed group
- stronger interdependency
- fixed major

* Wed Aug 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0-1mdk 
- first mdk package
