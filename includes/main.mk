# The "main" utility functions and helpers useful for the common case. Most
# ludicrous makefiles require this file, so it's sensible to `include` it first.

# Generates help text from specialized comments (lines prefixed with a `#>`).
# Free-standing comments are included in the prologue of the help text, while
# those immediately preceding a recipe will be displayed along with their
# respective target names
#
# Targets: help
# Requires: awk
# Side effects:
#   * .DEFAULT_GOAL is set to to the `help` target from this file
INCLUDES_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
HELP_PROGRAM := $(INCLUDES_DIR)/help.awk

#> displays this message
help: | _program_awk
	@awk -f $(HELP_PROGRAM) $(MAKEFILE_LIST)
.PHONY: help

.DEFAULT_GOAL := help

# Helper target for declaring an external executable as a recipe dependency.
# For example,
#   `my_target: | _program_awk`
# will fail before running the target named `my_target` if the command `awk` is
# not found on the system path.
_program_%: FORCE
	@_=$(or $(shell which $* 2> /dev/null),$(error `$*` command not found. Please install `$*` and try again))

# The defult build dir, if we have only one it'll be easier to cleanup
BUILD_DIR =: build

$(BUILD_DIR):
	mkdir -p $@

# text manipulation helpers
_awk_case = $(shell echo | awk '{ print $(1)("$(2)") }')
lc = $(call _awk_case,tolower,$(1))
uc = $(call _awk_case,toupper,$(1))

# Useful for forcing targets to build when .PHONY doesn't help
FORCE:
.PHONY: FORCE

# Provides two callables, `log` and `_log`, to facilitate consistent
# user-defined output, formatted using tput when available.
#
# Override TPUT_PREFIX to alter the formatting.
TPUT        := $(shell which tput 2> /dev/null)
TPUT_PREFIX := $(TPUT) bold
TPUT_SUFFIX := $(TPUT) sgr0

ifeq (,$(and $(TPUT),$(TERM)))

define _log
echo "===> $(1)"
endef

else

define _log
$(TPUT_PREFIX); echo "===> $(1)"; $(TPUT_SUFFIX)
endef

endif

define log
	@$(_log)
endef
