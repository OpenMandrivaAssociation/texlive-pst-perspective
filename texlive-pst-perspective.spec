%global tl_name pst-perspective
%global tl_revision 39585

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	Draw perspective views using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-perspective
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-perspective.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-perspective.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to draw an orthogonal parallel projection
with an arbitrarily chosen angle and a variable shortening factor.

