include includes/main.mk
include includes/clean.mk
include includes/virtualenv.mk

clean::
	${call log,clean transient jupyter files}
	rm -rf .ipynb_checkpoints/

#> Launch the candidate considerations notebook
run: virtualenv
	$(call log,launching the jupyter notebook server)
	$(VIRTUALENV_DIR)/bin/jupyter notebook Candidate\ Considerations\ Survey\ Visualization.ipynb
