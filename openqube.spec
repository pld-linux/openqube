Summary:	OpenQube - library for reading quantum chemistry data files
Summary(pl.UTF-8):	OpenQube - biblioteka do odczytu plików danych chemii kwantowej
Name:		openqube
Version:	0.1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/OpenChemistry/openqube/archive/%{version}.tar.gz
# Source0-md5:	c7939f66b0ab8311e5482cd93aa44ef4
URL:		http://wiki.openchemistry.org/OpenQube
BuildRequires:	QtCore-devel >= 4.6
BuildRequires:	cmake >= 2.8
BuildRequires:	eigen >= 2
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenQube is an open-source C++ library for reading quantum chemistry
data files, and calculating volumetric data such as molecular orbitals
and electron densities.

%description -l pl.UTF-8
OpenQube to mająca otwarte źródła biblioteka C++ do odczytu plików
danych chemii kwantowej oraz obliczania danych objętościowych, takich
jak orbitale cząsteczek i gęstości elektronów.

%package devel
Summary:	Header files for OpenQube library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenQube
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.6
Requires:	eigen >= 2

%description devel
Header files for OpenQube library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenQube.

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/libOpenQube.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenQube.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenQube.so
%{_includedir}/openqube
%{_libdir}/cmake/openqube
