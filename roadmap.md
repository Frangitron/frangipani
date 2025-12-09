# Roadmap

## Minimum viable product (12/2025)

December 2025

- [ ] Use interfaces and Injector

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

- [ ] channel
- [ ] universe

#### Item

- [ ] address
- [ ] definition
- [ ] name
- [ ] tags
- [ ] _(position)_

#### Store

- [ ] load from a file
- [ ] save to a file

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
