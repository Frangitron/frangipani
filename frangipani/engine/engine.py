import time

from pythonartnet.broadcaster import ArtnetBroadcaster

from pythonhelpers.injector import Injector

from frangipani.engine.configuration import EngineConfiguration
from frangipani.engine.driver_updater import DriverUpdater
from frangipani.engine.solver import Solver
from frangipani.patch.store import IPatchStore


class Engine:
    def __init__(self, configuration: EngineConfiguration):
        self.is_running = False

        self._initialized = False
        self._previous_broadcast_time = 0
        self._target_broadcast_interval = 1.0 / float(configuration.artnet_target_rate + 2)  # FIXME magic number

        self._artnet_broadcaster = ArtnetBroadcaster(
            target_ip=configuration.artnet_target_ip,
            bind_address=configuration.artnet_bind_address
        )
        self._driver_updater = DriverUpdater()
        self._patch_store = Injector().inject(IPatchStore)
        self._solver = Solver()

    def clear(self):
        self._artnet_broadcaster.clear()
        self._solver.clear()
        self._initialized = False

    def initialize(self):
        self.clear()

        for universe_number in self._patch_store.list_universes():
            self._artnet_broadcaster.add_universe(universe_number)

        self._solver.initialize()

        self._initialized = True

    def main_loop(self):
        if not self._initialized:
            raise RuntimeError("Engine not initialized")

        self.is_running = True
        while self.is_running:
            if not self._has_interval_elapsed():
                continue

            self._driver_updater.read_sources()

            self._solver.solve()

            for universe in self._artnet_broadcaster.universes.values():
                universe.buffer = self._solver.get_dmx_buffer(universe=universe.number)

            self._artnet_broadcaster.send_data_synced()

    def stop(self):
        self.is_running = False

    def _has_interval_elapsed(self):
        now = time.time()
        if now - self._previous_broadcast_time >= self._target_broadcast_interval:
            self._previous_broadcast_time = now
            return True

        time.sleep(self._target_broadcast_interval / 10.0)

        return False
