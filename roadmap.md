# Roadmap

## Minimum viable product (12/2025)

December 2025

- [X] Use interfaces and Injector
- [ ] Scalars everywhere !!

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

- [X] name
- [X] scope (fixture selection)
  - [X] by tag
  - [ ] _(by position)_
- [ ] values (dimmer, color)
- [X] opacity
- [ ] _(user interface)_
- [X] stack (name, layers)

#### Stack Store

- [X] load from a file
- [X] save to a file
- [X] script to create a demo stack
- [ ] _(write tests)_

#### Value

- [X] name
- [X] selector (parameter name and wildcards)
  - [ ] _(use tags in the future ?)_
- [X] type (subclass of base type)
  - [X] scalar \[0..1\]
  - [ ] color \[R, G, B\]
  - [ ] _(angle \[-360..360\])_
  - [ ] _(speed)_

### Driver

- [X] name
- [X] target (layer opacity, values)
- [X] source identifier
- [X] fade in/out time
- [X] enabled
- [ ] _(user interface)_
- [ ] _(target change notifies all connected drivers)_

#### Driver Pool Store

- [X] load from a file
- [X] save to a file
- [X] script to create a demo stack
- [ ] _(write tests)_

#### Driver Updater

- [X] update inputs

### Engine

- [X] init
  - [X] broadcaster universes
  - [X] solver
- [X] start/stop
- [X] main loop
  - [X] update driver inputs
  - [X] solve
  - [X] convert to DMX
  - [X] broadcast
- [X] demo script
- [ ] _(user interface)_

#### Solver

- [ ] basic synchronous solving 
  - [X] read driver sources
  - [X] update layer values
    - [ ] fade in/out (only for buttons ?)
  - [ ] _(notify drivers targeting same values)_
  - [X] update layer values
  - [X] convert to DMX

#### Resolver

- [X] patch items for scope
- [X] drivers for layer
- [ ] _(caching and invalidation)_  

#### Artnet broadcaster

- [X] basic synchronous broadcast

### WebServer

- [X] start/stop
- [X] load/save configuration
- [X] get all values
- [ ] fix ungraceful shutdown
