Name:			bonk
Version:		0.6
Release:		2
Summary:		A lossy and lossless audio coder
License:		GPLv2
Group:			Sound
URL:			http://www.logarithmic.net/pfh/bonk/
Source:			http://etree.org/shnutils/shntool/support/formats/bonk/win32/%{version}/%{name}-%{version}-shntool.tar.gz
Patch1:			%{name}-gcc4.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-build

%description
Bonk is high quality audio compression program. It can operate
in either lossless or lossy mode. In lossless mode, the exact
original WAV file can be recovered from the compressed file. In
lossy mode, some information is discarded in the compressed file,
yielding a much higher compression ratio. The information
discarded is perceptually unimportant, and the result should be
a *perceptually* lossless encoding. Bonk can compress some types
of sounds more than others, so the actual bit-rate achieved varies.

In lossy mode, it can compress some types of sound to as low as
95 kbps (a compression ration of 14:1) while maintaining
perceptually lossless CD quality stereo. In general, the
compression ratio achieved by Bonk is slightly higher than that
achieved using the more common MP3 format, for equivalent sound
quality. In particular it copes with transients (eg clapping,
drum beats) better. Performance on purely tonal sound is roughly
equivalent to MP3.

In lossless mode the compression ratio is typically around 2:1.

This version is patched with shntool patch.

%prep
%setup -q -n %{name}-%{version}-shntool
%patch1 -p1

%build
%make

%install
%__rm -rf %{buildroot}
%__install -dm 755  %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING
%{_bindir}/*



%changelog
* Sun Sep 18 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6-1
+ Revision: 700196
- imported package bonk

