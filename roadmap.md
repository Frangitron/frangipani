# Roadmap

## Minimum viable product (12/2025)

December 2025

- [X] Use interfaces and Injector

### Fixture 

#### Definition

- [X] _(manufacturer)_ 
- [X] identifier (@property)
- [X] model
- [X] parameter definitions
- [ ] _(? forbid char #)_
- [ ] _(mode)_

#### Definition store

- [X] load (generic)
- [X] fixture definition library
  - [X] api version
  - [X] name
- [X] error on invalid api_version loading
- [X] script to create generic fixture definition library
- [ ] _(write tests)_

#### Parameter definition

- [X] address
- [X] default value
- [X] name
- [X] resolution
- [X] type (dimmer, color)

### Patch

- [X] name
- [X] items

#### Address

- [X] channel
- [X] universe

#### Item

- [X] address
- [X] definition
- [X] name
- [X] tags
- [ ] _(position)_

#### Store

- [X] load from a file
- [X] save to a file
- [X] script to create demo patch
- [ ] _(write tests)_

### Layer

- [ ] scope (fixture selection)
  - [ ] by tag
  - [ ] _(by position)_
- [ ] values (dimmer, color)
- [ ] opacity
- [ ] user interface

### Driver

- [ ] target (layer opacity)
- [ ] source
  - [ ] web server widget
  - [ ] _(OSC widget)_
- [ ] user interface
- [ ] fade in/out time
- [ ] _(target change notifies all connected drivers)_
