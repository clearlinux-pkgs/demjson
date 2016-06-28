#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : demjson
Version  : 2.2.4
Release  : 17
URL      : http://deron.meranda.us/python/demjson/dist/demjson-2.2.4.tar.gz
Source0  : http://deron.meranda.us/python/demjson/dist/demjson-2.2.4.tar.gz
Summary  : encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: demjson-bin
Requires: demjson-python
BuildRequires : demjson
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
demjson
=======
MORE DOCUMENTATION IS IN THE "docs" SUBDIRECTORY.
'demjson' is a Python language module for encoding, decoding, and
syntax-checking JSON data. It works under both Python 2 and Python 3.

%package bin
Summary: bin components for the demjson package.
Group: Binaries

%description bin
bin components for the demjson package.


%package python
Summary: python components for the demjson package.
Group: Default

%description python
python components for the demjson package.


%prep
%setup -q -n demjson-2.2.4

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonlint

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
