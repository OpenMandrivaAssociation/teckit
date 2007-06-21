%define major 0
%define libname %mklibname teckit %{major}
%define libname_d %mklibname teckit -d
%define libname_d_s %mklibname teckit -d -s

Name:           teckit
Version:        2.2.1
Release:        %mkrel 1
Epoch:          0
Summary:        Conversion library and mapping compiler
License:        LGPL
Group:          System/Libraries
URL:            http://scripts.sil.org/teckit
Source0:        http://scripts.sil.org/svn-view/teckit/TAGS/TECkit_release_2006-09-19.tar.gz
BuildRequires:  chrpath
BuildRequires:  libexpat-devel
BuildRequires:  libz-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
Summary:        Conversion library and mapping compiler
Group:          System/Libraries

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
Summary:        Development files for teckit
Group:          Development/C
Requires:       %{libname} = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}

%description -n %{libname_d}
Development files for teckit.

%package -n %{libname_d_s} 
Summary:        Static Library for developing applications with %name
Group:          Development/C
Requires:       %{libname_d} = %{epoch}:%{version}-%{release}
Provides:       %{name}-static-devel = %{epoch}:%{version}-%{release}

%description -n %{libname_d_s}
Static library for teckit.

%prep
%setup -q -n TECkit_release_2006-09-19
%{__chmod} 0755 ./configure
%{__rm} -r zlib*

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/sfconv
%attr(0755,root,root) %{_bindir}/teckit_compile
%attr(0755,root,root) %{_bindir}/txtconv

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%attr(0755,root,root) %{_libdir}/libTECkit.so.*
%attr(0755,root,root) %{_libdir}/libTECkit_Compiler.so.*

%files -n %{libname_d}
%defattr(0644,root,root,0755)
%doc docs/*.pdf
%dir %{_includedir}/teckit/
%{_includedir}/teckit/TECkit_Common.h
%{_includedir}/teckit/TECkit_Compiler.h
%{_includedir}/teckit/TECkit_Engine.h
%attr(0755,root,root) %{_libdir}/libTECkit.la
%attr(0755,root,root) %{_libdir}/libTECkit_Compiler.la
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so

%files -n %{libname_d_s}
%defattr(0644,root,root,0755)
%{_libdir}/libTECkit.a
%{_libdir}/libTECkit_Compiler.a
