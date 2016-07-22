include includes/main.mk
include includes/clean.mk
include includes/virtualenv.mk

clean::
	${call log,clean transient jupyter files}
	rm -rf .ipynb_checkpoints/

$(HOME)/.matplotlib/matplotlibrc:
	$(call log,creating matplotlibrc)
	@mkdir $(HOME)/.matplotlib
	echo 'backend: TkAgg' >> $@

#> Launch the candidate considerations notebook
run: $(HOME)/.matplotlib/matplotlibrc virtualenv
	$(call log,launching the jupyter notebook server)
	$(VIRTUALENV_DIR)/bin/jupyter notebook Candidate\ Considerations\ Survey\ Visualization.ipynb

FORCE:
