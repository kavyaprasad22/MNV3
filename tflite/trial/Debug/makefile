################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include xip/subdir.mk
-include video/subdir.mk
-include utilities/subdir.mk
-include startup/subdir.mk
-include source/video/subdir.mk
-include source/model/subdir.mk
-include source/image/subdir.mk
-include source/subdir.mk
-include drivers/subdir.mk
-include device/subdir.mk
-include component/uart/subdir.mk
-include component/lists/subdir.mk
-include board/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: evkmimxrt1060_tensorflow_lite_label_image_kav.axf

# Tool invocations
evkmimxrt1060_tensorflow_lite_label_image_kav.axf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: MCU C++ Linker'
	arm-none-eabi-c++ -nostdlib -L"G:\tflite\trial\eiq\tensorflow-lite\lib\cm7\gcc" -Xlinker -Map="evkmimxrt1060_tensorflow_lite_label_image_kav.map" -Xlinker --gc-sections -Xlinker -print-memory-usage -Xlinker --sort-section=alignment -Xlinker --cref -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -T "evkmimxrt1060_tensorflow_lite_label_image_kav_Debug.ld" -o "evkmimxrt1060_tensorflow_lite_label_image_kav.axf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '
	$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(CC_DEPS)$(C++_DEPS)$(EXECUTABLES)$(C_UPPER_DEPS)$(CXX_DEPS)$(OBJS)$(CPP_DEPS)$(C_DEPS) evkmimxrt1060_tensorflow_lite_label_image_kav.axf
	-@echo ' '

post-build:
	-@echo 'Performing post-build steps'
	-arm-none-eabi-size "evkmimxrt1060_tensorflow_lite_label_image_kav.axf"; # arm-none-eabi-objcopy -v -O binary "evkmimxrt1060_tensorflow_lite_label_image_kav.axf" "evkmimxrt1060_tensorflow_lite_label_image_kav.bin" ; # checksum -p MIMXRT1062xxxxA -d "evkmimxrt1060_tensorflow_lite_label_image_kav.bin";
	-@echo ' '

.PHONY: all clean dependents post-build

-include ../makefile.targets
