from multiprocessing.shared_memory import SharedMemory

from frangipani_web_server.control.base import BaseWebControlDefinition


class SharedMemoryManager:

    def __init__(self, roolt_control_definition: BaseWebControlDefinition):
        self._root_control_definition = roolt_control_definition
        self._memory: SharedMemory | None = None

    def create_from_controls(self) -> str:
        """
        Creates a SharedMemory object from control definitions

        :return: the SharedMemory name
        """
        self._assert_not_created()
        self._memory = SharedMemory(create=True, size=2048)
        return self._memory.name

    def create_from_name(self, name: str) -> None:
        """
        Creates a SharedMemory object from an existing name

        :param name: Name of the shared memory
        :return: None
        """
        self._assert_not_created()
        self._memory = SharedMemory(name=name)

    def get_value(self, control_address: str) -> float | bool:
        return 0.0

    def get_all_values(self) -> dict[str, float | bool]:
        return {}

    def cleanup(self):
        if self._memory is not None:
            self._memory.close()
            self._memory.unlink()
            self._memory = None

    def _assert_not_created(self):
        if self._memory is not None:
            raise RuntimeError(f"Shared memory already created ({self._memory.name})")
