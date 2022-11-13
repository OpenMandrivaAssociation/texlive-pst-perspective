Name:		texlive-pst-perspective
Version:	39585
Release:	1
Summary:	Draw perspective views using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-perspective
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-perspective.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-perspective.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to draw an orthogonal parallel
projection with an arbitrarily chosen angle and a variable
shortening factor.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-perspective/pst-perspective.tex
%{_texmfdistdir}/tex/latex/pst-perspective/pst-perspective.sty
%doc %{_texmfdistdir}/doc/generic/pst-perspective/Parallelprojektion-Kreis.pdf
%doc %{_texmfdistdir}/doc/generic/pst-perspective/Parallelprojektion-Kreis.tex
%doc %{_texmfdistdir}/doc/generic/pst-perspective/README
%doc %{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-docEN.pdf
%doc %{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-docEN.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
