PYRCC4=pyrcc4
PYUIC4=pyuic4

UI_FILES=ui_laddereditor_window.py
RESOURCES_FILES=qrc_resources.py

all: ${RESOURCES_FILES}

$(RESOURCES_FILES): resources.qrc
	$(PYRCC4) -o $@ $<

$(UI_FILES): laddereditor_window.ui
	$(PYUIC4) -o $@ $<
