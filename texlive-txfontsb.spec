%global tl_name txfontsb
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Extensions to txfonts, using GNU Freefont
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/txfontsb
License:	gpl lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of fonts that extend the txfonts bundle with small caps and old
style numbers, together with Greek support. The extensions are made with
modifications of the GNU Freefont.

