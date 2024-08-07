from custom_components.nvenergy.thesimple import (
    TheSimpleClient,
    TheSimpleThermostat,
    TheSimpleError,
)

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACAction,
    HVACMode,
)

from homeassistant.components.climate.const import (
    FAN_AUTO,
    FAN_ON,
    PRESET_AWAY,
    PRESET_NONE,
)

from homeassistant.const import (
    ATTR_TEMPERATURE,
    CONF_PASSWORD,
    CONF_USERNAME,
    UnitOfTemperature,
)

BASE_URL = "https://my.ecofactor.com/ws/v1.0/"
DOMAIN = "nvenergy"
