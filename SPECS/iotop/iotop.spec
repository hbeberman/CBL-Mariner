%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Iotop is a Python program with a top like UI used to show the processes and their corresponding IO activity.
Name:           iotop
Version:        0.6
Release:        8%{?dist}
License:        GPLv2
URL:            http://guichaz.free.fr/iotop/
Group:          System/Monitoring
Vendor:         Microsoft Corporation
Distribution:   Mariner
Source0:        http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-libs
Requires:       python3
Requires:       python3-libs

Patch0:         fix_python3_compat.patch

BuildArch:      noarch

%description
Iotop is a Python program with a top like UI used to show the processes and their corresponding IO activity.

%prep
%autosetup

%build
python3 setup.py build

%install
#!/bin/bash
# http://bugs.python.org/issue644744
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} --record="INSTALLED_FILES"
# 'brp-compress' gzips the man pages without distutils knowing... fix this
sed -i -e 's@man/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@man/man\1/\2.gz@g' "INSTALLED_FILES"
sed -i -e 's@\(.\+\)\.py$@\1.py*@' \
       -e '/.\+\.pyc$/d' \
       "INSTALLED_FILES"
echo "%dir %{python3_sitelib}/iotop" >> INSTALLED_FILES

%clean
rm -rf %{buildroot}/*

%files -f INSTALLED_FILES
%defattr(-,root,root)
%license COPYING
%doc COPYING NEWS THANKS
%{python3_sitelib}/iotop/*

%changelog
*   Tue Feb 23 2021 Henry Beberman <henry.beberman@microsoft.com> 0.6-8
-   Switch from python2 to python3.
-   Add patch from upstream to fix python3.
*   Sat May 09 00:21:23 PST 2020 Nick Samson <nisamson@microsoft.com> 0.6-7
-   Added %%license line automatically
*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 0.6-6
-   Initial CBL-Mariner import from Photon (license: Apache2).
*	Fri Jun 16 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.6-5
-	Use python2 explicitly
*	Thu Jun 15 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.6-4
-	Add python2 to Requires
*	Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6-3
-	Fix arch
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6-2
-	GA - Bump release of all rpms
*	Mon Nov 30 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.6-1
-	Initial build.	First version
