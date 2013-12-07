%define major 0
%define libname %mklibname teckit %{major}
%define libname_d %mklibname teckit -d
%define libname_d_s %mklibname teckit -d -s

Name:		teckit
Version:	2.5.1
Release:	7
Epoch:		0
Summary:	Conversion library and mapping compiler
License:	LGPL
Group:		System/Libraries
URL:		http://scripts.sil.org/teckit
Source0:	http://scripts.sil.org/svn-view/teckit/TAGS/TECkit_2_5_1.tar.gz
Patch0:		TECkit-2.5.1-gcc44.patch
BuildRequires:	chrpath
BuildRequires:	expat-devel
BuildRequires:	zlib-devel

%description 
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%package -n %{libname}
Summary:	Conversion library and mapping compiler
Group:		System/Libraries

%description -n %{libname}
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%package -n %{libname_d}
Summary:	Development files for teckit
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{libname_d}
Development files for teckit.

%package -n %{libname_d_s} 
Summary:	Static Library for developing applications with %{name}
Group:		Development/C
Requires:	%{libname_d} = %{EVRD}
Provides:	%{name}-static-devel = %{EVRD}

%description -n %{libname_d_s}
Static library for teckit.

%prep
%setup -q -n TECkit_2_5_1
%__chmod 0755 ./configure
%__rm -r zlib*
%patch0 -p0 -b .gcc44

%build
%configure2_5x
%make

%install
%makeinstall_std

%{_bindir}/chrpath -d %{buildroot}%{_bindir}/sfconv
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/teckit_compile
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/txtconv

%check
%{make} check

%files
%{_bindir}/sfconv
%{_bindir}/teckit_compile
%{_bindir}/txtconv

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libTECkit.so.*
%{_libdir}/libTECkit_Compiler.so.*

%files -n %{libname_d}
%doc docs/*.pdf
%dir %{_includedir}/teckit/
%{_includedir}/teckit/TECkit_Common.h
%{_includedir}/teckit/TECkit_Compiler.h
%{_includedir}/teckit/TECkit_Engine.h
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so

%files -n %{libname_d_s}
%{_libdir}/libTECkit.a
%{_libdir}/libTECkit_Compiler.a


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0:2.5.1-5mdv2011.0
+ Revision: 670673
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.5.1-4mdv2011.0
+ Revision: 607986
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.5.1-3mdv2010.1
+ Revision: 524174
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:2.5.1-2mdv2010.0
+ Revision: 427289
- rebuild
- add missing include to fix gcc 4.4 compilation

* Sat Aug 16 2008 David Walluck <walluck@mandriva.org> 0:2.5.1-1mdv2009.0
+ Revision: 272753
- 2.5.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jan 07 2008 David Walluck <walluck@mandriva.org> 0:2.2.1-4mdv2008.1
+ Revision: 146183
- remove EXCLUDE_FROM_EOL_CONVERSION (no longer needed)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 David Walluck <walluck@mandriva.org> 0:2.2.1-3mdv2008.0
+ Revision: 42653
- workaround broken fix-eol rpm-helper script
- bump release
- BuildRequires: libexpat-devel

* Fri Jun 22 2007 David Walluck <walluck@mandriva.org> 0:2.2.1-1mdv2008.0
+ Revision: 42514
- Import teckit



* Thu Jun 21 2007 David Walluck <walluck@mandriva.org> 0:2.2.1-1mdv2008.0
- release
