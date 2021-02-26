################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../component/lists/fsl_component_generic_list.c 

OBJS += \
./component/lists/fsl_component_generic_list.o 

C_DEPS += \
./component/lists/fsl_component_generic_list.d 


# Each subdirectory must supply rules for building sources it contributes
component/lists/%.o: ../component/lists/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -D__NEWLIB__ -DCPU_MIMXRT1062DVL6A -DCPU_MIMXRT1062DVL6A_cm7 -DXIP_BOOT_HEADER_DCD_ENABLE=1 -DSKIP_SYSCLK_INIT -DDATA_SECTION_IS_CACHEABLE=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1 -DSDK_DEBUGCONSOLE_UART -DFLATBUFFERS_LITTLEENDIAN -DGEMMLOWP_MCU -DTFLITE_MCU -DARM_MATH_CM7 -D__FPU_PRESENT=1 -DSDK_I2C_BASED_COMPONENT_USED=1 -DCR_INTEGER_PRINTF -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"G:\tflite\trial\board" -I"G:\tflite\trial\source" -I"G:\tflite\trial\video" -I"G:\tflite\trial\drivers" -I"G:\tflite\trial\utilities" -I"G:\tflite\trial\source\video" -I"G:\tflite\trial\eiq\tensorflow-lite" -I"G:\tflite\trial\eiq\tensorflow-lite\third_party" -I"G:\tflite\trial\eiq\tensorflow-lite\third_party\flatbuffers\include" -I"G:\tflite\trial\eiq\tensorflow-lite\third_party\gemmlowp" -I"G:\tflite\trial\component\lists" -I"G:\tflite\trial\component\uart" -I"G:\tflite\trial\device" -I"G:\tflite\trial\xip" -I"G:\tflite\trial\CMSIS" -I"G:\tflite\trial\source\image" -I"G:\tflite\trial\source\model" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


