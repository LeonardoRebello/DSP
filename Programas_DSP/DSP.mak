# Generated by the VisualDSP++ IDDE

# Note:  Any changes made to this Makefile will be lost the next time the
# matching project file is loaded into the IDDE.  If you wish to preserve
# changes, rename this file and run it externally to the IDDE.

# The syntax of this Makefile is such that GNU Make v3.77 or higher is
# required.

# The current working directory should be the directory in which this
# Makefile resides.

# Supported targets:
#     DSP_Release
#     DSP_Release_clean

# Define this variable if you wish to run this Makefile on a host
# other than the host that created it and VisualDSP++ may be installed
# in a different directory.

ADI_DSP=C:\Program Files (x86)\Analog Devices\VisualDSP 5.1.2


# $VDSP is a gmake-friendly version of ADI_DIR

empty:=
space:= $(empty) $(empty)
VDSP_INTERMEDIATE=$(subst \,/,$(ADI_DSP))
VDSP=$(subst $(space),\$(space),$(VDSP_INTERMEDIATE))

RM=cmd /C del /F /Q

#
# Begin "DSP_Release" configuration
#

ifeq ($(MAKECMDGOALS),DSP_Release)

DSP_Release : ./Release/DSP.dxe 

Release/DSP.doj :DSP.c $(VDSP)/Blackfin/include/stdio.h $(VDSP)/Blackfin/include/yvals.h 
	@echo ".\DSP.c"
	$(VDSP)/ccblkfn.exe -c .\DSP.c -file-attr ProjectName=DSP -O -Ov100 -structs-do-not-overlap -no-multiline -D DO_CYCLE_COUNTS -double-size-32 -decls-strong -warn-protos -proc ADSP-BF533 -o .\Release\DSP.doj -MM

./Release/DSP.dxe :$(VDSP)/Blackfin/ldf/adsp-BF533.ldf $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtsf532y.doj ./Release/DSP.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/__initsbsz532.doj $(VDSP)/Blackfin/lib/cplbtab533.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtn532y.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsmall532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libc532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/librt_fileio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libevent532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libcpp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libf64ieee532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libdsp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsftflt532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libetsi532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libssl532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libdrv532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libusb532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libprofile532y.dlb 
	@echo "Linking..."
	$(VDSP)/ccblkfn.exe .\Release\DSP.doj -flags-link -ip -L .\Release -flags-link -e -flags-link -od,.\Release -o .\Release\DSP.dxe -proc ADSP-BF533 -MM

endif

ifeq ($(MAKECMDGOALS),DSP_Release_clean)

DSP_Release_clean:
	-$(RM) "Release\DSP.doj"
	-$(RM) ".\Release\DSP.dxe"
	-$(RM) ".\Release\*.ipa"
	-$(RM) ".\Release\*.opa"
	-$(RM) ".\Release\*.ti"
	-$(RM) ".\Release\*.pgi"
	-$(RM) ".\*.rbld"

endif


