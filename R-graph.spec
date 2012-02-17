%bcond_without bootstrap
%global packname  graph
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.0
Release:          1
Summary:          graph: A package to handle graph data structures
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods 
Requires:         R-methods R-stats R-tools R-utils 
%if %{with bootstrap}
Requires:         R-XML R-RUnit R-cluster 
%else
Requires:         R-SparseM R-XML R-RBGL R-RUnit R-cluster 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-methods R-stats R-tools R-utils 
%if %{with bootstrap}
BuildRequires:    R-XML R-RUnit R-cluster 
%else
BuildRequires:    R-SparseM R-XML R-RBGL R-RUnit R-cluster 
%endif

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
%{_bindir}/R CMD check %{packname}
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