FROM fedora:28

RUN dnf makecache && \
    dnf upgrade -y && \
    dnf install -y \
        createrepo \
        desktop-file-utils \
        libappstream-glib \
        make \
        rpm-build \
        && \
    dnf clean all

ENTRYPOINT ["/usr/bin/sh]
