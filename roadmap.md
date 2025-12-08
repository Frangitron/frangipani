# Roadmap

## Minimum viable product (12/2025)

December 2025

### Fixture definition

- [ ] model
- [ ] channels
  - [ ] dimmer
  - [ ] color
- [ ] _(manufacturer)_ 
- [ ] _(mode)_

### Patch

- [ ] fixture
  - [ ] name
  - [ ] definition
  - [ ] tags
  - [ ] universe
  - [ ] address
  - [ ] _(position)_

### Layer

- [ ] scope (fixture selection)
  - [ ] by tag
  - [ ] _(by position)_
- [ ] values (dimmer, color)
- [ ] opacity

### Driver

- [ ] target (layer opacity)
- [ ] source
  - [ ] web server widget
  - [ ] _(OSC widget)_
- [ ] _(target change notifies all connected drivers)_
