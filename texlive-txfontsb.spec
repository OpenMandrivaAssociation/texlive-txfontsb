%global tl_name txfontsb
%global tl_revision 54512
%global tl_version 1.1.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
A set of fonts that extend the txfonts bundle with small caps and old
style numbers, together with Greek support. The extensions are made with
modifications of the GNU Freefont.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from txfontsb:
Map gptimes.map
TL_DROPIN_EOF
