%global real_name cuda_cccl

%global major_package_version 11-8

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.0.90
Release:        1%{?dist}
Summary:        CXX Core Compute Libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 ppc64le aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/cuda_cccl/linux-x86_64/cuda_cccl-linux-x86_64-11.8.89-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-ppc64le/%{real_name}-linux-ppc64le-%{version}-archive.tar.xz
Source2:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-aarch64/%{real_name}-linux-aarch64-%{version}-archive.tar.xz

Requires:       cmake-filesystem
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description
CXX Core Compute Libraries.

%package devel
Summary:        CXX Core Compute Libraries development files

%description devel
CXX Core Compute Libraries development files.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch ppc64le
%setup -q -T -b 1 -n %{real_name}-linux-ppc64le-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 2 -n %{real_name}-linux-aarch64-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/cmake

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/cmake/* %{buildroot}%{_libdir}/cmake
rm -f %{buildroot}%{_libdir}/cmake/thrust/README.md

%files devel
%license LICENSE
%doc lib/cmake/thrust/README.md
%{_includedir}/*
%{_libdir}/cmake/*

%changelog
* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.90-1
- Update to 12.0.90.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.89-1
- Update to 11.8.89.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.91-1
- Update to 11.7.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.58-1
- Update to 11.7.58.

* Tue Jan 25 2022 Simone Caronni <negativo17@gmail.com> - 11.6.55-1
- First build with the new tarball components.

