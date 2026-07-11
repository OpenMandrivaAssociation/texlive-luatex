%global tl_name luatex
%global tl_revision 78218

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The LuaTeX engine
Group:		Publishing
URL:		https://www.ctan.org/pkg/luatex
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(etex)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(luatex.bin)
Requires:	texlive(plain)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LuaTeX is a greatly extended version of pdfTeX using Lua as an embedded
scripting language. The LuaTeX project's main objective is to provide an
open and configurable variant of TeX while at the same time offering
substantive backward compatibility. LuaTeX uses Unicode (as UTF-8) as
its default input encoding, and is able to use modern (OpenType and
TrueType) fonts (for both text and mathematics).

