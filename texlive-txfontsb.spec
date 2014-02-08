# revision 21578
# category Package
# catalog-ctan /fonts/txfontsb
# catalog-date 2011-03-01 17:09:11 +0100
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-txfontsb
Version:	1.1
Release:	3
Summary:	Extensions to txfonts, using GNU Freefont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/txfontsb
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfontsb.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb-SmallCaps.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb-SmallCapsAlt.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifb.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbBold.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbBoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/txfontsb/FreeSerifbItalic.afm
%{_texmfdistdir}/fonts/enc/dvips/txfontsb/gptimes.enc
%{_texmfdistdir}/fonts/enc/dvips/txfontsb/gptimesy.enc
%{_texmfdistdir}/fonts/map/dvips/txfontsb/gptimes.map
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimessco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesybi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesybi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesyrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/gtimesysco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/txfontsb/timessco6r.tfm
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb-SmallCaps.pfb
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb-SmallCapsAlt.pfb
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifb.pfb
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbBold.pfb
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbBoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/txfontsb/FreeSerifbItalic.pfb
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesb6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesbi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesrg6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimessc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimessco6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyb6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesybi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyi6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesyrg6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesysc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/gtimesysco6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/timessc6a.vf
%{_texmfdistdir}/fonts/vf/public/txfontsb/timessco6a.vf
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxr.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxrc.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxry.fd
%{_texmfdistdir}/tex/latex/txfontsb/lgrtxryc.fd
%{_texmfdistdir}/tex/latex/txfontsb/ot1txrc.fd
%{_texmfdistdir}/tex/latex/txfontsb/ot1txryc.fd
%{_texmfdistdir}/tex/latex/txfontsb/txfontsb.sty
%doc %{_texmfdistdir}/doc/fonts/txfontsb/README
%doc %{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.pdf
%doc %{_texmfdistdir}/doc/fonts/txfontsb/txfontsb.tex
#- source
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifb-SmallCaps.sfd
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifb-SmallCapsAlt.sfd
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifb.sfd
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifbBold.sfd
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifbBoldItalic.sfd
%doc %{_texmfdistdir}/source/fonts/txfontsb/FreeSerifbItalic.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757163
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719822
- texlive-txfontsb
- texlive-txfontsb
- texlive-txfontsb

