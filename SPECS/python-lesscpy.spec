%global pypi_name lesscpy

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        4%{?dist}
Summary:        Lesscss compiler

License:        MIT
URL:            https://github.com/robotis/lesscpy
Source0:        https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

Patch0:         https://github.com/lesscpy/lesscpy/pull/99.patch#/%{pypi_name}-fix-test.patch

BuildArch:      noarch
 
%global _description\
A compiler written in python 3 for the lesscss language.  For those of us not\
willing/able to have node.js installed in our environment.  Not all features\
of lesscss are supported (yet).  Some features wil probably never be\
supported (JavaScript evaluation).

%description %_description

%if %{with python2}
%package -n python2-lesscpy
Summary:        %summary
Requires:       python2-ply
Requires:       python2-six
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-ply
BuildRequires:  python2-nose
BuildRequires:  python2-coverage
BuildRequires:  python2-six
%{?python_provide:%python_provide python2-lesscpy}

%description -n python2-lesscpy %_description
%endif # with python2

%package -n python3-lesscpy
Summary:    %summary
Requires:   python3-ply
Requires:   python3-six
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-ply
BuildRequires: python3-nose
BuildRequires: python3-coverage
BuildRequires: python3-six
%{?python_provide:%python_provide python3-lesscpy}

%description -n python3-lesscpy
A compiler written in python 3 for the lesscss language.  For those of us not
willing/able to have node.js installed in our environment.  Not all features
of lesscss are supported (yet).  Some features wil probably never be
supported (JavaScript evaluation).

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif # with python2

%py3_build


%install
%if %{with python2}
%py2_install
rm %{buildroot}/%{_bindir}/lesscpy
%endif # with python2

%py3_install
# link for backwards compatibility. consider removal in Fedora 30+
ln -s ./lesscpy %{buildroot}/%{_bindir}/py3-lesscpy


%check
%if %{with python2}
%{__python2} -m nose -v
%endif # with python2
%{__python3} -m nose -v

%if %{with python2}
%files -n python2-lesscpy
%doc LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with python2

%files -n python3-lesscpy
%doc LICENSE
%{_bindir}/lesscpy
%{_bindir}/py3-lesscpy
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info


%changelog
* Fri Jun 22 2018 Petr Viktorin <pviktori@redhat.com> - 0.13.0-4
- Remove the unused flake8 build dependency

* Tue Jun 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- General spec cleanup
- Add missing dependency on six
- Run the tests

* Tue Jun 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- /usr/bin/lesscpy is Python 3

* Mon Jun 11 2018 Christian Heimes <cheimes@redhat.com> - 0.13.0-1
- New upstream release 0.13.0, resolves rhbz#1584773

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.1-11
- Python 2 binary package renamed to python2-lesscpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Feb 11 2014 Matthias Runge <mrunge@redhat.com> - 0.10.1-1
- update to 0.10.1

* Thu Aug 29 2013 Matthias Runge <mrunge@redhat.com> - 0.9j-3
- use python instead of python3 in python2 package

* Wed Aug 21 2013 Matthias Runge <mrunge@redhat.com> - 0.9j-2
- add br python-ply

* Mon Jul 29 2013 Matthias Runge <mrunge@redhat.com> - 0.9j-1
- Initial package.
