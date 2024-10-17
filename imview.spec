Summary:   Image display and analysis
Name:      imview
Version:   1.1.8
Release:   %mkrel 9
License:   GPLv2+
Group:     Graphics
Source:    http://experimental.act.cmis.csiro.au/imview/download/imview-src-%{version}.tar.bz2
# use www-browser instead of netscape to display docs
Patch0:    imview-www-browser.patch
Patch1:	   imview-1.1.8-dont-link-static.patch
Patch2:	   imview-1.1.8-includes.patch
URL: 	   https://www.cmis.csiro.au/hugues.talbot/imview
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: fltk-devel
BuildRequires: jpeg-devel
BuildRequires: libmagick-devel
BuildRequires: libxinerama-devel
BuildRequires: tiff-devel

%description
This application allows the user to display a variety of image formats
and to help analyse the content of images. It can perform as a general-
purpose image display program with some nice features, but it is
designed with the profesionnal image analysis/image processing person 
in mind.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
autoconf

%build
# needed to build on x86_64
export CXXFLAGS="$RPM_BUILD_OPTS -fpermissive"

%configure2_5x --with-jpeg --with-tiff --with-magick
%make depend
%make

%install
make DESTDIR="$RPM_BUILD_ROOT" install-strip
# man dir is wrong
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_bindir}/imview
%{_datadir}/Imview
%{_mandir}/man*/*
%doc README COPYING ChangeLog

