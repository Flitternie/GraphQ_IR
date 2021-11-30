NAME := fig
DEPS := $(shell ls external/*.jar) $(shell find src -name "*.java")

default: $(NAME).war

classes: $(DEPS)
	mkdir -p classes
	ant compile
	touch classes

$(NAME).jar: classes
	jar cf $(NAME).jar -C classes .
	jar uf $(NAME).jar -C src .

servlet: $(NAME).jar
	mkdir -p servlet/WEB-INF/lib
	cp $(NAME).jar servlet/WEB-INF/lib
	touch servlet

$(NAME).war: servlet
	(cd servlet && zip -qr ../$(NAME).war `/bin/ls | grep -v ^var$$`)

clean:
	rm -rf classes $(NAME).jar $(NAME).war
