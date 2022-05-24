set(IDF_TARGET esp32c3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/MYESP32_C3_2M/sdkconfig.2m
)

if(NOT MICROPY_FROZEN_MANIFEST)
	set(MICROPY_FROZEN_MANIFEST ${MICROPY_PORT_DIR}/boards/MYESP32_C3_2M/manifest.py)
endif()
