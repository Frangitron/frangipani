# Roadmap

## Minimum viable product (12/2025)

### Project structure

- Driver
- Fixture
  - Definition
  - Library
  - Store
  - Parameter
    - Definition
    - Channel
- Layer
  - Stack Store
  - Value
- Patch
  - Address
  - Item
  - Store
- TimeProvider
- Engine
  - Solver
  - Resolver
  - Artnet broadcaster
- WebServer

### General features / architecture

- [X] Scalars everywhere
- [X] Use interfaces and Injector
- [ ] StorableMixin interface for JSON serialization
- [ ] Schema version check for all stores
- [ ] Tests

### Driver

- [X] name
- [X] target identifier (layer opacity, values)
- [X] source identifier (web control address)
- [X] fade in/out
  - [X] use increments and time divisions (similar to audio compressor)
- [X] enabled
- [X] load/save from a file
- [X] script to create a demo driver pool
- [ ] _(write tests)_
- [ ] _(user interface)_
- [ ] _(target change notifies all connected drivers)_

### Fixture 

#### Definition

- [X] _(manufacturer)_ 
- [X] identifier (@property)
- [X] model
- [X] parameter definitions
- [ ] _(? forbid char #)_
- [ ] _(mode)_

#### Library

- [X] name
- [X] api version
- [X] fixtures
  
#### Store

- [X] load (generic)
- [X] fixture definition library
  - [X] api version
  - [X] name
- [X] error on invalid api_version loading
- [X] script to create generic fixture definition library
- [ ] _(write tests)_

#### Parameter

##### Definition

- [X] address
- [X] default value
- [X] name
- [X] resolution
- [X] type (dimmer, color)
  - [X] channel kinds

##### Channel

- [X] kind
- [X] interpolator

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

### TimeProvider

- [X] reset
- [X] tick
- [X] time_delta
- [X] current_time

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

- [X] basic synchronous solving 
  - [X] read driver sources
  - [X] update layer values
    - [X] fade in/out
  - [X] update layer values
  - [X] convert to DMX
  - [ ] _(notify drivers targeting same values)_

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
- [X] fix ungraceful shutdown
