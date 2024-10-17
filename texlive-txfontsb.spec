Name:		texlive-txfontsb
Version:	54512
Release:	2
Summary:	Extensions to txfonts, using GNU Freefont
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/txfontsb
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts that extend the txfonts bundle with small caps
and old style numbers, together with Greek support. The
extensions are made with modifications of the GNU Freefont.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/txfontsb
%{_texmfdistdir}/fonts/enc/dvips/txfontsb
%{_texmfdistdir}/fonts/map/dvips/txfontsb
%{_texmfdistdir}/fonts/opentype/public/txfontsb
%{_texmfdistdir}/fonts/tfm/public/txfontsb
%{_texmfdistdir}/fonts/type1/public/txfontsb
%{_texmfdistdir}/fonts/vf/public/txfontsb
%{_texmfdistdir}/tex/latex/txfontsb
%doc %{_texmfdistdir}/doc/fonts/txfontsb
#- source
%doc %{_texmfdistdir}/source/fonts/txfontsb

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
