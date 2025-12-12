## Common channel names (recommended)

### Intensity / dimming
- `DIMMER` (master intensity)
- `STROBE`
- `SHUTTER` (often combined with strobe modes)
- `BLACKOUT` (if you model it separately)

### Position (moving heads / scanners)
- `PAN`
- `TILT`
- `PAN_TILT_SPEED` (movement speed)

### Color (RGBW/A/UV, etc.)
- `RED`
- `GREEN`
- `BLUE`
- `WHITE`
- `AMBER`
- `UV`
- `CYAN`
- `MAGENTA`
- `YELLOW`
- `COLOR_WHEEL` (indexed/continuous wheel)
- `COLOR_MACRO` (built-in color presets)

### Beam / optics
- `ZOOM`
- `FOCUS`
- `IRIS`
- `FROST`
- `BEAM_SIZE` (if you want a generic alternative to zoom/iris)

### Gobos (spot fixtures)
- `GOBO_WHEEL`
- `GOBO_ROTATION`
- `GOBO_SHAKE` (if separate from wheel)

### Prism / effects
- `PRISM`
- `PRISM_ROTATION`
- `EFFECT_WHEEL`

### Pan/Tilt macros and special movement
- `PAN_TILT_MACRO`
- `PAN_TILT_MACRO_SPEED`

### Control / misc
- `DIMMER_SPEED` (dimmer curve/smoothing speed)
- `FAN` (fan mode/speed)
- `CONTROL` (reset, lamp on/off, calibration, etc.)
- `RESET` (if you prefer explicit)
- `LAMP` (legacy discharge fixtures)
- `SOUND_SENSITIVITY`
- `PROGRAM` (auto programs)
- `PROGRAM_SPEED`

### Pixel/segment control (LED bars, matrices)
- `PIXEL_RED`
- `PIXEL_GREEN`
- `PIXEL_BLUE`
- `PIXEL_WHITE`
- `PIXEL_INTENSITY`

---

## Optional: Python enum skeleton (if you want it)
```python
from enum import Enum, auto

class ChannelName(Enum):
    DIMMER = auto()
    PAN = auto()
    TILT = auto()
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = auto()
    GOBO_WHEEL = auto()
    # add the rest as needed
```
