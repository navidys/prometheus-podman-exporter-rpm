%global with_check 0
%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global goipath github.com/containers/prometheus-podman-exporter
Version: 0.4.0
%global tag v0.4.0
%gometa

%global goname prometheus-podman-exporter
%global shortname podman_exporter

%global common_description %{expand:
%{goname} is a prometheus exporter for podman environments exposing
containers, pods, images, volumes and networks information.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md MAINTAINERS.md SECURITY.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: %autorelease
Summary: Prometheus exporter for podman environments.
License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
URL: %{gourl}
Source0: %{gosource}

%if 0%{?fedora} && ! 0%{?rhel}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: gcc
%if 0%{?rhel} >= 9
BuildRequires: golang >= 1.17
%else
BuildRequires: golang >= 1.18.2
%endif
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make
BuildRequires: gpgme-devel
BuildRequires: device-mapper-devel
BuildRequires: libassuan-devel
%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif

# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver)) = v3.5.1+incompatible
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.1.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.1.2
Provides: bundled(golang(github.com/checkpoint_restore/checkpointctl)) = v0.0.0_20220321135231_33f4a66335f0
Provides: bundled(golang(github.com/checkpoint_restore/go_criu/v5)) = v5.3.0
Provides: bundled(golang(github.com/chzyer/readline)) = v0.0.0_20180603132655_2972be24d48e
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.3
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.4
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.11.4
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.0
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.1.1
Provides: bundled(golang(github.com/container_orchestrated_devices/container_device_interface)) = v0.4.0
Provides: bundled(golang(github.com/containers/buildah)) = v1.26.1
Provides: bundled(golang(github.com/containers/common)) = v0.48.0
Provides: bundled(golang(github.com/containers/conmon)) = v2.0.20+incompatible
Provides: bundled(golang(github.com/containers/image/v5)) = v5.21.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20200511145503_9c3a6c22cd9a
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.4
Provides: bundled(golang(github.com/containers/podman/v4)) = v4.1.1
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.2
Provides: bundled(golang(github.com/containers/storage)) = v1.40.2
Provides: bundled(golang(github.com/coreos/go_systemd)) = v0.0.0_20190620071333_e64a0ec8b42a
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/davecgh/go_spew)) = v1.1.1
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.6.4
Provides: bundled(golang(github.com/docker/docker)) = v20.10.14+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.1_0.20210727194412_58542c764a11
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_plugins_helpers)) = v0.0.0_20211224144127_6eecb7beb651
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/docker/libnetwork)) = v0.8.0_dev.2.0.20190625141545_5a177b73e316
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.5.4
Provides: bundled(golang(github.com/fsouza/go_dockerclient)) = v1.7.11
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/go_kit/log)) = v0.2.1
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/go_logfmt/logfmt)) = v0.5.1
Provides: bundled(golang(github.com/google/gofuzz)) = v1.2.0
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/google/shlex)) = v0.0.0_20191202100458_e7afc7fbc510
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.12
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.0
Provides: bundled(golang(github.com/ishidawataru/sctp)) = v0.0.0_20210226210310_f2269e66cdee
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.5
Provides: bundled(golang(github.com/jpillora/backoff)) = v1.0.0
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.2
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.5
Provides: bundled(golang(github.com/manifoldco/promptui)) = v0.9.0
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.13
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = v1.0.2_0.20181231171920_c182affec369
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.5.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.2
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/mistifyio/go_zfs)) = v2.1.2_0.20190413222219_f784269be439+incompatible
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.6.1
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.2.0
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/mwitkow/go_conntrack)) = v0.0.0_20190716064945_2f068394615f
Provides: bundled(golang(github.com/navidys/prometheus_podman_exporter)) = v0.4.0
Provides: bundled(golang(github.com/nxadm/tail)) = v1.4.8
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.3_0.20220114050600_8b9d41f48198
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.1
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20211214071223_8958f93039ab
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20220110225228_7e2d60f1e41f
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.1
Provides: bundled(golang(github.com/openshift/imagebuilder)) = v1.2.4_0.20220502172744_009dbc6cb805
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20210805093236_719684c64e4f
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/pmezard/go_difflib)) = v1.0.0
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.1
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.12.2
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.2.0
Provides: bundled(golang(github.com/prometheus/common)) = v0.35.0
Provides: bundled(golang(github.com/prometheus/exporter_toolkit)) = v0.7.1
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.7.3
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.9.2_0.20210429002308_3879420cc921
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.5.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.7.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/tchap/go_patricia)) = v2.3.0+incompatible
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.10
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.4.1
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.1_0.20220115184804_dd687eb2f2d4
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20210104183010_2eb08e3e575f
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = v1.3.0

%description
%{common_description}

%prep
%goprep

mkdir _depbundle
pushd _depbundle
/usr/bin/gzip -dc %{SOURCE0} | /usr/bin/tar -xof -
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%{__install} -m 0755 -vd %{gobuilddir}/src/
# copy required bundled libraries
%{__cp} -rp %{goname}-%{version}/vendor/* %{gobuilddir}/src/
popd
%{_bindir}/rm -rf _depbundle

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}/

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%{__install} -dp %{buildroot}%{_bindir}
%{__install} -dp %{buildroot}%{_unitdir}
%{__install} -dp %{buildroot}%{_userunitdir}
%{__install} -p ./bin/%{name} %{buildroot}%{_bindir}
%{__install} -Dpm0644 ./contrib/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
%{__install} -Dpm0644 ./contrib/systemd/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service

pushd %{buildroot}%{_unitdir}
ln -s %{name}.service %{shortname}.service
popd

pushd %{buildroot}%{_userunitdir}
ln -s %{name}.service %{shortname}.service
popd

pushd %{buildroot}%{_bindir}
ln -s %{name} %{shortname}
popd

%if 0%{?with_check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc     
%{_bindir}/*

%changelog
%autochangelog