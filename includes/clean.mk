# Removes build artifacts contained in the CLEAN env var. Makefiles that include
# this file can simply append to the CLEAN variable, and have their clean-able
# artifacts deleted when `make clean` is run.
#
# By default, the user is prompted to confirm the deletion of files. To disable
# this behavior, set SKIP_CLEAN_PROMPT to yes.
#
# Targets: clean
#

#> remove build artifacts
clean::
	$(call log,removing build artifacts)

.PHONY: clean
