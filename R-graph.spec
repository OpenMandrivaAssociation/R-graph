%bcond_with bootstrap
%global packname  graph
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.0
Release:          2
Summary:          graph: A package to handle graph data structures
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-stats R-tools R-utils R-XML R-RUnit R-cluster
%if %{without bootstrap}
Requires:         R-SparseM R-RBGL
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-stats R-tools R-utils R-XML R-RUnit R-cluster
%if %{without bootstrap}
BuildRequires:    R-SparseM R-RBGL
%endif
BuildRequires:    x11-server-xvfb

%description
A package that implements some simple graph handling capabilities.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
xvfb-run %{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/GXL
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/Scripts
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/perf
%{rlibdir}/%{packname}/unitTests
