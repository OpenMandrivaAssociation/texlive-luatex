# revision 30581
# category TLCore
# catalog-ctan /systems/luatex/base
# catalog-date 2011-11-09 15:33:34 +0100
# catalog-license gpl2
# catalog-version 0.70.1
Name:		texlive-luatex
Version:	0.70.1
Release:	6
Summary:	The LuaTeX engine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/luatex/base
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-luatex.bin

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/web2c/luatex
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/config/luatex-unicode-letters.tex
%{_texmfdistdir}/tex/generic/config/luatexiniconfig.tex
%{_texmfdistdir}/web2c/texmfcnf.lua
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
%doc %{_texmfdistdir}/doc/man/man1/luatex.man1.pdf
%doc %{_mandir}/man1/texlua.1*
%doc %{_texmfdistdir}/doc/man/man1/texlua.man1.pdf
%doc %{_mandir}/man1/texluac.1*
%doc %{_texmfdistdir}/doc/man/man1/texluac.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

perl -pi -e 's%^(\s*TEXMFMAIN\s+=\s+").*%$1%{_texmfdir}",%;'				\
	 -e 's%\bTEXMFCONTEXT\b%TEXMFDIST%g;'						\
	 -e 's%^(\s*TEXMFDIST\s+=\s+).*%$1"%{_texmfdistdir}",%;'			\
	 -e 's%^(\s*TEXMFLOCAL\s+=\s+).*%$1"%{_texmflocaldir}",%;'			\
	 -e 's%^(\s*TEXMFSYSVAR\s+=\s+).*%$1"%{_texmfvardir}",%;'			\
	 -e 's%^(\s*TEXMFSYSCONFIG\s+=\s+).*%$1"%{_texmfconfdir}",%;'			\
	 -e 's%^(\s*TEXMFHOME\s+=\s+").*%$1\$HOME/texmf",%;'				\
	 -e 's%^(\s*TEXMFVAR\s+=\s+").*%$1\$HOME/.texlive2013/texmf-var",%;'		\
	 -e 's%^(\s*TEXMFCONFIG\s+=\s+").*%$1\$HOME/.texlive2013/texmf-config",%;'	\
	 -e 's%^(\s*FONTCONFIG_PATH\s+=\s+").*%$1%{_sysconfdir}/fonts",%;'		\
	 -e 's|^local texmflocal.*$||;'							\
	 -e 's|^texmflocal.*$||;'							\
	texmf/web2c/texmfcnf.lua

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/luatex <<EOF
#
# from luatex:
luatex luatex language.def,language.dat.lua luatex.ini
dviluatex luatex language.def,language.dat.lua dviluatex.ini
EOF
