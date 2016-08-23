BINDIR=/usr/local/bin
UNAME_S:=$(shell uname -s)

.PHONY: install uninstall

install:
	install -m755 -d $(BINDIR)
	@if [ "$(UNAME_S)" = "Linux" ]; then\
		install -m755 -t $(BINDIR) auresult; \
	fi
	@if [ "$(UNAME_S)" = "Darwin" ]; then\
		install -m755  auresult $(BINDIR); \
	fi

uninstall:
	rm -f $(BINDIR)/auresult

