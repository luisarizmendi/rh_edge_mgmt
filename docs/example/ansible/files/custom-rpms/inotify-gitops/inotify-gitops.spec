Name:       inotify-gitops
Version:    0.0.1
Release:    rh1
Summary:    Checks ETC files are modified and if so send a webhook to AAP 
License:    BSD
Source0:    watch_etc.py
Source1:    watch-etc.service
Source2:    inotify-wait
Requires(pre): shadow-utils
Requires: python3-inotify
Requires: python3-pip
BuildRequires: systemd-rpm-macros
ExclusiveArch: x86_64

%description
Checks ETC files are modified and if so send a webhook to AAP 

# Since we don't recompile from source, disable the build_id checking
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global debug_package %{nil}

# We are evil, we have no changelog !
%global source_date_epoch_from_changelog 0

%prep
cp %{S:0} watch_etc.py
cp %{S:1} watch-etc.service
cp %{S:2} inotify-wait

%build

%install
install -m 0644 -D watch_etc.py %{buildroot}/usr/local/bin/watch_etc.py
install -m 0644 -D watch-etc.service %{buildroot}/etc/systemd/system/watch-etc.service
install -m 0644 -D inotify-wait %{buildroot}/root/inotify-wait


%files
%attr(0644, root, root) /usr/local/bin/watch_etc.py
%attr(0644, root, root) /etc/systemd/system/watch-etc.service
%attr(0644, root, root) /root/inotify-wait


%post
# Set SELinux context for the files
restorecon -R $RPM_BUILD_ROOT/etc/systemd/system 
systemctl enable watch-etc.service || :
systemctl start watch-etc.service || :
systemctl daemon-reload || :


%changelog