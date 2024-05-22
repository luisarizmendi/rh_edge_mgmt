Name:       workload-manifests
Version:    0.0.1
Release:    rh1
Summary:    Kubernetes Manifests for embedded APPs
License:    BSD
Source0:    workload-manifests.tar.gz
ExclusiveArch: x86_64

%description
Kubernetes Manifests for embedded APPs

# Since we don't recompile from source, disable the build_id checking
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global debug_package %{nil}

# We are evil, we have no changelog !
%global source_date_epoch_from_changelog 0

%prep
cp %{S:0} workload-manifests.tar.gz

%build

%install
mkdir -p %{buildroot}/var/lib/microshift/manifests/
tar -xzf workload-manifests.tar.gz -C %{buildroot}/var/lib/microshift/manifests/


%files
%attr(0644, root, root) /var/lib/microshift/manifests/**

%post
# Set SELinux context for the files
restorecon -R /var/lib/microshift

%changelog


