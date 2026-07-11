%global tl_name uhc
%global tl_revision 16791

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for the Korean language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/korean/HLaTeX
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uhc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uhc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Korean documents written in Korean standard KSC codes for
LaTeX2e.

