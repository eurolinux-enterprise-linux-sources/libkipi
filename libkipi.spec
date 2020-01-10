Name:    libkipi
Summary: Common plugin infrastructure for KDE image applications
Version: 4.10.5
Release: 3%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libkexiv2
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kdelibs4-devel

Requires: kdelibs4%{?_isa} >= %{_kde4_version}

# when split occurred
Conflicts: kdegraphics-libs < 7:4.6.95-10

%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common plugin
structure (for Digikam, Gwenview, etc.). Its aim is to share
image plugins among graphic applications.

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel 
%description devel
%{summary}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
pkg-config --modversion libkipi


%post
/sbin/ldconfig
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
fi


%files
%doc AUTHORS COPYING README
%{_kde4_libdir}/libkipi.so.10*
%{_kde4_appsdir}/kipi/
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_datadir}/kde4/servicetypes/kipiplugin.desktop

%files devel
%{_kde4_libdir}/libkipi.so
%{_kde4_libdir}/pkgconfig/libkipi.pc
%{_kde4_includedir}/libkipi/


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.10.5-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-2
- Mass rebuild 2013-12-27

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sat Jan 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Tue Nov 20 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.80-1
- 4.9.80

* Thu Sep 20 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.9.50-1
- libkipi update from digikam-3.0.0-beta1

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80
- bump soname version to 9*

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 14 2011 Radek Novacek <rnovacek@redhat.com> 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0

* Mon Jul 11 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-1
- 4.6.95
- fix URL

* Wed Jul 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-3
- Conflicts: kdegraphics < 7:4.6.90 

* Wed Jul 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-2
- License: GPLv2+
- fix scriptlets
- %%doc: +NEWS, -TODO 
- fix Source0 URL

* Tue Jul 05 2011 Rex Dieter <rdieter@fedoraproject.org>  4.6.90-1
- first try


