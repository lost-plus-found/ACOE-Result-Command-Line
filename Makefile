BINDIR=/usr/local/bin
UNAME_S:=$(shell uname -s)

.PHONY: install uninstall update

install:
	bash install
	install -m775 -d $(BINDIR)
	@if [ "$(UNAME_S)" = "Linux" ]; then\
		install -m775 -t $(BINDIR) auresult; \
	fi
	@if [ "$(UNAME_S)" = "Darwin" ]; then\
		install -m775  auresult $(BINDIR); \
	fi

uninstall:
	rm -f $(BINDIR)/auresult
	rm auresult

update:
	rm -f $(BINDIR)/auresult
	rm auresult
	git pull origin master
	bash install
	install -m775 -d $(BINDIR)
	@if [ "$(UNAME_S)" = "Linux" ]; then\
		install -m775 -t $(BINDIR) auresult; \
	fi
	@if [ "$(UNAME_S)" = "Darwin" ]; then\
		install -m775  auresult $(BINDIR); \
	fi
	
