# revision 23398
# category TLCore
# catalog-ctan /systems/luatex/base
# catalog-date 2011-06-07 11:25:20 +0200
# catalog-license gpl2
# catalog-version 0.70.1
Name:		texlive-luatex
Version:	0.70.1
Release:	1
Summary:	The LuaTeX engine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/luatex/base
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-luatex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-tetex

%description
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language. The LuaTeX project's main
objective is to provide an open and configurable variant of TeX
while at the same time offering downward compatibility. LuaTeX
uses Unicode (as UTF-8) as its default input encoding, and is
able to use modern (OpenType) fonts (for both text and
mathematics). It should be noted that LuaTeX is still under
development; its specification has been declared stable, but
absolute stability may not in practice be assumed.

%pre
    %_texmf_fmtutil_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_fmtutil_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/tex/generic/config/luatex-unicode-letters.tex
%{_texmfdir}/tex/generic/config/luatexiniconfig.tex
%{_texmfdir}/web2c/texmfcnf.lua
%_texmf_fmtutil_d/luatex
%doc %{_texmfdistdir}/doc/luatex/base/fdata.lua
%doc %{_texmfdistdir}/doc/luatex/base/fdata_epdf.lua
%doc %{_texmfdistdir}/doc/luatex/base/fdata_img.lua
%doc %{_texmfdistdir}/doc/luatex/base/functionref.pdf
%doc %{_texmfdistdir}/doc/luatex/base/functionref.tex
%doc %{_texmfdistdir}/doc/luatex/base/luatex.man
%doc %{_texmfdistdir}/doc/luatex/base/luatexref-env.tex
%doc %{_texmfdistdir}/doc/luatex/base/luatexref-t.pdf
%doc %{_texmfdistdir}/doc/luatex/base/luatexref-t.tex
%doc %{_mandir}/man1/luatex.1*
%doc %{_texmfdir}/doc/man/man1/luatex.man1.pdf
%doc %{_mandir}/man1/texlua.1*
%doc %{_texmfdir}/doc/man/man1/texlua.man1.pdf
%doc %{_mandir}/man1/texluac.1*
%doc %{_texmfdir}/doc/man/man1/texluac.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/luatex <<EOF
luatex luatex language.def,language.dat.lua luatex.ini
dviluatex luatex language.def,language.dat.lua dviluatex.ini
EOF
